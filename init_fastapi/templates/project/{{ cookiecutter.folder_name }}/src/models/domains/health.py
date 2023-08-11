from pydantic import BaseModel, Field
from src.models.attributes.health import Health as HealthAttrs


class Status(BaseModel):
    status = Field("OK", alias=HealthAttrs.status)
