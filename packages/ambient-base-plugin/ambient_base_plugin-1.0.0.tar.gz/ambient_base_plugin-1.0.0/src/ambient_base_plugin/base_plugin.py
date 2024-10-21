from abc import ABC, abstractmethod
from logging import Logger
from typing import Any, Union

from ambient_base_plugin.models.configuration import ConfigPayload
from ambient_base_plugin.models.message import Message


class BasePlugin(ABC):
    @abstractmethod
    async def configure(
        self, config: ConfigPayload, logger: Union[Logger, Any] = None
    ) -> None:
        pass

    @abstractmethod
    async def handle_event(self, message: Message) -> None:
        pass
