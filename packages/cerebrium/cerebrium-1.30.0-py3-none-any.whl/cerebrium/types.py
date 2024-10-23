from typing import Literal, TypedDict
from typing import Union, List, Dict, Any

LogLevel = Literal["DEBUG", "INFO", "ERROR", "INTERNAL", "WARNING"]
JSON = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]


class FileData(TypedDict):
    fileName: str
    hash: str
    dateModified: float
    size: int
