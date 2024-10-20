import abc
from collections import deque
import logging
import threading
import time
import urllib.parse

import requests


class RestClientBase:
    def __init__(
        self,
        base: str,
        *,
        headers: dict[str, str] | None = None,
        rate_limit_window_seconds: int | None = None,
        rate_limit_requests: int | None = None,
    ):
        self.base = base
        self.rate_limit_window_seconds = rate_limit_window_seconds
        self.rate_limit_requests = rate_limit_requests
        self._REQ_HISTORY_LOCK = threading.Lock()
        self._REQ_HISTORY: deque[float] = deque([])
        self.session = requests.Session()
        if headers:
            for k, v in headers.items():
                self.session.headers[k] = v
        return

    def _encode_query_params(self, params: dict) -> str:
        return "&".join(
            [f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in params.items()]
        )

    def _wait_turn_for_request(self) -> None:
        if not self.rate_limit_requests or not self.rate_limit_window_seconds:
            return
        now = time.time()
        cutoff = now - self.rate_limit_window_seconds
        with self._REQ_HISTORY_LOCK:
            while self._REQ_HISTORY and self._REQ_HISTORY[0] < cutoff:
                self._REQ_HISTORY.popleft()
            if len(self._REQ_HISTORY) < self.rate_limit_requests:
                self._REQ_HISTORY.append(now)
                return
        # otherwise, too many in-flight requests
        time.sleep(self.rate_limit_window_seconds)
        self._wait_turn_for_request()
        return

    def _req(self, method: str, path: str, *, ignore_error: bool = False, **kwargs):
        url = f"{self.base}{path}"
        self._wait_turn_for_request()
        res = self.session.request(method, url, **kwargs)
        if not res.ok:
            logging.error("request to %s failed: %s", url, res.text)
        if not ignore_error:
            res.raise_for_status()
        return res
