import uuid
from os import path
import tempfile 

def write_file(file, content_type) -> str:
    file_name = '{}.{}'.format(uuid.uuid4(), content_type.split('/')[1])
    temp_full_path = path.join(tempfile.gettempdir(), file_name)
    contents = file.read()
    with open(temp_full_path, 'wb+') as f:
        f.write(contents)
        f.close()
    return file_name