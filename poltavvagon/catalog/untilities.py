from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filemame):
    return "%s%s" % (datetime.now().timestamp(), splitext(filemame)[1])
