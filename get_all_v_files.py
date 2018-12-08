import os
os.chdir("C:/iverilog/bin")
print(os.getcwd())
import subprocess
cmd1 = 'iverilog -o struc_fa_golden struc_fa-golden.v'
cmd2 = 'vvp struc_fa_golden > out1.txt'
os.system(cmd1)
os.system(cmd2)

import glob, os
# os.chdir("C:\\Users\\ADMIN\\Anaconda3\\")
# for file in glob.glob("fault*.v"):
#     print(file)
    
test = glob.glob("fault*.v")
print(test)