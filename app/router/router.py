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
                return path.view(request=request, directory=directory)
            return path.view(request=request)
    print(path.path, 'path not exists')
    return get_response_not_found(request=request)
