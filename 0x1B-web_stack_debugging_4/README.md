# debugging :page_with_curl:0x17 Web stack debugging #4

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/efc98042-6e07-47b7-aa80-637a8c49467f)

## In this project :bulb:

I tested how well our web server setup featuring NGINX is doing under pressure 

## Requirements
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error

### Installation of puppet
`$ apt-get install -y ruby`
`$ gem install puppet-lint -v 2.1.1`

### Task 0
In this web stack debugging task, we are testing how well our web server setup featuring Nginx
is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of  
failed requests.
For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. 
In this case, I will make 2000 requests to my server with 100 requests at a time.
- 943 requests failed,SO i fixed our stack so that we get to 0 
remember that when something is going wrong, logs are your best friends!

- Make the 2000 requests)
`ab -c 100 -n 2000 localhost/`
- Run the file to fix it
`puppet apply 0-the_sky_is_the_limit_not.pp`
- Make the requests again to see if it was fixed
`ab -c 100 -n 2000 localhost/`
