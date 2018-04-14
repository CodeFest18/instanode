import requests
import time

while True:	
	try:
		for host in ["172.31.27.255","172.21.31.220","172.31.24.15"]:
			print("POLLING: " + host)
			res = requests.get("http://"+host+":5000/")
			print(res.__dict__)
	except Exception as e:
		print(e)

	time.sleep(1)
