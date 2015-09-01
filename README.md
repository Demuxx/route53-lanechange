# Route 53 Lane Change

This is a tool to update your dynamic IP address in AWS Route 53

## Installation

1. Install pip. e.g. sudo apt-get install python-pip
2. Install boto python package. e.g. sudo pip install boto
3. Create scripts directory and log file - sudo mkdir /var/scripts && sudo touch /var/scripts/r53.log
4. Create the boto.cfg file - sudo vim /etc/boto.cfg
5. Put r53.py and botoconf.py in /var/scripts
6. Set up the root cronjob

## Configuration

Change the botoconf.py functions to return your root domain name and the sub domain that you wish to update. In order for boto to work, you'll need to install it and configure your AWS API access tokens in ~/.boto or /etc/boto.cfg. boto.cfg should be used if you are running this as a cronjob. I use a cronjob similar to the following to update it regularly:

 >   */10 * * * * ~/scripts/r53.py >> ~/scripts/r53.log

Your ~/.boto or /etc/boto.cfg should look similar to:

>    [Credentials]
>    aws_access_key_id = AAAAAAAAAAAAAAAAAAA
>    aws_secret_access_key = BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

