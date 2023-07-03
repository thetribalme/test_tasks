'''
Написать функцию - генератор хэштегов, которая работает с введенным предложением:
- Оно должно начинаться с хэштега (#).
- Во всех словах первая буква должна быть заглавной.
- Если конечный результат длиннее 140 символов, он должен возвращать
значение false.
- Если входные данные или результат являются пустой строкой, они должны
возвращать значение false.
'''


def hashtag_generator(phrase: str, critical_length: int = 140):
    """
    Generates hashtag line containing # and modified user inputted phrase

    :param phrase: text WITHOUT any punctuation marks
    :param critical_length: max length of a generated hashtag
    :return: #UserText in str
    """
    hashtag_text = phrase.title().replace(' ', '')
    input_check = len(hashtag_text) > 0
    length_check = len(hashtag_text) < critical_length - 1
    if input_check is False or length_check is False:
        return False
    return '#' + hashtag_text


if __name__ == '__main__':
    user_text = input('Type your text for hashtag generation:\n')
    # for example: Ах сказочное бали Там сказоЧно ебали , generic hashtag ,
    # I am sure I can type more than one hundred and forty characters at one point maybe sooner maybe later but I will definetly do it aaaaaaany moment now aaaaaaaaaaany second
    print(hashtag_generator(user_text))
