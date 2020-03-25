WHAT IS ON MY WEBSITE

- CREATE A NEW USER
--> /signup
    Users are stored in accounts.csv in /data

- LOG IN
--> /signup
    Will look for the user in /data/accounts.csv

- SEND A MESSAGE TO SOMEBODY WITH A USER ACCOUNT
--> Go to contact, got to the form with the link, enter the name of the USER
    The message will be stored in data/messages.csv

- READ MESSAGE
--> If you received a message, log in with your account
    --> /myMessages
    Will look in messages.csv for messages with the user as the destination of the message


- SEE MY PROJECTS
--> /projects
    Dynamic list of projects created with the Github API located in data/github_projects.csv