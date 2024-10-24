import os
import sys
import hashlib
import glob

from google.protobuf.message import Message
from google.protobuf.json_format import MessageToJson, MessageToDict, ParseDict
from loguru import logger


def dir3(obj, excludes=[], excludes_type=[]):
    ret = []
    for attr in dir(obj):
        if attr.startswith('__') and attr.endswith('__'):
            continue
        if attr.startswith('_'):
            continue

        skip = False
        for pre in excludes:
            if attr.startswith(pre):
                skip = True
                logger.debug(f"skip {attr}")
                break
        if not skip:
            _attr = getattr(obj, attr)
            if type(_attr).__name__ in excludes_type:
                logger.debug(f"skip {attr} {type(_attr).__name__}")
                continue
            # check _attr is a callable object
            if callable(_attr):
                _attr_obj = _attr()
                if hasattr(_attr_obj, "DESCRIPTOR"):
                    schema = MessageToDict(_attr_obj, True)
            else:
                schema = None
            
            ret.append(
                {
                    "name": attr,
                    "type": type(_attr).__name__,
                    "schema": schema
                }
            )
    return ret


class ProtobufLoader(object):
    def __init__(self, proto_path):
        sys.path.append(proto_path)
        self.proto_path = proto_path
        self.proto_files = []
        self.proto_files_dict = {}
        self.modules = {}
        self.schemas = {}
        self._loaded = False

    def load(self):
        """加载 protobuf 文件"""
        if self._loaded:
            return
        for proto in glob.glob(f"{self.proto_path}/*.proto"):
            base_name = os.path.basename(proto)               # 文件名
            self.proto_files.append(base_name)
            self.proto_files_dict[base_name] = self._load_proto(proto)
        self._gen()
        self._load_module()
        self._loaded = True

    def _gen(self):
        """生成 protobuf 的 python 文件"""
        for proto in self.proto_files:
            os.system(f"protoc --python_out={self.proto_path} -I={self.proto_path} {proto}")

    def _load_module(self):
        """加载模块"""
        for proto in self.proto_files:
            base_name = os.path.basename(proto)                 # 文件名
            module_name = base_name.replace(".proto", "_pb2")   # 文件名转模块名
            module = __import__(module_name, globals(), locals(), [], 0)    # 动态导入模块
            self.modules[base_name] = module
            self.schemas[base_name] = dir3(module, excludes=["_"], excludes_type=["module", "int"])

    def _load_proto(self, proto):
        """加载 proto 文件"""
        with open(proto, "rb") as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
        return  {
            "filename": os.path.basename(proto),
            "size": os.stat(proto).st_size,
            "md5": md5,
            "data": data.decode(encoding="utf-8")
        }
    
    def filelist(self):
        """返回当前模块的所有文件"""
        return list(self.proto_files_dict.values())
    
    def create_message(self, proto_file, message_name) -> Message:
        """创建一个消息"""
        module = self.modules[proto_file]
        message = getattr(module, message_name)
        return message()
    
    def encode(self, proto_file, message_name, payload) -> bytes:
        """编码"""
        message = self.create_message(proto_file, message_name)
        ParseDict(payload, message)
        return message.SerializeToString()
    
    def decode(self, proto_file, message_name, payload) -> dict:
        """解码"""
        message = self.create_message(proto_file, message_name)
        message.ParseFromString(payload)
        return MessageToDict(message, use_integers_for_enums=True)