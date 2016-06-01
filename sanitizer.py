import re
import os

# raw data to be sanitized
infile = open("5-31-console.log", "r")

# where our sanitized data will be written to
outfile = open("data-sanitized.txt", "w")

#========== SANITATION ==========#
# Strings to be sanitized:
# 'Achievements disabled: cheats turned on in this app session.'
# 'Can't use cheat cvar cam_idealpitch in multiplayer, unless the server has sv_cheats set to 1'

# traverse the file
for line in infile:
    # we match 'achievements disabled...' string with regex
    match1 = re.search('(Ach)(.*)', line)
    if match1 is None:
        # we match 'Can't use cheat...' string with regex
        match2 = re.search('(Can\')(.*)', line)
        if match2 is None:
            outfile.write(line)
        else:
            continue
    else:
        # do nothing
        continue
# close both files
outfile.close()
infile.close()
os.system("parser.py")
