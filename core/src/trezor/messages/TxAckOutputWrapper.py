# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .TxAckOutputType import TxAckOutputType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckOutputWrapper(p.MessageType):

    def __init__(
        self,
        *,
        output: TxAckOutputType,
    ) -> None:
        self.output = output

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            5: ('output', TxAckOutputType, p.FLAG_REQUIRED),
        }