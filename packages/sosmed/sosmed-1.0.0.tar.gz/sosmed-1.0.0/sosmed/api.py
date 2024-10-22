# MIT License

# Copyright (c) 2024 AyiinXd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import aiohttp
import hmac
import hashlib
import os
from typing import Optional

from .exceptions import SosmedError
from .types import Response


class Api:
    apiToken: Optional[str]
    secret: Optional[str]
    baseUrl: str = "https://api.ayiin.fun/api"
    def __init__(self, apiToken: str, secret: str, path: Optional[str] = None):
        self.apiToken = apiToken
        self.secret = secret
        self.path = path if path else "downloads"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
        }

    async def post(self, path: str, url: Optional[str]) -> Response:
        signature = await self.createSignature(
            url=url if url else "",
            path=path,
            method="POST"
        )
        self.headers['Xd-Signature'] = signature
        self.headers['Xd-Api-Token'] = self.apiToken
        body = {"url": url} if url else None
        async with aiohttp.ClientSession(headers=self.headers) as session:
            res = await session.post(
                url=f"{self.baseUrl}{path}",
                json=body,
                headers=self.headers
            )
            json = await res.json()
            response: Response = Response(**json)
            if response.success:
                return response
            else:
                raise SosmedError(response.message)

    def validatePath(self, autoClean: bool = False):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
        if autoClean:
            for file in os.listdir(self.path):
                try:
                    os.remove(os.path.join(self.path, file))
                except FileNotFoundError:
                    pass

    async def createSignature(
        self,
        url: str,
        path: str,
        method: str,
    ):
        msg = f"METHOD={method}; PATH={path}; TOKEN={self.apiToken}; URL={url};"
        signature = hmac.new(
            bytes(self.secret, 'latin-1'),
            bytes(msg, 'latin-1'),
            hashlib.sha256
        ).hexdigest()
        return signature
