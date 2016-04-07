# ELEN4009 Project - FriendAnalyzer

## This document contains instructions on how to setup up the project environment for the FriendAnalyzer Project.
	Written by Julian Zeegers and James Allingham

**Pre-requisites:**

- Ubuntu 15.04 or later
- Python 2.7 is installed (sudo apt-get install python)
- pip is installed (sudo apt-get install python-pip python-dev build-essential)
- aptitude is installed (sudo apt-get install aptitude)
- Apache2 is installed (sudo apt-get install apache2)
- Java Develoment Kit is installed (audo apt-get install default-jdk)

**How to setup Django Framework (Ubuntu):**

1. Install Django, run: 
	- sudo pip install Django

2. Save the Project Folder "friendAnalyzer" in the following directory:
	- "/var/www"

3. Open "/var/www/friendAnalyzer", in a terminal:
	- run: python manage.py runserver
	- The Django server is now running

4. In a browser, go to: "127.0.0.1:8000"
	- If a friend Analyzer homepage loads, Django set up is complete.
	- The Django server can now be stopped (with Crlt + Z)  


**How to setup Apache Server (Ubuntu):**

1. Install modwsgi, run:
	- sudo apititude install libapache2-mod-wsgi

2. Replace "/etc/apache2/sites-available/000-default.conf" with  "$GITPATH/ELEN4009-Project/source/000-default.conf".

3. Open "000-default" and ensure that all the directories and Admin infomation is correct. Path directories should be valid and exist.

4. Open "/etc/apache2/apache.conf" and add (to the last line):
	- WSGIPythonPath /var/www/friendAnalyzer

5. Open "/var/www", in a terminal, and make a directory called "logs", run:
	- sudo mkdir logs	
	- sudo chmod 777 logs

6. Open "/var/www", in terminal, and run:
	- service apache2 restart

7. In a browser, go to : "localhost"
	- Again, Friend Analyzer Project homepage should load.
	- This time it is using the Apache server.
	- Setup is now complete.

**How to setup Neo4j Graph Database**

1. Download and install Neo4j by going to http://neo4j.com/download-thanks/?edition=community&flavour=unix&release=2.3.3, and following the instructions

2. Run Neo4j:
	$NEO4J_HOME/bin/neo4j start 

3. In a browser, go to: "127.0.0.1:7474"
	- You will be promted for a user name and password use "neo4j" and "neo4j"
	- Now, following the prompt, change the password to "nathan3j"
	- Leave this open for use in step 6

4. Install py2neo, run:
	- sudo pip install py2neo

5. python /var/www/friendAnalyzer/friendAnalyzer/dbSetup.py

6. Go back to the browser and in the console enter: "MATCH (n) return n"
	- You should see a small graph of 6 nodes and connecting edges
	- The browser can now be closed

7. Open "/var/www", in terminal, and run:
	- service apache2 restart
