from pydantic import BaseModel

class IsOddResponse(BaseModel):
    is_odd: bool
