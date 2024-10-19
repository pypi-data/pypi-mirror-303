from json import JSONDecodeError
from heaobject.data import AWSS3FileObject, ClipboardData
from heaobject.user import AWS_USER, NONE_USER, ALL_USERS
from heaobject.aws import S3StorageClass, S3Version
from heaobject.root import DesktopObjectDict, Tag, DesktopObject, Permission
from heaobject.activity import Status
from heaserver.service.activity import DesktopObjectActionLifecycle
from heaserver.service.oidcclaimhdrs import SUB
from heaserver.service.heaobjectsupport import new_heaobject_from_type
from heaserver.service.appproperty import HEA_DB, HEA_COMPONENT, HEA_CACHE
from heaserver.service.runner import init_cmd_line, routes, start
from heaserver.service.db import awsservicelib
from heaserver.service.db.aws import S3Manager, S3ClientContext, S3ObjectPermissionContext
from heaserver.service.db.awsaction import S3_GET_OBJECT, S3_PUT_OBJECT, S3_DELETE_OBJECT
from heaobject.awss3key import KeyDecodeException, decode_key, split, encode_key, is_root, parent
from heaserver.service.wstl import builder_factory, action, add_run_time_action
from heaserver.service.messagebroker import publisher_cleanup_context_factory, publish_desktop_object
from heaserver.service import response
from heaserver.service.sources import AWS_S3
from heaserver.service.mimetypes import guess_mime_type
from heaserver.service.aiohttp import StreamResponseFileLikeWrapper, RequestFileLikeWrapper
from aiohttp import web, hdrs
from aiohttp.helpers import ETag
import logging
from typing import Any
from functools import partial
import asyncio
from botocore.exceptions import ClientError as BotoClientError
from mypy_boto3_s3.client import S3Client
from mypy_boto3_s3.type_defs import TagTypeDef
from datetime import datetime, timezone
from collections.abc import Mapping
from humanize import naturaldelta

from heaserver.folderawss3.util import clear_target_in_cache

_logger = logging.getLogger(__name__)


@routes.get('/ping')
async def ping(request: web.Request) -> web.Response:
    """
    For testing whether the service is up.

    :param request: the HTTP request.
    :return: Always returns status code 200.
    """
    return response.status_ok()


