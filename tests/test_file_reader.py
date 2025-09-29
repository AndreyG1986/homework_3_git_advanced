from unittest.mock import Mock, patch

from src.file_reader import  read_xl_file, read_csv_file

def test_read_csv_file(path_to_file_csv, list_for_csv):
    mock_list_csv = Mock(return_value= list_for_csv[:2])
    list_for_csv = mock_list_csv
    assert read_csv_file(path_to_file_csv) == mock_list_csv
    mock_list_csv.assert_called_once_with(path_to_file_csv)


@patch("pd.read_excel")
def test_read_xl_file(path_to_file_xl,list_for_xl):
    list_for_xl.return_value = list_for_xl
    assert read_xl_file(path_to_file_xl) == list_for_xl



