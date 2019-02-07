# import_csv_to_oracle
Import .csv files into an oracle table while working on an 'external library restricted' server from your local machine.

As a beginner I had a hard time figuring out this stuff by myself, especially getting rid of the errors that were present, so I thought I share how I did it. I could have used libraries like pandas but external libraries were not allowed to be installed in the server, and my local machine did not have oracle installed.

Requirements
1. PuTTY
2. A secure FTP client
3. yourfile.csv
4. Access to the remote server [which has Oracle and TOAD installed]

Procedure:
1. Access the server remotely using remote desktop connection application on your machine, run TOAD (assumption: it is always running) and login to the database e.g "db".
2. Create a table of your choice in the database e.g "db_table".
3. Minimize the remote desktop application and log in to your database from your local machine using a secure FTP client of your choice and locate a directory of your choice.
4. Place the file <import_csv.py> inside the directory together with <yourfile.csv>. Make sure you edit the code according to the comments inside.
5. Minimize the SFTP client and login in to the server using PuTTY.
6. Migrate to the location where you placed your files [<import_csv.py> and <yourfile.csv>].
7. Run the command "python import_cvs.py" from PuTTY terminal.
8. After successfully running, confirm if the information has been loaded in the db_table.
9. Remove the files you copied from the server
