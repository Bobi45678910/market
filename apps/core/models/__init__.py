from enum import Enum

from apps.core.models.AreaModel import Area
from apps.core.models.CityModel import City
from apps.core.models.UserModel import User  # noqa: F401


class Models(Enum):
    area = Area
    city = City
