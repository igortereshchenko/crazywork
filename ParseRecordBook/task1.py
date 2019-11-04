def number():
    """
    Для чого функція?
    :return: Номер группи
    """
    name_group = input('Введіть группу: ')
    number = name_group[3:5]
    return number


print(number())