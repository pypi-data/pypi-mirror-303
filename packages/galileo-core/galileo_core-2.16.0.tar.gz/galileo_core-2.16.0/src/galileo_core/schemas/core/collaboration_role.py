from enum import Enum


class CollaboratorRole(str, Enum):
    owner = "owner"
    viewer = "viewer"
