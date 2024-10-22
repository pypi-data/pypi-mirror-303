from ...components import FormItem as BaseFormItem


class FormItem(BaseFormItem):
    XPATH_CURRENT = '//div[contains(@class, "ant-form-item ")]'

    pass
