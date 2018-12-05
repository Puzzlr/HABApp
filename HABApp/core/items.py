import typing, logging, ujson

import HABApp
from HABApp.util import PrintException
import HABApp.openhab

if typing.TYPE_CHECKING:
    import HABApp.openhab.items

log = logging.getLogger('HABApp.Items')

class Items:
    def __init__(self, parent):
        assert isinstance(parent, HABApp.habapp.Runtime)
        self.runtime = parent

        self.item_state = {}

    def item_exists(self, name):
        return name in self.item_state

    def set_state(self, name, state):

        self.item_state[name] = state

        # try:
        #     self.items[name].update_state( state)
        # except KeyError:
        #     # todo: vll. kann das ja einfach erstellt werden
        #     log.warning( f'Item {name} not in registry ({state})')

    @PrintException
    def set_items(self, data):
        data = ujson.loads(data) # type: list
        for _dict in data:
            #print(_dict)
            __item = HABApp.openhab.map_items(_dict['type'], _dict['state'])
            self.item_state[_dict['name']] = __item

        #remove items which are no longer available
        ist = set(self.item_state.keys())
        soll = { k['name'] for k in data}
        for k in ist - soll:
            self.item_state.pop(k)

        log.info( f'Updated all items')