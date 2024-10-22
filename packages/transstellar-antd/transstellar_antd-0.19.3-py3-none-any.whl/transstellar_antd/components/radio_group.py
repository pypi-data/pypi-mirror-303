from transstellar.framework import Element


class RadioGroup(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-radio-group")]'

    def is_enabled(self):
        radios = self.find_elements(Radio)

        return next((radio for radio in radios if radio.is_enabled()), False)

    def select(self, value):
        self.logger.info(f"Select radio: {value}")

        radio = self.find_element_by_label(Radio, value)
        radio.select()

    def get_current_item_text(self):
        dom_element = self.find_dom_element_by_xpath(Radio.XPATH_CHECKED)

        return dom_element.text


class Radio(Element):
    XPATH_CURRENT = '//label[contains(@class, "ant-radio-button-wrapper")]'
    XPATH_CHECKED = '//label[contains(@class, "ant-radio-button-wrapper-checked")]'

    def is_enabled(self):
        return "ant-radio-button-wrapper-disabled" not in self.get_classes()

    def select(self):
        self.click()
        self.sleep(2)

        assert "ant-radio-button-wrapper-checked" in self.get_classes()
