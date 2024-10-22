import importlib
from typing import Any, Dict, Type

import msgpack

from dbgpt.core.awel.flow import ResourceCategory, register_resource
from dbgpt.core.interface.serialization import Serializable, Serializer
from dbgpt.util.i18n_utils import _


class MessagePackSerializer(Serializer):
    """A serializer that uses MessagePack for serialization with dynamic object creation."""

    def serialize(self, obj: Serializable) -> bytes:
        """Serialize a cache object using MessagePack.

        Args:
            obj (Serializable): The object to serialize

        Returns:
            bytes: The MessagePack-encoded byte array
        """
        data = obj.to_dict()
        # Add class information to the serialized data
        data["__class__"] = f"{obj.__class__.__module__}.{obj.__class__.__name__}"
        return msgpack.packb(data, use_bin_type=True)

    def deserialize(self, data: bytes, cls: Type[Serializable] = None) -> Serializable:
        """Deserialize MessagePack data back into a cache object of the specified type.

        Args:
            data (bytes): The MessagePack-encoded byte array to deserialize
            cls (Type[Serializable], optional): The type of the object to create.
                                                If None, the type will be determined from the data.

        Returns:
            Serializable: The deserialized object
        """
        # Unpack the MessagePack data to a dictionary
        unpacked_data = msgpack.unpackb(data, raw=False)

        # If cls is not provided, determine the class from the unpacked data
        if cls is None:
            cls = self._get_class(unpacked_data.pop("__class__"))

        # Create an instance of the specified class using the unpacked data
        obj = cls(**{k: v for k, v in unpacked_data.items() if k != "__class__"})
        obj.set_serializer(self)
        return obj

    def _get_class(self, class_path: str) -> Type[Serializable]:
        """Dynamically import and return the class based on its full path.

        Args:
            class_path (str): Full path of the class (e.g., 'module.submodule.ClassName')

        Returns:
            Type[Serializable]: The class type
        """
        module_name, class_name = class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
