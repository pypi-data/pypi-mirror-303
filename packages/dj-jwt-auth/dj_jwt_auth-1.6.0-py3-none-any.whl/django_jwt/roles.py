from collections import namedtuple

ROLE = namedtuple("Role", ["name", "is_superuser", "groups", "permissions"], defaults=["", False, [], []])
