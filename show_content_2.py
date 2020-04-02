import sys
try:
    print(open(sys.argv[1], "r").read())
except IndexError:
        print ("Schon wieder das Argument vergessen! Es ist echt immer das Selbe mit dir!")


