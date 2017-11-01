class username:
    def add(z):
        while(True):
            add = open("{}.txt".format(z), 'a+')
            file = open("{}.txt".format(z), 'r')
            names = file.read()
            namelist = list(names.split())
            entered = str(input("Username: "))
            lower = entered.lower()
            test = (lower.split())
            if not(entered.isalpha()):
                print("Please enter a valid username\n")
                continue
            elif set(test).issubset(set(namelist)):
                print("That name is already in use.",
                      "\nPlease enter a different username. \n")
                continue
            elif len(lower) < 4 or len(lower) > 12:
                print("Please enter a username with 4-12 characters.\n")
                print(lower)
                continue
            else:
                plusnewline = lower + "\n"
                add.write(plusnewline)
                add.close()
                break
        
    def list(z):
        file = open("{}.txt".format(z),"r+")
        names = file.read()
        print(names)
        file.close()

username.add('usernames')
username.list('usernames')
