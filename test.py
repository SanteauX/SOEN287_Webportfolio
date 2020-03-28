import bcrypt



def matrixChartJS():
    ocsv = open("data/connections.csv", "r")
    ncsv = open("data/chartjs2.csv", "w")
    days = "Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday"
    ncsv.write(days)
    dayz = days.split(",")
    lines = ocsv.readlines()
    line2 = dayz
    for i in range(0, len(line2)):
        line2[i] = 0
    dayz = days.split(",")
    for i in range(0, len(lines)):
        line = lines[i].split(",")
        z = line[3]
        for j in range(0, len(dayz)):
            if z == dayz[j]:
                line2[j]+=1
    #ncsv.write(line)
    print(dayz)
    print(line2)

def change_password(username, email, phone, password, passwordConfirmation):
    accounts = open("data/accounts.csv", "r+")
    account_lines = accounts.readlines()
    for i in range(1, len(account_lines)):
        line = account_lines[i].split(",")
        print(line[0]+ " ==  " + username + "& "+ line[1] +" == "+ email+" & "+ line[2]+" == "+phone)
        if(line[0] == username and line[1] == email and line[2] == phone and password == passwordConfirmation):
            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(password.encode(), salt)
            line[3] == password
            print("changed")

change_password("Santeau", "berkham@gmail.com", "45678765434", "newpassword20192090IE","newpassword20192090IE" )