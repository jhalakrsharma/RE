# Final Python code

from collections import OrderedDict
import re
import random
import sys

#-------------------------------------------------------------------------------------------------------------------------------
### Creating an empty string to read the parameters.
parameters = ""

#-------------------------------------------------------------------------------------------------------------------------------
### Opening the file, reading line by line, searchin for input, output or wire keyboard and saving the lines in parameters string.
with open('E:\\MS by Research\\Thesis\\python files\\struc_fa_golden_py.v', 'r') as f:
    for line in f:
        if "output" in line or "wire" in line:
            #print(line.partition('//')[0])
            parameters += line.partition('//')[0]

#-------------------------------------------------------------------------------------------------------------------------------
### Removing tabs, new lines, input, output, wire, commas, semicolons, and splitting on spaces finally.
parameters = parameters.replace("\t", "")
parameters = parameters.replace("\n", "")
parameters = parameters.replace("input", "")
parameters = parameters.replace("output", "")

#-------------------------------------------------------------------------------------------------------------------------------
### Using regular expressions, to remove the [XX:XX] string in between.
parameters = re.sub("[\(\[].*?[\)\]]", "", parameters)
parameters = parameters.replace("wire", "")
parameters = parameters.replace(",", "")
parameters = parameters.replace(";","")
parameters = parameters.split(" ")

#-------------------------------------------------------------------------------------------------------------------------------
### Due to some spaces items in the list, removing them.
parameters = list(filter(None, parameters))
#print ("Parameters = ", parameters)

#-------------------------------------------------------------------------------------------------------------------------------
### OrderedDict does the same and preserves the order.
parameters = list(OrderedDict.fromkeys(parameters))
#prints all parameters in new line
#print(*parameters, sep = "\n")

# Removing clock from the list if present
if "clk" in parameters:
    parameters.remove("clk")
if "d" in parameters:
    parameters.remove("d")
if "q" in parameters:
    parameters.remove("q")
if "reg" in parameters:
    parameters.remove("reg")
    number = len(parameters)
    print ("Number of parameters = ", number)
    print ("Parameters = ", parameters)

#-------------------------------------------------------------------------------------------------------------------------------
### Generte a for loop to include all the parameters to inject fault, and above that create as many files as the number of parameters

lookup      = 'endmodule'
lookup1     = 'dut'
linenumber  = []
linenumber2 = []
enable      = ", en);"
input2      = parameters
lines_output = []
#print(type(parameters))

for parameter in parameters:
    with open('E:\\MS by Research\\Thesis\\python files\\fault{}.v'.format(parameter), "w") as f:
        with open('E:\\MS by Research\\Thesis\\python files\\struc_fa_golden_py.v', 'r') as h:
            for num, line in enumerate(h, 1):
                if lookup in line:
                    linenumber.append(num)

            change = "\txor u1 (error, en, " + parameter + ");\n"

        with open('E:\\MS by Research\\Thesis\\python files\\struc_fa_golden_py.v', 'r') as k:
            lines = k.readlines()

        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'w') as m:
            for i, line in enumerate(lines):
                if i == linenumber[0] - 1:
                    m.write(change)
                m.write(line)


#-------------------------------------------------------------------------------------------------------------------------------
### Adding enable port in the DUT in testbench
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as j:
            for num, line in enumerate(j, 1):
                if lookup1 in line:
                    linenumber2.append(num)

        dut_line = "\t.en(en),\n"

#-------------------------------------------------------------------------------------------------------------------------------
### Opening fault1 file in read mode, saving the contents in variable named "lines"
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as k:
            lines = k.readlines()
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'w') as m:
            for i, line in enumerate(lines):
                if i == linenumber2[0] + 1:
                    m.write(dut_line)
                m.write(line)

#-------------------------------------------------------------------------------------------------------------------------------
### Finding the line number to add new parameters in the faulty file
        new_parameter = []
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as k:
            for num, line in enumerate(k, 0):
                if "input" in line or "reg" in line or "wire" in line:
                      new_parameter.append(num)

#-------------------------------------------------------------------------------------------------------------------------------
### Adding new input 'enable' in the faulty file
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as p:
            lines_again = p.readlines()

        lines_again[new_parameter[0]] = lines_again[new_parameter[0]].replace("\n", "")
        lines_again[new_parameter[0]] = lines_again[new_parameter[0]] + " en, \n"

        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'w') as n:
            for item in lines_again:
                n.write("%s" % item)
                #f.write("%s" % item)

#-------------------------------------------------------------------------------------------------------------------------------
### Adding new wire erroror in the faulty file
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as z:
            lines_again = z.readlines()

        lines_again[new_parameter[1]] = lines_again[new_parameter[1]].replace("\n", "")
        lines_again[new_parameter[1]] = lines_again[new_parameter[1]].replace(";", "")
        lines_again[new_parameter[1]] = lines_again[new_parameter[1]] + ", error; \n"

        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'w') as b:
            for item in lines_again:
                b.write("%s" % item)
                #f.write("%s" % item)
#-------------------------------------------------------------------------------------------------------------------------------
### Adding new reg 'en' in the testbench in the faulty file
        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'r') as k:
            lines_again = k.readlines()

        lines_again[new_parameter[2]] = lines_again[new_parameter[2]].replace("\n", "")
        lines_again[new_parameter[2]] = lines_again[new_parameter[2]].replace(";", "")
        lines_again[new_parameter[2]] = lines_again[new_parameter[2]] + ", en; \n"

        with open('E:\\MS by Research\\Thesis\\python files\\fault1.v', 'w') as b:
            for item in lines_again:
                #b.write("%s" % item)
                f.write("%s" % item)
