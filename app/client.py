import requests
import time
import socket
import hashlib as hasher

HOSTNAME=socket.gethostname()

block_hashes = {}
largest_hash_count = 0
number_of_nodes = 0
mode_hash = 0
try:
  # BEGIN CONSENSUS
  for host in ["172.31.27.255","172.31.21.220","172.31.24.15"]:
    print("POLLING: " + host)
    res = requests.get("http://"+host+":5000/blockchain-hash")
    block_hash = res._content

    if block_hash in block_hashes:
      block_hashes[block_hash] +=1

    else:
      block_hashes[block_hash] = 1
    
    for hash_count in block_hashes:
      if block_hashes[hash_count] > largest_hash_count:
        largest_hash_count = block_hashes[hash_count]

    number_of_nodes += 1

  if largest_hash_count < number_of_nodes / 2:
    print("ERROR IN CONSENSUS")
    print("NUMBER OF NODES:", number_of_nodes)
    print("LARGEST HASH COUNT: ", largest_hash_count)

  # END CONSENSUS

except Exception as e:
  print(e)
