import base64
import logging
from typing import Optional
from urllib.parse import quote
from urllib.parse import unquote

from amsdal_utils.models.enums import Versions
from fastapi import HTTPException
from fastapi import Query
from fastapi import Request
from fastapi import Response

from amsdal_server.apps.common.thumbnail import resize_image
from amsdal_server.apps.objects.router import router
from amsdal_server.apps.objects.services.file_object import ObjectFileApi

logger = logging.getLogger(__name__)


def _download_file(
    object_id: str,
    request: Request,
    version_id: str = '',
    width: int | None = None,
    height: int | None = None,
) -> Response:
    file_obj = ObjectFileApi.get_file(
        request.user,
        object_id,
        version_id or Versions.LATEST,
    )

    if not file_obj:
        raise HTTPException(status_code=404, detail='File not found')

    _data = file_obj.data

    if isinstance(_data, bytes) and _data.startswith((b"b'", b'b"')):
        try:
            # legacy corrupted data
            _data = base64.b64decode(eval(_data))  # noqa: S307
        except SyntaxError:
            pass

    if width and height:
        size = (width, height)
    else:
        size = None

    try:
        content = resize_image(_data, size=size)
    except Exception as e:
        logger.warning('Unable to resize image (probably it is not an image): %s', e, exc_info=True)
        content = _data

    return Response(
        content=content,
        headers={
            'content-disposition': f'attachment; filename={quote(file_obj.filename)}',
        },
        media_type=file_obj.mimetype or 'application/octet-stream',
    )


@router.get('/api/objects/file-download/{object_id}/')
def file_download(
    object_id: str,
    request: Request,
    version_id: str = '',
    width: Optional[int] = Query(None),  # noqa: UP007
    height: Optional[int] = Query(None),  # noqa: UP007
) -> Response:
    return _download_file(object_id, request, version_id, width, height)


@router.get('/api/objects/download-file/')
def download_file(
    request: Request,
    object_id: str,
    version_id: str = '',
    width: Optional[int] = Query(None),  # noqa: UP007
    height: Optional[int] = Query(None),  # noqa: UP007
) -> Response:
    return _download_file(unquote(object_id), request, version_id, width, height)
