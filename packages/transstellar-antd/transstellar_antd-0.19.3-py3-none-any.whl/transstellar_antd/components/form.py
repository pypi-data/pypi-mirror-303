from transstellar.framework import Element

from .checkbox import Checkbox
from .form_item import FormItem
from .input import Input
from .select import Select
from .switch import Switch
from .text_area import TextArea


class Form(Element):
    XPATH_CURRENT = "//form"
    INPUT_CLASS = Input
    TEXT_AREA_CLASS = TextArea
    SELECT_CLASS = Select
    SWITCH_CLASS = Switch
    CHECKBOX_CLASS = Checkbox
    FORM_ITEM_CLASS = FormItem

    def input(self, form_item_label: str, value: str):
        input_element: Input = self.find_element_by_form_item_label(
            self.INPUT_CLASS, form_item_label
        )
        input_element.input(value)

    def text_area_input(self, form_item_label: str, value: str):
        text_area_element: TextArea = self.find_element_by_form_item_label(
            self.TEXT_AREA_CLASS,
            form_item_label,
        )
        text_area_element.input(value)

    def select(self, form_item_label: str, value: str):
        select_element: Select = self.find_element_by_form_item_label(
            self.SELECT_CLASS,
            form_item_label,
        )
        select_element.select(value)

    def switch(self, form_item_label: str, on: bool):
        switch_element: Switch = self.find_element_by_form_item_label(
            self.SWITCH_CLASS,
            form_item_label,
        )
        switch_element.switch(on)

    def check(self, form_item_label: str, on: bool):
        checkbox_element: Checkbox = self.find_element_by_form_item_label(
            self.CHECKBOX_CLASS,
            form_item_label,
        )
        checkbox_element.check(on)

    def direct_check(self, label: str, on: bool):
        checkbox_element: Checkbox = self.find_element_by_label(
            self.CHECKBOX_CLASS, label
        )
        checkbox_element.check(on)

    def find_element_by_form_item_label(self, element_class, form_item_label: str):
        form_item: FormItem = self.find_element_by_label(
            self.FORM_ITEM_CLASS, form_item_label
        )
        element: element_class = form_item.find_form_control(element_class)

        return element

    def is_form_item_present(self, form_item_label: str):
        try:
            self.find_element_by_label(self.FORM_ITEM_CLASS, form_item_label)

            return True
        except Exception:
            return False
