import asyncio


def get_all_items(queue: asyncio.Queue):
    """Get all items from the queue without waiting."""
    items = []
    try:
        while True:
            item = queue.get_nowait()
            items.append(item)
    except asyncio.QueueEmpty:
        # Once the queue is empty, get_nowait raises QueueEmpty, and we stop
        pass
    return items
