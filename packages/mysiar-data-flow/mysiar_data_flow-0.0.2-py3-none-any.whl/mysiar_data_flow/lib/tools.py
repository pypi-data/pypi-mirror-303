import os
import uuid


def delete_file(filename: str) -> bool:
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False


def generate_temporary_filename(ext: str = "tmp") -> str:
    return f"{uuid.uuid4()}-{uuid.uuid4()}.{ext}"
