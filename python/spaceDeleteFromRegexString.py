
import glob
import re
import os
files = glob.glob("./python/**/*.md", recursive=True)
for file in files:
    print(file + ":start")
    with open(file) as inFile:
        lines = inFile.readlines()
        with open(file.replace(" ",""),mode="w") as outFile:
            for line in lines:
                if(re.match("\(.*\s.*\)",line)):
                    outFile.write(line.replace(" ",""))
                else:
                    outFile.write(line)

    if(" " in file ):
        os.remove(file)