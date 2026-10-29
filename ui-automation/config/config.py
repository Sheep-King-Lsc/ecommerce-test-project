"""
配置文件
存放测试环境URL、账号密码等配置
"""


class Config:
    # 测试环境
    BASE_URL = "https://www.saucedemo.com/"
    API_BASE_URL = "https://jsonplaceholder.typicode.com"

    # 测试账号（saucedemo公开测试账号）
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"

    # 锁定账号（测试锁定场景）
    LOCKED_USERNAME = "locked_out_user"

    # 问题账号（会有图片加载问题）
    PROBLEM_USERNAME = "problem_user"

    # 超时设置
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15

    # 性能测试配置
    PERF_CONCURRENCY = [10, 50, 100]
    PERF_RAMP_UP = 10  # 秒
