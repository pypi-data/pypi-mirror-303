from transstellar.framework import Element


class Tab(Element):
    XPATH_CURRENT = (
        '//div[contains(@class, "ant-tabs")]//div[contains(@class, "ant-tabs-tab")]'
    )

    def click(self):
        self.get_current_dom_element().click()
