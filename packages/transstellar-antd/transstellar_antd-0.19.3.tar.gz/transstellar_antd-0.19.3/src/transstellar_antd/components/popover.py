from transstellar.framework import Element


class Popover(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-popover ")]'
    XPATH_POPOVER_TITLE = '//div[@class="ant-popover-title"]'

    def is_opened(self):
        return "ant-popover-hidden" not in self.get_classes()

    def get_title(self):
        title_element = self.find_dom_element_by_xpath(self.XPATH_POPOVER_TITLE)

        return title_element.text
