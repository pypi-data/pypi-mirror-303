from transstellar.framework import Element

from .button import Button


class PopoverConfirm(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-popover ant-popconfirm")]'
    XPATH_POPOVER_TITLE = '//div[@class="ant-popover-message-title"]'
    BUTTON_CLASS = Button

    def get_popover_confirm_xpath(self, message):
        return f'{self.XPATH_CURRENT} and {self.XPATH_POPOVER_TITLE}//button[contains(span/text(), "{message}")]'

    def click(self, button_text):
        self.logger.info(f"click {button_text} in popover confirm")
        button: Button = self.find_element_by_label(self.BUTTON_CLASS, button_text)

        # NOTE: need time to be clickable
        self.sleep(0.5)

        button.click()
