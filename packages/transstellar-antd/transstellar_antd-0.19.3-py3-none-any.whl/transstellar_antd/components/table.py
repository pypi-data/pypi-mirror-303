from typing import List, Union

from selenium.webdriver.common.by import By
from transstellar.framework import Element

from .row import Row


class Table(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-table-wrapper")]//div[contains(@class, "ant-table")]'
    SELECTOR_TABLE_HEADER = "thead.ant-table-thead th.ant-table-cell"
    SELECTOR_ROW = "tbody.ant-table-tbody tr.ant-table-row"
    ROW_CLASS = Row

    rows: List[Row]
    column_titles = {}

    def init_after_dom_element_is_set(self):
        header_columns = self.dom_element.find_elements(
            By.CSS_SELECTOR, self.SELECTOR_TABLE_HEADER
        )

        for index, column in enumerate(header_columns):
            column_name = column.get_attribute("innerHTML").strip()

            # Sometimes there is a column used as scrollbar
            if column_name == "":
                continue

            self.column_titles[column_name] = index

        if not self.is_empty():
            self.rows = self.find_elements(self.ROW_CLASS)

            for row in self.rows:
                row.set_column_titles(self.column_titles)

    def is_empty(self):
        classes = self.get_current_dom_element().get_attribute("class")

        return "ant-table-empty" in classes

    def find_row(self, column_title: str, column_text: str) -> Union[None, Row]:
        self.logger.info(f"finding row with column {column_title}: {column_text}")

        column_index = self.column_titles[column_title]

        if column_index is not None:
            for row in self.rows:
                if row.get_cell_text(column_title) == str(column_text):
                    self.logger.debug(
                        f"found row with column {column_title} as {column_text}"
                    )

                    return row

        raise LookupError(
            f"could not find row with column {column_title} as {column_text}"
        )

    def get_row(self, index: int):
        self.logger.info(f"finding row by index: {index}")

        return self.rows[index]
