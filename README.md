# mrqqawebapp
*Database handover notes*

*What is it, what is it made out of and how was it developed?* 
I was involved in the development of a prototype database to store results from a new MR quality assurance (QA) test. The current QA scheme involves a bi-annual QA test but it is hoped that by introducing a shorter quarterly QA test in addition to this will identify errors sooner thereby ensuring that the images used for diagnosis are maintained at optimal. A tool that can store and manipulate the data from these tests would very useful for tracking trends in quality over time as well as to provide evidence for audits. 

The database that you manipulate and browse within the web application has two parts: a back-end where the actual results are stored on a server and the front-end which is an API that sits on top of the database and is what user’s interact with. 
The back-end database is a typical MySQL database composed of multiple different tables all linked together by common columns; this is typically stored and hosted on a server or local computer. As the database is currently hosted locally on my laptop, an identical database will need to be built again on another PC or server using the SQL scripts provided. You do not need to change the mysql script which builds the database – simply loading in this file and running it will give you an empty database with all the same tables and joins. You can build the database using MySQL in the terminal or you can use MySQL workbench – a user-friendly application which takes away the requirement to use MySQL language and is free to download. Once the database is built, I recommend populating the database using the terminal:
There is one change you need to make to this file and this is the filepaths to where the data for each table is stored. Once you’ve done that, simply do the following commands: 

mysql -u (username) -p
prompt will appear to type in your password 
use mrqqa_database; 
copy and paste MySQL population script section by section 
After each section, the terminal will tell you how many warnings there are and you should aim for 0. If warnings appear, to find out more about those warnings type: show warnings; 

The front-end web application which you access through a web browser was built using the Django API (The Djangogirls tutorial is very helpful as a starting place for building a webapplication: https://tutorial.djangogirls.org/en/django_installation/). All the files needed can be accessed by cloning the “mrqqawebapp” repository from my GitHub account: github.com/rebeccaforrester. To run the web application you need to download the following packages: Django 1.10.7, python 2.7, pip (most up-to-date version). I suggest installing a new virtual environment and then pip installing these packages. 
To run the web application locally, activate your virtual environment and type:
Python manage.py runserver
Then open web browser and type in the loopback address: 127.0.0.1:8000 and you should reach the database homepage. 

*Future improvements and developments* 
Once the tests have been finalised and the types of data wanting to be stored in the database are known, it would be useful to develop the design of the mysql database – this could involve adding in more tables to reduce redundancy. This should be very simply to do with the code already supplied. I recommend testing the table joins using some mysql queries first before you migrate this design into Django. 
To allow multiple users to access the database, the web application should be deployed on a server. Some research will need to be done into the best option to use. A free option for example is pythonanywhere.org which will freely host light-weight projects such as this. The Djangogirls tutorial describes how to launch your webapplication using pythonanywhere. 
Finally, a way of adding data using the front-end web application would be useful to reduce time and effort. This will require some research but should be do-able – this could be implemented as an administrator privilege. For the time-being, data can be adding using MySQL statements and I recommend doing this using MySQL workbench. 







