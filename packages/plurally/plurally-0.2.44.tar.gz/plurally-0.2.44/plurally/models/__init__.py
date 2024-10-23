from plurally.models import calendar  # noqa: F403
from plurally.models import crm  # noqa: F403
from plurally.models import email  # noqa: F403
from plurally.models import eshop  # noqa: F403
from plurally.models import instagram  # noqa: F403
from plurally.models import logic  # noqa: F403
from plurally.models import table  # noqa: F403
from plurally.models import triggers  # noqa: F403
from plurally.models.action import ai  # noqa: F403
from plurally.models.action import arithmetic  # noqa: F403
from plurally.models.action import format  # noqa: F403
from plurally.models.action.ai import *  # noqa: F403
from plurally.models.action.arithmetic import *  # noqa: F403
from plurally.models.action.format import *  # noqa: F403
from plurally.models.email import *  # noqa: F403
from plurally.models.instagram import *  # noqa: F403
from plurally.models.logic import *  # noqa: F403
from plurally.models.meta import *  # noqa: F403
from plurally.models.node import Node, get_inner_type  # noqa: F401
from plurally.models.source import constant  # noqa: F403
from plurally.models.source import internet  # noqa: F403
from plurally.models.source.constant import *  # noqa: F403
from plurally.models.source.email_imap import *  # noqa: F403
from plurally.models.source.internet import *  # noqa: F403
from plurally.models.source.schedule import *  # noqa: F403
from plurally.models.table import *  # noqa: F403

GROUPS = [
    ("Triggers", triggers),
    ("AI", ai),
    ("Email", email),
    ("Instagram", instagram),
    ("Data", table),
    ("Scraping", internet),
    ("Calendar", calendar),
    ("CRM", crm),
    ("Eshop", eshop),
    ("Transforms & Validators", format),
    ("Constant Value", constant),
    ("Logic", logic),
    ("Maths", arithmetic),
]

# This is a hack to avoid circular imports
from plurally.models.flow import Flow  # noqa: F401, E402
from plurally.models.subflow import Subflow  # noqa: F401, E402
