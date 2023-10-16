# debugging :page_with_curl: Web stack debugging #2

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/e2963683-2a94-4ff9-9a35-8c9f0535f5e8)

## In this project :bulb:

A new container was used to practice the dubugging skills

### Task 0

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/849a6b48-0389-4967-a4bc-1738594f126e)

- The user root is, on Linux, the “superuser”. It can do anything it wants
-  A good practice is that one should never be logged in the root user
- as if you fat finger a command and for example run rm -rf /, there is no comeback
- That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:
- Bash script that accpets one argument
-  script should run the whoami command under the user passed as an argument
- try your script by passing different users
 - example

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/254d4bd1-2eb0-4cc4-8411-7ef7f5fa1a05)


### Task 1
- The root user is a superuser that can do anything on a Unix machine, the top administrator
- Security wise, you must do everything that you can to prevent an attacker from logging in as root
- With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations)
- and instead run the process as the less privileged nginx user instead.
- This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.
- Fix the container so that Nginx is running as the nginx user.
Requirements
- nginx must be running as nginx user
- nginx must be listening on all active IPs on port 8080
- You cannot use apt-get remove

After debugging

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/03a0ddf6-6712-4cc2-a1fc-7eb142155036)


### Task 2
- Making all the fix that was done in task 1 short and sweet


### some important resources
