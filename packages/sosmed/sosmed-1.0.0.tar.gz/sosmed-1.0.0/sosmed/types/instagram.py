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

from typing import Dict, List



class ClipsMusicAttributionInfo:
    def __init__(self, **kwargs):
        self.artistName: str = kwargs.get("artist_name", "")
        self.songName: str = kwargs.get("song_name", "")
        self.usesOriginalAudio: bool = kwargs.get("uses_original_audio", False)
        self.shouldMuteAudio: bool = kwargs.get("should_mute_audio", False)
        self.shouldMuteAudioReason: str = kwargs.get("should_mute_audio_reason", "")
        self.audioId: str = kwargs.get("audio_id", "")

    def parse(self) -> dict:
        return {
            "artistName": self.artistName,
            "songName": self.songName,
            "usesOriginalAudio": self.usesOriginalAudio,
            "shouldMuteAudio": self.shouldMuteAudio,
            "shouldMuteAudioReason": self.shouldMuteAudioReason,
            "audioId": self.audioId
        }


class Owner:
    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id", "")
        self.username: str = kwargs.get("username", "")
        self.isVerified: bool = kwargs.get("is_verified", False)
        self.profilePicUrl: str = kwargs.get("profile_pic_url", "")
        self.blockedByViewer: bool = kwargs.get("blocked_by_viewer", False)
        self.restrictedByViewer: bool = kwargs.get("restricted_by_viewer", False)
        self.followedByViewer: bool = kwargs.get("followed_by_viewer", False)
        self.fullName: str = kwargs.get("full_name", "")
        self.hasBlockedViewer: bool = kwargs.get("has_blocked_viewer", False)
        self.isEmbedsDisabled: bool = kwargs.get("is_embeds_disabled", False)
        self.isPrivate: bool = kwargs.get("is_private", False)
        self.isUnpublished: bool = kwargs.get("is_unpublished", False)
        self.requestedByViewer: bool = kwargs.get("requested_by_viewer", False)
        self.passTieringRecommendation: bool = kwargs.get("pass_tiering_recommendation", False)
        self.edgeOwnerToTimelineMedia: Dict[str, int] = kwargs.get("edge_owner_to_timeline_media", {})
        self.edgeFollowedBy: Dict[str, int] = kwargs.get("edge_followed_by", {})

    def parse(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "isVerified": self.isVerified,
            "profilePicUrl": self.profilePicUrl,
            "blockedByViewer": self.blockedByViewer,
            "restrictedByViewer": self.restrictedByViewer,
            "followedByViewer": self.followedByViewer,
            "fullName": self.fullName,
            "hasBlockedViewer": self.hasBlockedViewer,
            "isEmbedsDisabled": self.isEmbedsDisabled,
            "isPrivate": self.isPrivate,
            "isUnpublished": self.isUnpublished,
            "requestedByViewer": self.requestedByViewer,
            "passTieringRecommendation": self.passTieringRecommendation,
            "edgeOwnerToTimelineMedia": self.edgeOwnerToTimelineMedia,
            "edgeFollowedBy": self.edgeFollowedBy
        }


class DataEdgeMediaToTaggedUser:
    def __init__(self, **kwargs):
        self.node = kwargs.get("node", {})
        self.user = self.node.get("user", {})
        self.id: str = self.user.get("id", "")
        self.fullName: str = self.user.get("full_name", "")
        self.followedByViewer: bool = self.user.get("followed_by_viewer", False)
        self.isVerified: bool = self.user.get("is_verified", False)
        self.profilePicUrl: str = self.user.get("profile_pic_url", "")
        self.username: str = self.user.get("username", "")
        self.x: int = self.user.get("x", 0)
        self.y: int = self.user.get("y", 0)
        self.id: str = self.node.get("id", "")

    def parse(self) -> dict:
        return {
            "id": self.id,
            "fullName": self.fullName,
            "followedByViewer": self.followedByViewer,
            "isVerified": self.isVerified,
            "profilePicUrl": self.profilePicUrl,
            "username": self.username,
            "x": self.x,
            "y": self.y
        }


class EdgeMediaToTaggedUser:
    def __init__(self, **kwargs):
        self.edges: List[DataEdgeMediaToTaggedUser] = [
            DataEdgeMediaToTaggedUser(**edge) for edge in kwargs.get("edges", [])
        ]

    def parse(self) -> dict:
        return {
            "edges": [edge.parse() for edge in self.edges]
        }


class DataEdgeMediaToCaption:
    def __init__(self, **kwargs):
        self.node = kwargs.get("node", {})
        self.text: str = self.node.get("text", "")
        self.createdAt: int = self.node.get("created_at", "")
        self.id: str = self.node.get("id", "")

    def parse(self) -> dict:
        return {
            "text": self.text,
            "createdAt": self.createdAt,
            "id": self.id
        }


