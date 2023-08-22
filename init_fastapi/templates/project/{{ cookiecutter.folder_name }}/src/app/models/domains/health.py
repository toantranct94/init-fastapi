from pydantic import BaseModel, Field
from app.models.attributes.health import Health as HealthAttrs


class Status(BaseModel):
    status: str = Field("OK", alias=HealthAttrs.status)
