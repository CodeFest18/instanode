import flask
import time
import requests
import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash)).encode('utf-8'))
    return sha.hexdigest()


def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block, json_transaction):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = json_transaction
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

app = flask.Flask(__name__)

BLOCKCHAIN = [create_genesis_block()]

@app.route('/hash-block')
def get_hash():
	return str(BLOCKCHAIN[-1].hash_block())

@app.route('/push-block', methods=['POST'])
def home():
	BLOCKCHAIN.append(next_block(BLOCKCHAIN[-1], flask.request.json))
	return "SUCCESS"

@app.route('/gui')
def gui():
	return flask.render_template('gui.html')

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
