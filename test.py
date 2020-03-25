########################### PROJECTS GITHUB
def get_github_projects():
    projects = open("data/github_projects.csv")
    project_lines = projects.readlines()
    for i in range(0, len(project_lines)):
        project_lines[i] = project_lines[i].split(",")
    return project_lines

def myMessages():
    lines = getMessages(session['username'])
    number = len(lines) - 1
    return render_template("myMessages.html", lines = lines, number = number)

def getMessages(username):
    messages = open("data/messages.csv", "r")
    message_lines = messages.readlines()
    messages_for_me = message_lines[0].split(",")
    for i in range(0, len(message_lines)):
        if message_lines[i][3] == username:
            print(message_lines[i][3] + " ==  "+ username)
            mm = message_lines[i].split(",")
            messages_for_me.append(ml)
    return messages_for_me

print(getMessages("TestTest"))


#print(get_github_projects())