@routes.route('OPTIONS', '/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
async def get_file_options(request: web.Request) -> web.Response:
    """
    Gets the allowed HTTP methods for a file resource.

    :param request: the HTTP request (required).
    :return: the HTTP response.
    ---
    summary: Allowed HTTP methods.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        description: Expected response to a valid request.
        content:
            text/plain:
                schema:
                    type: string
                    example: "200: OK"
      '404':
        $ref: '#/components/responses/404'
    """
    return await response.get_options(request, ['GET', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'])


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/duplicator')
@action(name='heaserver-awss3files-file-duplicate-form')
async def get_file_duplicator(request: web.Request) -> web.Response:
    """
    Gets a form template for duplicating the requested file.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested file was not found.
    """
    logger = logging.getLogger(__name__)
    try:
        return await _get_file(request)
    except KeyDecodeException as e:
        logger.exception('Error getting parent key')
        return response.status_bad_request(f'Error getting parent folder: {e}')


@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files')
@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/')
async def post_file(request: web.Request) -> web.Response:
    """
    Creates a new file.

    :param request: the HTTP request. The body of the request is expected to be a file.
    :return: the response, with a 201 status code if a file was created or a 400 if not. If a folder was created, the
    Location header will contain the URL of the created file.
    ---
    summary: A specific file.
    tags:
        - heaserver-folders-folders
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
    requestBody:
        description: A new folder object.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: Folder example
                  value: {
                    "template": {
                      "data": [{
                        "name": "created",
                        "value": null
                      },
                      {
                        "name": "derived_by",
                        "value": null
                      },
                      {
                        "name": "derived_from",
                        "value": []
                      },
                      {
                        "name": "description",
                        "value": null
                      },
                      {
                        "name": "display_name",
                        "value": "Bob"
                      },
                      {
                        "name": "invited",
                        "value": []
                      },
                      {
                        "name": "modified",
                        "value": null
                      },
                      {
                        "name": "name",
                        "value": "bob"
                      },
                      {
                        "name": "owner",
                        "value": "system|none"
                      },
                      {
                        "name": "shares",
                        "value": []
                      },
                      {
                        "name": "source",
                        "value": null
                      },
                      {
                        "name": "version",
                        "value": null
                      },
                      {
                        "name": "type",
                        "value": "heaobject.folder.AWSS3Folder"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: Item example
                  value: {
                    "created": null,
                    "derived_by": null,
                    "derived_from": [],
                    "description": null,
                    "display_name": "Joe",
                    "invited": [],
                    "modified": null,
                    "name": "joe",
                    "owner": "system|none",
                    "shares": [],
                    "source": null,
                    "type": "heaobject.folder.AWSS3Folder",
                    "version": null
                  }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    resp = await awsservicelib.create_object(request, AWSS3FileObject)
    if resp == 201:
        request.app[HEA_CACHE].clear()
    return resp


@routes.put('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
async def put_file(request: web.Request) -> web.Response:
    """
    Updates file metadata.

    :param request: the HTTP request. The body of the request is expected to be a file.
    :return: the response, with a 201 status code if a file was created or a 400 if not. If a folder was created, the
    Location header will contain the URL of the created file.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: A new file object.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: File example
                  value: {
                    "template": {
                      "data": [{
                        "name": "created",
                        "value": null
                      },
                      {
                        "name": "derived_by",
                        "value": null
                      },
                      {
                        "name": "derived_from",
                        "value": []
                      },
                      {
                        "name": "description",
                        "value": null
                      },
                      {
                        "name": "display_name",
                        "value": "Bob"
                      },
                      {
                        "name": "invited",
                        "value": []
                      },
                      {
                        "name": "modified",
                        "value": null
                      },
                      {
                        "name": "name",
                        "value": "bob"
                      },
                      {
                        "name": "owner",
                        "value": "system|none"
                      },
                      {
                        "name": "shares",
                        "value": []
                      },
                      {
                        "name": "source",
                        "value": null
                      },
                      {
                        "name": "version",
                        "value": null
                      },
                      {
                        "name": "type",
                        "value": "heaobject.data.AWSS3FileObject"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: Item example
                  value: {
                    "created": null,
                    "derived_by": null,
                    "derived_from": [],
                    "description": null,
                    "display_name": "Joe",
                    "invited": [],
                    "modified": null,
                    "name": "joe",
                    "owner": "system|none",
                    "shares": [],
                    "source": null,
                    "type": "heaobject.folder.AWSS3Folder",
                    "tags": [],
                    "version": null
                  }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    id_ = request.match_info['id']

    try:
        key = decode_key(id_)
    except KeyDecodeException as e:
        return response.status_bad_request(f'Invalid id {id_}')

    try:
        file = await new_heaobject_from_type(request, AWSS3FileObject)
    except TypeError:
        return response.status_bad_request(f'Expected type {AWSS3FileObject}; actual object was {await request.text()}')
    if file.key is None:
        return response.status_bad_request(f'file.key cannot be None')

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-update',
                                            description=f'Updating {awsservicelib._activity_object_display_name(bucket_id, key)}',
                                            activity_cb=publish_desktop_object) as activity:
        activity.old_object_id = id_
        activity.old_object_type_name = AWSS3FileObject.get_type_name()
        activity.old_volume_id = volume_id
        activity.old_object_uri = f'volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id_}'
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                loop = asyncio.get_running_loop()
                if key != file.key:
                    await loop.run_in_executor(None, partial(s3_client.copy, Bucket=bucket_id, CopySource={'Bucket': bucket_id, 'Key': key}, Key=file.key))
                    await loop.run_in_executor(None, partial(s3_client.delete_object, Bucket=bucket_id, Key=key))
                folder_id = 'root' if is_root(key) else encode_key(parent(key))
                sub = request.headers.get(SUB, NONE_USER)
                await loop.run_in_executor(None, partial(s3_client.delete_object_tagging, Bucket=bucket_id, Key=file.key))
                await loop.run_in_executor(None, partial(s3_client.put_object_tagging, Bucket=bucket_id, Key=file.key, Tagging={'TagSet': await _to_aws_tags(file.tags)}))
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, id_, 'items'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, None, 'items'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, id_, 'actual'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, None, 'actual'), None)
                activity.new_object_id = id_
                activity.new_object_type_name = AWSS3FileObject.get_type_name()
                activity.new_volume_id = volume_id
                activity.new_object_uri = f'volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id_}'
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)

    return await response.put(True)


@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/archive')
async def post_file_archive(request: web.Request) -> web.Response:
    """
    Posts the provided file to archive it.

    :param request: the HTTP request.
    :return: a Response object with a status of No Content.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: The new name of the file and target for archiving it.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for archiving it.
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "storage_class",
                        "value": "DEEP_ARCHIVE"
                      }
                      ]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: The storage class to archive object to.
                  value: {
                    "storage_class": "DEEP_ARCHIVE"
                  }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        return await awsservicelib.archive_object(request)
    finally:
        id_ = request.match_info['id']
        volume_id = request.match_info['volume_id']
        bucket_id = request.match_info['bucket_id']
        sub = request.headers.get(SUB, NONE_USER)
        try:
            key: str | None = decode_key(id_)
        except KeyDecodeException:
            return response.status_not_found()
        folder_id = 'root' if is_root(key) else encode_key(parent(key))
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, id_, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, None, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, id_, 'actual'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, None, 'actual'), None)


@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/mover')
async def post_file_mover(request: web.Request) -> web.Response:
    """
    Posts the provided file to move it.

    :param request: the HTTP request.
    :return: a Response object with a status of No Content.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: The new name of the file and target for moving it.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for moving it.
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "target",
                        "value": "http://localhost:8080/volumes/666f6f2d6261722d71757578/buckets/my-bucket/awss3files/"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for moving it.
                  value: {
                    "target": "http://localhost:8080/volumes/666f6f2d6261722d71757578/buckets/my-bucket/awss3files/"
                  }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    id_ = request.match_info['id']
    target_uri, target_bucket_name, target_key, _ = await awsservicelib._copy_object_extract_target(await request.json())
    try:
        key = decode_key(id_)
    except KeyDecodeException as e:
        return response.status_bad_request(f'Invalid id {id_}')

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-move',
                                            description=f'Moving {awsservicelib._activity_object_display_name(bucket_id, key)} to {awsservicelib._activity_object_display_name(target_bucket_name, target_key)}',
                                            activity_cb=publish_desktop_object) as activity:
        try:
            copy_response = await awsservicelib.copy_object(request)
            match copy_response.status:
                case 201:
                    activity.new_object_uri = target_uri
                    return await awsservicelib.delete_object(request, recursive=True)
                case _:
                    activity.status = Status.FAILED
                    return response.status_generic(copy_response.status, copy_response.text)
        finally:
            await clear_target_in_cache(request)
            sub = request.headers.get(SUB, NONE_USER)
            folder_id = 'root' if is_root(key) else encode_key(parent(key))
            request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, None, 'actual'), None)
            request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, id_, 'actual'), None)
            request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, None, 'items'), None)
            request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, id_, 'items'), None)

