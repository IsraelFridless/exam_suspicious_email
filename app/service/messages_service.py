import toolz as t


def is_hostage_message(message: dict) -> bool:
    return t.pipe(
        message['sentences'],
        t.partial(any, key=lambda s: 'hostage' in s.lower())
    )

def is_explosive_message(message: dict) -> bool:
    return t.pipe(
        message['sentences'],
        t.partial(any, key=lambda s: 'explosive' in s.lower())
    )