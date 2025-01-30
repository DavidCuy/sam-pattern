from core_db.BaseService import BaseService
from core_db.models.measure_unit import MeasureUnit


class MeasureUnitService(BaseService):
    def __init__(self) -> None:
        super().__init__(MeasureUnit)