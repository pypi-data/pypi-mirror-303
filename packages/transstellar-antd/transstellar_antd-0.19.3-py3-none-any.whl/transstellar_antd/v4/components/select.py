from ...components import Select as BaseSelect


class Select(BaseSelect):
    XPATH_TARGET_ITEM_TEMPLATE = (
        '//div[contains(@class, "ant-select-item") and contains(@title, "{title}")]'
    )
