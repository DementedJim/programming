try:
    import json
    import pandas
    import pandas as pd
except:
    print("Ошибка при попытке импортировать модуль")

try:
    with open('ИСР.json', 'r') as read_file:
        data = pandas.read_json('ИСР.json')
        d = pd.DataFrame(data)
        print(d)
except json.JSONDecodeError:
    print("не json")