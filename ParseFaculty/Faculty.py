import string
def parse_faculty(text):
    """
        Функція зчитування рядка факультету та виведення у короткому вигляді

        :param text: data type: string
               format: Word word word. Word
               examples: Факультет прикладної математики. Денна
                         Факультет інформаціонної обчислювальної техніки. Заочна
      :return: data type: string
               format: XXX
               examples: ФПМ
                         ФІОТ
    """
    words = []
    words = text.split(".")
    contains = words[0].split()
    letters = []
    for word in contains:
        letters.append(word[0].upper())
    result = ""
    result = result.join(letters)
    return result