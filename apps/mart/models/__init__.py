from enum import Enum

from apps.mart.models.AdModel import Ad
from apps.mart.models.CategoryModel import Category
from apps.mart.models.ReviewModel import Review


class Models(Enum):
    category = Category
    ad = Ad
    review = Review
