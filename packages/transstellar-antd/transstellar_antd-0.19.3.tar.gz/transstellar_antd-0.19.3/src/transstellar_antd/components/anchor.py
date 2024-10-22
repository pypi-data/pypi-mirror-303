from transstellar.framework import Element


class Anchor(Element):
    XPATH_CURRENT = "//a"

    def click(self):
        self.dom_element.click()

    def get_text(self) -> str:
        return self.dom_element.text
