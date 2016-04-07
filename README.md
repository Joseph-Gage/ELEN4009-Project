# ELEN4009 Project - FriendAnalyzer

## This document contains instructions on how to setup up the project environment for the FriendAnalyzer Project.
	Written by Julian Zeegers and James Allingham

**Pre-requisites:**

- Ubuntu 15.04 or later
- Python 2.7 is installed (sudo apt-get install python)
- pip is installed (sudo apt-get install python-pip python-dev build-essential)
- aptitude is installed (sudo apt-get install aptitude)
- Apache2 is installed (sudo apt-get install apache2)
- Java Develoment Kit is installed (sudo apt-get install default-jdk)

**How to setup Django Framework (Ubuntu):**

1. Install Django, run: 
	- sudo pip install Django
	- note that there have been issues with incompatibilites with older versions of Django

2. Copy the Project Folder "$GITPATH/ELEN4009-Project/source/friendAnalyzer" to "/var/www":
	- sudo cp -r $GITPATH/ELEN4009-Project/source/friendAnalyzer /var/www

3. Install py2neo, run:
	- sudo pip install py2neo

4. Open "/var/www/friendAnalyzer", in a terminal:
	- run: python manage.py runserver
	- The Django server is now running

5. In a browser, go to: "127.0.0.1:8000"
	- If a friend Analyzer homepage loads, Django set up is complete.
	- The Django server can now be stopped (with Crlt + Z)  


**How to setup Apache Server (Ubuntu):**

1. Install modwsgi, run:
	- sudo apititude install libapache2-mod-wsgi

2. Replace "/etc/apache2/sites-available/000-default.conf" with  "$GITPATH/ELEN4009-Project/source/000-default.conf".

3. Open "000-default" and ensure that all the directories and Admin infomation is correct. Path directories should be valid and exist.

4. Open "/etc/apache2/apache2.conf" and add (to the last line):
	- "WSGIPythonPath /var/www/friendAnalyzer"

5. Open "/var/www", in a terminal, and make a directory called "logs", run:
	- sudo mkdir logs	
	- sudo chmod 777 logs

6. Open "/var/www", in terminal, and run:
	- sudo service apache2 stop

7. In a browser, go to : "localhost"
	- Again, Friend Analyzer Project homepage should load.
	- This time it is using the Apache server.
	- The links to other pages will not work yet.

**How to setup Neo4j Graph Database**

1. Download and install Neo4j by going to http://neo4j.com/download-thanks/?edition=community&flavour=unix&release=2.3.3, and following the instructions

2. Run Neo4j:
	$NEO4J_HOME/bin/neo4j start 

3. In a browser, go to: "127.0.0.1:7474"
	- You will be promted for a user name and password use "neo4j" and "neo4j"
	- Now, following the prompt, change the password to "nathan3j"
	- Leave this open for use in step 6

4. python /var/www/friendAnalyzer/friendAnalyzer/dbSetup.py

5. Go back to the browser and in the console enter: "MATCH (n) return n"
	- You should see a small graph of 6 nodes and connecting edges
	- The browser can now be closed

6. Open "/var/www", in terminal, and run:
	- sudo service apache2 start
