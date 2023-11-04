from server.types import HttpMethod
from router.path import Path
from router.views import *


urls = [
    Path('/', index),
    Path('/echo/', echo, start=True),
    Path('/user-agent', user_agent),
    Path('/files/', post_file, start=True,
         directory=True, method=HttpMethod.POST),
    Path('/files/', get_file, start=True, directory=True),
]
