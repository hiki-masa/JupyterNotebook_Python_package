import pytest
from src import exception

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        exception.user_name_validation(None)
    assert str(e.value) == '名前が設定されていません'