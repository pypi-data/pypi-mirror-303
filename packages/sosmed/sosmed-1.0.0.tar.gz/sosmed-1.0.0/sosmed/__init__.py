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


__version__ = "1.0.0"


from typing import Optional

from .api import Api
from .exceptions import SosmedError
from .types import (
    Instagram,
    Response,
    TikTok,
    Twitter
)


class Sosmed(Api):
    def __init__(self, apiToken: str, secret: str, path: Optional[str] = None):
        super().__init__(
            apiToken=apiToken,
            secret=secret,
            path=path
        )

    async def instagram(self, url: str) -> Instagram:
        res = await self.post(
            path="/instagram",
            url=url
        )
        return Instagram(**res.data)

    async def tiktok(self, url: str) -> TikTok:
        res = await self.post(
            path="/tiktok",
            url=url
        )
        return TikTok(**res.data)

    async def twitter(self, url: str) -> Twitter:
        res = await self.post(
            path="/twitter",
            url=url
        )
        return Twitter(**res.data)

    async def youtube(self, url: str) -> Response:
        return await self.post(
            path="/youtube",
            url=url
        )
