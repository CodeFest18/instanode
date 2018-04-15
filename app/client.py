import requests
import time
import socket

HOSTNAME=socket.gethostname()

while True:	
	block_hashes = {}
	largest_hash_count = 0
	number_of_nodes = 0
	mode_hash = 0
	try:
		for host in ["172.31.27.255","172.21.31.220","172.31.24.15"]:
			print("POLLING: " + host)
			# Get the latest hash from node
			res = requests.get("http://"+host+":5000/hash-block")
			block_hash = res._content

			if block_hash in block_hashes:
				block_hashes[block_hash] +=1

			else:
				block_hashes[block_hash] = 1
			
			for hash_count in block_hashes:
				if block_hashes[hash_count] > largest_hash_count:
					largest_hash_count = block_hashes[hash_count]

			number_of_nodes += 1

			print(res._content)

		if largest_hash_count < number_of_nodes / 2:
			print("ERROR IN CONSENSUS")
			print("NUMBER OF NODES:", number_of_nodes)
			print("LARGEST HASH COUNT: ", largest_hash_count)

	except Exception as e:
		print(e)

	time.sleep(1)
