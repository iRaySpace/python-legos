import time
from node.core.block import Block, get_hash


class Blockchain:
    def __init__(self):
        self.blocks = []

    def create_block(self):
        index = len(self.blocks)
        created_at = round(time.time() * 1000)

        new_block = Block(
            index=index,
            created_at=created_at,
            hash=get_hash(index, created_at),
            previous_hash=None
        )

        if self.blocks:
            last_block = self.blocks[-1]
            new_block.previous_hash = last_block.hash
        
        self.blocks.append(new_block)

        return new_block


_blockchain = Blockchain()
_blockchain.create_block() # Genesis Block

def get_blockchain():
    return _blockchain
