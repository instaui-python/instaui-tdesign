from typing import Any, Optional
from ._base_element import BaseElement


class ConfigProvider(BaseElement):
    def __init__(
        self,
        *,
        global_config: Optional[dict[str, Any]] = None,
    ):
        super().__init__("t-config-provider")
        self.props({"globalConfig": global_config})
