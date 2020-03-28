def fixco():
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
    print(dayz)
    print(line2)

fixco()