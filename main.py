import os
from web import request_problem
from updater import update_readme

'''
Converts id to string and inserts lacking zeros to the thousands.
'''
def parse_int(question_id):
    return str(question_id).zfill(4)

if __name__ == "__main__":
    # insert user here
    user = 'chees'
    print('Leetcode quickstart')
    url = input('URL: ').strip()
    problem_name_slug = url.replace('https://leetcode.com/problems/', '').replace('/', '')

    problem = request_problem(problem_name_slug)

    problem_id = parse_int(problem['stat']['question_id'])
    # create directory
    path = 'C:/Users/%s/Documents/leetcode/' % user
    if os.path.exists(path):
        try:
            os.mkdir('%s/algorithms/%s/' % (path, problem_id + '-' + problem_name_slug))
        except OSError:
            print ("Problem already exists!")
        else:
            print ("Successfully created the directory %s " % path)
            file_name = 'Solution.py' 
            folder_name = problem_id + '-' + problem_name_slug
            file_path = path + 'algorithms/' + folder_name + '/' + file_name
            
            with open(file_path, 'w') as f:
                f.write('\'\'\'\n %s. %s\n \'\'\'\nclass Solution:\n' % (problem['stat']['frontend_question_id'],problem['stat']['question__title']))
            
            if problem['difficulty']['level'] == 1:
                difficulty = 'Easy'
            elif problem['difficulty']['level'] == 2:
                difficulty = 'Medium'
            else:
                difficulty = 'Hard'

            update_readme(problem_id,problem['stat']['frontend_question_id'],url,'algorithms/%s/%s' % (folder_name,file_name),difficulty)