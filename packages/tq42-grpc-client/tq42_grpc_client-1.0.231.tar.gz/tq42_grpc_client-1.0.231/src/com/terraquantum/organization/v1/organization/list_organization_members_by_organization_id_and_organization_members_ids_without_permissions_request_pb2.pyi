from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListOrganizationMembersByOrganizationIdAndOrganizationMembersIdsWithoutPermissionsRequest(_message.Message):
    __slots__ = ("organization_id", "organization_members_ids")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_MEMBERS_IDS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    organization_members_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, organization_id: _Optional[str] = ..., organization_members_ids: _Optional[_Iterable[str]] = ...) -> None: ...
