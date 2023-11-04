from server.server import Request, Response
from utils.response import get_response_not_found
from router.urls import urls


def router(request: Request, directory: str = None) -> Response:
    for path in urls:
        if path.method != request.path:
            continue
        if (path.start and request.path.startswith(path.path)) or \
                (not path.start and request.path == path.path):
            if path.directory:
                return path.view(request, directory)
            return path.view(request)
    return get_response_not_found()
