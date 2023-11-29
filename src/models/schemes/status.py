from pydantic import BaseModel, Field


class StatusSchema(BaseModel):
    id: int = Field(primary_key=True, nullable=False)
    name: str = Field(title="StatusName")

    class Config:
        from_attributes = True
