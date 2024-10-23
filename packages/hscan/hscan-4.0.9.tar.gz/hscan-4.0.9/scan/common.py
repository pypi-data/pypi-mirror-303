import os
import sys
import platform
from scan.log import get_logger


if platform.system().lower() == 'windows':
    sn = 'hscan'
else:
    try:
        file_path = os.path.abspath(sys.argv[0])
        sn = file_path.split('/')[-1].replace('.py', '')
    except:
        sn = 'hscan'

logger = get_logger(sn)
