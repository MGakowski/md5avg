# Title
print ""
print " _____ ____  ___                "
print "|     |    \|  _|   ___ _ _ ___  {v1.0}"
print "| | | |  |  |_  |  | .'| | | . |"
print "|_|_|_|____/|___|  |__,|\_/|_  |"
print "          by MGakowski     |___| "
print ""
print "[#] Outputs average digest from a given list of digests."
print"[#] Ensure list is a .txt & has no blank lines!"

# Gets filename of hash list
filename = str(raw_input("File name of hash list? "))

# Gets Line count & hash length
load_profile = open(filename+'.txt', "r")
with open(filename+'.txt') as f:
    linecount = sum(1 for _ in f)
    print str(linecount)+" hashes loaded"
hashlength = int(raw_input("Length of hash; 32=md5, 40=sha1? "))

currentl = 0
val0 = int()
currentavghash = str()
charpos = 0

for y in range(0, hashlength):
    for x in range(0, linecount):
        
        load_profile = open(filename+'.txt', "r")
        read_it = load_profile.read().splitlines()[currentl]
        currenth = str(read_it)

        if currenth[charpos] == "0":
            val0 += 1

        if currenth[charpos] == "1":
            val0 += 2

        if currenth[charpos] == "2":
            val0 += 3

        if currenth[charpos] == "3":
            val0 += 4

        if currenth[charpos] == "4":
            val0 += 5

        if currenth[charpos] == "5":
            val0 += 6

        if currenth[charpos] == "6":
            val0 += 7

        if currenth[charpos] == "7":
            val0 += 8

        if currenth[charpos] == "8":
            val0 += 9

        if currenth[charpos] == "9":
            val0 += 10

        if currenth[charpos] == "a":
            val0 += 11

        if currenth[charpos] == "b":
            val0 += 12

        if currenth[charpos] == "c":
            val0 += 13

        if currenth[charpos] == "d":
            val0 += 14

        if currenth[charpos] == "e":
            val0 += 15

        if currenth[charpos] == "f":
            val0 += 16

        if currentl < linecount-1:
            currentl += 1
        else:
            currentl = 0

        #print val0
        thischar = str(val0/linecount)

    if thischar == "1":
        currentavghash += str("0")

    if thischar == "2":
        currentavghash += str("1")

    if thischar == "3":
        currentavghash += str("2")

    if thischar == "4":
        currentavghash += str("3")

    if thischar == "5":
        currentavghash += str("4")

    if thischar == "6":
        currentavghash += str("5")

    if thischar == "7":
        currentavghash += str("6")

    if thischar == "8":
        currentavghash += str("7")

    if thischar == "9":
        currentavghash += str("8")

    if thischar == "10":
        currentavghash += str("9")

    if thischar == "11":
        currentavghash += str("a")

    if thischar == "12":
        currentavghash += str("b")

    if thischar == "13":
        currentavghash += str("c")

    if thischar == "14":
        currentavghash += str("d")

    if thischar == "15":
        currentavghash += str("e")

    if thischar == "16":
        currentavghash += str("f")

    #print thischar+str(" $")
    val0 = 0
    charpos += 1

print str("Average hash for these "+str(linecount)+" hashes:")
print currentavghash
