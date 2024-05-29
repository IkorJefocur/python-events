from .events import Events


class EventSlotListener:
    def __init__(self, event_slot):
        self.__slot__ = event_slot

    def __repr__(self):
        return repr(self.__slot__) + ' listener'

    def __iadd__(self, f):
        self.__slot__ += f
        return self

    def __isub__(self, f):
        self.__slot__ -= f
        return self


def events_listeners(events):
    for slot in events:
        yield EventSlotListener(slot)


def events_and_listeners(*args, **kwargs):
    events = Events(*args, **kwargs)
    yield events
    yield from events_listeners(events)