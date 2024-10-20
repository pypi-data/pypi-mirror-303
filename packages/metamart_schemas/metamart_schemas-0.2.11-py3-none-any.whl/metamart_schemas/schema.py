from typing import Dict, Literal, Union

from metamart_schemas.base import MetamartType
from metamart_schemas.generics import MetamartBaseModel


class Schema(MetamartBaseModel):
    """Class definition of Schema

    Attributes:
        entity: A Metamart object

    """

    entity: MetamartType

    @classmethod
    def to_model(cls, item: Dict, version: Literal["v1"], typing_type: Literal["Node", "Edge"]) -> MetamartType:
        """Convert an item spec to a Metamart object

        Args:
            item: An item spec to be converted to a Metamart object
            version: which version of the schema to use
            typing_type: The type of the object e.g. Node, Edge, etc.

        Returns:
            The Metamart object

        Raises:

        """
        result = {
            "type": typing_type,
            "version": version,
            "spec": item,
        }
        return cls(entity=result).entity
