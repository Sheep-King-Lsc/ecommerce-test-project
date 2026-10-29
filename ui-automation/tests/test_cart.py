"""
购物车功能测试用例
覆盖：添加、删除、数量、空购物车等场景
"""
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class TestCart:
    """购物车功能测试类"""

    def test_add_product_to_cart(self, logged_in_driver):
        """TC-CART-001: 添加商品到购物车"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()

        assert cart_page.get_cart_item_count() == 1, "购物车商品数量不正确"

    def test_remove_product_from_cart(self, logged_in_driver):
        """TC-CART-002: 从购物车移除商品"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        # 添加商品
        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        assert cart_page.get_cart_item_count() == 1

        # 移除商品
        cart_page.remove_first_item()
        assert cart_page.is_cart_empty(), "购物车未清空"

    def test_cart_item_name_matches(self, logged_in_driver):
        """TC-CART-003: 购物车商品名称与商品列表一致"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        # 获取第一个商品名称
        product_names = product_page.get_product_names()
        first_product = product_names[0]

        # 添加到购物车
        product_page.add_first_product_to_cart()
        product_page.go_to_cart()

        cart_names = cart_page.get_item_names()
        assert first_product in cart_names, f"购物车商品名称不匹配: 预期{first_product}, 实际{cart_names}"

    def test_continue_shopping(self, logged_in_driver):
        """TC-CART-004: 继续购物返回商品列表"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.continue_shopping()

        # 验证回到商品列表
        assert product_page.get_product_count() > 0, "未返回商品列表页"

    def test_cart_total_quantity(self, logged_in_driver):
        """TC-CART-005: 购物车总数量正确"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        # 添加两个不同商品
        product_page.add_product_by_index(0)
        product_page.add_product_by_index(1)
        product_page.go_to_cart()

        total = cart_page.get_total_quantity()
        assert total == 2, f"购物车总数量不正确: 预期2, 实际{total}"
