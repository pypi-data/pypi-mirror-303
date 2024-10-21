import logging

logger = logging.getLogger(__name__)


class StationRegistry:
    def __init__(self):
        self.publishers: list = []
        self.updater_handlers: list = []
        self.kafka_updater_handlers: dict = {}
        self.periodic_updaters = None

    def set_publishers(self, publishers: list) -> None:
        self.publishers = publishers

    def set_updater_handlers(self, handlers: list) -> None:
        self.updater_handlers = handlers

    def set_kafka_updater_handlers(
        self, handlers: dict
    ) -> None:  # topic_name -> UpdaterHandler
        self.kafka_updater_handlers = handlers

    def set_periodic_updaters(self, updaters):
        self.periodic_updaters = updaters


station_registry = StationRegistry()
