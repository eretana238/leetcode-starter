import os
from web import request_problem
from updater import update_readme

"""Converts id to string and inserts lacking zeros to the thousands."""


def parse_int(question_id):
    return str(question_id).zfill(4)


"""Creates a folder for the problem to be solved"""


def create_dir(path: str) -> bool:
    if not os.path.exists(path):
        raise FileNotFoundError('Cannot find directory')

    try:
        os.mkdir('%s/%s/' % (path, problem_id + '-' + problem_name_slug))
    except OSError:
        print("Problem already exists!")
    else:
        print("Successfully created the directory %s " % path)
    return True


if __name__ == "__main__":
    # insert user here
    user = 'chees'
    path = 'C:/Users/%s/Documents/projects/leetcode' % user

    print('Leetcode quickstart')
    url = input('URL: ').strip()

    problem_name_slug = url.replace(
        'https://leetcode.com/problems/', '').replace('/', '')

    problem = request_problem(problem_name_slug)

    problem_id = parse_int(problem['stat']['frontend_question_id'])
    # create directory
    if not create_dir(path):
        raise Exception('Could not create directory')

    folder_name = problem_id + '-' + problem_name_slug
    relative_path = folder_name + '/Solution.py'
    full_path = path + '/' + relative_path

    with open(full_path, 'w') as f:
        f.write('\'\'\'\n %s. %s\n \'\'\'\nclass Solution:\n' % (
            problem['stat']['frontend_question_id'], problem['stat']['question__title']))

    if problem['difficulty']['level'] == 1:
        difficulty = 'Easy'
    elif problem['difficulty']['level'] == 2:
        difficulty = 'Medium'
    else:
        difficulty = 'Hard'

    update_readme(problem, relative_path, url)