@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/unarchive')
async def unarchive_file(request: web.Request) -> web.Response:
    """

    :param request:
    :return: a Response object with status 202 Accept

    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        return await awsservicelib.unarchive_object(request=request, activity_cb=publish_desktop_object)
    finally:
        id_ = request.match_info['id']
        volume_id = request.match_info['volume_id']
        bucket_id = request.match_info['bucket_id']
        sub = request.headers.get(SUB, NONE_USER)
        try:
            key: str | None = decode_key(id_)
        except KeyDecodeException:
            return response.status_not_found()
        folder_id = 'root' if is_root(key) else encode_key(parent(key))
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, id_, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, None, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, id_, 'actual'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, None, 'actual'), None)


@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/duplicator')
async def post_file_duplicator(request: web.Request) -> web.Response:
    """
    Posts the provided file for duplication.

    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: The new name of the file and target for duplicating it.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for duplicating it.
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "target",
                        "value": "http://localhost:8080/volumes/666f6f2d6261722d71757578/buckets/my-bucket"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for moving it.
                  value: {
                    "target": "http://localhost:8080/volumes/666f6f2d6261722d71757578/buckets/my-bucket"
                  }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        return await awsservicelib.copy_object(request, activity_cb=publish_desktop_object)
    finally:
        await clear_target_in_cache(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/mover')
@action(name='heaserver-awss3files-file-move-form')
async def get_file_mover(request: web.Request) -> web.Response:
    """
    Gets a form template for moving the requested file.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested file was not found.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file_move_template(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/archive')
@action(name='heaserver-awss3files-file-archive-form')
async def get_file_archive(request: web.Request) -> web.Response:
    """
    Gets a form template for archiving the requested file.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested file was not found.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file_move_template(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/unarchive')
@action(name='heaserver-awss3files-file-unarchive-form')
async def get_file_unarchive_form(request: web.Request) -> web.Response:
    """
    Gets a form template for unarchiving the requested file.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested file was not found.
    ---
    summary: Get a specific file to unarchive.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file_move_template(request)


@routes.put('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/content')
async def put_file_content(request: web.Request) -> web.Response:
    """
    Updates the content of the requested file.
    :param request: the HTTP request. Required.
    :return: a Response object with the value No Content or Not Found.
    ---
    summary: File content
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: File contents.
        required: true
        content:
            application/octet-stream:
                schema:
                    type: string
                    format: binary
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _put_object_content(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/content')
async def get_file_content(request: web.Request) -> web.StreamResponse:
    """
    :param request:
    :return:
    ---
    summary: File content
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_object_content(request)



@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
@action('heaserver-awss3files-file-get-open-choices', rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/opener')
@action(name='heaserver-awss3files-file-get-properties', rel='hea-properties hea-context-menu')
@action(name='heaserver-awss3files-file-duplicate', rel='hea-dynamic-standard hea-icon-duplicator hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/duplicator')
@action(name='heaserver-awss3files-file-move', rel='hea-dynamic-standard hea-icon-mover hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/mover')
@action(name='heaserver-awss3files-file-unarchive', rel='hea-dynamic-standard hea-unarchive hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/unarchive')
@action(name='heaserver-awss3files-file-archive', rel='hea-dynamic-standard hea-archive hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/archive')
@action(name='heaserver-awss3files-file-get-trash', rel='hea-trash hea-context-menu',
        path='volumes/{volume_id}/awss3trash')
@action(name='heaserver-awss3files-file-get-presigned-url', rel='hea-dynamic-clipboard hea-icon-for-clipboard hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/presignedurl')
@action(name='heaserver-awss3files-file-get-versions', rel='hea-versions hea-context-menu', itemif="version is not None",
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/versions/')
@action('heaserver-awss3files-file-get-self', rel='self', path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
@action(name='heaserver-awss3files-file-get-volume', rel='hea-volume', path='volumes/{volume_id}')
@action(name='heaserver-awss3files-file-get-awsaccount', rel='hea-account', path='volumes/{volume_id}/awsaccounts/me')
async def get_file(request: web.Request) -> web.Response:
    """
    Gets the file with the specified id.

    :param request: the HTTP request.
    :return: the requested file or Not Found.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/byname/{name}')
@action('heaserver-awss3files-file-get-self', rel='self', path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
@action(name='heaserver-awss3files-file-get-volume', rel='hea-volume', path='volumes/{volume_id}')
@action(name='heaserver-awss3files-file-get-awsaccount', rel='hea-account', path='volumes/{volume_id}/awsaccounts/me')
async def get_file_by_name(request: web.Request) -> web.Response:
    """
    Gets the file with the specified name.

    :param request: the HTTP request.
    :return: the requested file or Not Found.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/name'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file_by_name(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/')
@action('heaserver-awss3files-file-get-open-choices', rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/opener')
@action(name='heaserver-awss3files-file-get-properties', rel='hea-properties hea-context-menu')
@action(name='heaserver-awss3files-file-duplicate', rel='hea-dynamic-standard hea-icon-duplicator hea-context-menu', path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/duplicator')
@action(name='heaserver-awss3files-file-move', rel='hea-dynamic-standard hea-icon-mover hea-context-menu', path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/mover')
@action(name='heaserver-awss3files-file-unarchive', rel='hea-dynamic-standard hea-unarchive hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/unarchive')
@action(name='heaserver-awss3files-file-archive', rel='hea-dynamic-standard hea-archive hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/archive')
@action(name='heaserver-awss3files-file-get-trash', rel='hea-trash hea-context-menu',
        path='volumes/{volume_id}/awss3trash')
@action(name='heaserver-awss3files-file-get-presigned-url', rel='hea-dynamic-clipboard hea-icon-for-clipboard hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/presignedurl')
@action(name='heaserver-awss3files-file-get-versions', itemif="version is not None", rel='hea-versions hea-context-menu',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/versions/')
@action('heaserver-awss3files-file-get-self', rel='self', path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
async def get_files(request: web.Request) -> web.Response:
    """
    Gets the file with the specified id.

    :param request: the HTTP request.
    :return: the requested file or Not Found.
    ---
    summary: A specific file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_all_files(request)


@routes.route('OPTIONS', '/volumes/{volume_id}/buckets/{bucket_id}/awss3files')
@routes.route('OPTIONS', '/volumes/{volume_id}/buckets/{bucket_id}/awss3files/')
async def get_files_options(request: web.Request) -> web.Response:
    """
    Gets the allowed HTTP methods for a files resource.

    :param request: the HTTP request (required).
    :response: the HTTP response.
    ---
    summary: Allowed HTTP methods.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
    responses:
      '200':
        description: Expected response to a valid request.
        content:
            text/plain:
                schema:
                    type: string
                    example: "200: OK"
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    return await response.get_options(request, ['GET', 'DELETE', 'HEAD', 'OPTIONS', 'POST'])


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions')
@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/')
@action(name='heaserver-awss3files-file-make-current-version', rel='hea-current-version-maker', itemif="not current",
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}/currentmaker')
@action(name='heaserver-awss3files-file-version-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}')
async def get_versions(request: web.Request) -> web.Response:
    """
    Gets all the versions of a file.

    :param request: the HTTP request.
    :return: the requested file or Not Found.
    ---
    summary: A file's versions.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: file_id
          in: path
          required: true
          description: The id of the file.
          schema:
            type: string
          examples:
            example:
              summary: A file id
              value: my-file
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
        file_id = request.match_info['file_id']
    except KeyError as e:
        return response.status_bad_request(str(e))

    try:
        key: str | None = decode_key(file_id)
        if awsservicelib.is_folder(key):
            return response.status_bad_request(f'Object with id {file_id} is not a file')
    except KeyDecodeException:
        return response.status_bad_request(f'Invalid id {file_id}')

    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting {awsservicelib._activity_object_display_name(bucket_name, key)} versions',
                                                activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                versions: list[DesktopObjectDict] = []
                if await awsservicelib.is_versioning_enabled(s3_client, bucket_name):
                    async for aws_version_dict in awsservicelib.list_object_versions(s3_client, bucket_name, key):
                        if aws_version_dict['Key'] == key:
                            version = S3Version()
                            version.id = aws_version_dict['VersionId']
                            version.display_name = f'Version {aws_version_dict["VersionId"]}'
                            version.modified = aws_version_dict['LastModified']
                            version.current = aws_version_dict['IsLatest']
                            version.set_storage_class_from_str(aws_version_dict['StorageClass'])
                            version.version_of_id = file_id
                            versions.append(version.to_dict())
                activity.new_object_id = file_id
                activity.new_object_type_name = AWSS3FileObject.get_type_name()
                activity.new_volume_id = volume_id
                activity.new_object_uri = f'volumes/{volume_id}/buckets/{bucket_name}/awss3files/{file_id}'
                return await response.get_all(request, versions)
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}')
@action(name='heaserver-awss3files-file-make-current-version', rel='hea-current-version-maker', itemif="not current",
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}/currentmaker')
@action(name='heaserver-awss3files-file-version-get-self', rel='self',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}')
async def get_version(request: web.Request) -> web.Response:
    """
    Gets the version with the specified id.

    :param request: the HTTP request.
    :return: the requested version or Not Found.
    ---
    summary: A specific version of a file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: file_id
          in: path
          required: true
          description: The id of the file.
          schema:
            type: string
          examples:
            example:
              summary: A file id
              value: my-file
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
        file_id = request.match_info['file_id']
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))

    try:
        key: str | None = decode_key(file_id)
        if awsservicelib.is_folder(key):
            return response.status_bad_request(f'Object with id {file_id} is not a file')
    except KeyDecodeException:
        return response.status_bad_request(f'Invalid id {file_id}')

    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting {awsservicelib._activity_object_display_name(bucket_name, key)} version {id_}',
                                                activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                if await awsservicelib.is_versioning_enabled(s3_client, bucket_name):
                    async for aws_version_dict in awsservicelib.list_object_versions(s3_client, bucket_name, key):
                        if key == aws_version_dict['Key'] and id_ == aws_version_dict['VersionId']:
                            version = S3Version()
                            version.id = id_
                            version.display_name = f'Version {id_}'
                            version.modified = aws_version_dict['LastModified']
                            version.current = aws_version_dict['IsLatest']
                            version.set_storage_class_from_str(aws_version_dict['StorageClass'])
                            version.version_of_id = file_id
                            activity.new_object_id = file_id
                            activity.new_object_type_name = AWSS3FileObject.get_type_name()
                            activity.new_volume_id = volume_id
                            activity.new_object_uri = f'volumes/{volume_id}/buckets/{bucket_name}/awss3files/{file_id}'
                            return await response.get(request, version.to_dict())
                activity.status = Status.FAILED
                return await response.get(request, None)
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)



@routes.delete('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}')
async def delete_version(request: web.Request) -> web.Response:
    """
    Deletes the version with the specified id.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Version deletion
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: file_id
          in: path
          required: true
          description: The id of the file.
          schema:
            type: string
          examples:
            example:
              summary: A file id
              value: my-file
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_id = request.match_info['file_id']
    id_ = request.match_info['id']
    sub = request.headers.get(SUB, NONE_USER)

    try:
        key = decode_key(file_id)
        if awsservicelib.is_folder(key):
            return response.status_bad_request(f'Object with id {file_id} is not a file')
    except KeyDecodeException:
        return response.status_bad_request(f'Invalid id {file_id}')

    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-delete',
                                                description=f'Deleting {awsservicelib._activity_object_display_name(bucket_name, key)}',
                                                activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                delete_response = s3_client.delete_object(Bucket=bucket_name, Key=key, VersionId=id_)
                if delete_response.get('VersionId'):
                    folder_id = 'root' if is_root(key) else encode_key(parent(key))
                    request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, folder_id, id_, 'items'), None)
                    request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, folder_id, None, 'items'), None)
                    request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, id_, 'actual'), None)
                    request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, None, 'actual'), None)
                    return await response.delete(True)
                else:
                    activity.status = Status.FAILED
                    return await response.delete(False)
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}/currentmaker')
async def make_current_version(request: web.Request) -> web.Response:
    """
    Makes the specified version the current one.

    :param request: the HTTP request.
    :return: the response, with a 201 status code if the current version successfully changed, or a 400 if not. If
    successfully changed, the Location header will be set to the URL of the newly created version.
    ---
    summary: A specific version of a file.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: file_id
          in: path
          required: true
          description: The id of the file.
          schema:
            type: string
          examples:
            example:
              summary: A file id
              value: my-file
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_id = request.match_info['file_id']
    id_ = request.match_info['id']
    sub = request.headers.get(SUB, NONE_USER)

    try:
        key = decode_key(file_id)
        if awsservicelib.is_folder(key):
            return response.status_bad_request(f'Object with id {file_id} is not a file')
    except KeyDecodeException:
        return response.status_bad_request(f'Invalid id {file_id}')

    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-update',
                                                description=f'Making version {id_} of {awsservicelib._activity_object_display_name(bucket_name, key)} the current version',
                                                activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                copy_response = s3_client.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': key, 'VersionId': id_}, Key=key)
                new_version = copy_response.get('VersionId')
                if new_version is None:
                    activity.status = Status.FAILED
                    return response.status_internal_error('Operation failed')
                s3_client.delete_object(Bucket=bucket_name, Key=key, VersionId=id_)
                folder_id = 'root' if is_root(key) else encode_key(parent(key))
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, folder_id, id_, 'items'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, folder_id, None, 'items'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, id_, 'actual'), None)
                request.app[HEA_CACHE].pop((sub, volume_id, bucket_name, None, 'actual'), None)
                return response.status_created(request.app[HEA_COMPONENT],
                                            f'volumes/{volume_id}/buckets/{bucket_name}/awss3files/{file_id}/versions',
                                            new_version)
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


@routes.options('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{file_id}/versions/{id}')
async def get_version_options(request: web.Request) -> web.Response:
    """
    Gets the allowed HTTP methods for a file's versions.

    :param request: the HTTP request (required).
    :response: the HTTP response.
    ---
    summary: Allowed HTTP methods.
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - name: file_id
          in: path
          required: true
          description: The id of the file.
          schema:
            type: string
          examples:
            example:
              summary: A file id
              value: my-bucket
        - $ref: '#/components/parameters/id'

    responses:
      '200':
        description: Expected response to a valid request.
        content:
            text/plain:
                schema:
                    type: string
                    example: "200: OK"
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        volume_id = request.match_info['volume_id']
        bucket_name = request.match_info['bucket_id']
        file_id = request.match_info['file_id']
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))

    s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
    try:
        key: str | None = decode_key(file_id)
        if awsservicelib.is_folder(key):
            return response.status_bad_request(f'Object with id {file_id} is not a file')
    except KeyDecodeException:
        return response.status_bad_request(f'Invalid id {file_id}')

    if await awsservicelib.is_versioning_enabled(s3_client, bucket_name):
        async for aws_version_dict in awsservicelib.list_object_versions(s3_client, bucket_name, key):
            if key == aws_version_dict['Key'] and id_ == aws_version_dict['VersionId']:
                return await response.get_options(request, ['GET', 'DELETE', 'HEAD', 'OPTIONS'])

    return response.status_not_found()


