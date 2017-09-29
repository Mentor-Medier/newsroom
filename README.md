Newsroom
========

A web application for storing and managing news stories.

### Milestones

1. Phase 1 (Running)

   - Necessary package installation
   
   - Database creation
   
   - Sign up and login system for users

   - A page to list all stored storis

   - A page to create new story

2. Phase 2

   - Add JSON format for each story

   - Update story list page to include JSON link

3. Phase 3
 
   - Add date field in story form

   - Modify database design
   
   - Add XML format for each story

   - Update story list page to include XML link

4. Phase 4

   - Add edit and delete functinoalities for each story

   - Delete function should include confirmation alert
   
### Software Requirements

The application is coded in a Windows 8 (64 bit) machine using PyCharm Professional (Version: 2017.2.3).

The following tools are necessary to run the application:

- **Python** : 3.6.2 (64 bit)
- **MySQL** : 10.1.21-MariaDB

I used XAMPP (Version 3.2.2) as it includes both MySQL and phpMyAdmin

### Necessary Package Installation

- Install virtual environment

		$ python -m venv newsroom_venv

- Activate virtual environment

		$ newsroom_venv\Scripts\activate.bat

- Install necessary packages included in requirements.txt

		$ pip install -r webapp\requirements.txt

In CMD, the above commands are executed like below:

![Package Installation](Screenshot/Phase1/install_package.png)		
		
### Create Database

- From phpMyAdmin create database `newsroom_database`

![Database Creation](Screenshot/Phase1/create_database.png)

- Activate virtual environment (if not activated)

		$ newsroom_venv\Scripts\activate.bat

- Change directory to webapp

		$ cd webapp

- Change MySQL configuration in `config.py` using own MySQL username, password and database name. 
Here my MySQL username is root, password is empty and database name is newsroom_database

		$ SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/newsroom_database'

- To create the database run `db_create.py`. Run only one time.

		$ python db_create.py

- To track down the schema changes of database, I have used migration techniques.
To migrate database run `db_migrate.py`. This script should run after every modification in database schema.

		$ python db_migrate.py

The relationship between table looks like below in phpMyAdmin

![Database Creation](Screenshot/Phase1/database.png)		
		
### To Run the Application

- Activate virtual environment (if not activated)

		$ newsroom_venv\Scripts\activate.bat

- Run the `application.py`

		$ python application.py


### What is this repository for?

- Quick summary
- Version Controlling
- Screenshot enlisting of each phase (See attached Screenshot folder)
- [Issue Tracking](https://bitbucket.org/arsho/newsroom/issues)


### Change log

See CHANGELOG in CHANGELOG.md