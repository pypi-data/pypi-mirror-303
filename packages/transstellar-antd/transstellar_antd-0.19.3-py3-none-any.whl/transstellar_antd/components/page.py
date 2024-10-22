import time

from transstellar.framework import BasePage

from .message import Message


class Page(BasePage):
    MESSAGE_CLASS = Message

    def get_ant_message(self) -> str:
        message_element: Message = self.find_global_element(self.MESSAGE_CLASS)

        return message_element.get_content()

    def wait_until_ant_message(self, message: str, timeout: int = 10) -> str:
        start_time = time.time()

        while True:
            current_time = time.time()

            if current_time - start_time > timeout:
                raise TimeoutError(f"could not find message: {message}")

            if self.get_ant_message() == message:
                return message

            time.sleep(1)
