# Application server:page_with_curl:0x1A. Application server

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/55a1592e-9ee9-4030-b198-8912d46fdc0b)
![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/aa596d19-28af-42ed-ad5b-6ad438a52580)

My web infrastructure is already serving webpages vi web server Nginx that installed in my `first web stack project`.
While a webserver can also serve dynamic content,this task is usually given  to an application server.

## In this project :bulb:
- I added an application server to my infrastrucutre,plugged it into my `Nginx` and made it serve my Airbnb clone project

### Task 0
Serve my AirBnB clone v2 - Web framework on my `web-01` server.
- This is to set up my development environment for testing an debugging code before deploying it to production
- Requirements
 - Install `net-tools` package on `web-01` server: `sudo apt install -y net-tools`
 - Git clone AirBnB_clone_v2 on `web-01` server
 - Configure `web_flask/0-hello_route.py` to serve it content from the route /airbnb-onepage/ on port 5000

Run to see if web_flask/0-hello_route.py is running  on port 5000 sucesfully

```
ubuntu@264281-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 
 * Serving Flask app '0-hello_route'
 
 * Debug mode: off

Address already in use

Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```

But it could not run,there was an error message that a service is already running on port 5000
so i run
`sudo netstat -ltnp`

and saw that it is the datadog agent that is running on that port
so i changed  both agent port from 5000 > 5005 and from 5001 > 5006
so that way we can work on my  project on 5000 and 5001

`sudo sed -i 's/# expvar_port: 5000/expvar_port: 5005/g' /etc/datadog-agent/datadog.yaml`

`sudo sed -i 's/# cmd_port: 5001/cmd_port: 5006/g' /etc/datadog-agent/datadog.yaml`

`sudo ufw allow 5005`

`sudo ufw allow 5006`

`sudo ufw reload`

`sudo service datadog-agent restart`

I could have also done it manually by

- sudo vi /etc/datadog-agent/datadog.yaml
- find : # expvar_port: 5000
- remove hashtag and change it to port u want
- do the same with cmd_port
- sudo service datadog-agent restart

then i run `sudo netstat -ltnp` to see that the change of port was made sucessfull

No i can run my app

`ubuntu@264281-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route`

`* Serving Flask app '0-hello_route'`

`* Debug mode: off`

`WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.`

` * Running on all addresses (0.0.0.0)`

`* Running on http://127.0.0.1:5000`

`Press CTRL+C to quit`

Then on my second window 

`ubuntu@264281-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/`

`Hello HBNB! ubuntu@264281-web-01:~/AirBnB_clone_v2$`

# Task 1
Now that you have your development environment set up, 
let’s get your production application server set up with Gunicorn on `web-01`, port `5000`
You’ll need to install Gunicorn and any libraries required by your application.
Your Flask application object will serve as a WSGI entry point into your application.
This will be your production environment. As you can see we want the production and development
of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
- Requirements
  - Installed `Gunicorn`  `sudo pip3 install gunicorn==19.9.0`  and `sudo ln -s "$(which gunicorn)" /usr/bin/gunicorn`
  - I served the same content from the same route as the previous task.
  - So i verified that it's working by binding a `Gunicorn` instance to localhot listening on port 5000
  - with my application object as the entry point

SO i run it this way

- Terminal 1:
```
ubuntu@264281-web-01:~/AirBnB_clone_v2$`gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app`
[2019-05-03 20:47:20 +0000] [3595] [INFO] Starting gunicorn 19.9.0
[2019-05-03 20:47:20 +0000] [3595] [INFO] Listening at: http://0.0.0.0:5000 (3595)
[2019-05-03 20:47:20 +0000] [3595] [INFO] Using worker: sync
[2019-05-03 20:47:20 +0000] [3598] [INFO] Booting worker with pid: 3598
```

- Terminal 2:
```
ubuntu@264281-web-01:~//AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~$
```

# Task 2
Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/
Requirements
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000
Notes
- In order to test this you’ll have to spin up either your production or development application server (listening on port 5000)
- In an actual production environment the application server will be configured to start upon startup in a system initialization script.
 - This will be covered in the advanced tasks.

Run the app
```
Window 1
ubuntu@264281-web-01:~//AirBnB_clone_v2$ gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
[2019-05-06 20:43:57 +0000] [14026] [INFO] Starting gunicorn 19.9.0
[2019-05-06 20:43:57 +0000] [14026] [INFO] Listening at: http://0.0.0.0:5000 (14026)
[2019-05-06 20:43:57 +0000] [14026] [INFO] Using worker: sync
[2019-05-06 20:43:57 +0000] [14029] [INFO] Booting worker with pid: 14029
```

```
Window2
ubuntu@264281-web-01:~//AirBnB_clone_v2$ curl 127.0.0.1/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```

```
On my local terminal
```
vagrant@ubuntu-xenial:~$ curl -sI 54.160.114.180/airbnb-onepage/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Mon, 06 May 2019 20:44:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 11
Connection: keep-alive
X-Served-By: 229-web-01

vagrant@ubuntu-xenial:~$ curl 54.160.114.180/airbnb-onepage/
Hello HBNB!vagrant@ubuntu-xenial:~$
- Nginx configuration file in `File: 2-app_server-nginx_config`










### Resource
[Help articlie](https://shazaali.substack.com/p/0x1a-application-server-part-1)
