from src import functions
from tests.test_config import TEST_OPERATIONS_PATH, FALSE_PATH

operations_data = [
    {
        "id": 879660146,
        "state": "EXECUTED",
        "date": "2018-07-22T07:42:32.953324",
        "operationAmount": {
            "amount": "92130.50",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 19628854383215954147",
        "to": "Счет 90887717138446397473"
    },
    {
        "id": 710136990,
        "state": "CANCELED",
        "date": "2018-08-17T03:57:28.607101",
        "operationAmount": {
            "amount": "66906.45",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1913883747791351",
        "to": "Счет 11492155674319392427"
    }
]


def test_load_data():
    assert functions.load_data(TEST_OPERATIONS_PATH) == operations_data
    assert functions.load_data(FALSE_PATH) == []


def test_mask_card_acc_number():
    assert functions.mask_card_acc_number("Счет 71687416928274675290") == "Счет **5290"
    assert functions.mask_card_acc_number("МИР 5211277418228469") == "МИР 5211 27** **** 8469"
    assert functions.mask_card_acc_number("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"


def test_format_date():
    assert functions.format_date("2019-07-13T18:51:29.313309") == "13.07.2019"
    assert functions.format_date("2018-12-24T20:16:18.819037") == "24.12.2018"
