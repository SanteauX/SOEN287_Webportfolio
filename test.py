def return_me(id, username):
    messages = open("data/messages.csv")
    message_lines = messages.readlines()
    for i in range(1, len(message_lines)):
        line = message_lines[i].split(",")
        print("\n")
        print(line)
        #print(str(line[0])+" == "+str(id)+ " and "+str(line[3])+" == "+str(username))
        if str(line[0]) == str(id):
            print(str(line[0])+" == "+str(id)+" : True\n")
            print(str(line[3])+" == "+str(username)+" : ?")
            print(len(str(line[3])))
            print(len(str(username)))
            if(line[4] == username):
                print(str(line[3])+" == "+str(username)+" : True\n")
                print("Found")
                return message_lines[i]

    return False
id = 1000008
username = "Jiji"

def return_message(id):
    messages = open("data/messages.csv")
    message_lines = messages.readlines()
    for i in range(1, len(message_lines)):
        line = message_lines[i].split(",")
        if str(line[0]) == str(id):
                print("Found")
                return message_lines[i]

    return False


print(return_message(id))
