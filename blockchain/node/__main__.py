import uvicorn
from node.core.blockchain import Blockchain


if __name__ == '__main__':
    uvicorn.run(
        'node.core.api:api',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
