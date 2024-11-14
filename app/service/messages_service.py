import toolz as t


def is_hostage_message(message: dict) -> bool:
    return t.pipe(
        message['sentences'],
        lambda sentences: any('hostage' in s.lower() for s in sentences)
    )

def is_explosive_message(message: dict) -> bool:
    return t.pipe(
        message['sentences'],
        lambda sentences: any('explosive' in s.lower() for s in sentences)
    )
