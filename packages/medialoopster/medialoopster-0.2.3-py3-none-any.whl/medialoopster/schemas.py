from __future__ import annotations

from typing import List, Dict
from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Production(BaseModel):
    id: int
    company: str
    can_write: bool
    can_delete_assets: bool
    name: str
    codename: str
    storage_root: str
    san_mount: str
    proxy_root: str
    proxy_url: str
    export_type: str
    default_approval_status: int
    direct_attached_site: int
    upload_device: int
    audioasset_device: int
    imageasset_device: int
    videoasset_device: int
    projectasset_device: int | None = None
    network_attached_site: List[int]
    members: List
    member_groups: List[int]


class MetaFieldStore(BaseModel):
    pass


class VideoAsset(BaseModel):
    id: int
    name: str
    description: str
    date_crt: datetime | None
    date_add: datetime
    date_mod: datetime
    date_del: datetime | None
    locked_by: str | None = None
    production: int
    production_name: str
    meta_field_store: Dict
    status_asset: int
    status_asset_description: str
    status_editing: int
    status_approval: int
    path_file: str
    is_archive: bool
    is_production: bool
    device: int
    display_name: str
    filename: str
    projects: List
    path_proxy: str
    name_proxy: str
    thumbnail_url: str
    proxy_url: str
    shared_with_productions: List
    is_available: bool
    name_editor: str
    video_format: str
    video_codec: str
    video_size: str
    aspect_ratio: str
    duration: int
    offset_frames: int
    fps: str
    abstract: str
    transcript: str
    width: int
    height: int
    codec_name: str
    display_aspect_ratio: str
    vpms_title: str
    vpms_description: str
    path_thumbnail: str
    is_proxy_available: bool
    video_url: str
    rotation: int
    poster_url: str


class Shot(BaseModel):
    name: str
    description: str | None = None
    timecode_start: int  # ms
    timecode_end: int  # ms
    duration: int  # ms
    id: int
    asset: int
    licensor: str | None = None
    license: str | None = None
    location_city: str | None = None
    copyright: str | None = None
    ancestor: str | None = None
    keywords: List[str] = []
    path_thumbnail: str
    is_compositing: bool
    thumbnail_url: HttpUrl


class Sequence(BaseModel):
    name: str
    description: str | None = None
    timecode_start: int  # ms
    timecode_end: int  # ms
    duration: int  # ms
    keywords: List[str] = []
    asset: int
    shots: List[Shot]
