import re

from selenium.webdriver.common.keys import Keys
from transstellar.framework import Element

from .popover import Popover
from .select import Select


class ColorPicker(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-color-picker-trigger")]'
    XPATH_TRIGGER_COLOR = (
        '//div[contains(@class, "ant-color-picker-color-block-inner")]'
    )

    XPATH_PICKER = '//div[contains(@class, "ant-popover ant-color-picker")]'
    XPATH_COLOR_CODE = '//div[@class="ant-color-picker-input"]//input'

    POPOVER_CLASS = Popover
    SELECT_CLASS = Select

    CODE_TYPE_HEX = "HEX"
    CODE_TYPE_HSB = "HSB"
    CODE_TYPE_RGB = "RGB"

    def is_enabled(self):
        return "ant-color-picker-trigger-disabled" not in self.get_classes()

    def pick_color_by_hex(self, hex_code: str):
        self.logger.info(f"pick color by hex: {hex_code}")

        self.__update_color_by_code(self.CODE_TYPE_HEX, hex_code)

    def get_current_color(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_TRIGGER_COLOR)
        style = dom_element.get_attribute("style")
        hex_code = self.__rgb_to_hex(style)

        return hex_code

    def __update_color_by_code(self, code_type: str, color_code: str):
        self.click()
        # Wait for popover to show
        self.sleep(4)

        self.picker_popover = self.find_global_element(self.POPOVER_CLASS)
        self.code_type_select = self.picker_popover.find_element(self.SELECT_CLASS)
        self.code_type_select.select(code_type)

        input_element = self.picker_popover.find_dom_element_by_xpath(
            self.XPATH_COLOR_CODE
        )

        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(color_code)
        input_element.send_keys(Keys.ENTER)

        # Wait for popover to hide
        self.sleep(3)

        new_value = input_element.get_attribute("value")

        assert new_value.lower() == color_code.lower()

        return new_value

    def __rgb_to_hex(self, rgb_str: str):
        match = re.search(r"rgb\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", rgb_str)
        if not match:
            raise ValueError("Invalid RGB format")

        r, g, b = map(int, match.groups())

        hex_color = f"{r:02x}{g:02x}{b:02x}"

        return hex_color.upper()
