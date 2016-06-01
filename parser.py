import re
import os

# raw data to be read
infile = open("data-sanitized.txt", "r")

# where our sanitized data will be written to
# sanitized = open("sanitized.txt", "W")

outfile = open("data/result.txt", "w")

#========== PARSING ==========#
# traverse the file
def enumerate(infile):
    # n = count;
    for line in infile:
        # we match for --Attackers:
        match = re.search('(--[A])(.*)', line)
        if match is None:
            # we match for --Victims:
            match = re.search('(--[V])(.*)', line)
            if match is None:
                continue
            else: # matched --Victims
                target = match.group(0)
                # print(target)
                outfile.write(target)

                #advance our pointer to read the next line
                ne = next(infile)
                # print(ne)

                # we match for 'Damage Taken'
                match = re.search('(Damage Taken )(.*)', ne)
                # as long as current line is not our delimiter,
                # we keep reading and advancing our pointer
                # through the range
                while match is None:
                    outfile.write(ne)
                    ne = next(infile) # next line
                    match = re.search('(Damage Taken )(.*)', ne) # match again
                    # print(ne)
                    outfile.write(ne)
                else:
                    outfile.write("\n=====Round Score Break=====")
                    print("\n=====Round Score Break=====")

        else: # matched --Attackers
            target = match.group(0)
            # print(target)
            outfile.write(line)

            # advance our pointer to read the next line
            ne = next(infile)

            # we match for 'Damage Taken'
            match = re.search('(Damage Taken )(.*)', ne)
            # as long as line is not our delimiter, we keep reading
            # and advancing our pointer through the range
            while match is None:
                outfile.write(ne)
                ne = next(infile) # next line
                match = re.search('(Damage Taken )(.*)', ne) # match again
                # print(ne)
                outfile.write(ne)
            else:
                outfile.write("\n=====Round Score Break=====")
                print("\n=====Round Score Break=====")
# call function
enumerate(infile)
# close files
outfile.close()
infile.close()
# os.unlink(infile)
