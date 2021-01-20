import requests

api_url = 'https://leetcode.com/api/problems/algorithms/'

'''
Requests problem
'''
def request_problem(problem_name_slug) -> list:
    r = requests.get(api_url)
    if r.status_code == 200:
        res = r.json()
        if 'stat_status_pairs' in res:
            for p in res['stat_status_pairs']:
                if p['stat']['question__title_slug'] == problem_name_slug:
                    return p
        else:
            return None
    return None