@routes.delete('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}')
async def delete_file(request: web.Request) -> web.Response:
    """
    Deletes the file with the specified id.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: File deletion
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        return await awsservicelib.delete_object(request, activity_cb=publish_desktop_object)
    finally:
        id_ = request.match_info['id']
        volume_id = request.match_info['volume_id']
        bucket_id = request.match_info['bucket_id']
        sub = request.headers.get(SUB, NONE_USER)
        try:
            key: str | None = decode_key(id_)
        except KeyDecodeException:
            return response.status_not_found()
        folder_id = 'root' if is_root(key) else encode_key(parent(key))
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, id_, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, folder_id, None, 'items'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, id_, 'actual'), None)
        request.app[HEA_CACHE].pop((sub, volume_id, bucket_id, None, 'actual'), None)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/opener')
@action('heaserver-awss3files-file-open-default', rel='hea-opener hea-default',
        path='volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/content')
async def get_file_opener(request: web.Request) -> web.Response:
    """
    Opens the requested file.

    :param request: the HTTP request. Required.
    :return: the opened file, or Not Found if the requested file does not exist.
    ---
    summary: File opener choices
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file(request)


@routes.get('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/presignedurl')
@action(name='heaserver-awss3files-file-get-presigned-url-form')
async def get_presigned_url_form(request: web.Request) -> web.Response:
    """
    Returns a template for requesting the generation of a presigned URL.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Presigned url for file
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _get_file(request)


@routes.post('/volumes/{volume_id}/buckets/{bucket_id}/awss3files/{id}/presignedurl')
async def post_presigned_url_form(request: web.Request) -> web.Response:
    """
    Posts a template for requesting the generation of a presigned URL.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Presigned url for file
    tags:
        - heaserver-files-aws-s3
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - name: bucket_id
          in: path
          required: true
          description: The id of the bucket to retrieve.
          schema:
            type: string
          examples:
            example:
              summary: A bucket id
              value: my-bucket
        - $ref: '#/components/parameters/id'
    requestBody:
        description: The expiration time for the presigned URL.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: The expiration time for the presigned URL.
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "link_expiration",
                        "value": 259200
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: The new name of the file and target for moving it.
                  value: {
                    "link_expiration": 259200
                  }
    responses:
      '200':
        $ref: '#/components/responses/200'
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    return await _generate_presigned_url(request)


