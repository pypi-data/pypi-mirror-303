from selenium.webdriver.common.keys import Keys
from transstellar.framework import Element


class Input(Element):
    XPATH_CURRENT = '//input[contains(@class, "ant-input")]'

    def is_enabled(self):
        return "ant-input-disabled" not in self.get_classes()

    def input(self, value: str):
        self.logger.info(f"input to value: {value}")

        dom_element = self.get_current_dom_element()
        dom_element.send_keys(Keys.CONTROL + "a")
        dom_element.send_keys(Keys.DELETE)
        dom_element.send_keys(value)

        new_value = self.get_value()

        assert new_value == value

    def append(self, value: str):
        self.logger.info(f"input to value: {value}")

        self.get_current_dom_element().send_keys(value)

    def get_value(self):
        return self.dom_element.get_attribute("value")
