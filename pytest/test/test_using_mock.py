from src import mock

def get_json_data_mock(id):
    return {'name':'田中'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        # 第1引数：モックに差し替えたい関数のモジュール
        # 第2引数：モックに差し替えたい関数名の文字列
        # 第3引数：実際に置き換えるモックの関数
        mock, 'get_json_data', get_json_data_mock
    )
    result = mock.get_user_names(['001', '009'])
    
    assert list(result.keys()) == ['001', '009']
    assert list(result.values()) == ['田中', '田中']