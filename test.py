def register_user(username, email, password):
    accounts = open("data/accounts.csv", "r+")
    account_lines = accounts.readlines()
    print(len(accounts.readlines()))
    for i in range(0, len(accounts.readlines())):
        print(account_lines[i])
        if username == account_lines[i][1] or email == account_lines[i][2]:
            return "Account not created, username or email already exists"
    id = 1000000+len(account_lines)
    line = str(id) + "," + str(username) + "," + str(email) + "," + str(password)+"\n"
    accounts.write(line)
    return "Account created"

#print(register_user("Welson", "hugo.joncour.k2o@gmail.com", "dGpWLzejkt4P"))


def test_accounts():
    accounts = open("data/accounts.csv", "r+")
    al = accounts.readlines()
    for i in range(0, len(al)):
        print(al[i])

test_accounts()