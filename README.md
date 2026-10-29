# 电商平台综合测试项目

## 项目简介

基于公开测试环境（SauceDemo Web 商城 + JSONPlaceholder REST API）开展的全流程测试实践项目，覆盖**功能测试、接口测试、UI自动化测试、性能测试**四个维度，从测试计划制定到测试报告输出完整闭环。

> 测试对象：https://www.saucedemo.com（Web UI 自动化）和 https://jsonplaceholder.typicode.com（接口测试），均为公开可访问的测试环境，可直接运行验证。

## 技术栈

| 维度 | 技术/工具 |
|------|-----------|
| 功能测试 | 测试用例设计（等价类 / 边界值 / 场景法） |
| 接口测试 | Postman、RESTful API、HTTP 协议 |
| UI自动化 | Python + Selenium + pytest + PO 模式 |
| 性能测试 | JMeter、聚合报告、并发测试 |
| 版本管理 | Git + GitHub |

## 项目结构

```
project1-ecommerce-test/
├── README.md                    # 项目说明（本文件）
├── docs/                        # 测试文档
│   ├── 测试计划.md              # 测试计划
│   ├── 测试用例.csv             # 功能测试用例（120条）
│   ├── 缺陷报告.md              # 缺陷记录
│   └── 测试总结报告.md          # 测试总结
├── interface-test/              # 接口测试
│   └── 接口测试用例.csv         # 接口测试用例（35条）
├── ui-automation/               # UI自动化测试
│   ├── base/
│   │   └── base_page.py         # 页面对象基类
│   ├── pages/                   # 页面对象
│   │   ├── login_page.py
│   │   ├── product_page.py
│   │   ├── cart_page.py
│   │   └── order_page.py
│   ├── tests/                   # 测试用例
│   │   ├── conftest.py
│   │   ├── test_login.py
│   │   ├── test_product.py
│   │   ├── test_cart.py
│   │   └── test_order.py
│   ├── config/
│   │   └── config.py            # 配置文件
│   ├── reports/                 # 测试报告（运行 pytest 后生成）
│   ├── requirements.txt
│   └── pytest.ini
└── performance-test/            # 性能测试
    └── 性能测试报告.md          # 性能测试报告（JMeter）
```

## 测试成果概览

- 设计功能测试用例 **120+条**，覆盖登录、商品、购物车、结算全流程
- 编写接口测试用例 **35条**，覆盖用户、帖子、待办事项等核心业务接口的正常与异常场景
- 搭建 Selenium + pytest UI 自动化框架（PO 模式），编写 **26条**自动化用例，覆盖登录、商品、购物车、结算全流程
- 使用 JMeter 对登录、下单接口开展 **10 / 50 / 100 并发**性能测试，输出完整性能分析报告
- 所有测试文档、用例、报告均在本仓库可查

## 快速开始

### UI自动化运行

```bash
cd ui-automation
pip install -r requirements.txt
pytest tests/ --html=reports/report.html
```

### 接口测试

1. 打开 Postman → 根据 `interface-test/接口测试用例.csv` 手动创建 Collection
2. 或直接对 https://jsonplaceholder.typicode.com 执行对应请求
3. 使用 Newman 命令行批量执行：
```bash
newman run collection.json -r html
```

### 性能测试

使用 JMeter 创建线程组（并发数参数化 10 / 50 / 100），对登录、下单接口加压，配置聚合报告监听器，输出结果详见 `performance-test/性能测试报告.md`。
