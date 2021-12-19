import requests
from requests.models import HTTPError

def get_quest_info(slug: str):
    query = """
    query questionData($titleSlug: String!) {\n
        question(titleSlug: $titleSlug) {\n
            questionId\n    
            questionFrontendId\n    
            title\n    
            titleSlug\n    
            content\n    
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
            "titleSlug": slug
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

print(get_quest_info('couples-holding-hands'))