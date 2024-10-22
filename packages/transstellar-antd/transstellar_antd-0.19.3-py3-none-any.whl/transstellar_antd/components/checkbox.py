from transstellar.framework import Element


class Checkbox(Element):
    XPATH_CURRENT = '//label[contains(@class, "ant-checkbox-wrapper")]'
    XPATH_CHECKBOX = '//span[contains(@class, "ant-checkbox")]'

    def get_checkbox_dom_element(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_CHECKBOX)

        return dom_element

    def is_enabled(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_CHECKBOX)

        return "ant-checkbox-disabled" not in dom_element.get_attribute("class")

    def check(self, on: bool):
        self.logger.info(f"check on: {on}")

        ant_checkbox = self.get_checkbox_dom_element()
        class_names = ant_checkbox.get_attribute("class")
        current_checked = "ant-checkbox-checked" in class_names.split()

        should_click = (not current_checked and on) or (current_checked and not on)
        self.logger.debug(
            f"current_checked: {current_checked}, should_click: {should_click}, on: {on}"
        )

        if should_click:
            ant_checkbox.click()

        current_checked = ant_checkbox.get_attribute("aria-checked")

        updated_class_names = ant_checkbox.get_attribute("class")
        current_checked = "ant-checkbox-checked" in updated_class_names.split()

        assert current_checked == on
