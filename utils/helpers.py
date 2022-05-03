import os
from hashlib import md5
from time import time


def generate_upload_name(instance, filename, prefix=None, unique=False):
    """
    Авто генерация имени для файла и ImageFields.
    """
    ext = os.path.splitext(filename)[1]
    name = str(instance.pk or "") + filename + (str(time()) if unique else "")

    filename = md5(name.encode("utf8")).hexdigest() + ext
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    if prefix:
        basedir = os.path.join(basedir, prefix)
    return os.path.join(basedir, filename[:2], filename[2:4], filename)
