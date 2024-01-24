import json
from loguru import logger


def setup_logger():
    def make_format(record):
        record['extra']['serialized'] = json.dumps({
            'message': record['message'],
            'level': record['level'].name,
            'time': record['time'].isoformat(),
        })
        return '{extra[serialized]}\n'

    logger.remove(0)
    logger.add('./logs/{time}.log', format=make_format)


def main():
    setup_logger()
    logger.info('Logging with structlog')


if __name__ == '__main__':
    main()
