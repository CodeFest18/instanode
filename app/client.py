import requests
import time
import socket

HOSTNAME=socket.gethostname()

while True:	
	try:
		#for host in ["172.31.27.255","172.21.31.220","172.31.24.15"]:
		for host in ["localhost"]:
			print("POLLING: " + host)
			res = requests.post("http://"+host+":5000/",json={HOSTNAME:"test"}, headers={'Content-Type':'application/json'})
			print(res.__dict__)
	except Exception as e:
		print(e)

	time.sleep(1)
