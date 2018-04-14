import requests
import time

while True:	
	try:
		for host in "18.222.52.182","13.59.211.35","18.188.5.1":
			print("POLLING: " + host)
			res = requests.get("http://"+host+":5000/")
			print(res.__dict__)
	except Exception as e:
		print(e)

	time.sleep(1)
