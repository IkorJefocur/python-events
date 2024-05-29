from asyncio import run_coroutine_threadsafe


def run_coroutine(coro, loop):
    run_coroutine_threadsafe(coro, loop) \
        .add_done_callback(propagate_future_exception)

def propagate_future_exception(future):
    if future.exception():
        raise future.exception()