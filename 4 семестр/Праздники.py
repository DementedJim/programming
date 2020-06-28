class Today:
    req = 'https://datazen.katren.ru/calendar/day/'
    def __init__(self):

      import requests
      import pprint

      req_result = requests.request('GET', Today.req)

      pprint.pprint(req_result.json())

Today()