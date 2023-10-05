#                         0x10.HTTPS SSL
Devops -   SysAdmin   -Security
## Overview
- what happens when you don't secure your website traffic 😂🤣
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/xCmOCgw.gif


This project involves 3 tasks
In this project,
- I add SSL certificate to my network connections(on my load balancer serving two webservers)
- I use SSL encript the communication between web browsers and my web server
- so that posible hackers can not intercept any information

## Project details
- Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains. 

- “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

- A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS

### Dependant resources used

[What is HTTPS?](https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ)

[What are the 2 main elements that SSL is providing](https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw)

[HAProxy SSL termination on Ubuntu16.04](https://intranet.alxswe.com/rltoken/XD_RckEgjds0UkoMsfxp2A)

[SSL termination](https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g)

[Bash function](https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ)

### Requirements for the tasks
- Used the vi editor
- Bash scripts are executable
- Bash scripts pass Shellcheck(version 0.3.7) without any error
- First line of Bash scripts `#!/usr/bin/env bash`
- Second line of bash scripts are comments explaining what the script is doing
