from plurally.models.source.constant import Text


class Hubspot(Text):
    ICON = "hubspot"


class SalesForce(Text):
    ICON = "salesforce"


__all__ = ["Hubspot", "SalesForce"]
