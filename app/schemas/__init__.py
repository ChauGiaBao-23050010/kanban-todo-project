"""Schemas package: expose schema modules and resolve forward refs."""

from .user import *
from .board import *
from .task import *

# Resolve forward references if needed
try:
    BoardWithTasks.update_forward_refs()
except Exception:
    pass
