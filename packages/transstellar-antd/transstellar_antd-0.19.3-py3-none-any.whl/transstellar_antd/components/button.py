from transstellar.framework import Element


class Button(Element):
    XPATH_CURRENT = '//button[contains(@class, "ant-btn")]'

    def is_enabled(self):
        return self.get_current_dom_element().get_attribute("disabled") is None

    def click(self):
        self.dom_element.click()

    def get_text(self) -> str:
        return self.dom_element.text
