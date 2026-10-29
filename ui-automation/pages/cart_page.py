"""
购物车页面对象
封装购物车商品管理操作
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class CartPage(BasePage):
    # 元素定位器
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id*='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".cart_list")

    def get_cart_item_count(self):
        """获取购物车商品种类数量"""
        if self.is_element_visible(self.CART_ITEMS):
            return len(self.find_elements(self.CART_ITEMS))
        return 0

    def get_item_names(self):
        """获取购物车所有商品名称"""
        elements = self.find_elements(self.ITEM_NAME)
        return [elem.text for elem in elements]

    def get_total_quantity(self):
        """获取购物车商品总数量"""
        elements = self.find_elements(self.CART_QUANTITY)
        return sum(int(elem.text) for elem in elements)

    def remove_first_item(self):
        """移除第一个商品"""
        if self.is_element_visible(self.REMOVE_BUTTON):
            self.find_elements(self.REMOVE_BUTTON)[0].click()

    def remove_all_items(self):
        """移除所有商品"""
        while self.is_element_visible(self.REMOVE_BUTTON, timeout=2):
            self.find_elements(self.REMOVE_BUTTON)[0].click()

    def continue_shopping(self):
        """继续购物（返回商品列表）"""
        self.click(self.CONTINUE_SHOPPING)

    def go_to_checkout(self):
        """去结算"""
        self.click(self.CHECKOUT_BUTTON)

    def is_cart_empty(self):
        """判断购物车是否为空"""
        return not self.is_element_visible(self.CART_ITEMS, timeout=2)
