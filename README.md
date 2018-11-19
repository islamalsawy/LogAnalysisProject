**Logs Analysis Project**
---
This is  Logs Analysis project a part of udacity Uconnect Full stack engineer program.
We we're supposed to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.

The output queries should answer the following questions. 

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

**Requirements**
---
The project code requires the following software:

- Python 3.5.2 or later
- psycopg2 2.7.3.2 or later
- PostgreSQL 9.5.10 or later

You can run the project in a Vagrant managed virtual machine (VM) which includes all the required dependencies (see below for how to run the VM). For this you will need [Vagrant](https://www.vagrantup.com/downloads) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on your system.


**Project contents**
---
This project consists of the following files:

`Queries.py` - The Python program that connects to the PostgreSQL database, executes the SQL queries and displays the results.
`README.md` - This read me file.
`Outputs.txt`- TXT file contains sample outputs.

**Running the Project**
---

• Run in the working folder `vagrant up` to configure the VM
• Run `vagrant ssh` to log into the VM
• Download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and save it in the working VM folder
• Run `psql -d news -f newsdata.sql` to generate the database
• Run `python Queries.py` in terminal to generate the database report