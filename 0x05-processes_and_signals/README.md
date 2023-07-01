# 0x05. Processes and signals
- This is a bash scripting  project done in my ALX Software engineering

## What to expect from this project
|        Table of contents           | 
| -----------------------------------| 
|   What i learnt in this project    |
|   Project tasks(task 0 - task 12)  |

## What i learnt in this project(explained briefly)
- In this project i learnt about processes and signals in Bash scripting
- What a PID is in Bash scripting
   - A unique numeric identifier assigned to each running process in a computer system
- What a process is
   - running task or a series of instructions being executed on the computer's operating system
- How to find a process’ PID
   - using the pgrep or ps command with options
- How to kill a process
   - Using the kill command or kill with options
- What is a signal and how it is used
   - used to communicate and control the behavior of processes.
- Signals that cannot be ignored by a process
   - 2 signals cannot be ignored by a process are "SIGKILL" and "SIGSTOP."

## Project tasks
### 0. What is my PID
Bash script that displays its own PID.
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/eb0831dd-4662-499d-ba59-afc3606291e4)
- file: 0-what-is-my-pid

### 1. List your processes
Bash script that displays a list of currently running processes
Requirements:
- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/dc72961d-ebfc-4b5b-84e9-b33db497e608)
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/06407f19-95d8-4bff-825b-f9a81a2d0179)
- file: 1-list_your_processes

### 2.Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
Requirements:
- You cannot use pgrep
- The third line of your script must be # shellcheck disable=SC2009
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/b42a932c-cc87-4084-824f-50635c4e2b0f)
- file:2-show_your_bash_pid

### 3.Show your Bash PID made easy
Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
Requirements:
- You cannot use ps
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/296c7ff6-420c-4e34-b7e1-2b81d5620edf)
- file:3-show_your_bash_pid_made_easy

### 4.To infinity and beyond
Bash script that displays To infinity and beyond indefinitely.
Requirements:
- In between each iteration of the loop, add a sleep 2
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/813afc2d-bf1b-45b4-8362-28944eea39fa)
- file: 4-to_infinity_and_beyond

### 5. Don't stop me now!
We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.
Write a Bash script that stops 4-to_infinity_and_beyond process.
Requirements:
- You must use kill
#### Tested code by
- Terminal #0
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/66ae3dcd-6bdf-4727-8941-cb0d0ed23d54)
- Terminal #1
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/b7cde57b-0fd4-4912-849c-099123258f63)
- File: 5-dont_stop_me_now

### 6. Stop me if you can
Bash script that stops 4-to_infinity_and_beyond process.
Requirements:
- You cannot use kill or killall
#### Tested code by
- Terminal #0
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/ddb072fd-3df9-4efb-94fe-a5b818111995)
- Terminal #1
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/94188a75-d49e-48d9-a991-5d8a7269502b)
- File: 6-stop_me_if_you_can

### 7. Highlander
Bash script that displays:
- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal
- Make a copy of your 6-stop_me_if_you_can script, name it 67-stop_me_if_you_can, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.
#### Tested code by
Terminal #0
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/3691b76e-e614-4dc5-ac63-ec4566889287)
Terminal #1
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/5610f970-b473-40ac-b586-c098c305e778)
- File: 7-highlander

### 8. Beheaded process
Bash script that kills the process 7-highlander.
#### Tested code by
Terminal #0
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/5810b99f-3233-4ab0-bc65-48dbe1bb74f2)
Terminal #1
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/6ff87b49-8cb3-4f30-a29a-5b7b4f726caa)
- File: 8-beheaded_process

###9. Process and PID file
Bash script that:
- Creates the file /var/run/myscript.pid containing its PID
- Displays To infinity and beyond indefinitely
- Displays I hate the kill command when receiving a SIGTERM signal
- Displays Y U no love me?! when receiving a SIGINT signal
- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/9993506f-988f-4d76-b3e5-b1bf9691b0c3)
Executing the 100-process_and_pid_file script and killing it with ctrl+c.
Terminal #0
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/a835f72c-cd12-48bc-b211-b016a1818367)
Terminal #1
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/09704a43-7939-4728-9a12-6dee23dc7513)
- File: 100-process_and_pid_file

### 10.Manage my process
Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: start, restart and stop. The most popular way of doing so on Unix system is to use the init scripts.

Write a manage_my_process Bash script that:
- Indefinitely writes I am alive! to the file /tmp/my_process
- In between every I am alive! message, the program should pause for 2 seconds
- Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

Requirements:
- When passing the argument start:
- Starts manage_my_process
- Creates a file containing its PID in /var/run/my_process.pid
- Displays manage_my_process started
- When passing the argument stop:
- Stops manage_my_process
- Deletes the file /var/run/my_process.pid
- Displays manage_my_process stopped
- When passing the argument restart
- Stops manage_my_process
- Deletes the file /var/run/my_process.pid
- Starts manage_my_process
- Creates a file containing its PID in /var/run/my_process.pid
- Displays manage_my_process restarted
- Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/67b545a1-328a-4002-a0f0-e7b238b425c4)
- File: 101-manage_my_process, manage_my_process

### 11. Zombie
Write a C program that creates 5 zombie processes.

Requirements:
- For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- When your code is done creating the parent process and the zombies, use the function bellow
#### Tested code by
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/351d594b-50cf-4617-847d-b44bb3f5ba86)
![image](https://github.com/arkoaikins/alx-higher_level_programming/assets/110135034/744adc5b-c3ce-4991-ab4b-9aa05736b1cb)
- File: 102-zombie.c

## Author:page_with_curl:
Edwin Arko Aikins
