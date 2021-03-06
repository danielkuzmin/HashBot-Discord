# HashBot - Discord
This bot returns the hash of a given file via Discord. List of hashes supported below. Written in Python.
## Getting Started
If you'd like to host the bot yourself, these instructions will show you how to get it running on a Linux machine in the background.
### Prerequisites
You will need a machine running Linux, preferably something that can be used as a server, such as a raspberry Pi. You'll need Python 3 on this machine. To check if you already have Python3, run the following command:
```
$ python3 --version
```
If this does not come back with a version number, you will have to install it yourself. Run the following command (if on a Debian-based platform):
```
$ sudo apt-get install python3.6
```
If you are using RHEL or CentOS, use this command instead:
```
$ sudo yum install rh-python36
```
After this, create a directory and put all the source files from this repository into it.

### Adding a Token
Create a file called credentials.py in the same directory as the rest of the source files. Generate a bot token from the Discord Developer Portal. Finally, edit credentials.py and paste the following:
```
TOKEN = 'YOURUNIQUETOKENGOESHERE'
```
Save the file.
### Running the Bot as a Background Task
In a terminal window, navigate to the directory you put the source files in. Run the following command:
```
$ nohup python3 hashBot.py&
```
This will start the bot. You can close the terminal window, or the SSH window, and the bot will keep running as long as the machine doesn't shut down or lose connection to the internet.
### Changing Permissions
Put all the bot's files into a directory of your choice. You may have to modify the permissions slightly.
## Using the Bot
This bot uses the prefix '$' and comes with the following commands:
### $hash
Hashes the attached file with the selected hash. Ex:
```
$hash SHA256
```
### $help
Sends a message containing the bot's command list and a short description with usages of each command to the channel it was invoked in.
### $about
Sends a message containing the author's github and version number.
### List of Supported Hashes
SHA1, SHA256, SHA512, SHA3_512, MD5, BLAKE25, Whirlpool
