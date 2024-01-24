import os


def navigate_up(current_path: str, levels: int):
    new_path = current_path
    for _ in range(levels):
        new_path = os.path.dirname(new_path)

    return new_path.replace("/", "\\")
