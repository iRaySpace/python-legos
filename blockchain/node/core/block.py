import hashlib
from dataclasses import dataclass


@dataclass
class Block:
    index: int
    created_at: int
    hash: str
    previous_hash: str


def get_hash(index: int, created_at: int) -> str:
    contents = str(index) + str(created_at)
    return hashlib.sha256(contents.encode()).hexdigest()
