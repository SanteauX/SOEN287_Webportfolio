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



aaa = "auteur"
day = 29
month = 3
year = 1997
title = "Naissance"
content = "Wesh wesh"

print(create_blog_post(aaa,day, month, year, title, content))