class EdgeMediaToCaption:
    def __init__(self, **kwargs):
        self.edges: List[DataEdgeMediaToCaption] = [
            DataEdgeMediaToCaption(**edge) for edge in kwargs.get("edges", [])
        ]

    def parse(self) -> dict:
        return {
            "edges": [edge.parse() for edge in self.edges]
        }


class EdgeMediaToComment:
    def __init__(self, **kwargs):
        self.count: int = kwargs.get("count", 0)
        self.pageInfo = kwargs.get("page_info", {})
        self.edges: list = kwargs.get("edges", [])

    def parse(self) -> dict:
        return {
            "count": self.count,
            "pageInfo": self.pageInfo,
            "edges": self.edges
        }


class CoauthorProducers:
    def __init__(self, **kwargs):
        self.id: str = kwargs.get("id", "")
        self.isVerified: bool = kwargs.get("is_verified", False)
        self.profilePicUrl: str = kwargs.get("profile_pic_url", "")
        self.username: str = kwargs.get("username", "")

    def parse(self) -> dict:
        return {
            "id": self.id,
            "isVerified": self.isVerified,
            "profilePicUrl": self.profilePicUrl,
            "username": self.username
        }


class DisplayResource:
    def __init__(self, **kwargs):
        self.src: str = kwargs.get("src", "")
        self.configWidth: int = kwargs.get("config_width", 0)
        self.configWeight: int = kwargs.get("config_height", 0)

    def parse(self) -> dict:
        return {
            "src": self.src,
            "configWidth": self.configWidth,
            "configWeight": self.configWeight
        }


class DataEdgeRelatedProfiles:
    def __init__(self, **kwargs):
        self.node = kwargs.get("node", {})
        self.id: str = self.node.get("id", "")
        self.fullName: str = self.node.get("full_name", "")
        self.isPrivate: bool = self.node.get("is_private", False)
        self.isVerified: bool = self.node.get("is_verified", False)
        self.profilePicUrl: str = self.node.get("profile_pic_url", "")
        self.username: str = self.node.get("username", "")
        self.edgeFollowedBy: Dict[str, int] = self.node.get("edge_followed_by", {})
        self.edgeOwnerToTimelineMedia: Dict[str, int] = self.node.get("edge_owner_to_timeline_media", {})

    def parse(self) -> dict:
        return {
            "id": self.id,
            "fullName": self.fullName,
            "isPrivate": self.isPrivate,
            "isVerified": self.isVerified,
            "profilePicUrl": self.profilePicUrl,
            "username": self.username,
            "edgeFollowedBy": self.edgeFollowedBy,
            "edgeOwnerToTimelineMedia": self.edgeOwnerToTimelineMedia
        }


class EdgeRelatedProfiles:
    def __init__(self, **kwargs):
        self.edges: List[DataEdgeRelatedProfiles] = [DataEdgeRelatedProfiles(**edge) for edge in kwargs.get("edges", [])]

    def parse(self) -> dict:
        return {
            "edges": [edge.parse() for edge in self.edges]
        }


