from enum import Enum

from apps.dashboard.models.FavoriteModel import Favorite
from apps.dashboard.models.HistoryViewModel import HistoryView


class Models(Enum):
    favorite = Favorite
    history_view = HistoryView