def main():
    config = init_cmd_line(description='Repository of files in AWS S3 buckets', default_port=8080)
    start(package_name='heaserver-files-aws-s3', db=S3Manager,
          wstl_builder_factory=builder_factory(__package__),
          cleanup_ctx=[publisher_cleanup_context_factory(config)],
          config=config)


async def _get_file(request: web.Request) -> web.Response:
    """
    Gets the requested file. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The file id must be in
    the id entry of the request's match_info dictionary, or the file name must be in the name entry of the request's
    match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response containing a heaobject.data.AWSS3FileObject object in the body.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info and 'name' not in request.match_info:
        return response.status_bad_request('either id or name is required')
    sub = request.headers.get(SUB, NONE_USER)
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id'] if 'id' in request.match_info else request.match_info['name']
    try:
        file_id: str | None = decode_key(file_name)
        if awsservicelib.is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-get',
                                            description=f'Getting {awsservicelib._activity_object_display_name(bucket_name, file_id)}',
                                            activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                logger.debug('About to get file %s', file_id)
                if file_id is None:
                    # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
                    # decide which HTTP status code to respond with (Forbidden vs Not Found).
                    s3_client.head_bucket(Bucket=bucket_name)
                    logger.debug('Returning not found 1')
                    activity.status = Status.FAILED
                    return response.status_not_found()
                loop = asyncio.get_running_loop()
                response_ = await loop.run_in_executor(None, partial(s3_client.list_objects_v2, Bucket=bucket_name,
                                                                     Prefix=file_id, MaxKeys=1,
                                                                     OptionalObjectAttributes=['RestoreStatus']))
                logger.debug('Result of get_file: %s', response_)
                if file_id is None or response_['KeyCount'] == 0:
                    logger.debug('Returning not found 2')
                    activity.status = Status.FAILED
                    return response.status_not_found()
                contents = response_['Contents'][0]
                key = contents['Key']
                encoded_key = encode_key(key)
                display_name = key[key.rfind('/', 1) + 1:]
                logger.debug('Creating file %s', file_id)
                context = S3ObjectPermissionContext(request, volume_id)
                file = await _new_file(s3_client, bucket_name, contents, display_name, key, encoded_key, context)
                activity.new_object_id = file_name
                activity.new_object_type_name = AWSS3FileObject.get_type_name()
                activity.new_volume_id = volume_id
                activity.new_object_uri = f'volumes/{volume_id}/buckets/{bucket_name}/awss3files/{file_name}'

                return await response.get(request, file.to_dict(),
                                          permissions=await file.get_permissions(context),
                                          attribute_permissions=await file.get_all_attribute_permissions(context))
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


async def _new_file(s3: S3Client, bucket_name: str, contents: Mapping[str, Any], display_name: str, key: str, encoded_key: str,
                    context: S3ObjectPermissionContext) -> AWSS3FileObject:
    file = AWSS3FileObject()
    file.id = encoded_key
    file.name = encoded_key
    file.display_name = display_name
    file.modified = contents['LastModified']
    file.created = contents['LastModified']
    file.owner = AWS_USER
    file.mime_type = guess_mime_type(display_name)
    file.size = contents['Size']
    file.storage_class = S3StorageClass[contents['StorageClass']]
    _set_file_source(contents, file)
    file.bucket_id = bucket_name
    file.key = key
    version_dict = await awsservicelib.get_latest_object_version(s3, bucket_name, key)
    file.version = version_dict['VersionId'] if version_dict is not None else None
    object_tagging = await asyncio.get_running_loop().run_in_executor(None, partial(s3.get_object_tagging, Bucket=bucket_name, Key=key))
    tags = []
    for aws_tag in object_tagging.get('TagSet', []):
        tag = Tag()
        tag.key = aws_tag['Key']
        tag.value = aws_tag['Value']
        tags.append(tag)
    file.tags = tags
    file.shares = [await context.get_permissions_as_share(file)]
    return file

def _set_file_source(obj: Mapping[str, Any], item: DesktopObject):
    item.source = None
    item.source_detail = None
    retrieval = obj.get('RestoreStatus')
    if retrieval is not None:
        if (retrieval.get("IsRestoreInProgress")):
            item.source = "AWS S3 (Unarchiving...)"
            item.source_detail = "Typically completes within 12 hours"
        if (retrieval.get("RestoreExpiryDate") is not None):
            item.source = "AWS S3 (Unarchived)"
            temporarily_available_until = retrieval.get("RestoreExpiryDate")
            item.source_detail = f"Available for {naturaldelta(temporarily_available_until - datetime.now(timezone.utc))}"
    if item.source is None:
        s = f'AWS S3 ({S3StorageClass[obj["StorageClass"]].display_name})'
        item.source = s
        item.source_detail = s

async def _get_all_files(request: web.Request) -> web.Response:
    """
    Gets all files in a bucket. The volume id must be in the volume_id entry of the request's
    match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and a Collection+JSON document in the body
    containing any heaobject.data.AWSS3FileObject objects, 403 if access was denied, or 500 if an internal error occurred. The
    body's format depends on the Accept header in the request.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    sub = request.headers.get(SUB, NONE_USER)
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-get',
                                            description=f'Getting all folders in bucket {bucket_name}',
                                            activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3:
            loop = asyncio.get_running_loop()
            try:
                logger.debug('Getting all files from bucket %s', bucket_name)
                files: list[DesktopObjectDict] = []
                permissions: list[list[Permission]] = []
                attribute_permissions: list[dict[str, list[Permission]]] = []
                context = S3ObjectPermissionContext(request, volume_id)
                async for obj in awsservicelib.list_objects(s3, bucket_id=bucket_name, loop=loop,
                                                            include_restore_status=True):
                    key = obj['Key']
                    if not awsservicelib.is_folder(key):
                        encoded_key = encode_key(key)
                        logger.debug('Found file %s in bucket %s', key, bucket_name)
                        display_name = key.split('/')[-1]
                        file = await _new_file(s3, bucket_name, obj, display_name, key, encoded_key, context)
                        permissions.append(await file.get_permissions(context))
                        attribute_permissions.append(await file.get_all_attribute_permissions(context))
                        files.append(file.to_dict())
                activity.new_object_type_name = AWSS3FileObject.get_type_name()
                activity.new_volume_id = volume_id
                activity.new_object_uri = f'volumes/{volume_id}/buckets/{bucket_name}/awss3files/'
                return await response.get_all(request, files,
                                              permissions=permissions,
                                              attribute_permissions=attribute_permissions)
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


