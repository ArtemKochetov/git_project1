from requests import get, post
from pprint import pprint

pprint(get('http://localhost:5000/api/records').json())
pprint(get('http://localhost:5000/api/records/1').json())
pprint(get('http://localhost:5000/api/records/999').json())
pprint(get('http://localhost:5000/api/records/q').json())

pprint(post('http://localhost:5000/api/records',
            json={
                'title': 'api_test_title',
                'about': 'api_test_about',
                'cost': 123,
                'user_id': 1,
                'note': 'api_test_note'
            }).json())