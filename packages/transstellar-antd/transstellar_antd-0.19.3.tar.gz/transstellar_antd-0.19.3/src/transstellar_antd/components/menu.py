from transstellar.framework import Element


class Menu(Element):
    XPATH_CURRENT = '//ul[contains(@class, "ant-menu ")]'
    XPATH_CURRENT_ITEM_TITLE = '//li[contains(@class, "ant-menu-item-selected")]'
    XPATH_TARGET_ITEM_TEMPLATE = (
        '//li[contains(@class, "ant-menu-item") and contains(.//text(), "{title}")]'
    )

    def select(self, text):
        self.logger.info(f"selecting text: {text}")

        self.get_current_dom_element().click()

        select_item = self.find_global_dom_element_by_xpath(
            self.XPATH_TARGET_ITEM_TEMPLATE.format(title=text)
        )
        select_item.click()

        # NOTE: need to find a better way to assert account has been totally changed
        self.sleep(0.5)

    def get_current_item_title(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_CURRENT_ITEM_TITLE)

        return dom_element.text
