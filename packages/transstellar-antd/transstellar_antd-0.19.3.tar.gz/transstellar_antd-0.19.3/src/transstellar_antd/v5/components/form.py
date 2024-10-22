from ...components import Form as BaseForm
from .checkbox import Checkbox
from .form_item import FormItem
from .input import Input
from .select import Select
from .switch import Switch
from .text_area import TextArea


class Form(BaseForm):
    INPUT_CLASS = Input
    TEXT_AREA_CLASS = TextArea
    SELECT_CLASS = Select
    SWITCH_CLASS = Switch
    CHECKBOX_CLASS = Checkbox
    FORM_ITEM_CLASS = FormItem
