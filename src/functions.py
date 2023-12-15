import json
import os
from datetime import datetime


def load_data(path: str) -> list[dict]:
    """
    Функция для чтения данных из файла.
    :param path: путь к файлу
    :return: json файл с транзакциями
    """
    if os.path.exists(path):
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    return []


def mask_card_acc_number(card_acc_number_text: str) -> str:
    """
    Функция проверки откуда/куда был сделан перевод: со счета или с карты.
    Также приводит номер счета или карты к требуемому, замаскированному виду.
    :param card_acc_number_text: стока с номером счета/карты
    :return: строка с замаскированным номером счета/карты
    """
    if card_acc_number_text.startswith("Счет"):
        masked_number = ''.join([card_acc_number_text[:5], '**', card_acc_number_text[-4:]])
    else:
        masked_number = ''.join(
            [card_acc_number_text[:-12], ' ', card_acc_number_text[-12:-10], '**', ' **** ', card_acc_number_text[-4:]])
    return masked_number


def format_date(date_string: str) -> str:
    """
    Функция форматирования даты в требуемый вид.
    :param: строка с датой в исходном формате
    :return: строка с датой в требуемом формате
    """
    datetime_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = datetime_obj.strftime("%d.%m.%Y")
    return formatted_date
