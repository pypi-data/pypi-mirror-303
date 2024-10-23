from pydantic import BaseModel, Field

class InputPayload(BaseModel):
    name: str = Field(..., min_length=1, description="The name of the requestor")
    input: str = Field(..., min_length=1, description="The input string to be converted to uppercase")