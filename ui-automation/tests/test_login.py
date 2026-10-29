"""
登录功能测试用例
覆盖：正常登录、错误密码、空值、锁定账号等场景
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """登录功能测试类"""

    def test_login_success(self, driver):
        """TC-LOGIN-001: 正确账号密码登录成功"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        # 断言：登录成功后页面标题显示"Products"
        assert login_page.is_login_success(), "登录失败，未跳转到商品页"
        assert login_page.get_page_title() == "Products", "页面标题不正确"

    def test_login_wrong_password(self, driver):
        """TC-LOGIN-002: 错误密码登录失败"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(Config.VALID_USERNAME, "wrong_password")

        # 断言：显示错误提示
        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg, f"错误提示不正确: {error_msg}"

    def test_login_empty_username(self, driver):
        """TC-LOGIN-003: 用户名为空登录失败"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", Config.VALID_PASSWORD)

        error_msg = login_page.get_error_message()
        assert "Username is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_login_empty_password(self, driver):
        """TC-LOGIN-004: 密码为空登录失败"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(Config.VALID_USERNAME, "")

        error_msg = login_page.get_error_message()
        assert "Password is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_login_empty_both(self, driver):
        """TC-LOGIN-005: 用户名密码都为空"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", "")

        error_msg = login_page.get_error_message()
        assert "Username is required" in error_msg, f"错误提示不正确: {error_msg}"

    def test_login_locked_user(self, driver):
        """TC-LOGIN-006: 锁定账号登录失败"""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(Config.LOCKED_USERNAME, Config.VALID_PASSWORD)

        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg.lower(), f"错误提示不正确: {error_msg}"

    def test_login_page_title(self, driver):
        """TC-LOGIN-007: 验证登录页标题"""
        login_page = LoginPage(driver)
        login_page.open()
        assert "Swag Labs" in login_page.get_title(), "页面标题不正确"
