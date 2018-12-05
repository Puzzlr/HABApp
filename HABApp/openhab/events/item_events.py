from .map_events import map_events
from .base_event import BaseItemEvent


class ItemStateEvent(BaseItemEvent):
    def __init__(self, _in_dict):
        super().__init__(_in_dict)

        # smarthome/items/NAME/state
        self.item  = self._topic[16:-6]
        self.value = map_events(self._payload['type'], self._payload['value'])

    def __repr__(self):
        return f'<{self.__class__.__name__} item: {self.item}, value: {self.value}>'

class ItemStateChangedEvent(BaseItemEvent):
    def __init__(self, _in_dict):
        super().__init__(_in_dict)

        # smarthome/items/Ping/statechanged
        self.item = self._topic[16:-13]
        self.value = map_events(self._payload['type'], self._payload['value'])
        self.old_value = map_events(self._payload['oldType'], self._payload['oldValue'])

    def __repr__(self):
        return f'<{self.__class__.__name__} item: {self.item}, value: {self.value}, old_value: {self.old_value}>'


class ItemCommandEvent(BaseItemEvent):
    def __init__(self, _in_dict):
        super().__init__(_in_dict)

        # smarthome/items/NAME/command
        self.item = self._topic[16:-8]
        self.value = map_events(self._payload['type'], self._payload['value'])

    def __repr__(self):
        return f'<{self.__class__.__name__} item: {self.item}, value: {self.value}>'



class ItemAddedEvent(BaseItemEvent):
    def __init__(self, _in_dict):
        super().__init__(_in_dict)

        self.item = self._payload['name']
        self.type = self._payload['type']


class ItemUpdatedEvent(BaseItemEvent):
    def __init__(self, _in_dict):
        super().__init__(_in_dict)

        # smarthome/items/NAME/updated
        self.item = self._topic[16:-8]