import sys
import argparse

import requests

def err(*args, **kwargs):
	print(*args, file = sys.stderr, **kwargs)

parser = argparse.ArgumentParser(description = 'Spam-vote in strawpoll.com polls')
parser.add_argument('pid', help = 'The poll ID to vote in (found at end of URL).')
parser.add_argument('oids', help = 'The checkbox ID(s) to submit votes for. Separated by #s. You can find this with inspect element (name= attribute on input[type=checkbox]).')

args = parser.parse_args()

session = requests.Session()

headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.8',
	'DNT': '1',
	'Host': 'strawpoll.com',
	'Origin': 'https://strawpoll.com',
	'Referer': 'https://strawpoll.com/' + args.pid,
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}

print('^C to stop')

try:
	while True:
		req = session.get('https://strawpoll.com/' + args.pid, headers = headers, stream = False)

		if req.status_code != 200:
			err('Failed to fetch page :', req.status_code)
		
		req = session.post('https://strawpoll.com/vote', data = {'pid': args.pid, 'oids': args.oids}, headers = headers, stream = False)

		if req.status_code != 200:
			err('Failed to vote :', req.status_code)
		
		req = session.post('https://strawpoll.com/refresh', data = {'pid': args.pid}, headers = headers, stream = False)

		if req.status_code != 200:
			err('Failed to refresh :', req.status_code)

		session = requests.Session()

		print('Vote submitted.')
except KeyboardInterrupt:
	print('Shutting down gracefully...')