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
