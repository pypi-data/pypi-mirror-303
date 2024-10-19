"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MessageContainer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text
        value: typing.Text
        def __init__(self,
            *,
            key: typing.Text = ...,
            value: typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    METADATA_FIELD_NUMBER: builtins.int
    GRPC_MESSAGE_NAME_FIELD_NUMBER: builtins.int
    GRPC_MESSAGE_CONTENT_FIELD_NUMBER: builtins.int
    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    grpc_message_name: typing.Text
    grpc_message_content: builtins.bytes
    def __init__(self,
        *,
        metadata: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        grpc_message_name: typing.Text = ...,
        grpc_message_content: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["grpc_message_content",b"grpc_message_content","grpc_message_name",b"grpc_message_name","metadata",b"metadata"]) -> None: ...
global___MessageContainer = MessageContainer
