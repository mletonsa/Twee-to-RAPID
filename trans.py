import re

with open("UTM.twee", "rt") as fin:
    with open("UTM.rapid", "wt") as fout:
        for line in fin:
            if line[0:2] == "::":
                fout.write ("\n")
                fout.write (line[3:-1] + ":\n")
            if line[0:2] == "[[":
                x = line.split("|")
                if len(x) == 1:
                    fout.write("Goto " + re.search('->(.*)]]', line).group(1)+";\n")
                else:
                    fout.write ("GetSymbol"+";\n")
                    fout.write ("Test symbol\n")
                    for i in range(len(x)):
                        fout.write("Case " + re.search('\[\[Read (.*)->', x[i]).group(1) + ":\n")
                        fout.write("    Goto " + re.search('->(.*)]]', x[i]).group(1)+";\n")
            subline = re.search('You will write (.*) and', line)
            if subline:
                fout.write("PutSymbol " + re.search('You will write (.*) and', line).group(1)+";\n")
                fout.write("TurnRobot_" + re.search('and move (.*)\.', line).group(1)+";\n")
                    
                     