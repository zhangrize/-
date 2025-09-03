import pytest
from utils.request_util import api_get
from utils.data_util import load_json_data
from business.user_business import UserBusiness  # 业务层封装

@pytest.mark.smoke
@pytest.mark.parametrize("user_id", load_json_data("user_data.json")["valid_users"])
def test_user_query_success(user_id):
    user_info = UserBusiness.get_user_info(user_id)
    assert user_info["id"] == user_id
def test_get_status_code():
    response = api_get("health")
    assert response.status_code == 200

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_query(user_id):
    response = api_get(f"users/{user_id}")
    assert response.json()["id"] == user_id
