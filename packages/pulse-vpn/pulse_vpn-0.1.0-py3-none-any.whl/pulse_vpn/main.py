from pathlib import Path
import argparse
import os
import shlex
import subprocess
import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtNetwork import QNetworkCookie
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow


class CookieExtractor(QMainWindow):
    def __init__(self, *, url: str, cookie_name: str):
        super().__init__()

        self.cookie = None

        self._webview = QWebEngineView()
        self._cookie_name = cookie_name

        profile = QWebEngineProfile(parent=self._webview)
        cookie_store = profile.cookieStore()
        cookie_store.cookieAdded.connect(self.on_cookie_added)

        self._page = QWebEnginePage(profile, self._webview)
        self._webview.setPage(self._page)
        self._webview.load(QUrl(url))
        self.setCentralWidget(self._webview)

    def on_cookie_added(self, cookie) -> None:
        c = QNetworkCookie(cookie)
        if bytearray(c.name()).decode() == self._cookie_name:
            self.cookie = bytearray(c.value()).decode()
            self.close()


def extract_cookie(*, url: str, cookie_name: str) -> str:
    app = QApplication(sys.argv)
    window = CookieExtractor(url=url, cookie_name=cookie_name)
    window.show()
    app.exec()
    return window.cookie


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pulse-cookie",
        description="open SSO/SAML page to retrieve authentication cookie for Pulse Connect Secure VPN",
    )
    parser.add_argument(
        "--host",
        help="URL of the Pulse Connect Secure VPN server",
        type=str,
        default="vpn.pulsepoint.com",
    )
    parser.add_argument(
        "-n",
        "--name",
        help="name of the cookie",
        type=str,
        default="DSID",
    )
    args = parser.parse_args()
    _try_connect_loop(host=args.host, cookie_name=args.name)


def _get_endpoint(host: str) -> str:
    return f"https://{host}/saml"


def _maybe_cached_cookie(
    host: str,
    cookie_name: str,
    force_new_cookie: bool = False,
):
    cookie_path = Path(os.environ["HOME"]) / ".pulse-vpn" / host / cookie_name
    if cookie_path.exists() and not force_new_cookie:
        return cookie_path.read_text()

    cookie = extract_cookie(url=_get_endpoint(host), cookie_name=cookie_name)
    cookie_path.parent.mkdir(parents=True, exist_ok=True)
    cookie_path.write_text(cookie)


def _try_connect_loop(
    host: str,
    cookie_name: str,
):
    force_new_cookie = False
    while True:
        cookie = _maybe_cached_cookie(
            host=host,
            cookie_name=cookie_name,
            force_new_cookie=force_new_cookie,
        )
        endpoint = _get_endpoint(host)
        command = f"sudo openconnect --protocol nc -C DSID={cookie} {endpoint}"
        try:
            subprocess.run(
                shlex.split(command),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            sys.stderr.buffer.write(e.stderr)
            if b"Cookie was rejected by server" in e.stderr:
                force_new_cookie = True
                continue
            raise


if __name__ == "__main__":
    main()
