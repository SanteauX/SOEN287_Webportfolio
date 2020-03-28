def create_blog_post(author, day, month, year, title, content):
    print("create blog post")
    posts = open("blog_posts.csv", "r+")
    post_lines = post.readlines()
    id = 1000000+len(post_lines)
    print("id: "+id)
    line = str(id) + "," +str(flask_login.current_user.username) + "," + str(day) + "," + str(month) + "," + str(year) + "," + str(title) + "," + str(content)+"\n"
    print("write line: "+line)
    posts.write(line)
    return True

def fixco():
    ocsv = open("data/connection.csv", "r")
    ncsv = open("data/chartjs.csv", "w")
    ncsv.write("Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday")
    Monday = 0
    Tuesday = 0
    Wednesday = 0
    Thursday = 0
    Friday = 0
    Saturday = 0
    Sunday = 0
    # for i in range(0, len(ocsv.readlines())):
    #     if

def connection_chart():
    ocsv = open("data/connections.csv", "r")
    ncsv = open("data/chartjs.csv", "w")
    ocsv_lines = ocsv.readlines()
    line = "0"
    for i in range(1, 24):
        line+= ","+str(i)
    ncsv.write(line+"\n")
    line2 = line.split(",")
    for i in range(0, len(line2)):
        line2[i] = 0
    for i in range(1, len(ocsv_lines)):
        ocsv_line = ocsv_lines[i].split(",")
        z = int(ocsv_line[4])
        line2[z]+=1
    csv2 = str(line2[0])
    for i in range(1, len(line2)):
        csv2+= ","+str(line2[i])
    ncsv.write(csv2)
    print(line)
    print(csv2)

connection_chart()