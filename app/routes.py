import flask
import time
import requests
import hashlib as hasher
import datetime as date
import subprocess
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Block:
  def __init__(self, index, data, previous_hash):
    self.index = index
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + 
               str(self.data) + 
             str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()


def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, "Genesis Block", "0")


def next_block(last_block, json_transaction):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = json_transaction
  this_hash = last_block.hash
  return Block(this_index, this_data, this_hash)

app = flask.Flask(__name__)

BLOCKCHAIN = [create_genesis_block()]

# BEGIN KEY GENERATION
# NOT CRYTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PRIV_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
PUB_KEY = PRIV_KEY.public_key()
PUB_KEY_STR = PUB_KEY.public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# END KEY GENERATION
with subprocess.Popen(["hostname", "-i"], stdout=subprocess.PIPE) as hostname_proc:
      ip_addr = hostname_proc.stdout.read().strip()
hosts = [host for host in ["172.31.27.255","172.31.21.220","172.31.24.15"] if host != ip_addr]
print(hosts)

@app.route('/determine-if-leader')
def leader_determine():
  # BEGIN LEADER SORTITION
  lowest_sortition_hash = None
  for host in hosts:
    # THIS ASSUMES A PERFECT CONSENSUS OF THE BLOCK HASH
    res = requests.get('http://'+host+':5000/pub-key', headers={"Accept":"text/plaintext"})
    remote_pub_key = res._content
    sha = hasher.sha256()
    sha.update((str(BLOCKCHAIN[-1].hash_block())+str(remote_pub_key)).encode('utf-8'))
    sortition_hash = sha.hexdigest()
    if lowest_sortition_hash == None or\
      int(sortition_hash) < lowest_sortition_hash:
      lowest_sortition_hash = sortition_hash
    
    # poll your own key
    sha = hasher.sha256()
    sha.update((str(BLOCKCHAIN[-1].hash_block())+str(PUB_KEY_STR)).encode('utf-8'))
    sortition_hash = sha.hexdigest()
   
    if sortition_hash == lowest_sortition_hash:
      print("YOU ARE THE LEADER")
      return '\n'.join(open('static/leader.html').readlines())
    else:
      print("YOU ARE NOT THE LEADER")
      return '\n'.join(open('static/transfer.html').readlines())
    
		# END LEADER SORTITION

@app.route('/pub-key')
def leader_hash():
  print(str(PUB_KEY_STR))
  return str(PUB_KEY_STR)

@app.route('/blockchain-hash')
def get_hash():
	return str(BLOCKCHAIN[-1].hash_block())

@app.route('/push-block', methods=['POST'])
def home():
	print(flask.request.json)
	BLOCKCHAIN.append(next_block(BLOCKCHAIN[-1], flask.request.json))
	return "SUCCESS"

@app.route('/')
@app.route('/index')
def index():
	return flask.render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
