def how_many_users():
    users = open("data/accounts.csv")
    user_lines = users.readlines()
    return len(user_lines)-1

def how_many_messages():
    messages = open("data/messages.csv")
    message_lines = messages.readlines()
    return len(message_lines)-1

def how_many_connections():
    connections = open("data/connections.csv")
    connection_line = connections.readlines()
    return len(connection_line)-1

print(how_many_users())

print(how_many_messages())