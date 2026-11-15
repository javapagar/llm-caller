

def build(message: str, role_type: str = "user") -> dict[str, str]:
    return {
        "role": role_type,
        "content": message,
    }