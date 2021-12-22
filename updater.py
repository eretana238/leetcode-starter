import re

"""Updates the readme file with the newly created leetcode problem"""


def update_readme(problem, relative_path, url):
    with open('C:/Users/chees/Documents/projects/leetcode/README.md', 'r+') as f:
        lines = f.readlines()
        row = ''
        if not lines:
            row = 'Problem # | Problem Link | Solution | Difficulty | Language\n'
            row += ' --- | --- | --- | --- | ---\n'

        row += '%s | [%s](%s) | [Solution](%s) | %s | Python\n' % (str(problem['stat']['frontend_question_id']).zfill(4),
                                                                   problem['stat']['question__title'], url, relative_path, level_to_str(problem['difficulty']))
        lines.append(row)

        if len(lines) > 3:
            lines[2:] = sort_solution(lines)

        f.seek(0)
        f.writelines(lines)


def level_to_str(difficulty: int) -> str:
    if difficulty['level'] == 1:
        return 'Easy'
    elif difficulty['level'] == 2:
        return 'Medium'
    return 'Hard'


def sort_solution(lines: list[str]):
    s = sorted(lines[2:])
    return s
