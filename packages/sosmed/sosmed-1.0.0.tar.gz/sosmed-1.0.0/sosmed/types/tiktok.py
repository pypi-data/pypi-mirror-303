# MIT License

# Copyright (c) 2024 AyiinXd

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following "conditions":

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

from typing import Dict, List, Optional


class MusicInfo:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "")
        self.title = kwargs.get("title", "")
        self.play = kwargs.get("play", "")
        self.cover = kwargs.get("cover", "")
        self.author = kwargs.get("author", "")
        self.original = kwargs.get("original", False)
        self.duration = kwargs.get("duration", 0)
        self.album = kwargs.get("album", "")

    def parse(self):
        return {
            "id": self.id,
            "title": self.title,
            "play": self.play,
            "cover": self.cover,
            "author": self.author,
            "original": self.original,
            "duration": self.duration,
            "album": self.album
        }

class CommerceInfo:
    def __init__(self, **kwargs):
        self.advPromotable = kwargs.get("adv_promotable", False)
        self.auctionAdInvited = kwargs.get("auction_ad_invited", False)
        self.brandedContentType = kwargs.get("branded_content_type", 0)
        self.withCommentFilterWords = kwargs.get("with_comment_filter_words", False)

    def parse(self):
        return {
            "advPromotable": self.advPromotable,
            "auctionAdInvited": self.auctionAdInvited,
            "brandedContentType": self.brandedContentType,
            "withCommentFilterWords": self.withCommentFilterWords
        }


class Author:
    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id", "")
        self.uniqueId: str = kwargs.get("unique_id", "")
        self.nickname: str = kwargs.get("nickname", "")
        self.avatar: str = kwargs.get("avatar", "")

    def parse(self):
        return {
            "id": self.id,
            "uniqueId": self.uniqueId,
            "nickname": self.nickname,
            "avatar": self.avatar
        }


class TikTok:
    def __init__(self, **kwargs):
        self.awemeId: str = kwargs.get("aweme_id", "")
        self.id: str = kwargs.get("id", "")
        self.region: str = kwargs.get("region", "")
        self.title: str = kwargs.get("title", "")
        self.cover: str = kwargs.get("cover", "")
        self.aiDynamicCover: str = kwargs.get("ai_dynamic_cover", "")
        self.originCover: str = kwargs.get("origin_cover", "")
        self.duration: int = kwargs.get("duration", 0)
        self.play: str = kwargs.get("play", "")
        self.wmPlay: str = kwargs.get("wmplay", "")
        self.size: int = kwargs.get("size", 0)
        self.wmSize: int = kwargs.get("wm_size", 0)
        self.music: str = kwargs.get("music", "")
        self.musicInfo: MusicInfo = MusicInfo(**kwargs.get("music_info", {}))
        self.playCount: int = kwargs.get("play_count", 0)
        self.diggCount: int = kwargs.get("digg_count", 0)
        self.commentCount: int = kwargs.get("comment_count", 0)
        self.shareCount: int = kwargs.get("share_count", 0)
        self.downloadCount: int = kwargs.get("download_count", 0)
        self.collectCount: int = kwargs.get("collect_count", 0)
        self.createTime: int = kwargs.get("create_time", 0)
        self.anchors: any = kwargs.get("anchors", {})
        self.anchorsExtras: Optional[str] = kwargs.get("anchors_extras", None)
        self.isAd: bool = kwargs.get("is_ad", False)
        self.commerceInfo: CommerceInfo = CommerceInfo(**kwargs.get("commerce_info", {}))
        self.commercialVideoInfo: Optional[str] = kwargs.get("commercial_video_info", None)
        self.itemCommentSettings: int = kwargs.get("item_comment_settings", 0)
        self.mentionedUsers: Optional[str] = kwargs.get("mentioned_users", None)
        self.author: Author = Author(**kwargs.get("author", {}))

    async def download(self):
        # Check if file is exists
        if os.path.exists(f"downloads/tiktok-{self.id}.mp4"):
            return f"downloads/tiktok-{self.id}.mp4"

        # Create Folder if not exists
        if not os.path.isdir("downloads"):
            os.mkdir("downloads")

        async with aiohttp.ClientSession() as session:
            stream = await session.get(self.play)
            async with aiofiles.open(f"downloads/tiktok-{self.id}.mp4", mode="wb") as file:
                await file.write(await stream.read())
                return f"downloads/tiktok-{self.id}.mp4"

    def parse(self) -> dict:
        return {
            "awemeId": self.awemeId,
            "id": self.id,
            "region": self.region,
            "title": self.title,
            "cover": self.cover,
            "aiDynamicCover": self.aiDynamicCover,
            "originCover": self.originCover,
            "duration": self.duration,
            "play": self.play,
            "wmPlay": self.wmPlay,
            "size": self.size,
            "wmSize": self.wmSize,
            "music": self.music,
            "musicInfo": self.musicInfo.parse(),
            "playCount": self.playCount,
            "diggCount": self.diggCount,
            "commentCount": self.commentCount,
            "shareCount": self.shareCount,
            "downloadCount": self.downloadCount,
            "collectCount": self.collectCount,
            "createTime": self.createTime,
            "anchors": self.anchors,
            "anchorsExtras": self.anchorsExtras,
            "isAd": self.isAd, 
            "commerceInfo": self.commerceInfo.parse(),
            "commercialVideoInfo": self.commercialVideoInfo,
            "itemCommentSettings": self.itemCommentSettings,
            "mentionedUsers": self.mentionedUsers,
            "author": self.author.parse(),
        }
