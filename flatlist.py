#def main
def main():
    x =[12,34,[45,67]]
    flatlist(x)

#define stuff
def flatlist(combo):
    if(isinstance(combo,list)==True):
        for i in combo:
            print combo
    else:
	print combo


#boiler plate main
if __name__ == '__main__':
  main()
