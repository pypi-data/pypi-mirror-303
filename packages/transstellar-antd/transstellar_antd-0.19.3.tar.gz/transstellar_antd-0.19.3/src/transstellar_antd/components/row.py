from selenium.webdriver.common.by import By
from transstellar.framework import Element


class Row(Element):
    XPATH_CURRENT = '//tr[contains(@class, "ant-table-row")]'

    column_titles = {}

    def set_column_titles(self, column_titles):
        self.column_titles = column_titles

    def get_cell_text(self, column_title: str):
        self.logger.debug(f"get cell text of column: {column_title}")

        cell = self.__get_cell_dom_element(column_title)

        return cell.text.strip()

    def find_dom_element_in_cell_by_xpath(self, column_title: str, xpath: str):
        self.logger.debug(
            f"get element in cell of column {column_title} by xpath: {xpath}"
        )
        cell = self.__get_cell_dom_element(column_title)

        dom_element = cell.find_element(By.XPATH, f".{xpath}")

        self.sleep(0.5)

        return dom_element

    def get_cells(self):
        cells = {}

        for column_title in self.column_titles:
            cells[column_title] = self.get_cell_text(column_title)

        return cells

    def __get_cell_dom_element(self, column_name: str):
        self.logger.debug(f"get cell of column {column_name}")

        column_index = self.column_titles[column_name]
        cells = self.find_dom_elements_by_tag_name("td")

        return cells[column_index]
