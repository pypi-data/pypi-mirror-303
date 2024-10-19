from .bytebuffer import ByteBuffer
from .struct import JceStruct
from .stream import JceInputStream


def jce_to_json(_data):
    """将 Jce 数据转换为 JSON 格式"""
    _stream = JceInputStream(_data)
    jce = JceStruct()
    jce.read_from(_stream)
    return jce.to_json()
