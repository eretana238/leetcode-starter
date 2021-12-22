import requests
import time

from requests.models import HTTPError

api_url = 'https://leetcode.com/api/problems/algorithms/'

"""Requests all problems"""

def request_problem(problem_name_slug):
    # need to improve algorithm, maybe binary search would be better
    query = """
    query questionData($titleSlug: String!) {\n
        question(titleSlug: $titleSlug) {\n
            questionId\n    
            questionFrontendId\n    
            title\n    
            titleSlug\n    
            isPaidOnly\n    
            difficulty\n    
            likes\n    
            dislikes\n    
            isLiked\n    
            similarQuestions\n     
        }\n
    }\n
    """
    body = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": problem_name_slug
        },
        "query": query
    }

    url = "https://leetcode.com/graphql"
    try:
        response = requests.post(url, json=body)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        r_json = response.json()
        return r_json["data"]["question"]


if __name__ == '__main__':
    start = time.time()
    request_problem('restore-the-array-from-adjacent-pairs')
    end = time.time()
    print('Time took to find the problem: ', end-start)