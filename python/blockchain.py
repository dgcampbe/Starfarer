#!/usr/bin/env python
"""A simple program for making a blockchain."""
# import socket
# import sys
import json
# import threading
# import random
import time
import math
# import itertools
# import subprocess
# pymerkle
import merkletools
import Crypto.Hash.SHA256
import sign


class Chain:
    """Chain."""

    def __init__(self, addGenesis=True):

        print("Chain created.")
        self.blocks = []
        if addGenesis:
            self.blocks.append(GenesisBlock(1, 3, 3.14, 0, 0, ["blah"], secret_message="Let there be blocks."))

    def add_block(self, block):
        """Add block."""
        self.blocks.append(block)

    def write(self):
        """Write."""
        i = 0
        for block in self.blocks:
            f = open("blockchain/block_" + str(i) + ".txt", "w")
            f.write(str(block))
            f.close()
            i += 1
            print("Wrote block successfully.")


class Block:
    """Block."""

    def __init__(self, size, vote, version, difficulty, timestamp, previous_block, data):

        print("Block created.")
        self.version = version
        self.size = size
        self.timestamp = timestamp
        self.difficulty = difficulty
        self.vote = vote
        self.data = data
        self.nonce = 0
        self.previous_hash = previous_block.block_hash

    def __str__(self):
        """String."""
        rep = ""
        rep += self.header + "\n" + str(self.block_hash) + "\n" + str(self.data)
        return rep

    @property
    def block_hash(self):
        """Block hash."""
        return Crypto.Hash.SHA256.new(self.header.encode("utf-8")).hexdigest()

    @property
    def header(self):
        """Header."""
        return json.dumps({
            "Size": self.size,
            "Version": self.version,
            "Vote": self.vote,
            "Previous Block Header Hash": self.previous_hash,
            "Timestamp": self.timestamp,
            "Difficulty": self.difficulty,
            "Nonce": self.nonce,
            "Merkle Root": self.merkle_root
        })

    @property
    def merkle_root(self):
        """Merkle root."""
        mt = merkletools.MerkleTools()
        mt.add_leaf(self.data, True)
        mt.make_tree()
        return mt.get_merkle_root()

    def mine(self):
        """Mine."""
        print("Mining with difficulty: " + str(self.difficulty))
        start_time = time.time()
        hashes = 0
        while True:
            hashes += 1
            # line below makes mining faster, but less fun
            # print(str(self.block_hash))
            if int(self.block_hash, 16) < self.difficulty:
                elapsed_time = time.time() - start_time
                print("Found solution in " + str(elapsed_time) + " seconds, with " + str(hashes) + " hashes for a total of " + str(hashes/(elapsed_time)) + " hashes per second.")
                print("Solution: " + str(self.block_hash) + " with nonce: " + str(self.nonce))
                break
            else:
                self.nonce += 1
        return (elapsed_time, hashes)


class GenesisBlock(Block):
    """Genesis Block."""

    def __init__(self, size, vote, version, difficulty, timestamp, data, secret_message=None):

        print("Genesis Block Created.")
        self.secret_message = secret_message
        self.version = version
        self.size = size
        self.timestamp = timestamp
        self.difficulty = difficulty
        self.vote = vote
        self.previous_hash = 0
        self.data = data
        self.nonce = 0

class Transaction:
    """Transaction."""

    def __init__(self, token, giver, receiver, data_type, data):

        self.token = token
        self.giver = giver
        self.receiver = receiver
        self.data_type = data_type
        self.data = data

    def __str__(self):
        """String."""
        return json.dumps({
            "Token": self.token,
            "Giver": self.giver,
            "Receiver": self.receiver,
            "Data Type": self.data_type,
            "Data": self.data,
        })

    def sign_transaction(self):
        """Sign Transaction."""
        signature = sign(self.transaction.encode("utf-8"))
        if sign.verify(self.transaction.encode("utf-8"), signature):
            print("Transaction Signed Successfully!")
            return signature
        else:
            print("Transaction could not be signed.")
            return None


class Token:
    """Token."""

    def __init__(self, permissions):

        print("Token Created.")
        self.permissions = permissions


def main():
    """Main."""
    test = Transaction(123, "Dane", "Someone else", "memes", "memez")
    print(test.sign_transaction)
    text = b"Meow Meow Meow"
    sign.verify(text, sign.sign(text))
    print("Unix Epoch: " + str(time.time()))
    data1 = ["314", "123", "987", "000", "555"]
    # 0x20000f00
    difficulty = int(hex(0x000f00 * int((math.pow(2, 8 * (0x20 - 3))))), 16)
    chain1 = Chain()
    block1 = Block(1, 2, "Richard Nixon :P", difficulty, time.time(), chain1.blocks[-1], data1)
    block1.mine()
    chain1.add_block(block1)
    chain1.write()
    print("Header:\n" + block1.header)
    print("Data:\n" + str(block1.data))
    Transactions = []
    for i in range(64):
        Transactions.append(Transaction("token1", "John" + str(i), "John" + str(i + 1), "Block Talk", "Blah Blah Blah " + str(i)).transaction)
    block2 = Block(1, 2, "Al Gore :P", difficulty, time.time(), chain1.blocks[-1], Transactions)
    block2.mine()


if __name__ == "__main__":

    main()
