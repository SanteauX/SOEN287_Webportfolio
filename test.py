def register_user(username, email, password):
    accounts = open("data/accounts.csv", "r+")
    account_lines = accounts.readlines()
    for i in range(0, len(account_lines)):
        print("line: "+account_lines[i])
        if username == account_lines[i][1] or email == account_lines[i][2]:
            return "Account not created, username or email already exists"
    id = 1000001+len(account_lines)
    line = str(id) + "," + str(username) + "," + str(email) + "," + str(password)
    print(line)
    accounts.write(line)
    return "Account created"
    accounts.close()
    accounts = open("data/accounts.csv", "r+")
    account_lines = accounts.readlines()
    for i in range(0, len(account_lines)):
        print("line: "+account_lines[i])

print(register_user("Welson", "hugo.joncour.k2o@gmail.com", "dGpWLzejkt4P"))