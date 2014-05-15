# Route 53 Lane Change

This is a tool to update your dynamic IP address in AWS Route 53

## Configuration

Change the botoconf.py functions to return your root domain name and the sub domain that you wish to update. In order for boto to work, you'll need to install it and configure your AWS API access tokens in ~/.boto. I use a cronjob similar to the following to update it regularly:

    */10 * * * * ~/scripts/r53.py >> ~/scripts/r53.log

Your ~/.boto should look similar to:

  [Credentials]
  aws_access_key_id = AAAAAAAAAAAAAAAAAAA
  aws_secret_access_key = BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

