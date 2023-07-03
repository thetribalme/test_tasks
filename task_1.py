'''
Необходимо написать функцию, которая при задании URL адреса в виде строки анализирует
только доменное имя и возвращает его в виде строки
'''


def domain_name_extract(url: str):
    """Extracts full domain name in str formatted www.domain_name.TLD from URL"""
    subdomain = 'www.'
    domain_name = url.split('/')[2]
    if subdomain not in domain_name:
        return subdomain + domain_name
    return domain_name


def second_lvl_domain_name_extract(url: str):
    """Extracts second level domain name in str from URL"""
    return url.split('/')[2].strip('www.').split('.')[0]


if __name__ == '__main__':
    # income box
    user_input = input('Insert URL:\n')
    # examples: https://www.youtube.com/watch?v=adDW9OKbKFs , https://pythonru.com/uroki/funkcija-zip-dlja-nachinajushhih
    # , https://украса.рф/category/pryadyeniye/ , https://talkingaboutww2.com/Python_bases/pull/6

    print(domain_name_extract(user_input))
    print(second_lvl_domain_name_extract(user_input))
