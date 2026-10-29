"""
页面对象基类
封装Selenium常用操作，所有页面对象继承此类
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 显式等待10秒

    def open_url(self, url):
        """打开URL"""
        self.driver.get(url)

    def find_element(self, locator):
        """
        定位单个元素（显式等待元素可见）
        :param locator: 元组 (By.ID, "id值")
        :return: 元素对象
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        """定位多个元素"""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """点击元素"""
        self.find_element(locator).click()

    def input_text(self, locator, text):
        """输入文本（先清空再输入）"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取元素文本"""
        return self.find_element(locator).text

    def get_attribute(self, locator, name):
        """获取元素属性"""
        return self.find_element(locator).get_attribute(name)

    def is_element_visible(self, locator, timeout=3):
        """判断元素是否可见（不抛异常）"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def switch_to_frame(self, locator):
        """切换到iframe"""
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def switch_to_default_content(self):
        """切回主文档"""
        self.driver.switch_to.default_content()

    def get_current_url(self):
        """获取当前URL"""
        return self.driver.current_url

    def get_title(self):
        """获取页面标题"""
        return self.driver.title

    def take_screenshot(self, filepath):
        """截图"""
        self.driver.save_screenshot(filepath)

    def scroll_to_element(self, locator):
        """滚动到元素位置"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def accept_alert(self):
        """接受弹窗"""
        self.wait.until(EC.alert_is_present()).accept()

    def dismiss_alert(self):
        """取消弹窗"""
        self.wait.until(EC.alert_is_present()).dismiss()
