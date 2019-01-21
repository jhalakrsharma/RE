import re

parameters =  ['w1', 'w2', 'w3', 'da', 'db', 'dCin', 'dsum', 'dCout']
for parameter in parameters:
    lines_output = []
    with open('fault' + parameter + '.v', 'r') as k:
        lines = k.readlines()

    for item in lines:
        if(re.match("^(|\t)(xor|and|or|dff)", item)):
            if(re.search("/*\("+ parameter +",", item)):
                lines_output.append(item)
            elif(re.search("/*\(error,", item)):
                lines_output.append(item)
            elif(re.search("( |,)" + parameter + "( |,|\))", item)):
                item = item.replace(parameter, "error")
                lines_output.append(item)
            else:
                lines_output.append(item)
        else:
            lines_output.append(item)

    with open('fault' + parameter + '.v', 'w') as n:
        for item in lines_output:
            n.write("%s" % item)
