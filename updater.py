import re

def update_readme(p_number, p_name,p_link,p_url,p_level):
    with open('C:/Users/chees/Documents/leetcode/README.md','r+') as f:
        lines = f.readlines()
        shift = []
        row = '| %s | [%s](%s) | [View](%s) | %s | Java |\n' % (p_number,p_name,p_link,p_url,p_level)
        if len(lines) <= 5:
            lines.append('\n'+row)
        else:
            for i in range(5,len(lines)):
                n = re.match('\d*',lines[i][2:8]).group()
                if int(n) > int(p_number): 
                    shift = lines[i:]
                    lines[i] = row
                    lines[i+1:] = shift
                    break
                if i == len(lines)-1:
                    lines.append(row)
        f.seek(0)
        f.writelines(lines)