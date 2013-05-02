#!/usr/bin/env python
import json
import argparse
from subprocess import *
from time import sleep
import os
from urllib import urlretrieve 

parser = argparse.ArgumentParser()
parser.add_argument('option', choices = ['update', 'start', 'status', 'end', 'quit', 'stat'], help = "")
args = parser.parse_args()

NONE   = "\033[m"
GRAY   = "\033[1;30m"
RED    = "\033[1;31m"
GREEN  = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE   = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN   = "\033[1;36m"
WHITE  = "\033[1;37m"

def printf(msg, mark, color=NONE):
	print '{0}[{1:^10}] {2}{3}'.format(color, mark, msg, NONE)

if __name__ == '__main__':
	if args.option == 'update':
		github_url = 'https://raw.github.com/xuancaishaun/fyp_test/master/'
		#BASE = '~/fyp/fyp_nep2p/'
		BASE = '' # relative path

		# ~/fyp/fyp_nep2p/lib/
		url = github_url + 'external_gateway.py'
		out = BASE + 'lib/external_gateway.py'
		try: r = urlretrieve(url, out), printf('lib/external_gateway.py', 'Updated', GREEN)		
		except: printf('Failed to update: lib/external_gateway.py', 'Error', RED)

		url = github_url + 'scheduler.py'
		out = BASE + 'lib/scheduler.py'
		try: r = urlretrieve(url, out), printf('lib/scheduler.py', 'Updated', GREEN)		
		except: printf('Failed to update: lib/scheduler.py', 'Error', RED)	
	 	
		url = github_url + 'app_worker.py'
		out = BASE + 'lib/app_worker.py'
		try: r = urlretrieve(url, out), printf('lib/app_worker.py', 'Updated', GREEN)		
		except: printf('Failed to update: lib/app_worker.py', 'Error', RED)
 
		# ~/fyp/fyp_nep2p/lib/utl/
		url = github_url + 'logger.py'
		out = BASE + 'lib/util/logger.py'
		try: r = urlretrieve(url, out), printf('lib/util/logger.py', 'Updated', GREEN)		
		except: printf('Failed to update: lib/util/app_worker.py', 'Error', RED)

		# ~/fyp/fyp_nep2p/
		url = github_url + 'statCollect.py'
		out = BASE + 'statCollect.py'
		try: r = urlretrieve(url, out), printf('statCollect.py', 'Updated', GREEN)		
		except: printf('Failed to update: statCollectr.py', 'Error', RED)

		url = github_url + 'run.py'
		out = BASE + 'run.py'
		try: r = urlretrieve(url, out), printf('run.py', 'Updated', GREEN)		
		except: printf('Failed to update: run.py', 'Error', RED)

		url = github_url + 'cli.py'
		out = BASE + 'cli.py'
		try: r = urlretrieve(url, out), printf('cli.py', 'Updated', GREEN)		
		except: printf('Failed to update: cli.py', 'Error', RED)

		url = github_url + 'ddM16m8r92TO.txt'
		out = BASE + 'ddM16m8r92TO.txt'
		try: r = urlretrieve(url, out), printf('ddM16m8r92TO.txt', 'Updated', GREEN)		
		except: printf('Failed to update: ddM16m8r92TO.txt', 'Error', RED)


	if args.option == 'stat':
		printf('Executing statCollect.py', 'INFO', YELLOW)
		try:
			with open(os.devnull, "w") as f:
			# Write the output to the electronic trash can
				r = call(['python','statCollect.py','config.json'], stdout=f, stderr=f)
			if r == 0: printf('Success!', 'INFO', GREEN)
			else: printf('No such files: statCollect.py or config.json', 'ERROR', RED)
		except: 
			printf('Call Failed!', 'ERROR', RED)
		f.close()
	if args.option == 'start':
		s_p = Popen(['python','run.py'])
		c_p = Popen(['python','cli.py'])
		d = dict()
		d['service_pid'] = s_p.pid
		d['client_pid'] = c_p.pid
		f = open('info.json', 'w+')
		f.write(json.dumps(d))
		f.close()
		printf('Service started: %d'%s_p.pid, 'INFO', GREEN)
		printf('Client  started: %d'%c_p.pid, 'INFO', GREEN)
	if args.option == 'status':
		try: info = json.loads(open('info.json','r').read())	
		except: printf('No info.json', 'ERROR', RED)
		s_pid = info['service_pid']
                c_pid = info['client_pid']
		if os.path.exists('/proc/%d'%s_pid):
			printf('Service is alive: %d'%s_pid, 'INFO', GREEN)
		else: printf('No such service: %d'%s_pid, 'INFO', YELLOW)
		if os.path.exists('/proc/%d'%c_pid):
                        printf('Client  is alive: %d'%c_pid, 'INFO', GREEN)
		else: printf('No such service: %d'%c_pid, 'INFO', YELLOW)
	if args.option == 'end': # End the service when client is closed	
		try: info = json.loads(open('info.json','r').read())
                except: printf('No info.json', 'ERROR', RED)
		s_pid = info['service_pid']
		c_pid = info['client_pid']
		while True:
			if os.path.exists('/proc/%d'%c_pid):
				printf('Cannot kill service: Client(%d) is Alive'%c_pid,'INFO', YELLOW)
				sleep(3)
			else: 
				call(['kill', '-9', s_pid])
				printf('Service is killed: %d'%s_pid,'INFO',GREEN)
	if args.option == 'quit': # End both service and client process
		try: info = json.loads(open('info.json','r').read())
                except: printf('No info.json', 'ERROR', RED)
                s_pid = info['service_pid']
                c_pid = info['client_pid']
		r = call(['kill', '-9', str(s_pid)])
		if r == 0: printf('Service is killed: %d'%s_pid, 'INFO', GREEN)
		else: printf('Failed: no such service - %d'%s_pid, 'ERROR', RED)
		r = call(['kill', '-9', str(c_pid)])
		if r == 0: printf('Client  is killed: %d'%c_pid, 'INFO', GREEN)
                else: printf('Failed: no such service - %d'%c_pid, 'ERROR', RED)
	