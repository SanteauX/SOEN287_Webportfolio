ASSIGNMENT FOR THE CLASS SOEN 287

WHAT IS ON MY WEBSITE

- CREATE A NEW USER
--> /signup
    Users are stored in accounts.csv in /data

- LOG IN
--> /signup
    Will look for the user in /data/accounts.csv
    When connected you can see in the footer in purple text if you're connected or not

- LOG OUT
--> /logout in the URL
    or go to /account and click on logout
    Will disconnect the current user

- SEND A MESSAGE TO SOMEBODY WITH A USER ACCOUNT
--> Go to contact, got to the form with the link, enter the name of the USER
    The message will be stored in data/messages.csv

- READ MESSAGE
--> If you received a message, log in with your account
    --> /myMessages
    Will look in messages.csv for messages with the user as the destination of the message

- SEE MY PROJECTS (HUGO JONCOUR'S PROJECTS / GITHUB: @SanteauX)
--> /projects (link in navbar)
    Dynamic list of projects created with the Github API located in data/github_projects.csv

- SEE STATISTICS
--> Must be connected /login
    Once connected you will be redirected to /account
    Once in /account you can click on "See statistics",

- POST A BLOG ARTICLE
--> Must be connected /login
    Once connected you will be redirected to /account
    Once in /account you can click on "Make a new blog post",
    Write article, click on "post article"
    it will appear in /blog

OTHER:

myProjects.py uses the GitHub API to get my projects to the .csv
histograms.js is a work in progress


######################################## REQUIREMENTS OF THE ASSIGNMENT: ########################################

All your forms should be defined as subclasses of FlaskForm, and should have properly defined validators. 

and should have properly defined validators.
--> Validtors are either part of the form or in the function creating the data send to csv, but are checked anyway

Your forms should be handled properly, by defining a route accepting GET and POST methods, and you should use the POST/REDIRECT/GET pattern when the form data validates (as shown in class).
--> They are

and you should use the POST/REDIRECT/GET pattern when the form data validates (as shown in class).
--> They do. Exemple: /login & /logout


Your web site data should be stored in files, located in the data subfolder. The data should in CSV or JSON formats.
--> accounts.csv
--> blog_posts.csv
--> github_projects.csv
--> messages.csv

Your web site should contain:
            At least 2 forms:
            with at least one of these forms which must be significantly different 
            from the ones included in the examples covered in class and in the tutorials.
            --> Signup          1
            --> Login           2
            --> ContactForm     3
            --> Post (blog)     4

            At least 1 table and at least 1 list created dynamically from data stored in a local file
            --> myMessages          1
            --> blog                2
            --> projects (github)   3
            --> Connections (chart) 4

            A way to support user logins:
            --> it does /login
                You can test with ID: "TestTest"; Password: "TestTestTestTestTestTest"

            Some pages should be protected and viewable by only the logged in users.
            --> messages
            --> account
            --> statistics

            There should be a way, in each page, to figure out if a user is logged in or not.
            xxxxxxxxxxxxx

            You could have a special div in your base template that displays whether a user is logged in or not.
            --> Login


At least 3 of the following features:

            I didn't do:

                    JavaScript input or form validation, using regular expressions where appropriate, on at least 2 forms.
                    
                    JavaScript Ajax call(s) to dynamically load data from the server, and the server code to support it.
            
                    Using a database instead of local files to store data.
                    
                    search page (or possibly a div in a block shared among your templates) to search for something interesting on your site (for example, search for some blog posts).

            I did:
                    A Forgot password page to help reset a user's lost password.
                    ------------------> Login -> Forgot password: Username + PhoneNumber + email --> Reset Password

                    More advanced user interface (more professional design, with animations, ... , using external JS libraries or other tricks)
                    ------------------> Histogram Chart of connections in /statistics (uses Chart.JS)


            
Some other advanced feature, going beyond the basic examples presented in class and in the tutorials, including, but not limited to
            
            I didn't do:

                    A RESTful API for your web site

                    The ability to send emails from your web site

            I did:
                    Using external APIs to connect to other web sites (like using the Facebook API for example)
                    ------------------> Github

                    More advanced session mangement (tracking, user statistics, ...)
                    ------------------> /statistics (connection/hour)

                    Role-based access control or other more adbvanced user permissions management
                    ------------------> Only registered users are allowed to post on the blog section
                    ------------------> Only registered users can see messages

