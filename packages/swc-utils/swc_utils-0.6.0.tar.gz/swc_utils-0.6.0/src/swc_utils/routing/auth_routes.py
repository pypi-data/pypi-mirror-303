from time import time
from flask import request, redirect, make_response, session, Flask

from ..other.decorators import deprecated
from ..tools.config import Config
from ..web.auth_manager import check_auth


def register_auth_routes(app: Flask, config: Config, app_name: str):
    ums_route = config.get("UMS_ROUTE", "https://ums.software-city.org")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        url = request.root_url
        if "http://" in url or "https://" in url:
            url = url.split("//")[1]

        resp = make_response(
            redirect(f"{ums_route}/login?title={app_name}&redirect={url}{request.args.get('redirect') or '/'}")
        )

        if session.get("uuid") is None:
            session.clear()
            resp.delete_cookie("session")

        return resp

    @app.before_request
    def update_session():
        if session.get("uuid") is None:
            return
        session["updated"] = time()
        session["user_agent"] = request.headers.get("User-Agent")
        session["ip"] = request.headers.get("X-Real-IP") or request.remote_addr

    @app.route("/logout")
    def logout():
        url = request.root_url
        if "http://" in url or "https://" in url:
            url = url.split("//")[1]

        return redirect(f"{ums_route}/logout?redirect={url}")


@deprecated
def register_session_refresh(app: Flask, session_duration: int = 3600):
    @app.after_request
    def refresh_session(response):
        if not check_auth():
            return response

        # Check if the session has been updated in the last hour and redirect to the login if not
        if request.method == "GET" and request.path == "/":  # Make sure the session is only checked on the main page
            updated = session.get("updated")
            if updated is None or (time() - updated) > session_duration:
                return redirect(f"/login?redirect={request.path}")

        return response
