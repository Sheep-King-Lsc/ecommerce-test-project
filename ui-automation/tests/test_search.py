"""
商品搜索与排序测试用例
覆盖：商品列表、排序、价格验证等场景
"""
import pytest
from pages.product_page import ProductPage


class TestProduct:
    """商品功能测试类"""

    def test_product_list_displayed(self, logged_in_driver):
        """TC-PROD-001: 商品列表正常显示"""
        product_page = ProductPage(logged_in_driver)
        count = product_page.get_product_count()
        assert count > 0, "商品列表为空"
        assert count == 6, f"商品数量不正确，预期6个，实际{count}个"

    def test_product_names_not_empty(self, logged_in_driver):
        """TC-PROD-002: 所有商品名称不为空"""
        product_page = ProductPage(logged_in_driver)
        names = product_page.get_product_names()
        assert len(names) > 0, "没有获取到商品名称"
        for name in names:
            assert name.strip() != "", "存在商品名称为空"

    def test_product_prices_positive(self, logged_in_driver):
        """TC-PROD-003: 所有商品价格为正数"""
        product_page = ProductPage(logged_in_driver)
        prices = product_page.get_product_prices()
        assert len(prices) > 0, "没有获取到商品价格"
        for price in prices:
            assert price > 0, f"商品价格异常: {price}"

    def test_sort_price_low_to_high(self, logged_in_driver):
        """TC-PROD-004: 价格从低到高排序"""
        product_page = ProductPage(logged_in_driver)
        product_page.sort_by("lohi")
        prices = product_page.get_product_prices()
        # 断言价格升序
        assert prices == sorted(prices), f"价格排序不正确: {prices}"

    def test_sort_price_high_to_low(self, logged_in_driver):
        """TC-PROD-005: 价格从高到低排序"""
        product_page = ProductPage(logged_in_driver)
        product_page.sort_by("hilo")
        prices = product_page.get_product_prices()
        # 断言价格降序
        assert prices == sorted(prices, reverse=True), f"价格排序不正确: {prices}"

    def test_sort_name_a_to_z(self, logged_in_driver):
        """TC-PROD-006: 名称A-Z排序"""
        product_page = ProductPage(logged_in_driver)
        product_page.sort_by("az")
        names = product_page.get_product_names()
        assert names == sorted(names), f"名称排序不正确: {names}"

    def test_sort_name_z_to_a(self, logged_in_driver):
        """TC-PROD-007: 名称Z-A排序"""
        product_page = ProductPage(logged_in_driver)
        product_page.sort_by("za")
        names = product_page.get_product_names()
        assert names == sorted(names, reverse=True), f"名称排序不正确: {names}"

    def test_add_to_cart_updates_badge(self, logged_in_driver):
        """TC-PROD-008: 加入购物车后角标更新"""
        product_page = ProductPage(logged_in_driver)
        initial_count = product_page.get_cart_count()
        product_page.add_first_product_to_cart()
        new_count = product_page.get_cart_count()
        assert new_count == initial_count + 1, "购物车数量未更新"
