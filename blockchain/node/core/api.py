from fastapi import FastAPI, HTTPException
from node.core.blockchain import get_blockchain


api = FastAPI()
blockchain = get_blockchain()


@api.post('/create-block')
async def create_block():
    new_block = blockchain.create_block()
    return {'hash': new_block.hash}


@api.get('/block/{hash}')
async def get_block(hash: str):
    for block in blockchain.blocks:
        if block.hash == hash:
            return block
    raise HTTPException(status_code=404, detail='Block not found')

