
def comparing(words):
    """
    Функція приймає рядок з трьома значеннями(Прізвище Ім'я По-батькові), і вертає Прізвище та ім'я

    :param text: str, str, Прізвище Ім'я По-батькові
    :return:str, str, Прізвище Ім'я
    """

    final=[]
    new_text = words.split(" ")
    for element in new_text:
        if element!=2:
            final.append(element)
    print(final)
    return final
comparing("Yes God No")