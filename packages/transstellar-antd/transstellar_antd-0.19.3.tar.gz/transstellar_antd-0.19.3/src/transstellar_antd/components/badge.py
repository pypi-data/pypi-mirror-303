from transstellar.framework import Element


class Badge(Element):
    XPATH_CURRENT = '//span[contains(@class, "ant-badge")]'

    def click(self):
        self.dom_element.click()
