def main():
#the main code
    x =[1,2,3]
    check(x)

#define specific functionality
def check(combo):
    if(isinstance(combo,list)==True):
        print("Horay")
        for i in combo:
		print combo[i]
        return
    else:
	print("Nope")
    

#Standard boilerplate to call main()
if __name__ == '__main__':
   main()