async def _get_file_by_name(request: web.Request) -> web.Response:
    """
    Gets the requested file. The volume id must be in the volume_id entry of the request's match_info dictionary.
    The bucket id must be in the bucket_id entry of the request's match_info dictionary. The file name must be in the
    name entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and the heaobject.data.AWSS3FileObject in the body,
    403 if access was denied, 404 if no such file was found, or 500 if an internal error occurred. The body's format
    depends on the Accept header in the request.
    """
    return await _get_file(request)


async def _has_file(request: web.Request) -> web.Response:
    """
    Checks for the existence of the requested file object. The volume id must be in the volume_id entry of the
    request's match_info dictionary. The bucket id must be in the bucket_id entry of the request's match_info
    dictionary. The file id must be in the id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the file exists, 403 if access was denied, or 500 if an
    internal error occurred.
    """
    logger = logging.getLogger(__name__)

    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')

    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']

    s3 = await request.app[HEA_DB].get_client(request, 's3', volume_id)

    try:
        file_id: str | None = decode_key(request.match_info['id'])
        if awsservicelib.is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None
    loop = asyncio.get_running_loop()
    try:
        if file_id is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
        logger.debug('Checking if file %s in bucket %s exists', file_id, bucket_name)
        response_ = await loop.run_in_executor(None, partial(s3.list_objects_v2, Bucket=bucket_name, Prefix=file_id,
                                                             MaxKeys=1))
        if response_['KeyCount'] > 0:
            return response.status_ok()
        return await response.get(request, None)
    except BotoClientError as e:
        return awsservicelib.handle_client_error(e)
    except KeyDecodeException:
        return response.status_not_found()


