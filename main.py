import datetime
import json
import requests

def logger(file_path):

    def _logger_decorator(old_function):

        def new_function(*args, **kwargs):
            now = datetime.datetime.now()
            date_time = f'Дата и время вызова функции: {now.strftime("%d-%m-%Y %H:%M")}'
            name = f'Имя вызванной функции: {old_function.__name__}'
            arguments = f'Аргументы вызванной функции: {args} {kwargs}'
            result = old_function(*args, **kwargs)
            def_result = f'Результат вызванной функции: {result}'
            with open(file_path, 'w+', encoding='utf-8') as file:
                res = date_time, name, arguments, def_result
                if res not in file:
                    json.dump(res, file, indent=2, ensure_ascii=False)
            return result

        return new_function

    return _logger_decorator

@logger('logs.json')
def get_country(index=None):
    response = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json').json()
    return response[index]['name']['common']
get_country(3)