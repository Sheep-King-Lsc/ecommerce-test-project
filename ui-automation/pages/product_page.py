"""
商品列表页面对象
封装商品列表、排序、详情等操作
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductPage(BasePage):
    # 元素定位器
    PRODUCT_LIST = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id*='add-to-cart']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_product_count(self):
        """获取商品数量"""
        return len(self.find_elements(self.PRODUCT_LIST))

    def get_product_names(self):
        """获取所有商品名称列表"""
        elements = self.find_elements(self.PRODUCT_NAME)
        return [elem.text for elem in elements]

    def get_product_prices(self):
        """获取所有商品价格列表（转为float）"""
        elements = self.find_elements(self.PRODUCT_PRICE)
        return [float(elem.text.replace("$", "")) for elem in elements]

    def add_first_product_to_cart(self):
        """将第一个商品加入购物车"""
        self.find_elements(self.ADD_TO_CART_BTN)[0].click()

    def add_product_by_index(self, index):
        """按索引添加商品到购物车"""
        buttons = self.find_elements(self.ADD_TO_CART_BTN)
        if index < len(buttons):
            buttons[index].click()

    def get_cart_count(self):
        """获取购物车商品数量"""
        if self.is_element_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        """进入购物车"""
        self.click(self.CART_LINK)

    def sort_by(self, value):
        """
        排序
        :param value: "az"名称A-Z, "za"名称Z-A, "lohi"价格低到高, "hilo"价格高到低
        """
        from selenium.webdriver.support.ui import Select
        dropdown = self.find_element(self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(value)

    def logout(self):
        """退出登录"""
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
