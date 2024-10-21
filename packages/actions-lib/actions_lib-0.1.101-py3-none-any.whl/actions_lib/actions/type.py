from typing import Optional


class ActionData:

    func: str

    group: str

    params: dict

    def __init__(self, func, group, params) -> None:
        self.func = func
        self.group = group
        self.params = params

class Action:

    type: str

    msg: Optional[str] = None

    data: dict

    def __init__(self, type, msg, data) -> None:
        self.data = data
        self.type = type
        self.msg = msg

