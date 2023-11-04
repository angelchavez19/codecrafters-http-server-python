from app.router.urls import urls
from app.server.server import Request, Response
from app.utils.response import get_response_not_found


def router(request: Request, directory: str = None) -> Response:
    for path in urls:
        if path.method != request.path:
            continue
        if (path.start and request.path.startswith(path.path)) or \
                (not path.start and request.path == path.path):
            if path.directory:
                return path.view(request, directory)
            return path.view(request)
    return get_response_not_found(request=request)
