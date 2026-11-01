"""A parcel is just a package with a random delivery time."""
import random
from dataclasses import dataclass, field

_next_id = 0


def _make_id():
    global _next_id
    _next_id += 1
    return _next_id - 1


@dataclass
class Parcel:
    id: int = field(default_factory=_make_id)
    delivery_time: int = field(default_factory=lambda: random.randint(5, 25))
