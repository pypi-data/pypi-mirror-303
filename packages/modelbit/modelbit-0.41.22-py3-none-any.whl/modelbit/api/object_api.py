import logging
from typing import Any, Dict, Optional

from modelbit.api import MbApi, readLimiter
from modelbit.internal.secure_storage import DownloadableObjectInfo, UploadableObjectInfo

from .api import MbApi

logger = logging.getLogger(__name__)


class EncryptedObjectInfo(DownloadableObjectInfo):

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
    self.contentHash: str = data["contentHash"]
    self.objectExists: bool = data["objectExists"]

  def cachekey(self) -> str:
    return self.contentHash


class ObjectApi:
  api: MbApi

  def __init__(self, api: MbApi):
    self.api = api

  def runtimeObjectUploadInfo(self, contentHash: str) -> UploadableObjectInfo:
    readLimiter.maybeDelay()
    resp = self.api.getJsonOrThrow("api/cli/v1/runtime_object_upload_info", {
        "contentHash": contentHash,
    })
    return UploadableObjectInfo(resp)

  def runtimeObjectDownloadUrl(self, contentHash: str, isShared: Optional[bool]) -> EncryptedObjectInfo:
    readLimiter.maybeDelay()
    resp = self.api.getJsonOrThrow("api/cli/v1/runtime_object_download_url", {
        "contentHash": contentHash,
        "isShared": bool(isShared)
    })
    return EncryptedObjectInfo(resp)
