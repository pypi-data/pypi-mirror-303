import uuid
from collections import defaultdict
from contextlib import suppress
from copy import deepcopy
from typing import Any, Dict, List, Union

import tenacity
from loguru import logger
from pydantic import BaseModel, create_model

from plurally.models import factory, flow_utils, utils
from plurally.models.meta import InstagramNewDm, InstagramSendDm
from plurally.models.node import Node
from plurally.models.source.constant import ConstantSource
from plurally.models.subflow import Subflow


class Flow:

    @staticmethod
    def create_id():
        return f"fl-{str(uuid.uuid4())}"

    def __init__(self, name: str = "") -> None:
        global nx
        import networkx as nx

        self._flow_id = Flow.create_id()
        self.name = name
        self.graph = nx.MultiDiGraph()
        self._inter_subflow_run_links = {}

    @property
    def flow_id(self):
        return self._flow_id

    def __eq__(self, other: "Flow") -> bool:
        return (
            isinstance(other, Flow)
            and self.graph.nodes == other.graph.nodes
            and self.graph.edges == other.graph.edges
        )

    def __contains__(self, node: Node):
        assert isinstance(node, Node)
        return node in self.graph

    def get_scopes_and_meta_data(self):
        scopes_and_meta_data = []
        for child in self.graph.nodes:
            child_scopes_and_meta_datas = child.get_scopes_and_meta_data()
            for child_scopes_and_meta_data in child_scopes_and_meta_datas:
                child_scopes = child_scopes_and_meta_data[0]
                if child_scopes:
                    scopes_and_meta_data.append(child_scopes_and_meta_data)
        return scopes_and_meta_data

    def add_node(
        self,
        node: Node,
        subflow_id: str = None,
    ) -> Node:
        if node in self:
            raise ValueError(f"Block with id={node.node_id[:7]} already registered")
        if subflow_id:
            subflow = self.get_node(subflow_id)
            graph = subflow.graph
        else:
            graph = self.graph
        graph.add_node(node)
        return node

    def get_node(self, node_id: str, traverse_subflows: bool = False) -> Node:
        for child in self.graph.nodes:
            if isinstance(child, (Node, Subflow)) and child.node_id == node_id:
                return child
            if isinstance(child, Subflow) and traverse_subflows:
                with suppress(ValueError):
                    return child.get_node(node_id)
        raise ValueError(f"Node with {node_id=} not found")

    def connect_nodes(
        self,
        src_node: Union[str, "Node"],
        src_handle: str,
        tgt_node: Union[str, "Node"],
        tgt_handle: str,
        subflow: Union[str, "Subflow"] = None,
    ):
        """Connect this node's output to another node's input."""
        if subflow is None:
            flow_or_subflow = self
        else:
            subflow = self.get_node(subflow) if isinstance(subflow, str) else subflow
            flow_or_subflow = subflow

        if isinstance(src_node, str):
            src_node = flow_or_subflow.get_node(src_node)
        else:
            assert (
                src_node in flow_or_subflow.graph
            ), f"{src_node} not in {flow_or_subflow.graph}"

        if isinstance(tgt_node, str):
            tgt_node = flow_or_subflow.get_node(tgt_node)
        else:
            assert (
                tgt_node in flow_or_subflow.graph
            ), f"{tgt_node} not in {flow_or_subflow.graph}"

        return flow_utils.connect_nodes(
            flow_or_subflow.graph, src_node, src_handle, tgt_node, tgt_handle
        )

    def disconnect_nodes(
        self,
        src_node: Union[str, "Node"],
        src_handle: str,
        tgt_node: Union[str, "Node"],
        tgt_handle: str,
        subflow: Union[str, "Subflow"] = None,
    ):
        """Disconnect this node connection."""

        if subflow is None:
            flow_or_subflow = self
        else:
            subflow = self.get_node(subflow) if isinstance(subflow, str) else subflow
            flow_or_subflow = subflow

        if isinstance(src_node, str):
            src_node = flow_or_subflow.get_node(src_node)
        if isinstance(tgt_node, str):
            tgt_node = flow_or_subflow.get_node(tgt_node)
        if src_node is tgt_node:
            raise ValueError(f"Cannot connect node with itself: {src_node}")
        try:
            flow_or_subflow.graph.remove_edge(
                src_node, tgt_node, key=f"{src_handle}###{tgt_handle}"
            )
        except nx.NetworkXError:
            raise ValueError(
                f"Connection between {src_node} and {tgt_node} with {src_handle=} and {tgt_handle=} not found"
            )

    def delete_node(self, node: Union[str, "Node"], traverse_subflows: bool = False):
        """Remove a node from the flow."""
        node_id = node if isinstance(node, str) else node.node_id
        for child in self.graph.nodes:
            if isinstance(child, Subflow) and traverse_subflows:
                with suppress(ValueError):
                    child.delete_node(node_id)
                    flow_utils.disconnect_all_nodes_connected_to(
                        child.graph, node_id, None, mode="all"
                    )
                    # need to disconnect subflow's handles as well
                    edges_to_rm = []
                    for src, tgt, key in self.graph.edges:
                        src_handle, tgt_handle = key.split("###")
                        if (src_handle.startswith(node_id) and src == child) or (
                            tgt_handle.startswith(node_id) and tgt == child
                        ):
                            edges_to_rm.append((src, tgt, key))
                    for src, tgt, key in edges_to_rm:
                        self.graph.remove_edge(src, tgt, key=key)
                    return
            if isinstance(child, (Node, Subflow)) and child.node_id == node_id:
                self.graph.remove_node(child)
                return
        raise ValueError(f"Node with id {node_id} not found")

    def run_callbacks(self, items: list[Node]):
        for item in items:
            item.callback()

    @staticmethod
    def get_sorted_nodes(graph) -> List[Node]:
        return list(nx.topological_sort(graph))

    def get_flatten_graph(self):
        return flow_utils.get_flatten_graph(self.graph)

    def get_flatten_subflow(self, subflow_id) -> tuple["Flow", Subflow]:
        subflow = self.get_node(subflow_id)
        graph = flow_utils.get_flatten_graph(subflow.graph)
        flow = Flow(subflow.name)
        flow.graph = graph
        return flow, subflow

    def __call__(self, output_overrides: Dict[str, BaseModel] = None) -> Any:
        state = self.states()
        graph = self.get_flatten_graph()
        try:
            output_overrides = output_overrides if output_overrides else {}
            if output_overrides:
                logger.debug(f"Will override for nodes: {','.join(output_overrides)}")
            no_run = set()

            sorted_nodes = self.get_sorted_nodes(graph)

            trigger_ix = None
            for item in sorted_nodes:
                if item.is_trigger:
                    trigger_ix = item

                if not isinstance(item, Node):
                    break

                if isinstance(item, ConstantSource):
                    # constant source always have outputs and it is not reset at every iteration
                    continue

                item.outputs = {}

            assert trigger_ix, "Flow must have a trigger block"

            # make sure trigger block is the first one
            # this will make sure that the flow is immediatlly aborted if the trigger node has no outputs
            sorted_nodes.remove(trigger_ix)
            sorted_nodes = [trigger_ix] + sorted_nodes

            for item in sorted_nodes:
                try:
                    if not isinstance(item, Node):
                        break
                    kwargs = {}
                    for src_node, tgt_node, attrs in graph.in_edges(item, True):
                        src_handle = attrs["src_handle"]
                        tgt_handle = attrs["tgt_handle"]

                        src_value = src_node.outputs.get(src_handle)
                        # if it is a list, it should append
                        if utils.is_list_type(
                            tgt_node.InputSchema.model_fields[tgt_handle]
                        ):
                            if tgt_handle not in kwargs:
                                kwargs[tgt_handle] = []
                            kwargs[tgt_handle].append(src_value)
                        else:
                            kwargs[tgt_handle] = src_value
                        logger.debug(f"Processing {src_node} -> {tgt_node}")

                    node_overrides = output_overrides.get(item.node_id)
                    if node_overrides:
                        logger.debug(f"Overriding execution of {item}")
                        item.outputs = node_overrides.model_dump()
                    else:
                        parent_no_run = item in no_run
                        is_no_run = not kwargs.get("run", True)
                        if parent_no_run or is_no_run:
                            if parent_no_run:
                                logger.debug(
                                    f"Skipping {item} - parent was marked as no_run"
                                )
                            if is_no_run:
                                logger.debug(f"Skipping {item} - run is set to False")
                            for node in graph.successors(item):
                                no_run.add(node)
                            continue

                        logger.debug(f"Forwarding {item} with {list(kwargs)}")
                        item(**kwargs)

                        if item.outputs is None:
                            logger.debug(f"Node {item} has no outputs")
                        else:
                            logger.debug(
                                f"Finished {item}, outputs: {list(item.outputs) if item.outputs else None}"
                            )

                        item.early_stop_if_needed(graph)

                        if item.is_trigger and item.outputs is None:
                            # skip if trigger has no outputs
                            logger.debug(
                                f"Aborting execution due to missing outputs from {item}"
                            )
                            self.run_callbacks(sorted_nodes)
                            return

                except Exception as e:
                    # if RetryError is raised, log the source
                    if isinstance(e, tenacity.RetryError):
                        e = e.last_attempt.exception()
                    raise RuntimeError(f"{type(item).__name__} failed: {e}") from e

            self.run_callbacks(sorted_nodes)

        except Exception:
            self.update(state)
            raise

    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, id={self._flow_id[:4]})"

    def create_subflow(self, name: str, node_ids: list[str]) -> "Flow":
        assert len(node_ids) > 1, "Subflow must have at least two nodes"
        subflow_node_ids = set()
        subflow_nodes = []
        for node_id in node_ids:
            node = self.get_node(node_id)
            assert not isinstance(node, Subflow), "Cannot nest subflows"
            subflow_node_ids.add(node_id)
            subflow_nodes.append(node)

        # subflow_links are the inner links of the subflow
        subflow_links = set()
        # inter_flow_links are the links between the subflow and the rest of the flow
        inter_flow_links = set()
        inter_subflow_run_links = []
        force_show_src = []
        for node in subflow_nodes:
            in_edges = list(self.graph.in_edges(node, data=True))
            for src, _, key in in_edges:
                assert _ is node

                if src.node_id in subflow_node_ids:
                    subflow_links.add(
                        (
                            src.node_id,
                            key["src_handle"],
                            node.node_id,
                            key["tgt_handle"],
                        )
                    )
                else:
                    if key["tgt_handle"] == "run":
                        # connect to subflow's run, not inner node's run
                        # and save the connection to be reconnected later
                        subflow_tgt_handle = "run"
                        inter_subflow_run_links.append(
                            (src.node_id, key["src_handle"], node.node_id, "run")
                        )
                    else:
                        subflow_tgt_handle = f"{node.node_id}.{key['tgt_handle']}"
                    inter_flow_links.add(
                        (src.node_id, key["src_handle"], None, subflow_tgt_handle)
                    )

            out_edges = list(self.graph.out_edges(node, data=True))
            for _, tgt, key in out_edges:
                assert _ is node
                if tgt.node_id in subflow_node_ids:
                    subflow_links.add(
                        (
                            node.node_id,
                            key["src_handle"],
                            tgt.node_id,
                            key["tgt_handle"],
                        )
                    )
                else:
                    src_handle = f"{node.node_id}.{key['src_handle']}"
                    force_show_src.append(src_handle)
                    inter_flow_links.add(
                        (None, src_handle, tgt.node_id, key["tgt_handle"])
                    )

        min_x = min([node.pos_x for node in subflow_nodes])
        max_x = max([node.pos_x for node in subflow_nodes])
        pos_x = (min_x + max_x) // 2

        min_y = min([node.pos_y for node in subflow_nodes])
        max_y = max([node.pos_y for node in subflow_nodes])
        pos_y = (min_y + max_y) // 2

        # make them relative to the top left
        for node in subflow_nodes:
            node.pos_x -= pos_x
            node.pos_y -= pos_y

        subflow = Subflow(
            Subflow.InitSchema(
                name=name,
                pos_x=pos_x,
                pos_y=pos_y,
            ),
            nodes=subflow_nodes,
            links=subflow_links,
            force_show_src=force_show_src,
        )

        # this is to reconstruct the inter flow links to inner nodes' run handles
        # observe that they might have been changed by the time we ungroup the subflow
        # and in this case we will not be able to reconnect them (which is fine)
        self._inter_subflow_run_links[subflow.node_id] = inter_subflow_run_links

        for node in subflow_nodes:
            self.delete_node(node)

        self.add_node(subflow)
        for src, src_handle, tgt, tgt_handle in inter_flow_links:
            self.connect_nodes(src or subflow, src_handle, tgt or subflow, tgt_handle)

        if not nx.is_directed_acyclic_graph(self.graph):
            raise ValueError("Resulting subflow is not valid")

        return subflow

    def ungroup_subflow(self, subflow: Subflow | str):
        if isinstance(subflow, str):
            subflow = self.get_node(subflow)
        assert subflow in self.graph, f"Subflow {subflow} not found in the current Flow"
        subflow_nodes = list(subflow.graph.nodes)
        inner_subflow_links = list(subflow.graph.edges(data=True))

        for node in subflow_nodes:
            node.pos_x += subflow.pos_x
            node.pos_y += subflow.pos_y
            self.add_node(node)

        for src, tgt, key in inner_subflow_links:
            src_handle = key["src_handle"]
            tgt_handle = key["tgt_handle"]
            self.connect_nodes(src, src_handle, tgt, tgt_handle)

        inter_flow_edges = set()
        inter_flow_in_edges = self.graph.in_edges(subflow, data=True)
        for src, _, data in inter_flow_in_edges:
            src_handle = data["src_handle"]
            if data["tgt_handle"] == "run":
                # these inter_flow links are saved in _inter_subflow_run_links
                continue

            tgt_node_id, tgt_handle = data["tgt_handle"].split(".")
            inter_flow_edges.add(
                (src, src_handle, subflow.get_node(tgt_node_id), tgt_handle)
            )

        inter_flow_out_edges = self.graph.out_edges(subflow, data=True)
        for _, tgt, data in inter_flow_out_edges:
            src_node_id, src_handle = data["src_handle"].split(".")
            tgt_handle = data["tgt_handle"]
            inter_flow_edges.add(
                (subflow.get_node(src_node_id), src_handle, tgt, tgt_handle)
            )

        inter_subflow_run_links = self._inter_subflow_run_links.pop(subflow.node_id, [])
        self.delete_node(subflow)

        # here subflow must be disconnected otherwise
        # we might end up with multiple connections
        for inter_flow_edge in inter_flow_edges:
            self.connect_nodes(*inter_flow_edge)

        for src, src_handle, tgt, tgt_handle in inter_subflow_run_links:
            # nodes could have been deleted or handles changed by now
            with suppress(Exception):
                self.connect_nodes(src, src_handle, tgt, tgt_handle)

    def _get_title(self, schema, handle):
        return schema.model_fields[handle].title or handle.title().replace("_", " ")

    def serialize(self) -> Dict:
        input_schemas = utils.get_input_schemas(self.graph.nodes, to_json=False)
        output_schemas = utils.get_output_schemas(self.graph.nodes, to_json=False)

        s = nx.node_link_data(self.graph)
        s["nodes"] = [{**n, "id": n["id"].serialize()} for n in s["nodes"]]

        links = []
        for link in s["links"]:
            source = link["source"]
            target = link["target"]

            src_handle_title = self._get_title(
                output_schemas[source.node_id], link["src_handle"]
            )
            tgt_handle_title = self._get_title(
                input_schemas[target.node_id], link["tgt_handle"]
            )

            label = f"{src_handle_title} -> {tgt_handle_title}"
            links.append(
                {
                    **link,
                    "label": label,
                    "source": source.node_id,
                    "target": target.node_id,
                }
            )
        s["links"] = links
        s["name"] = self.name
        s["id"] = self.flow_id
        s["_inter_subflow_run_links"] = self._inter_subflow_run_links
        return s

    def states(self) -> Dict[str, Dict]:
        all_states = {}
        for child in self.graph.nodes:
            all_states[child.node_id] = child.state()
        return all_states

    def update(self, state: Dict[str, Dict]):
        for child in self.graph.nodes:
            state_update = state.get(child.node_id)
            child.update_state(state_update)

    @classmethod
    def parse(cls, data: Dict) -> "Flow":
        global nx
        import networkx as nx

        data = deepcopy(data)

        flow = cls()
        nodes = {}
        nodes_list = []
        for n in data["nodes"]:
            node = factory.create_node(**n["id"])
            nodes[node.node_id] = node
            nodes_list.append(node)
        data["nodes"] = [{**n, "id": nodes[n["id"]["_node_id"]]} for n in data["nodes"]]
        data["links"] = [
            {**link, "source": nodes[link["source"]], "target": nodes[link["target"]]}
            for link in data["links"]
        ]

        flow.graph = nx.node_link_graph(data)
        flow._flow_id = data.get("id", "no-id")
        flow.name = data.get("name", "no-name")
        flow._inter_subflow_run_links = data.get("_inter_subflow_run_links", {})
        return flow

    def get_necessary_env_vars(self) -> List[str]:
        env_vars = []
        for node in self.graph.nodes:
            env_vars.extend(node.get_necessary_env_vars())
        return env_vars

    def num_triggers(self):
        n = 0
        for child in self.graph.nodes:
            if isinstance(child, Node) and child.is_trigger:
                n += 1
        return n

    def _get_insta_issues(self, graph, insta_nodes):
        issues = []
        send_dm_nodes = [
            node for node in insta_nodes if isinstance(node, InstagramSendDm)
        ]
        if len(send_dm_nodes) > 1:
            issues.append("Flow can only have one 'Send DM (Insta)' block")

        new_dm_nodes = [
            node for node in insta_nodes if isinstance(node, InstagramNewDm)
        ]
        if send_dm_nodes:
            [send_dm_node] = send_dm_nodes
            if len(new_dm_nodes) != 1:
                issues.append(
                    "In order to send Instagram DMs, you need to use exactly one the 'Incoming DM (Insta)' block."
                )
            else:
                [new_dm_node] = new_dm_nodes
                # elif not connected to the 'Incoming DM (Insta)' block:
                if not any(
                    [
                        (src, tgt, key)
                        for src, tgt, key in graph.in_edges(send_dm_node, data=True)
                        if all(
                            [
                                key["tgt_handle"] == "recipient_id",
                                key["src_handle"] == "sender_id",
                                src == new_dm_node,
                                tgt == send_dm_node,
                            ]
                        )
                    ]
                ):
                    issues.append(
                        "The 'Incoming DM (Insta)' sender ID output must be connected to the 'Send DM (Insta)' recipient ID input."
                    )

                # elif not connected to the 'Incoming DM (Insta)' block:
                if not any(
                    [
                        (src, tgt, key)
                        for src, tgt, key in graph.in_edges(send_dm_node, data=True)
                        if all(
                            [
                                key["tgt_handle"] == "was_escalated_previously_",
                                key["src_handle"] == "was_escalated_previously_",
                                src == new_dm_node,
                                tgt == send_dm_node,
                            ]
                        )
                    ]
                ):
                    issues.append(
                        "The 'Incoming DM (Insta)' Is Escalation Triggered output must be connected to the 'Send DM (Insta)' run input."
                    )
        return issues

    def get_issues(self) -> List[str]:
        issues = []
        graph = self.get_flatten_graph()
        if not nx.is_directed_acyclic_graph(graph):
            issues.append("Graph is not a directed acyclic graph")

        num_triggers = self.num_triggers()
        if num_triggers == 0:
            issues.append("Flow is missing a trigger block")

        if num_triggers > 1:
            issues.append("Flow can only have one trigger block")

        if not graph.nodes:
            issues.append("Flow is empty")

        # ensure that all nodes are connected (when handle is not optional)
        insta_nodes = set()
        for node in graph.nodes:
            if isinstance(node, (InstagramSendDm, InstagramNewDm)):
                insta_nodes.add(node)
            required_inputs = utils.get_required_fields(node.InputSchema)
            for input_name in required_inputs:
                if not any(
                    [
                        (src, tgt, key)
                        for src, tgt, key in graph.in_edges(node, data=True)
                        if key["tgt_handle"] == input_name
                    ]
                ):
                    issues.append(
                        f"Node {node.name} is missing required input {input_name}"
                    )

            if node.EnvVars:
                logger.debug(f"Loading env vars for {node}")
                issues.extend(node.EnvVars.get_issues())
        issues.extend(self._get_insta_issues(graph, insta_nodes))

        for node in graph.nodes:
            issues.extend(node.get_issues(graph))
        return issues

    def is_valid(self) -> bool:
        return not self.get_issues()

    def get_source_nodes(self) -> List[Node]:
        if not self.is_valid():
            raise ValueError("Cannot get source nodes on invalid flow")
        source_nodes = []
        graph = self.get_flatten_graph()
        for child in graph:
            if isinstance(child, Node) and graph.in_degree(child) == 0:
                source_nodes.append(child)
        return source_nodes

    def _delete_sensitive_fields(self, node):
        kls, *_ = factory.MAP[node["kls"]]
        if kls == Subflow:
            for child in node["subflow_nodes"]:
                self._delete_sensitive_fields(child)
        else:
            for sensitive_field in kls.SensitiveFields:
                if sensitive_field in node:
                    del node[sensitive_field]

    def create_template(self):
        template = self.serialize()
        for node in template["nodes"]:
            self._delete_sensitive_fields(node["id"])
        return template

    @classmethod
    def _get_overrides_for_node(cls, node_attrs):
        name = node_attrs["name"]
        kls, *_ = factory.MAP[node_attrs["kls"]]
        overrides = {}
        if kls == Subflow:
            for child in node_attrs["subflow_nodes"]:
                overrides.update(cls._get_overrides_for_node(child))
        else:
            init_schema = kls.InitSchema.model_fields
            overrideable_fields = kls.InitSchema.get_overrideable_fields()
            overrides_for_node = {}
            for field_name, field_info in init_schema.items():
                if field_name not in overrideable_fields and (
                    not field_info.is_required() or field_name in node_attrs
                ):
                    continue
                overrides_for_node[field_name] = (field_info.annotation, field_info)
            override_schema = create_model(
                name, __config__=kls.InitSchema.model_config, **overrides_for_node
            )
            overrides[node_attrs["_node_id"]] = override_schema
        return overrides

    @classmethod
    def get_overrides_for_template(cls, template) -> Dict[str, BaseModel]:
        required_overrides = {}
        for node in template["nodes"]:
            node_attrs = node["id"]
            required_overrides.update(cls._get_overrides_for_node(node_attrs))
        return required_overrides

    @classmethod
    def from_template(cls, template, data: dict = None):
        data = defaultdict(dict, data or {})

        template = deepcopy(template)
        for node in template["nodes"]:
            node_attrs = node["id"]
            node_id = node["id"]["_node_id"]
            kls, *_ = factory.MAP[node_attrs["kls"]]
            if kls == Subflow:
                for child in node_attrs["subflow_nodes"]:
                    child_data = data[child["_node_id"]]
                    child.update(child_data)
            else:
                node["id"].update(data[node_id])
        return cls.parse(template)

    def disconnect_all_nodes_connected_to(
        self, node_id: str, handle: str = None, mode: str = "all"
    ):
        return flow_utils.disconnect_all_nodes_connected_to(
            self.graph, node_id, handle, mode
        )

    def propagate_new_handle_to_subflows(
        self, child_node: Node, handle: str, mode: str
    ):
        assert mode in ("source", "target")
        for node in self.graph.nodes:
            if isinstance(node, Subflow) and child_node in node.graph.nodes:
                if mode == "target":
                    node.tgt_handles = list(
                        set(node.tgt_handles) | {f"{child_node.node_id}.{handle}"}
                    )
                else:
                    node.src_handles = list(
                        set(node.src_handles) | {f"{child_node.node_id}.{handle}"}
                    )

    def add_target_handle(self, node_id: str, src_handle: str) -> str:
        node = self.get_node(node_id)
        return node.add_target_handle(src_handle)

    def rename_handles(self, node: Node, renamed_handles: Dict[str, str], mode: str):
        connections = []
        deconnections = []
        subflows = [n for n in self.graph.nodes if isinstance(n, Subflow)]
        if mode == "source":
            if node in self.graph:
                for _, tgt, data in self.graph.out_edges(node, data=True):
                    src_handle = data["src_handle"]
                    new_handle = renamed_handles.get(src_handle)
                    if new_handle:
                        deconnections.append(
                            (node, src_handle, tgt, data["tgt_handle"])
                        )
                        connections.append((node, new_handle, tgt, data["tgt_handle"]))
            else:
                # node is part of subflow
                for subflow in subflows:
                    if node in subflow.graph:
                        # inner subflow connections
                        for _, tgt, data in subflow.graph.out_edges(node, data=True):
                            src_handle = data["src_handle"]
                            new_handle = renamed_handles.get(src_handle)
                            if new_handle:
                                deconnections.append(
                                    (node, src_handle, tgt, data["tgt_handle"], subflow)
                                )
                                connections.append(
                                    (node, new_handle, tgt, data["tgt_handle"], subflow)
                                )

                        # intra subflow connections
                        for src, tgt, data in self.graph.out_edges(subflow, data=True):
                            src_handle = data["src_handle"]
                            is_subflow_handle = len(src_handle.split(".")) > 1
                            if is_subflow_handle:
                                subflow_node_id, subflow_handle = src_handle.split(".")
                                if subflow_node_id == node.node_id:
                                    new_handle = renamed_handles.get(subflow_handle)
                                    if new_handle:
                                        new_handle = f"{node.node_id}.{new_handle}"
                                        deconnections.append(
                                            (src, src_handle, tgt, data["tgt_handle"])
                                        )
                                        connections.append(
                                            (src, new_handle, tgt, data["tgt_handle"])
                                        )

        elif mode == "target":
            if node in self.graph:
                for src, _, data in self.graph.in_edges(node, data=True):
                    tgt_handle = data["tgt_handle"]
                    new_handle = renamed_handles.get(tgt_handle)
                    if new_handle:
                        deconnections.append(
                            (src, data["src_handle"], node, tgt_handle)
                        )
                        connections.append((src, data["src_handle"], node, new_handle))
            else:
                # node is part of subflow
                for subflow in subflows:
                    if node in subflow.graph:
                        # inner subflow connections
                        for src, _, data in subflow.graph.in_edges(node, data=True):
                            tgt_handle = data["tgt_handle"]
                            new_handle = renamed_handles.get(tgt_handle)
                            if new_handle:
                                deconnections.append(
                                    (src, data["src_handle"], node, tgt_handle, subflow)
                                )
                                connections.append(
                                    (src, data["src_handle"], node, new_handle, subflow)
                                )

                        # intra subflow connections
                        for src, tgt, data in self.graph.in_edges(subflow, data=True):
                            tgt_handle = data["tgt_handle"]
                            is_subflow_handle = len(tgt_handle.split(".")) > 1
                            if is_subflow_handle:
                                subflow_node_id, subflow_handle = tgt_handle.split(".")
                                if subflow_node_id == node.node_id:
                                    new_handle = renamed_handles.get(subflow_handle)
                                    if new_handle:
                                        new_handle = f"{node.node_id}.{new_handle}"
                                        deconnections.append(
                                            (src, data["src_handle"], tgt, tgt_handle)
                                        )
                                        connections.append(
                                            (src, data["src_handle"], tgt, new_handle)
                                        )

        for deconnection in deconnections:
            self.disconnect_nodes(*deconnection)
        # need to refresh schemas for subflows here, but not before, otherwise it won't manage
        # to do the disconnections
        for subflow in subflows:
            subflow._set_schemas()

        for connection in connections:
            self.connect_nodes(*connection)

    def refresh_connections(
        self, node, before_model_fields, after_model_fields, mode: str
    ):
        assert mode in ("source", "target")

        before_handle_ids = {
            (handle_field.json_schema_extra or {}).get(
                "handle_id", handle_name
            ): handle_name
            for handle_name, handle_field in before_model_fields.items()
        }
        after_handle_ids = {
            (handle_field.json_schema_extra or {}).get(
                "handle_id", handle_name
            ): handle_name
            for handle_name, handle_field in after_model_fields.items()
        }

        removed_handles, added_handles = [], []
        renamed_handles = {}
        for handle_id, handle_name in before_handle_ids.items():
            after_handle_name = after_handle_ids.get(handle_id)
            if after_handle_name is None:
                removed_handles.append(handle_name)
            elif handle_name != after_handle_name:
                renamed_handles[handle_name] = after_handle_name
                added_handles.append(after_handle_name)  # need to propagate

        for handle_id, handle_name in after_model_fields.items():
            if handle_id not in before_handle_ids:
                added_handles.append(handle_id)

        for removed_handle in removed_handles:
            self.disconnect_all_nodes_connected_to(node.node_id, removed_handle, mode)
        if renamed_handles:
            self.rename_handles(node, renamed_handles, mode)
        for added_handle in added_handles:
            self.propagate_new_handle_to_subflows(node, added_handle, mode)
