from datetime import datetime


def make_session_id() -> str:
    return f"{datetime.now():%y%m%d%H%M%S}"


def make_name(outer_context: dict, dirty=True, short=False):
    user_id = outer_context["UserId"]
    session_id = outer_context["SessionId"]
    client_id = outer_context["ClientId"]
    if short:
        return f"{user_id}_{session_id}_{client_id}"
    long = f"user_{user_id}_session_{session_id}_client_{client_id}"
    if dirty:
        return f"{long}.json"
    return f"{long}_clean.json"
