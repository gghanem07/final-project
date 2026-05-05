"""
Calculation Schemas Module
"""

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, model_validator, field_validator
from typing import List, Optional
from uuid import UUID
from datetime import datetime


class CalculationType(str, Enum):
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"
    DIVISION = "division"


class CalculationBase(BaseModel):
    type: CalculationType = Field(
        ...,
        description="Type of calculation",
        example="addition"
    )

    inputs: List[float] = Field(
        ...,
        description="List of numeric inputs",
        example=[10.5, 3, 2],
        min_items=2
    )

    @field_validator("type", mode="before")
    @classmethod
    def validate_type(cls, v):
        allowed = {e.value for e in CalculationType}
        if not isinstance(v, str) or v.lower() not in allowed:
            raise ValueError(f"Type must be one of: {', '.join(sorted(allowed))}")
        return v.lower()

    @field_validator("inputs", mode="before")
    @classmethod
    def check_inputs_is_list(cls, v):
        if not isinstance(v, list):
            raise ValueError("Input should be a valid list")
        return v

    @model_validator(mode='after')
    def validate_inputs(self):
        if len(self.inputs) < 2:
            raise ValueError("At least two numbers are required")
        if self.type == CalculationType.DIVISION:
            if any(x == 0 for x in self.inputs[1:]):
                raise ValueError("Cannot divide by zero")
        return self

    model_config = ConfigDict(from_attributes=True)


class CalculationCreate(CalculationBase):
    user_id: UUID


class CalculationUpdate(BaseModel):
    inputs: Optional[List[float]] = Field(
        None,
        min_items=2
    )

    @model_validator(mode='after')
    def validate_inputs(self):
        if self.inputs is not None and len(self.inputs) < 2:
            raise ValueError("At least two numbers required")
        return self

    model_config = ConfigDict(from_attributes=True)


class CalculationResponse(CalculationBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    result: float

    # ✅ NEW FIELDS FOR UNDO / REDO
    previous_inputs: Optional[List[float]] = None
    redo_inputs: Optional[List[float]] = None

    model_config = ConfigDict(from_attributes=True)