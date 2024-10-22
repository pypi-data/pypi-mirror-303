from selenium.webdriver.common.keys import Keys
from transstellar.framework import Element


class Select(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-select ")]'
    XPATH_SELECT_SEARCH = (
        '//input[contains(@class, "ant-select-selection-search-input")]'
    )
    XPATH_CURRENT_ITEM_TITLE = '//span[contains(@class, "ant-select-selection-item")]'
    XPATH_TARGET_ITEM_TEMPLATE = (
        '//div[contains(@class, "ant-select-item") and @title="{title}"]'
    )
    SHOULD_DOUBLE_CLICK = False

    def is_enabled(self):
        return "ant-select-disabled" not in self.get_classes()

    def select(self, text):
        self.logger.info(f"selecting text: {text}")

        self.click()

        select_item = self.find_global_dom_element_by_xpath(
            self.XPATH_TARGET_ITEM_TEMPLATE.format(title=text)
        )
        select_item.click()

        # NOTE: need to find a better way to assert account has been totally changed
        self.sleep(0.5)

    def select_by_search(self, text):
        self.logger.info(f"selecting text: {text}")

        self.get_current_dom_element().click()

        search_input = self.find_dom_element_by_xpath(self.XPATH_SELECT_SEARCH)
        search_input.send_keys(text)
        search_input.send_keys(Keys.RETURN)

        # NOTE: need to find a better way to assert account has been totally changed
        self.sleep(0.5)

    def get_current_item_title(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_CURRENT_ITEM_TITLE)

        return dom_element.get_attribute("title")
