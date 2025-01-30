from typing import Any, Dict, List
from sqlalchemy import Column, Integer, String
from ..BaseModel import BaseModel

class MeasureUnit(BaseModel):
    """ Table MeasureUnits Database model

    Args:
        BaseModel (ORMClass): Parent class

    Returns:
        MeasureUnit: Instance of model
    """
    __tablename__ = 'measure_unit'
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(512))
    symbol = Column("symbol", String(512))
    
    model_path_name = "measure_unit"

    filter_columns = ["name", "symbol"]
    relationship_names = []
    search_columns = ["name"]
    
    @classmethod
    def property_map(self) -> Dict:
        return {}
    
    @classmethod
    def display_members(cls_) -> List[str]:
        return [
            "id",
            "name",
            "symbol"
        ]
    
    @classmethod
    def rules_for_store(cls_) -> Dict[str, List[Any]]:
        return {
            "name": ["required"],
            "symbol": ["required"]
        }
