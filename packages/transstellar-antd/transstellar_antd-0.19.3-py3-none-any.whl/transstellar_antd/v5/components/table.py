from ...components import Table as BaseTable
from .row import Row


class Table(BaseTable):
    ROW_CLASS = Row

    pass
