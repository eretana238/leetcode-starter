import re

"""Updates the readme file with the newly created leetcode problem"""
def update_readme(problem_id, p_name,p_link,p_url,p_level):
    with open('C:/Users/chees/Documents/projects/leetcode/README.md','r+') as f:
        lines = f.readlines()
        print(type(lines))
        row = ''
        if not len(lines):
            row = 'Problem # | Problem Link | Solution | Difficulty | Language\n'
            row += ' --- | --- | --- | --- | ---\n'
        shift = []
        row += '%s | [%s](%s) | [View](%s) | %s | Python\n'% (problem_id,p_name,p_link,p_url,p_level)

        # place the solution in the correct row

        f.seek(0)
        f.writelines(lines)
def sort_solution():
    for i in range(3,len(lines)):
        n = re.match('\d*',lines[i][2:8]).group()
        if int(n) > int(problem_id): 
            shift = lines[i:]
            lines[i] = row
            lines[i+1:] = shift
            break
        if i == len(lines)-1:
            lines.append(row)