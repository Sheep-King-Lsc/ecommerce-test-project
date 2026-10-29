"""
登录页面对象
封装登录页面的元素和操作
"""
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    # 元素定位器
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    TITLE = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        """打开登录页"""
        self.open_url(self.url)

    def login(self, username, password):
        """
        执行登录操作
        :param username: 用户名
        :param password: 密码
        """
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """获取登录错误提示"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_success(self):
        """判断是否登录成功（通过页面标题）"""
        return self.is_element_visible(self.TITLE)

    def get_page_title(self):
        """获取登录后的页面标题"""
        return self.get_text(self.TITLE)
