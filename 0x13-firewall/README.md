# Firewall :page_with_curl: 0x13-firewall

## In this project :bulb:

### Task 1
- Installed `ufw` firewall on my web-01 server
- I use the firewall to block all incoming traffic,except the following TCP ports:
   - 22 (SSH)
   - 443 (HTTPS SSL)
   - 80 (HTTP)
- The ufw commands used have been shared in  my anwer file `0-block_all_incoming_traffic_but`


firewall rules!:
if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH
and we will not be able to recover it. When you install UFW, port 22 is blocked by default,
so you should unblock it immediately before logging out of your server.


### Task 2
- Configured web-01 firewall to redirect port 8080/TCP to port 80 TCP
- a copy of my ufw modified configuration file is share in the answer file `100-port_forwarding`


### some important resources
[what is a firewall](https://www.wikiwand.com/en/Firewall_%28computing%29)

[Web stack debugging](https://intranet.alxswe.com/concepts/68)

[The Ultimate Firewall Guide](https://devmuiru.me/9-potent-strategies-for-firewall-mastery/)

[How To Set Up a Firewall with UFW on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-20-04)
