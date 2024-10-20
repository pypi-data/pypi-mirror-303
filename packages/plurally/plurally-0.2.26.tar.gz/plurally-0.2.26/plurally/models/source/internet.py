import requests
from pydantic import Field

from plurally.models.misc import Table
from plurally.models.node import Node


class ScrapePageBase(Node):
    class OutputSchema(Node.OutputSchema):
        content: str = Field(
            title="Content",
            description="The content of the page",
        )

    def _get_html_content(self, url):
        req = requests.get(url)
        req.raise_for_status()

        return req.text

    def scrape(self, url, selector):
        from bs4 import BeautifulSoup

        req = requests.get(url)
        req.raise_for_status()

        html_content = self._get_html_content(url)

        soup = BeautifulSoup(html_content, "html.parser")
        selected = soup.select_one(selector)
        if selected is None:
            self.outputs = {"content": ""}
        else:
            content = selected.get_text()
            self.outputs = {"content": content}


class ScrapePageDynamic(ScrapePageBase):

    ICON = "scrape-one"

    class InitSchema(Node.InitSchema):
        """Scrape the content of a webpage, with dynamic inputs"""

    class InputSchema(Node.InputSchema):
        url: str = Field(
            title="URL",
            description="The URL of the page to scrape",
            examples=["https://example.com"],
        )
        selector: str = Field(
            "body",
            title="Selector",
            description="The selector to use to scrape the content, defaults to 'body' which will scrape the entire page",
            examples=["h1"],
        )

    DESC = InitSchema.__doc__

    def forward(self, node_inputs):
        return self.scrape(node_inputs.url, node_inputs.selector)


class ScrapePagesDynamic(ScrapePageBase):
    ICON = "scrape-many"

    class InitSchema(Node.InitSchema):
        """Scrape the content of multiple webpages.\n\nEach row in the input table should contain a url and a selector.\n\nInput columns should be named 'url' and 'selector'. The output will be a table with the content of the pages, with one column named 'content'."""

    class InputSchema(Node.InputSchema):
        urls_and_selectors: Table = Field(
            title="URLs and Selectors",
            description="The urls and selectors to use to scrape the content",
        )

    class OutputSchema(Node.OutputSchema):
        contents: Table = Field(
            title="Contents",
            description="The contents of the pages, with one column named 'content'.",
        )

    DESC = InitSchema.__doc__

    def forward(self, node_inputs):
        urls_and_selectors = node_inputs.urls_and_selectors
        if urls_and_selectors.is_empty():
            self.outputs = {"contents": Table(data=[])}
            return

        contents = []
        if not all(col in urls_and_selectors.columns for col in ["url", "selector"]):
            raise ValueError("Input table must have columns 'url' and 'selector'")

        for row in urls_and_selectors.data:
            url = row["url"]
            selector = row["selector"]
            self.scrape(url, selector)
            contents.append({"content": self.outputs["content"]})
        self.outputs = {"contents": Table(data=contents)}


class ScrapePageStatic(ScrapePageBase):
    ICON = "scrape-one"

    class InitSchema(Node.InitSchema):
        """Scrape the content of a webpage, with static inputs"""

        url: str = Field(
            title="URL",
            description="The URL of the page to scrape",
            examples=["https://example.com"],
            min_length=1,
            json_schema_extra={
                "uiSchema": {
                    "ui:widget": "url",
                    "ui:placeholder": "https://example.com",
                }
            },
        )
        selector: str = Field(
            "body",
            title="Selector",
            description="The selector to use to scrape the content, defaults to 'body' which will scrape the entire page",
            examples=["h1"],
            min_length=1,
            json_schema_extra={
                "uiSchema": {
                    "ui:placeholder": "Html selector, e.g. h1. If not sure use 'body'.",
                }
            },
        )

    class InputSchema(Node.InputSchema): ...

    DESC = InitSchema.__doc__

    def __init__(self, init_inputs: InitSchema, outputs=None):
        self.url = init_inputs.url
        self.selector = init_inputs.selector
        super().__init__(init_inputs, outputs)

    def forward(self, _: Node.InputSchema):
        return self.scrape(self.url, self.selector)

    def serialize(self):
        return super().serialize() | {
            "url": self.url,
            "selector": self.selector,
        }


__all__ = ["ScrapePageDynamic", "ScrapePageStatic", "ScrapePagesDynamic"]
