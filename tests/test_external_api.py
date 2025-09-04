import json
from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles


@patch("src.external_api.requests.request")
def test_convert_to_rubles_info(mock_request):
    test_data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    # Создаем мок объект ответа
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = json.dumps(
        {
            "date": "2018-02-22",
            "historical": "",
            "info": {"rate": 148.972231, "timestamp": 1519328414},
            "query": {"amount": 31957.58, "from": "USD", "to": "RUB"},
            "result": 2575114.472669,
            "success": True,
        }
    )

    # Настраиваем мок запроса
    mock_request.return_value = mock_response

    # Вызываем функцию и проверяем результат
    result = convert_to_rubles(test_data)
    assert result == 2575114.472669
