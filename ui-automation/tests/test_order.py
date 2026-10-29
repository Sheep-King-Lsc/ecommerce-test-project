"""
订单结算流程测试用例
覆盖：完整下单流程、信息校验、金额计算等场景
"""
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage


class TestOrder:
    """订单功能测试类"""

    def test_complete_checkout_flow(self, logged_in_driver):
        """TC-ORDER-001: 完整下单流程成功"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        # 1. 添加商品到购物车
        product_page.add_first_product_to_cart()
        product_page.go_to_cart()

        # 2. 去结算
        cart_page.go_to_checkout()

        # 3. 填写信息并完成下单
        success = order_page.complete_checkout(
            first_name="Test",
            last_name="User",
            postal_code="100000"
        )
        assert success, "订单未成功完成"
        assert "Thank you" in order_page.get_complete_message(), "订单完成提示不正确"

    def test_checkout_empty_first_name(self, logged_in_driver):
        """TC-ORDER-002: 结算时姓名为空"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.go_to_checkout()

        # 不填姓名直接继续
        order_page.fill_shipping_info("", "User", "100000")
        order_page.click_continue()

        error_msg = order_page.get_error_message()
        assert "First Name is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_checkout_empty_last_name(self, logged_in_driver):
        """TC-ORDER-003: 结算时姓氏为空"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.go_to_checkout()

        order_page.fill_shipping_info("Test", "", "100000")
        order_page.click_continue()

        error_msg = order_page.get_error_message()
        assert "Last Name is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_checkout_empty_postal_code(self, logged_in_driver):
        """TC-ORDER-004: 结算时邮编为空"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.go_to_checkout()

        order_page.fill_shipping_info("Test", "User", "")
        order_page.click_continue()

        error_msg = order_page.get_error_message()
        assert "Postal Code is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_order_total_price_calculation(self, logged_in_driver):
        """TC-ORDER-005: 订单金额计算正确"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        # 添加商品
        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.go_to_checkout()

        # 填写信息进入确认页
        order_page.fill_shipping_info("Test", "User", "100000")
        order_page.click_continue()

        # 验证金额：总价 = 商品价 + 税
        item_total = order_page.get_item_total()
        tax = order_page.get_tax()
        total = order_page.get_total_price()

        assert abs(total - (item_total + tax)) < 0.01, \
            f"金额计算错误: 商品价{item_total} + 税{tax} != 总价{total}"

    def test_back_to_home_after_order(self, logged_in_driver):
        """TC-ORDER-006: 下单完成后返回首页"""
        product_page = ProductPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)
        order_page = OrderPage(logged_in_driver)

        product_page.add_first_product_to_cart()
        product_page.go_to_cart()
        cart_page.go_to_checkout()
        order_page.complete_checkout()

        order_page.back_to_home()
        assert product_page.get_product_count() > 0, "未返回商品列表页"
