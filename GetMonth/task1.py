import re


def get_month(text_string=None, separator=' '):
    """
    Ця функція з даного рядка, за шаблоном, виділяє місяць, та виводить його
    :param separator: string, 'роздільник', '*'
    :param text_string: string, 'число місяць рікр.', '1 вересня 2019р.' => 'вересень'
    :return: string, 'місяць', 'вересень'
    """

    if text_string is None:

        # Data is empty

        return None
    else:
        if bool(re.match('^[0-9]\\s[а-яієїщш]+\\s[0-9]{4}[р]\\.$', text_string)):
            array = text_string.split(separator)
            month = array[1]

            new_month = month[:-2] + 'ень'
            return new_month
