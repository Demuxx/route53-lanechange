#!/usr/bin/python
import boto
import requests
import datetime
import botoconf

def log_msg(msg):
	f = open('/scripts/r53.log', 'a')
	f.write(msg)
	f.close()
	return True

def fetch_old_ip(zone, root):
        a_record = zone.get_a(root)
        return a_record.resource_records[0]

def fetch_ip():
	headers = { "User-Agent": "curl/7.21.2 (i386-pc-win32) libcurl/7.21.2 OpenSSL/0.9.8o zlib/1.2.5" }
        r = requests.get("http://ifconfig.me", headers=headers)
        return r.text.strip()

domains = botoconf.domains()
for domain in domains:
        conn = boto.connect_route53()
        root = domain["root"]
	subdomains = domain["subdomains"]
	zone = conn.get_zone(root)
        oldip = fetch_old_ip(zone, root)
        ipaddr = fetch_ip()
	if oldip != ipaddr:
		for subdomain in subdomains:
			try:
				log_msg("\n["+datetime.datetime.now().strftime("%m/%d/%y %I:%M%p")+"] Updating IP Address, old: "+oldip+" new: "+ipaddr)
				name = subdomain+root
				zone.update_a(name, ipaddr)
			except:
				print "Error!:", sys.exc_info()[0]
        else:
                log_msg(".")
