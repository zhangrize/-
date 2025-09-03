import pytest
import allure
import requests

@pytest.fixture(scope="session")
def auth_token():
    # 获取全局token的逻辑
    return "generated_token"
def pytest_runtest_makereport(item, call):
    """用例失败截图"""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        with allure.step("用例失败截图"):
            # 接口测试可添加响应信息
            if hasattr(item, "request"):
                allure.attach(
                    str(item.request.url),
                    name="请求URL",
                    attachment_type=allure.attachment_type.TEXT
                )