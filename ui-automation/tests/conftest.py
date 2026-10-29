"""
pytest配置文件
包含fixture：浏览器驱动初始化、登录前置、截图等
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    """
    浏览器驱动fixture（每个测试函数独立驱动）
    测试结束后自动关闭浏览器
    """
    chrome_options = Options()
    # 无头模式（CI环境使用，本地调试可注释掉）
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)  # 隐式等待10秒
    driver.maximize_window()

    yield driver

    # 测试结束后关闭浏览器
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    已登录的浏览器驱动fixture
    自动完成登录，测试用例直接使用
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    测试失败时自动截图
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver:
            import os
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{item.name}_failed.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n失败截图已保存: {screenshot_path}")
