from unittest.mock import mock_open, patch

from src.utils import get_list_of_transactions


def test_get_list_of_transactions_success(path, test_data):
    """Тест на успешное получение списка транзакций из json файла"""

    # Мокаем открытие файла и чтение JSON
    with patch("builtins.open", mock_open()) as mock_file:
        with patch("json.load") as mock_json_load:
            # Настраиваем моки
            mock_json_load.return_value = test_data

            # Вызываем тестируемую функцию
            result = get_list_of_transactions(path)

            # Проверяем результаты
            assert result == test_data
            mock_json_load.assert_called_once()
