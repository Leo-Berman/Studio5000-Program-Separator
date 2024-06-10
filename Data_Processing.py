#!usr/bin/env python3

import easygui as eg
import pandas as pd
import re

# perform the data processing
def separate(output_folder,content,Verbose = False):

    held_program = ""
    file = None
    # iterate through each line
    for i,x in enumerate(content):
        
        # perform regex
        tmp_program = re.search(r'(PROGRAM \w+)((?= \((Description) := .+,)|(?= \((MODE) := .+,)|(?= \((MAIN) := .+,))',x)

        if tmp_program != None:
            print("Temp = ",tmp_program.group())
            held_program = tmp_program.group()
            file = open(output_folder+"\\"+tmp_program.group()+".txt","w")
            file.write(x)

        elif x.__contains__("END_PROGRAM") and not file.closed:
            print("End should be = ",x)
            print("Held = ",held_program)
            held_program = ""
            file.write(x)
            file.close()

        elif held_program != "":
            file.write(x)
