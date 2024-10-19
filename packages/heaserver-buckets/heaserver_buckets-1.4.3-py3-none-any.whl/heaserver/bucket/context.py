from heaserver.service.db.aws import AWSPermissionContext, is_account_owner
from heaserver.service.db.awsaction import S3_LIST_BUCKET, S3_DELETE_BUCKET, S3_GET_BUCKET_TAGGING, S3_PUT_BUCKET_TAGGING
from heaobject.bucket import AWSBucket
from heaobject.root import Permission
from aiohttp.web import Request
from cachetools import TTLCache
from pickle import dumps
from copy import copy
from typing import NamedTuple


class _CacheKey(NamedTuple):
    obj_str: str
    attr: str

class S3BucketPermissionsContext(AWSPermissionContext[AWSBucket]):
    def __init__(self, request: Request, volume_id: str, **kwargs):
        actions = [S3_LIST_BUCKET, S3_PUT_BUCKET_TAGGING, S3_DELETE_BUCKET]
        super().__init__(request=request, volume_id=volume_id, actions=actions, **kwargs)
        self.__cache: TTLCache[_CacheKey, list[Permission]] = TTLCache(maxsize=128, ttl=30)

    async def get_attribute_permissions(self, obj: AWSBucket, attr: str) -> list[Permission]:
        key = _CacheKey(repr(obj), attr)
        perms = self.__cache.get(key)
        if perms is None:
            if attr == 'tags' and not await self.is_account_owner():
                perms = await self._simulate_perms(obj, [S3_GET_BUCKET_TAGGING, S3_PUT_BUCKET_TAGGING])
            else:
                perms = await super().get_attribute_permissions(obj, attr)
            self.__cache[key] = perms
        return copy(perms)

    def _caller_arn(self, obj: AWSBucket):
        return f'arn:aws:s3:::{obj.bucket_id}'
