from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from transstellar.framework import Element


class DatePicker(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-picker-input")]/ancestor::div[contains(@class, "ant-picker")]'

    XPATH_INPUT = '//div[contains(@class, "ant-picker-input")]/input'

    def pick_date(self, target_date, is_datetime=False):
        self.logger.info(f"pick date: {target_date}")

        dom_element = self.find_dom_element_by_xpath(self.XPATH_INPUT)

        self.__update_date(dom_element, target_date, is_datetime)

    def pick_date_range(self, from_date, to_date, is_datetime=False):
        self.logger.info(f"pick date range, from: {from_date}, to: {to_date}")

        inputs = self.find_dom_elements_by_tag_name("input")
        from_date_input = inputs[0]
        to_date_input = inputs[1]

        self.__update_date(from_date_input, from_date, is_datetime)
        self.__update_date(to_date_input, to_date, is_datetime)

    def get_basic_date_value(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_INPUT)

        return dom_element.get_attribute("value")

    def get_date_range_values(self):
        inputs = self.find_dom_elements_by_tag_name("input")

        return [inputs[0].get_attribute("value"), inputs[1].get_attribute("value")]

    def __update_date(self, input_element, date, is_datetime=False):
        date_format = "%Y-%m-%d"

        if is_datetime:
            date_format = "%Y-%m-%d %H:%M:%S"

        formatted_date = date.strftime(date_format)

        input_element.click()

        # Wait for calendar to show
        self.sleep(3)

        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(formatted_date)
        input_element.send_keys(Keys.ENTER)

        # Wait for calendar to hide
        self.sleep(3)

        new_value = input_element.get_attribute("value")

        assert new_value == formatted_date

        return new_value
