import pytest
import os

if __name__ == "__main__":
    pytest.main()
    os.system("allure serve allure-results")  # 生成Allure报告
