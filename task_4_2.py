import requests


def currency_rates(val):
    site = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = site.content.decode(encoding=site.encoding)
    result = None
    if val not in content:
        return result
    else:
        for elem in content.split(f'{val}')[1:]:
            for elem_1 in elem.split('</Value>')[:1]:
                result = round(float(elem_1.split('<Value>')[1].replace(',', '.')),2)
                return f'Курс валюты: {result} руб.'


if __name__ == '__main__':
    print('USD: ' + currency_rates('USD'))
    print('EUR: ' + currency_rates('EUR'))
    code_val = (input('Введите название валюты: '))
    print(currency_rates(code_val))