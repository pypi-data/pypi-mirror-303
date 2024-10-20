
from flask import make_response, send_file, Response

from .request_codes import RequestCode


def send_binary_image(data, content_type="image/webp", cache_control=3600) -> Response:
    if data is None:
        return make_response(
            send_file("static/img/noimage.png"),
            # RequestCode.ClientError.NotFound
            RequestCode.Success.OK
        )

    resp = make_response(data, RequestCode.Success.OK)
    resp.headers.set("Content-Type", content_type)
    resp.cache_control.max_age = cache_control
    return resp
