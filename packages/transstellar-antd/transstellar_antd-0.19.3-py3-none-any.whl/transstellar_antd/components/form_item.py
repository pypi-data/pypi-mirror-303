from urllib.parse import urlparse

from transstellar.framework import Element


class FormItem(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-form-item ")]'

    def find_form_control(self, element_class):
        self.logger.info(
            f"finding form control element with label: {self.label}, element: {element_class.__name__}"
        )

        return self.find_element(element_class)
