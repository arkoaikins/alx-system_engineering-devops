# MySQL :page_with_curl: 0x14. MySQL

## In this project :bulb:

### Task 0
- Installed `MySQL` on both servers web-01 and web-02
  - MySQL distribution is 5.7.x
- Installed using the help of this material
[How to Install mysql 5.7](https://intranet.alxswe.com/concepts/100002)

### Task 1
- Created a user and password for both MySQL databases
  - User has the permission to check the primary/replica status of the databases

### Task 2
In order for you to set up replication,there should be a database with at least one
table and one row in the primary MySQL server(web-01) to replicate the form
- Created database named `tyrell_corp`
   - a table `nexus6` in the database with two entry to it
   - Users have permission on the table

### Task 3
Before primary-replica synchronization,On the primary MySQL server (web-01), 
I created a new user for the replica server.
- Name of the new user is `replica_user`
   - with the host name  `%` and a password
   - replica has the permission to replicate the primary MySQL server

### Task 4
Setup a Primary-Replica infrastructure using MySQL
Having a replica member on for your MySQL database has 2 advantages:
- Redundancy: If you lose one of the database servers, you will still have another
working one and a copy of your data
- Load distribution: You can split the read operations between the 2 servers,reducing
the load on the primary member and improving query response speed

My SQL primary is hosted on `web-01`,no `bind-address` just comment on this parameter
My SQL replica is hosted on `web-02`
Setup replication for the MySQL database named tyrell_corp

-  UFW must allow connections on port 3306(default MySQL port)

### Task 5
What if the data center where both your primary and replica database servers are hosted are down
because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost.
That’s why you want to backup and store them in a different system in another physical location.
This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.

- Bash script that generates a MySQL dump and creates a compressed archive out of it.
   - The MySQL dump contain all  MySQL databases
   - The MySQL dump is named backup.sql
   - The MySQL dump file is compressed to a tar.gz archive file
   - This archive have the name : day-month-year.tar.gz
   - The user to connect to the MySQL database must be root
   - This  have the name format: day-month-year.tar.gz
Bash script accepts one argument that is the password used to connect to the MySQL database

### some important resources
[Database administration](https://intranet.alxswe.com/concepts/49)
[Web stack debugging](https://intranet.alxswe.com/concepts/68)
[How to Install mysql 5.7](https://intranet.alxswe.com/concepts/100002)
[What is a primary-replica cluster](https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA)
[MySQL primary replica setup](https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg)
[Build a robust database backup strategy](https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q)
[MySQL replication](https://devmuiru.me/2-steps-to-mastering-mysql-replication/)



