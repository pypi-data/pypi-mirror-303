from transstellar.framework import Element


class Message(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-message ")]/div/div'

    def get_content(self):
        return self.get_current_dom_element().get_attribute("textContent")
