import re
def getNumber(text):
    """
    Функція зчитує рядок та повертає номер групи

    :param test: str, str, KM-91
    :return: str, str, 91
    """

    group_number = re.findall('\d{2}', text)

    return group_number

from ParseRecordBook.Parser import parseRecordBook, getemaildata



print( getNumber( getemaildata() ))