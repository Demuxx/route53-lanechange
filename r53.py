#!/usr/bin/python
import boto
import requests
import botoconf

headers = { "User-Agent": "curl/7.21.2 (i386-pc-win32) libcurl/7.21.2 OpenSSL/0.9.8o zlib/1.2.5" }
r = requests.get("http://ifconfig.me", headers=headers)
ipaddr = r.text.strip()
conn = boto.connect_route53()
zone = conn.get_zone(botoconf.root_domain())
a_record =  zone.get_a(botoconf.sub_domain())
oldip = a_record.resource_records[0]
if oldip != ipaddr:
    print "Updating IP Address, old: "+oldip+" new: "+ipaddr
      cloud.update_a(botoconf.sub_domain(), ipaddr)
    else:
        print "Didn't need to update IP address, still: "+oldip

