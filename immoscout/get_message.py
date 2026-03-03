
def get_message(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()
