"""
@Project ：危险化学品溯源后台第一版
@File    ：Blockchain.py
@Author  ：TXL
@Date    ：2022/1/8 20:37
"""
# -*- coding: UTF-8 -*-
import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

from bean.Chain import Chain

class Blockchain(object):
    """
    Blockchain类 用来管理链条，它能存储交易、加入新块等
    """

    def __init__(self):
        self.chain_len = 0
        """
        2022-2-9 11:23
            这里专门设计一个属性chain_len用来表示当前区块链中的长度
            主要是因为考虑到了由于如果本项目部署在服务器上常年累月地运行的话
            就很容易出现内存占用滚雪球似的增大，因为整个区块链的核心都是使用的Blockchain类
            而整个类对内存的占用则不会有任何程序进行释放
            所以我认为，专门设计一个属性用来表示区块长度
            并设计清空算法，及时将那些早已过期的区块数据清理出内存（可以丢弃，当然也可以存储在硬盘介质中，根据实际情况做决定）
        """
        self.current_transactions = []
        self.chain = []
        # Create the genesis block.在本类被实例化的时候，需要有一个创世块并为其加上一个工作量证明
        self.new_block(previous_hash=1, proof=100)

        self.nodes = set()

    def new_block(self, proof, previous_hash=None):
        # Reset the current list of transactions
        """
        生成新块
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': self.chain_len,  # 创建新块原有链条长度+1
            'timestamp': time(),  # 对应创建的时间
            'transactions':  # 交易列表
                self.current_transactions,
            'proof': proof,  # 工作量证明
            'previous_hash':  # 前一个区块的Hash值
                previous_hash or self.hash(self.chain[-1]),
        }

        if previous_hash is None:
            self.chain_len += 1
            block['index'] = self.chain_len

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount, information):
        # Adds a new transaction to the list of transactions
        """
        生成新交易信息，信息将加入到下一个待挖的区块中
        :param information: <str> Information of the transaction
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction

        方法向列表中添加一个交易记录
        并返回该记录将被添加到的区块(下一个待挖掘的区块)的索引
        等下在用户提交交易时会有用。
        """
        self.current_transactions.append({
            # 将对应的交易信息添加到区块中
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'information': information
        })
        return self.chain_len + 1
        # 方法向列表中添加一个交易记录，并返回该记录将被添加到的区块(下一个待挖掘的区块)的索引，等下在用户提交交易时会有用。

    @property
    def last_block(self):
        # Returns the last Block in the chain_local
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        生成块的 SHA-256 hash值
        :param block: <dict> Block
        :return: <str>
        """
        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        简单的工作量证明:
         - 查找一个 p' 使得 hash(pp') 以4个0开头
         - p 是上一个块的证明,  p' 是当前的证明
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            # print(proof)
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        验证证明: 是否hash(last_proof, proof)以4个0开头?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        # print("guess="+str(guess))
        guess_hash = hashlib.sha256(guess).hexdigest()
        # print("guesshash=" + str(guess_hash))
        return guess_hash[:4] == "0000"

    def register_node(self, address):
        """
        注册节点
        Add a new node to the list of nodes
        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("-----------")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1
        return True

    def resolve_conflicts(self):
        """
        共识算法解决冲突
        使用网络中最长的链.
        :return: <bool> True 如果链被取代, 否则为False
        """
        neighbours = self.nodes
        new_chain = None
        # We're only looking for chains longer than ours
        max_length = len(self.chain)
        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain_local')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain_local']
                # Check if the length is longer and the chain_local is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        # Replace our chain_local if we discovered a new, valid chain_local longer than ours
        if new_chain:
            self.chain = new_chain
            return True
        return False





'''Something'''
block_demo = {
    # 每个区块都包括以下几个部分
    'index': 1,  # 索引
    'timestamp': 1506057125.900785,  # Unix时间戳
    'transactions': [  # 交易列表
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,  # 工作量证明
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    # 前一个区块的Hash值
}
