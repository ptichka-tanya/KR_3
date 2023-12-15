from src import main
from src.main import get_5_last_transactions
from tests.test_config import TEST_OPERATIONS_PATH


def test_main():
    main.main()


def test_get_5_last_transactions():
    result = get_5_last_transactions(TEST_OPERATIONS_PATH)
    expected_result = ['22.07.2018 Перевод организации\nСчет **4147 -> Счет **7473\n92130.50 USD\n']
    assert result == expected_result
