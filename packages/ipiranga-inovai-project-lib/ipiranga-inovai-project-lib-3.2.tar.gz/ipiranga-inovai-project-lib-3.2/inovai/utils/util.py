import logging

from dateutil import parser


def format_date(date_str, formatter: str = '%d/%m/%Y') -> str:
    try:
        date_obj = parser.parse(date_str)
        date_formatted = date_obj.strftime(formatter)
        return date_formatted
    except ValueError:
        logging.error(f"Formato de data invalido. Data {date_str}")
        return ''
