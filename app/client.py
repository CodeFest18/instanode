import requests
import time

while True:	
	try:
		res = requests.get("http://localhost:5000/")
		print(res.__dict__)
	except Exception as e:
		print(e)

	time.sleep(1)
