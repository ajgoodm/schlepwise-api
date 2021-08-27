import shortuuid


def short_id() -> str:
    return shortuuid.uuid()[:8]
