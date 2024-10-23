import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from strideutils.sheets_connector import GoogleSheetsClient
from gspread.exceptions import WorksheetNotFound, SpreadsheetNotFound

@pytest.fixture
def sheets_client():
    with patch('gspread.authorize') as mock_authorize:
        client = GoogleSheetsClient()
        client.client = MagicMock()
        yield client

def test_sheets_grab_sheet(sheets_client):
    mock_worksheet = MagicMock()
    mock_worksheet.get_all_records.return_value = [{'A': 1, 'B': 2}, {'A': 3, 'B': 4}]
    sheets_client.client.open_by_key.return_value.worksheet.return_value = mock_worksheet

    result = sheets_client.grab_sheet('sheet_id', 'sheet_name')

    sheets_client.client.open_by_key.assert_called_once_with('sheet_id')
    sheets_client.client.open_by_key.return_value.worksheet.assert_called_once_with('sheet_name')
    assert isinstance(result, pd.DataFrame)
    assert result.to_dict('records') == [{'A': 1, 'B': 2}, {'A': 3, 'B': 4}]

def test_sheets_grab_sheet_not_found(sheets_client):
    sheets_client.client.open_by_key.side_effect = SpreadsheetNotFound

    with pytest.raises(SpreadsheetNotFound):
        sheets_client.grab_sheet('nonexistent_id', 'sheet_name')

def test_sheets_grab_sheet_with_cache(sheets_client):
    sheets_client.cache_enabled = True
    sheets_client._cache['sheet_id_sheet_name'] = pd.DataFrame({'A': [1,3], 'B': [2,4]})

    results = sheets_client.grab_sheet('sheet_id', 'sheet_name')

    assert isinstance(results, pd.DataFrame)
    assert results.to_dict('records') == [{'A': 1, 'B': 2}, {'A': 3, 'B': 4}]
    sheets_client.client.open_by_key.assert_not_called()

def test_sheets_write_sheet(sheets_client):
    mock_worksheet = MagicMock()
    sheets_client.client.open_by_key.return_value.worksheet.return_value = mock_worksheet

    df = pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
    sheets_client.write_sheet(df, 'sheet_id', 'sheet_name')

    sheets_client.client.open_by_key.assert_called_once_with('sheet_id')
    sheets_client.client.open_by_key.return_value.worksheet.assert_called_once_with('sheet_name')
    mock_worksheet.update.assert_called_once()

def test_sheets_write_sheet_new_worksheet(sheets_client):
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.worksheet.side_effect = WorksheetNotFound
    sheets_client.client.open_by_key.return_value = mock_spreadsheet

    df = pd.DataFrame({'A': [1, 3], 'B': [2, 4]})
    sheets_client.write_sheet(df, 'sheet_id', 'new_sheet')

    mock_spreadsheet.add_worksheet.assert_called_once_with(title='new_sheet', rows=1, cols=1)

def test_sheets_reorder_sheet(sheets_client):
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.worksheets.return_value = [
        MagicMock(title='Sheet1', id=1),
        MagicMock(title='Sheet2', id=2),
        MagicMock(title='Sheet3', id=3)
    ]
    sheets_client.client.open_by_key.return_value = mock_spreadsheet

    sheets_client.reorder_sheet('sheet_id', 'Sheet2', 0)

    mock_spreadsheet.batch_update.assert_called_once()
    call_args = mock_spreadsheet.batch_update.call_args[0][0]
    assert call_args['requests'][0]['updateSheetProperties']['properties']['index'] == 1
    assert call_args['requests'][0]['updateSheetProperties']['properties']['sheetId'] == 2


def test_sheets_reorder_sheet_invalid_name(sheets_client):
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.worksheets.return_value = [
        MagicMock(title='Sheet1', id=1),
        MagicMock(title='Sheet2', id=2)
    ]
    sheets_client.client.open_by_key.return_value = mock_spreadsheet

    with pytest.raises(ValueError, match="Sheet3 not found"):
        sheets_client.reorder_sheet('sheet_id', 'Sheet3', 0)

def test_sheets_get_sheet_names(sheets_client):
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.worksheets.return_value = [
        MagicMock(title='Sheet1'),
        MagicMock(title='Sheet2'),
        MagicMock(title='Sheet3')
    ]
    sheets_client.client.open_by_key.return_value = mock_spreadsheet

    result = sheets_client.get_sheet_names('sheet_id')

    assert result == ['Sheet1', 'Sheet2', 'Sheet3']

def test_sheets_get_sheet_names_empty(sheets_client):
    mock_spreadsheet = MagicMock()
    mock_spreadsheet.worksheets.return_value = []
    sheets_client.client.open_by_key.return_value = mock_spreadsheet

    result = sheets_client.get_sheet_names('sheet_id')

    assert result == []
