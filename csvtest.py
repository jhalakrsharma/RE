import glob, os
import subprocess
import csv

parameter =  ['A', 'B', 'Cin', 'sum', 'Cout', 'w1', 'w2', 'w3', 'da', 'db', 'dCin', 'dsum', 'dCout', 'd', 'q'];
toAdd = ["clk", "A", "B", "Cin", "en", "sum", "Cout"];

os.chdir("C:\\iverilog\\bin\\")
for para in parameter:
    with open('C:\\iverilog\\bin\\fault{}.v'.format(para), "r") as f: 
        cmd1 = 'iverilog -o fault' + para + " " + 'fault' + para + '.v'
        #print(cmd1)
        cmd2 = 'vvp fault' + para + " " + '> fault' + para + '.csv'
        os.system(cmd1)
        os.system(cmd2) 
    
    with open('C:\\iverilog\\bin\\fault{}.csv'.format(para), "r") as infile:
        reader = list(csv.reader(infile))
        reader.insert(0, toAdd)

    with open('C:\\iverilog\\bin\\fault{}.csv'.format(para), "w", newline = '') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)
