from ...components import Upload as BaseUpload


class Upload(BaseUpload):
    XPATH_INNER = '//span[contains(@class, "ant-upload")]'

    def is_enabled(self):
        element = self.find_dom_element_by_xpath(self.XPATH_INNER)
        classes = element.get_attribute("class")

        return "ant-upload-disabled" not in classes
