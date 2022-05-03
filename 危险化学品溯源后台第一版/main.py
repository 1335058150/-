"""
@Project ：危险化学品溯源后台第一版
@File    ：main.py
@Author  ：TXL
@Date    ：2022/1/7 11:56
"""
# -*- coding: UTF-8 -*-
import _pickle
import os
import pickle
from uuid import uuid4

from flask import Flask, jsonify, request

from bean.Blockchain import Blockchain
from bean.LocalChain import LocalChain
from bean import Globals
from util import TimeNow, To_File, GetInt, search

app = Flask(__name__)
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
# 初始化一条全新的区块链
blockchain = Blockchain()
# 初始化一条辅链条
localchain = LocalChain()
# 全局变量存储类
Globals.__init__()

"""创建一个新的模块并返回对应的各项参数指标"""
@app.route('/mine', methods=['GET'])
def mine():
    # 创造一个新的区块
    last_block = blockchain.last_block  # 上一个旧的节点
    last_proof = last_block['proof']  # 上一个节点的工作量证明
    proof = blockchain.proof_of_work(last_proof)
    # 给工作量证明的节点提供奖励.
    # 发送者为 "0" 表明是新挖出的币
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
        information=None
    )
    # Forge the new Block by adding it to the chain_local
    block = blockchain.new_block(proof)
    response = {
        'message': Globals.get_value(["CREATE BLOCK", "MESSAGE"]),
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


"""以POST方式传入json参数从而为下一个节点添加数据"""
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    from conf.config import Block_Properties  # 从配置文件中导入所需属性
    required = Block_Properties.get_transactions_types(Block_Properties())
    # 如果传入的json参数不符合上边给到的规则就给你传个400玩玩（请求头错误）
    if not all(k in values for k in required):
        return 'Missing values', 400
    # Create a new Transaction
    index = blockchain.new_transaction(
        values['sender'],
        values['recipient'],
        values['amount'],
        values['information']
    )
    response = {
        'message': f'Transaction will be added to Block {index}',
        'TrulyGet': values,
        'index': index
    }
    return jsonify(response), 201


"""返回当前全部的区块信息并且修改后不会返回创世节点"""
@app.route('/chain_local', methods=['GET'])
def full_chain():
    response = {
        'chain_local': blockchain.chain[1:],
        'length': len(blockchain.chain) - 1,
    }
    return jsonify(response), 200


"""通过POST方式json传参将指定url的加入区块链中"""
@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        # 节点为空时报错
        return Globals.get_value(["REGISTER NODES", "E-NONE NODES"]), 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        # 全新节点目录上传成功并且给予上传成功的全部节点予以正反馈
        'message': Globals.get_value(["REGISTER NODES", "ADD SUCCESSFULLY"]),
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


"""和区块链网络中其他服务器的内容同步更新"""
@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            # 根据共识算法，这里的链条已经被成功更新
            'message': Globals.get_value(["RESOLVE NODES", "REPLACE YES"]),
            'new_chain': blockchain.chain
        }
    else:
        response = {
            # 根据共识算法，本地链条不应当被更新
            'message': Globals.get_value(["RESOLVE NODES", "REPLACE NO"]),
            'chain_local': blockchain.chain
        }
    return jsonify(response), 200


"""可以通过index的参数值查找其中某个区块的信息"""
@app.route('/getchain', methods=['GET'])
def get_chain():
    index_num = GetInt.getint(request.values.get('index'))
    if index_num is None:
        return "Bad request", 400
    response_block = search.search_block(chain=blockchain.chain, index=index_num)
    response = {'Got the result': response_block}
    if response_block == {}:
        response = {'end': [Globals.get_value(["SELECT NOTHING"])]}
    return jsonify(response), 200


"""将当前实验使用的区块链内容对象序列化并保存在指定文件中"""
@app.route('/rem')
def serialization_and_save():
    now_time = TimeNow.getTime_Full()

    chain_serialization = pickle.dumps(blockchain)

    To_File.writefile_bytes(
        # 在这里传入的是二进制数据是序列化后的blockchain对象，用来稍后再读取的时候进行反序列化操作
        bytes__=chain_serialization,
        # 由于文件名中不能出现冒号，又为了防止后期访问文件出现中文乱码，在这里使用分号代替冒号
        filepath=os.getcwd() + "\\BlockChainRem\\" + now_time.replace(":", ";")
    )
    return Globals.get_value(["FILE", "SERIALIZATION", "SUCC SAVE"])


"""获得上一次实验进行的最新数据或者使用GET请求传入的对象序列化参数进行更新"""
@app.route("/reload", methods=["GET"])
def reload():
    response = {
        "GET": False,
        "LoadFile": "Correct",
        "Load_File_Time": "",
        "Error": None
    }
    value = request.values.get('path')
    if value is not None:
        # 如果传入参数非空，就用传入的参数来
        target_file = os.getcwd() + "\\BlockChainRem\\" + value
        response["GET"] = True
        response["Load_File_Time"] = value.replace(";", ":")
    else:
        newest_file = To_File.choose_newest_file(os.getcwd() + "\\BlockChainRem")
        if newest_file is not None:
            target_file = \
                os.getcwd() + \
                "\\BlockChainRem\\" + \
                To_File.choose_newest_file(os.getcwd() + "\\BlockChainRem")
            response["Load_File_Time"] = newest_file.replace(";", ":")
        else:
            # 读文件的过程出错              File Reading Error
            response["LoadFile"] = Globals.get_value(["FILE", "LOADING", "ERROR"])[1]
            return jsonify(response), 404
    try:
        serialization = To_File.readfile_bytes(target_file)
    except FileNotFoundError:
        # 文件路径（文件加载）过程出错        File Loading Error
        response["LoadFile"] = Globals.get_value(["FILE", "LOADING", "ERROR"])[0]
        return jsonify(response), 400
    try:
        global blockchain
        blockchain = pickle.loads(serialization)
        return jsonify(response), 201
    except _pickle.UnpicklingError as e:
        response["LoadFile"] = Globals.get_value(["FILE", "SERIALIZATION", "FAIL SAVE"])
        response["Error"] = str(e)
        return jsonify(response), 400


@app.route('/test')
def test():
    # print(Globals.get_value(["TEST3", "TEST", "TES", "TE", "T"]))
    print(Globals.get_value(["FILE", "LOADING", "ERROR"])[0])

    return "Test Successfully"


if __name__ == '__main__':

    """
    2022.2.18 15:44
    下边这一段本来的设计思路是设计一个新的函数，定期对Blockchain类中的内容进行清理
    创建一个新的进程的同时不影响主进程的运行
    这就需要获取到flask服务器当前的负载量以决定所需要的资源消耗
    """
    # import threading
    # threading.Thread().start()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
