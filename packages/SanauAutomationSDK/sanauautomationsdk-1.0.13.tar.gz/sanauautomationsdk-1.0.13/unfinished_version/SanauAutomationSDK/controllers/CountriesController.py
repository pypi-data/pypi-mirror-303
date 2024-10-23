from .BaseController import BaseController
from ..database.models.Country import Country


class CountriesController(BaseController):

    def __init__(self, db):
        super().__init__(model=Country(db=db))

    # TODO: сделать качественное кэширование для меньшего количества запросов
    # def get_and_cache(self, **kwargs):
    #     ref_key = kwargs.get('ref_key', None)
    #
    #     if not ref_key:
    #         return None
    #
    #     if not hasattr(self, 'country_cache'):
    #         self.country_cache = {}
    #
    #     if ref_key not in self.country_cache:
    #         result = super().get_by(**kwargs)
    #
    #     return self.country_cache[ref_key]
