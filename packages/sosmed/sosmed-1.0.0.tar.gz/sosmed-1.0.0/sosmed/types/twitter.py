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

import aiofiles
import aiohttp
import os

from typing import Dict, List, Union, Optional

import sosmed.exceptions as ex


class Size:
    def __init__(self, **kwargs):
        self.height: int = kwargs.get("height", 0)
        self.width: int = kwargs.get("width", 0)

    def parse(self) -> Dict[str, int]:
        return {
            "height": self.height,
            "width": self.width
        }


class MediaExtended:
    def __init__(self, **kwargs):
        self.altText: str = kwargs.get("altText", "")
        self.durationMillis: int = kwargs.get("duration_millis", 0)
        self.size: Size = Size(**kwargs.get("size", {}))
        self.thumbnailUrl: str = kwargs.get("thumbnail_url", "")
        self.type: str = kwargs.get("type", "")
        self.url: str = kwargs.get("url", "")

    def parse(self) -> Dict[str, Union[str, int]]:
        return {
            "altText": self.altText,
            "durationMillis": self.durationMillis,
            "size": self.size.parse(),
            "thumbnailUrl": self.thumbnailUrl,
            "type": self.type,
            "url": self.url
        }


class Twitter:
    def __init__(self, **kwargs):
        self.allSameType: bool = kwargs.get("allSameType", False)
        self.article: Optional[any] = kwargs.get("article", None)
        self.combinedMediaUrl: Optional[any] = kwargs.get("combinedMediaUrl", None)
        self.communityNote: Optional[any] = kwargs.get("communityNote", None)
        self.conversationId: str = kwargs.get("conversationID", "")
        self.date: str = kwargs.get("date", "")
        self.dateEpoch: int = kwargs.get("date_epoch", 0)
        self.hasMedia: bool = kwargs.get("hasMedia", False)
        self.hashtags: List[any] = kwargs.get("hashtags", [])
        self.lang: str = kwargs.get("lang", "")
        self.likes: int = kwargs.get("likes", 0)
        self.mediaURLs: List[str] = kwargs.get("mediaURLs", [])
        self.mediaExtended: List[MediaExtended] = [MediaExtended(**media) for media in kwargs.get("media_extended", [])]
        self.pollData: Optional[any] = kwargs.get("pollData", None)
        self.possiblySensitive: bool = kwargs.get("possibly_sensitive", False)
        self.qrt: Optional[any] = kwargs.get("qrt", None)
        self.qrtUrl: Optional[any] = kwargs.get("qrtURL", None)
        self.replies: int = kwargs.get("replies", 0)
        self.retweets: int = kwargs.get("retweets", 0)
        self.text: str = kwargs.get("text", "")
        self.tweetId: str = kwargs.get("tweetID", "")
        self.tweetUrl: str = kwargs.get("tweetURL", "")
        self.userName: str = kwargs.get("user_name", "")
        self.userProfileImageUrl: str = kwargs.get("user_profile_image_url", "")
        self.userScreenName: str = kwargs.get("user_screen_name", "")

    async def download(self):
        # Check if file is exists
        if os.path.exists(f"downloads/tweet-{self.tweetId}.mp4"):
            return f"downloads/tweet-{self.tweetId}.mp4"

        # Create Folder if not exists
        if not os.path.isdir("downloads"):
            os.mkdir("downloads")

        target: Optional[MediaExtended] = None
        if len(self.mediaExtended) > 1:
            target = self.mediaExtended[0]
        else:
            target = None

        if not target:
            raise ex.SosmedError("Download Error (caused 'No Downloaded Url Found')")

        async with aiohttp.ClientSession() as session:
            stream = await session.get(target.url)
            async with aiofiles.open(f"downloads/tweet-{self.tweetId}.mp4", mode="wb") as file:
                await file.write(await stream.read())
                return f"downloads/tweet-{self.tweetId}.mp4"

    def parse(self) -> dict:
        return {
            "allSameType": self.allSameType,
            "article": self.article,
            "combinedMediaUrl": self.combinedMediaUrl,
            "communityNote": self.communityNote,
            "conversationId": self.conversationId,
            "date": self.date,
            "dateEpoch": self.dateEpoch,
            "hasMedia": self.hasMedia,
            "hashtags": self.hashtags,
            "lang": self.lang,
            "likes": self.likes,
            "mediaURLs": self.mediaURLs,
            "mediaExtended": self.mediaExtended,
            "pollData": self.pollData,
            "possiblySensitive": self.possiblySensitive,
            "qrt": self.qrt,
            "qrtUrl": self.qrtUrl,
            "replies": self.replies,
            "retweets": self.retweets,
            "text": self.text,
            "tweetId": self.tweetId,
            "tweetUrl": self.tweetUrl,
            "userName": self.userName,
            "userProfile_image_url": self.userProfile_image_url,
            "userScreen_name": self.userScreen_name
        }
