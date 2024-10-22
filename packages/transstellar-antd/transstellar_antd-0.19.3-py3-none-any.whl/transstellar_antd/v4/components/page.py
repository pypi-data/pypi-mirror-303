from ...components import Page as BasePage
from .message import Message


class Page(BasePage):
    MESSAGE_CLASS = Message

    pass
