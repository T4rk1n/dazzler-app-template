from dazzler.system import Page
from dazzler.components import core

page = Page(
    __name__,
    core.Container('home'),
    url='/',
)
