from transstellar.framework import Element


class Upload(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-upload ant-upload-select")]'

    def is_enabled(self):
        element = self.find_dom_element_by_xpath("//button")

        return element.get_attribute("disabled") is None
