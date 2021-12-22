from updater import update_readme

problem = {
    'stat': {'question_id': 3,
             'question__article__live': True,
             'question__article__slug': 'longest-substring-without-repeating-characters',
             'question__article__has_video_solution': True,
             'question__title': 'Longest Substring Without Repeating Characters',
             'question__title_slug': 'longest-substring-without-repeating-characters',
             'question__hide': False,
             'total_acs': 2771414,
             'total_submitted': 8510914,
             'frontend_question_id': 3,
             'is_new_question': False},
    'status': None,
    'difficulty': {'level': 2},
    'paid_only': False,
    'is_favor': False,
    'frequency': 0,
    'progress': 0
}

update_readme(problem, '0003-longest-substring-without-repeating-characters/Solution.py',
              'https://leetcode.com/problems/longest-substring-without-repeating-characters/')