class Instagram:
    def __init__(self, **kwargs):
        self._typeName: str = kwargs.get("__typename", "")
        self._isXDTGraphMediaInterface: str = kwargs.get("__isXDTGraphMediaInterface", '')
        self.id: str = kwargs.get("id", "")
        self.shortCode: str = kwargs.get("shortcode", "")
        self.thumbnailSrc: str = kwargs.get("thumbnail_src", "")
        self.dimensions: Dict[str, int] = kwargs.get("dimensions", {})
        self.gatingInfo = kwargs.get("gating_info", None)
        self.factCheckOverallRating = kwargs.get("fact_check_overall_rating", None)
        self.factCheckInformation = kwargs.get("fact_check_information", None)
        self.sensitivityFrictionInfo = kwargs.get("sensitivity_friction_info", None)
        self.sharingFrictionInfo = kwargs.get("sharing_friction_info", None)
        self.mediaOverlayInfo = kwargs.get("media_overlay_info", None)
        self.mediaPreview: str = kwargs.get("media_preview", '')
        self.displayUrl: str = kwargs.get("display_url", '')
        self.displayResource: List[DisplayResource] = [DisplayResource(**i) for i in kwargs.get("display_resources", [])]
        self.accessibilityCaption = kwargs.get("accessibility_caption", None)
        self.dashInfo: Dict[str, any] = kwargs.get("dash_info", {})
        self.hashAudio: bool = kwargs.get("hash_audio", False)
        self.videoUrl: str = kwargs.get("video_url", '')
        self.videoViewCount: int = kwargs.get("video_view_count", 0)
        self.videoPlayCount: int = kwargs.get("video_play_count", 0)
        self.videoDuration: int = kwargs.get("video_duration", 0)
        self.isVideo: bool = kwargs.get("is_video", False)
        self.encodingStatus = kwargs.get("encoding_status", None)
        self.isPublished: bool = kwargs.get("is_published", False)
        self.productType: str = kwargs.get("product_type", "")
        self.title: str = kwargs.get("title", "")
        self.clipsMusicAttributionInfo: ClipsMusicAttributionInfo = kwargs.get("clips_music_attribution_info", {})
        self.relatedProfiles: EdgeRelatedProfiles = EdgeRelatedProfiles(**kwargs.get("edge_related_profiles", {}))
        self.coauthorProducers: List[CoauthorProducers] = [CoauthorProducers(**i) for i in kwargs.get("coauthor_producers", [])]
        self.trackingToken: str = kwargs.get("tracking_token", '')
        self.upcomingEvent = kwargs.get("upcoming_event", None)
        self.owner: Owner = Owner(**kwargs.get("owner", {}))
        self.edgeMediaToTaggedUser: EdgeMediaToTaggedUser = EdgeMediaToTaggedUser(**kwargs.get("edge_media_to_tagged_user", {}))
        self.edgeMediaToCaption: EdgeMediaToCaption = EdgeMediaToCaption(**kwargs.get("edge_media_to_caption", {}))
        self.canSeeInsightsAsBrand: bool = kwargs.get("can_see_insights_as_brand", False)
        self.captionIsEdited: bool = kwargs.get("caption_is_edited", False)
        self.hasRankedComments: bool = kwargs.get("has_ranked_comments", False)
        self.likeAndViewCountsDisabled: bool = kwargs.get("like_and_view_counts_disabled", False)
        self.edgeMediaToComment: EdgeMediaToComment = EdgeMediaToComment(**kwargs.get("edge_media_to_comment", {}))
        self.commentDisabled: bool = kwargs.get("comment_disabled", False)
        self.commentingDisabledForViewer: bool = kwargs.get("commenting_disabled_for_viewer", False)
        self.takenAtTimestamp: int = kwargs.get("taken_at_timestamp", 0)
        self.edgeMediaPreviewLike = kwargs.get("edge_media_preview_like", {})
        self.edgeMediaToSponsorUser = kwargs.get("edge_media_to_sponsor_user", {})
        self.isAffiliate: bool = kwargs.get("is_affiliate", False)
        self.isPaidPartnership: bool = kwargs.get("is_paid_partnership", False)
        self.location = kwargs.get("location", None)
        self.nftAssetInfo = kwargs.get("nft_asset_info", None)
        self.viewerHasLiked: bool = kwargs.get("viewer_has_liked", False)
        self.viewerHasSaved: bool = kwargs.get("viewer_has_saved", False)
        self.viewerHasSavedToCollection: bool = kwargs.get("viewer_has_saved_to_collection", False)
        self.viewerInPhotoOfYou: bool = kwargs.get("viewer_in_photo_of_you", False)
        self.viewerCanReshare: bool = kwargs.get("viewer_can_reshare", False)
        self.isAd: bool = kwargs.get("is_ad", False)
        self.edgeWebMediaToRelatedMedia = kwargs.get("edge_web_media_to_related_media", {})
        self.pinnedForUsers = kwargs.get("pinned_for_users", [])
        self.error: bool = kwargs.get("error", False)

    async def download(self):
        title = self.title if self.title != "" else self.id
        # Check if file is exists
        if os.path.exists(f"downloads/ig-{title}.mp4"):
            return f"downloads/ig-{title}.mp4"

        # Create Folder if not exists
        if not os.path.isdir("downloads"):
            os.mkdir("downloads")

        async with aiohttp.ClientSession() as session:
            stream = await session.get(self.videoUrl)
            async with aiofiles.open(f"downloads/ig-{title}.mp4", mode="wb") as file:
                await file.write(await stream.read())
                return f"downloads/ig-{title}.mp4"

    def parse(self) -> dict:
        return {
            "id": self.id,
            "shortcode": self.shortCode,
            "thumbnail_src": self.thumbnailSrc,
            "dimensions": self.dimensions,
            "gatingInfo": self.gatingInfo,
            "factCheckOverallRating": self.factCheckOverallRating,
            "factCheckInformation": self.factCheckInformation,
            "sensitivityFrictionInfo": self.sensitivityFrictionInfo,
            "sharingFrictionInfo": self.sharingFrictionInfo,
            "mediaOverlayInfo": self.mediaOverlayInfo,
            "mediaPreview": self.mediaPreview,
            "displayUrl": self.displayUrl,
            "displayResource": [i.parse() for i in self.displayResource],
            "accessibilityCaption": self.accessibilityCaption,
            "dashInfo": self.dashInfo,
            "hashAudio": self.hashAudio,
            "videoUrl": self.videoUrl,
            "videoViewCount": self.videoViewCount,
            "videoPlayCount": self.videoPlayCount,
            "videoDuration": self.videoDuration,
        }
