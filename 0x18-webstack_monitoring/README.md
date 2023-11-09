# Webstack monitoring :page_with_curl: 0x18. Webstack monitoring
## In this project :bulb:
## Overview
![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/c715d587-490d-443d-a5a2-bf82d18e8108)
![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/bee13354-a912-4203-9b4e-6773857e130f)

- "You cannot fix or improve what you cannot measure" is a famous saying in the Tech industry
- In the age of the data-ism,monitoring how our software systems are doing is an important thing
- In this project,I implement one of many tools to measure what is going on in my servers

Webstack monitoring can be broken down into 2 categories:
- Application monitoring: Getting data about your running software and making sure it is behaving as expected
- Server monitoring: Getting data about your virtual or physical server and making sure they are not overloaded(cloud
be CPU,memory,disk or network overload)

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/42760450-127c-4cbe-9809-dc3ad6582d5c)

## Requirements of the project
- Use Vi/Vim editor
- All bash scripts are executable
- Bash scripts pass `Shellcheck`(version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- all modules have documention`(python3 -c 'print(__import__("my_module").__doc__)')`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### Resources used
[Monitoring](https://intranet.alxswe.com/concepts/13)

[Server](https://intranet.alxswe.com/concepts/67)

[What is server monitoring](https://intranet.alxswe.com/rltoken/km_XUDAfXEBoXZQsIWEo5Q)

[What is application monitoring](https://intranet.alxswe.com/rltoken/z9jsikINjrsUo2QY5_Xz8g)

[System monitoring by Google](https://intranet.alxswe.com/rltoken/_8KIbIUNzMgKi_LiGMBWAw)

[Nginx logging and monitoring](https://intranet.alxswe.com/rltoken/V3GsrDcMHPdgrizShj4RCg)

### Task 0
Set up a data Datadog account and install the Datadog agent unto your server

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/3bc66463-f421-4a75-9d9e-aa2da2191ab0)

Requirements
- Sign up for Datadog - Please make sure you are using the US website of [Datadog](https://app.datadoghq.com)
- Use the US1 region
- Install `datadog-agent` on `web-01`
- Create an `application key`
- Server `web-01` should be visible in Datadog under the hostname `XX-web-01`

[helped to solve task](https://youtu.be/ZtDyQUkqRMs)


### Task 1
Among the litany of data your monitoring service can report to you are system metrics.You can use these metrics to
determine statistics such as read/write per second,which can help your company determine if/how they should scale.
Set up monitors within datadog

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/a1d67f64-d493-4851-8b98-98fbb3ab1370)

Requirements
- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.

Read about the various system metrics that you can monitor here. [System Check](https://intranet.alxswe.com/rltoken/4RPOEVDTqKXuvyU4Gkj2Bw)
- for read  : avg:system.io.r_s{*}
- for wirite : avg:system.io.w_s{*}

### Task 2
Now create a dashboard with different metrics displayed in order to get a few different visualizations
- Create a new `dashboard`
- Add at least 4 `widgets` to your dashboard.

[help here](https://youtu.be/fR9sd5V6pUE)
