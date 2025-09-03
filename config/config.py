import os
import yaml
from dotenv import load_dotenv  #需要安装python-dotenv

#加载环境变量
load_dotenv()

# 读取YAML配置
with open(os.path.join(os.path.dirname(__file__), "env_config.yaml"), encoding="utf-8") as f:
    env_config = yaml.safe_load(f)

# 获取当前环境（默认测试环境）
current_env = os.getenv("TEST_ENV", "testing")

# 环境配置导出
BASE_URL = env_config[current_env]["base_url"]
TIMEOUT = env_config[current_env]["timeout"]
API_KEY = os.getenv("API_KEY")  # 从环境变量获取敏感信息
BASE_URL = "http://101.89.127.196:12001"
API_KEY = "your_api_key_here"
token = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjE1MTg3OTgwOTc1OTEyMTQwODAsImlhdCI6MTc1NjcxNTc0NSwianRpIjoidG9rZW5JZCJ9.fA9gJCp5S27vQ2jhndIdGwcnHnn5m3NURruFORVvs2Y"


