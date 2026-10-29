"""
订单/结算页面对象
封装结算流程、订单信息填写等操作
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class OrderPage(BasePage):
    # 结算信息页元素
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 订单确认页元素
    ITEM_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    # 订单完成页元素
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    COMPLETE_TEXT = (By.CSS_SELECTOR, ".complete-text")

    def fill_shipping_info(self, first_name, last_name, postal_code):
        """填写收货信息"""
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        """点击继续"""
        self.click(self.CONTINUE_BUTTON)

    def get_error_message(self):
        """获取错误提示"""
        return self.get_text(self.ERROR_MESSAGE)

    def get_item_total(self):
        """获取商品总价"""
        text = self.get_text(self.ITEM_TOTAL)
        return float(text.split("$")[-1])

    def get_tax(self):
        """获取税费"""
        text = self.get_text(self.TAX)
        return float(text.split("$")[-1])

    def get_total_price(self):
        """获取总价"""
        text = self.get_text(self.TOTAL_PRICE)
        return float(text.split("$")[-1])

    def finish_order(self):
        """完成下单"""
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self):
        """判断订单是否完成"""
        return self.is_element_visible(self.COMPLETE_HEADER)

    def get_complete_message(self):
        """获取订单完成提示"""
        return self.get_text(self.COMPLETE_HEADER)

    def back_to_home(self):
        """返回首页"""
        self.click(self.BACK_HOME_BUTTON)

    def complete_checkout(self, first_name="Test", last_name="User", postal_code="100000"):
        """
        完整结算流程
        :return: 订单是否成功
        """
        self.fill_shipping_info(first_name, last_name, postal_code)
        self.click_continue()
        self.finish_order()
        return self.is_order_complete()
