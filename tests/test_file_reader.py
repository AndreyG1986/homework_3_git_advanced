from unittest.mock import patch

from src.file_reader import read_xl_file, read_csv_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv, list_for_csv):
    mock_read_csv.return_value.to_dict.return_value = list_for_csv
    assert read_csv_file("test_path") == list_for_csv
    mock_read_csv.assert_called_once_with("test_path", delimiter=";")


@patch("pandas.read_excel")
def test_read_xl_file(mock_read_xl, list_for_xl):
    mock_read_xl.return_value.to_dict.return_value = list_for_xl
    assert read_xl_file("test_path") == list_for_xl
    mock_read_xl.assert_called_once_with("test_path")
