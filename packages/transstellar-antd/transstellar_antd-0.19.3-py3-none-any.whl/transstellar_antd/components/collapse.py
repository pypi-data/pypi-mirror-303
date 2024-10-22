from transstellar.framework import Element


class Collapse(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-collapse ")]'

    def get_items(self):
        collapse_elements = self.find_elements(CollapseItem)

        return collapse_elements

    def find_item(self, header: str):
        collapse_element = self.find_element_by_label(CollapseItem, header)

        return collapse_element


class CollapseItem(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-collapse-item")]'
    XPATH_HEADER = '//div[@class="ant-collapse-header"]'
    XPATH_CONTENT = '//div[contains(@class, "ant-collapse-content")]'

    def click(self):
        self.get_header().click()
        self.sleep(1)

    def is_expanded(self):
        header = self.get_header()
        expanded_text = header.get_attribute("aria-expanded")

        return expanded_text == "true"

    def get_header(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_HEADER)

        return dom_element

    def get_header_text(self):
        dom_element = self.get_header()

        return dom_element.text

    def get_content(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_CONTENT)

        return dom_element

    def get_content_text(self):
        dom_element = self.get_content()

        return dom_element.text