async def _get_object_content(request: web.Request) -> web.StreamResponse:
    """
    preview object in object explorer
    :param request: the aiohttp Request (required).
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request('volume_id is required')
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request('bucket_id is required')
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id']

    try:
        key: str | None = decode_key(file_name)
        if awsservicelib.is_folder(key):
            key = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        key = None

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-get',
                                            description=f'Getting {awsservicelib._activity_object_display_name(bucket_name, key)} content',
                                            activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            loop = asyncio.get_running_loop()
            try:
                if key is None:
                    # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
                    # decide which HTTP status code to respond with (Forbidden vs Not Found).
                    await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_name))
                    raise response.status_not_found()
                logger.debug('Checking storage class')
                resp = await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_name, Key=key))
                logger.debug('Got response from head_object: %s', resp)
                storage_class = resp.get('StorageClass', S3StorageClass.STANDARD.name)
                if storage_class in (S3StorageClass.DEEP_ARCHIVE.name, S3StorageClass.GLACIER.name) and ((restore := resp.get('Restore')) is None or 'expiry-date' not in restore):
                    return response.status_internal_error(f'Cannot access {awsservicelib._activity_object_display_name(bucket_name, key)} because it is archived in {S3StorageClass[storage_class].display_name}. Unarchive it and try again.')
                etag = resp['ETag'].strip('"')
                last_modified = resp['LastModified']
                if request.if_none_match and ETag(etag) in request.if_none_match:
                    activity.status = Status.FAILED
                    return web.HTTPNotModified()
                if request.if_modified_since and last_modified and request.if_modified_since >= last_modified:
                    activity.status = Status.FAILED
                    return web.HTTPNotModified()
                mode = request.query.get('mode', 'download')
                if mode not in ('download', 'open'):
                    return response.status_bad_request(f'Invalid mode {mode}')
                logger.debug('Getting content of object %s', resp)
                response_ = web.StreamResponse(status=200, reason='OK',
                                               headers={hdrs.CONTENT_DISPOSITION: f'{"attachment" if mode == "download" else "inline"}; filename={key.split("/")[-1]}'})
                mime_type = guess_mime_type(key)
                if mime_type is None:
                    mime_type = 'application/octet-stream'
                response_.content_type = mime_type
                response_.last_modified = last_modified
                response_.content_length = resp['ContentLength']
                response_.etag = ETag(etag)
                await response_.prepare(request)
                async with StreamResponseFileLikeWrapper(response_) as fileobj:
                    logger.debug('After initialize')
                    await loop.run_in_executor(None, s3_client.download_fileobj, bucket_name, key, fileobj)
                logger.debug('Content length is %d bytes', response_.content_length)
                return response_
            except BotoClientError as e:
                raise awsservicelib.handle_client_error(e)


async def _generate_presigned_url(request: web.Request):
    """Generate a presigned URL to share an S3 object

    :param request: the aiohttp Request (required).
    :param volume_id: the id string of the volume representing the user's AWS account.
    :param path_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: HTTP response containing a presigned URL in a heaobject.data.ClipboardData object with status code 200. If
    error, returns 404.

    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
    """
    logger = logging.getLogger(__name__)
    # Generate a presigned URL for the S3 object
    volume_id = request.match_info['volume_id']
    bucket_id = request.match_info['bucket_id']
    object_id = request.match_info['id']
    # three days default for expiration
    try:
        expiration_seconds = await _extract_expiration(await request.json())
    except JSONDecodeError as e:
        return response.status_bad_request(str(e))
    try:
        object_key = decode_key(object_id)
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        return response.status_not_found()

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-update',
                                            description=f'Getting pre-signed URL for {awsservicelib._activity_object_display_name(bucket_id, object_key)}',
                                            activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                loop = asyncio.get_running_loop()
                url = await loop.run_in_executor(None, partial(s3_client.generate_presigned_url, 'get_object',
                                                            Params={'Bucket': bucket_id, 'Key': object_key},
                                                            ExpiresIn=expiration_seconds if expiration_seconds is not None else 259200))
                data = ClipboardData()
                data.mime_type = 'text/plain;encoding=utf-8'
                data.data = url
                data.created = datetime.now()
                f = AWSS3FileObject()
                f.bucket_id = bucket_id
                f.id = object_id
                data.display_name = f'Presigned URL for {f.display_name}'
                return await response.get(request, data.to_dict())
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)



async def _put_object_content(request: web.Request) -> web.Response:
    """
    Upload a file to an S3 bucket. Will fail if the file already exists.
    See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html for more information.

    The following information must be specified in request.match_info:
    volume_id (str): the id of the target volume,
    bucket_id (str): the name of the target bucket,
    id (str): the name of the file.

    :param request: the aiohttp Request (required).
    :return: the HTTP response, with a 204 status code if successful, 400 if one of the above values was not specified,
    403 if uploading access was denied, 404 if the volume or bucket could not be found, or 500 if an internal error
    occurred.
    """
    logger = logging.getLogger(__name__)
    if 'volume_id' not in request.match_info:
        return response.status_bad_request("volume_id is required")
    if 'bucket_id' not in request.match_info:
        return response.status_bad_request("bucket_id is required")
    if 'id' not in request.match_info:
        return response.status_bad_request('id is required')
    volume_id = request.match_info['volume_id']
    bucket_name = request.match_info['bucket_id']
    file_name = request.match_info['id']
    try:
        storage_class = request.query.get('storage_class', 'STANDARD')
    except KeyError:
        return response.status_bad_request(f"Invalid storage_class type")

    try:
        file_id: str | None = decode_key(file_name)
        if awsservicelib.is_folder(file_id):
            file_id = None
    except KeyDecodeException:
        # Let the bucket query happen so that we consistently return Forbidden if the user lacks permissions
        # for the bucket.
        file_id = None

    loop = asyncio.get_running_loop()

    try:
        s3_client = await request.app[HEA_DB].get_client(request, 's3', volume_id)
        if file_id is None:
            # We couldn't decode the file_id, and we need to check if the user can access the bucket in order to
            # decide which HTTP status code to respond with (Forbidden vs Not Found).
            await loop.run_in_executor(None, partial(s3_client.head_bucket, Bucket=bucket_name))
            return response.status_not_found()
    except BotoClientError as e:
        return awsservicelib.handle_client_error(e)

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-update',
                                            description=f'Upload {awsservicelib._activity_object_display_name(bucket_name, file_id)}',
                                            activity_cb=publish_desktop_object) as activity:
        async with S3ClientContext(request=request, volume_id=volume_id) as s3_client:
            try:
                await loop.run_in_executor(None, partial(s3_client.head_object, Bucket=bucket_name, Key=file_id))
                fileobj = RequestFileLikeWrapper(request)
                done = False
                try:
                    fileobj.initialize()

                    p = partial(s3_client.upload_fileobj, Fileobj=fileobj, Bucket=bucket_name, Key=file_id,
                                ExtraArgs={'StorageClass': storage_class})
                    upload_response = await loop.run_in_executor(None, p)
                    logger.info(upload_response)
                    fileobj.close()
                    done = True
                except Exception as e:
                    if not done:
                        try:
                            fileobj.close()
                        except:
                            pass
                        done = True
                        raise e
                return response.status_no_content()
            except BotoClientError as e:
                activity.status = Status.FAILED
                return awsservicelib.handle_client_error(e)


async def _get_file_move_template(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    try:
        return await _get_file(request)
    except KeyDecodeException as e:
        logger.exception('Error getting parent key')
        return response.status_bad_request(f'Error getting parent folder: {e}')


async def _to_aws_tags(hea_tags: list[Tag]) -> list[TagTypeDef]:
    """
    :param hea_tags: HEA tags to converted to aws tags compatible with boto3 api
    :return: aws tags
    """
    aws_tag_dicts: list[TagTypeDef] = []
    for hea_tag in hea_tags:
        if hea_tag.key is None:
            raise ValueError("A tag's key cannot be None")
        if hea_tag.value is None:
            raise ValueError("A tag's value cannot be None")
        aws_tag_dict: TagTypeDef = {
            'Key': hea_tag.key,
            'Value': hea_tag.value
        }
        aws_tag_dicts.append(aws_tag_dict)
    return aws_tag_dicts


async def _extract_expiration(body: dict[str, Any]) -> int:
    """
    Extracts the target URL and expiration time for a presigned URL request. It un-escapes them
    as needed.

    :param body: a Collection+JSON template dict.
    :return: the expiration time in seconds.
    :raises web.HTTPBadRequest: if the given body is invalid.
    """
    try:
        expiration_seconds = next(
            int(item['value']) for item in body['template']['data'] if item['name'] == 'link_expiration')
        return expiration_seconds
    except (KeyError, ValueError, StopIteration) as e:
        raise web.HTTPBadRequest(body=f'Invalid template: {e}') from e
