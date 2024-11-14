from pydantic import BaseModel

class todo(BaseModel):
    id : int
    item : str

    class Config:
        json_schema_extra = {
                "example": {
                    "id": 1,
                    "item": "Example schema"
                }
        }

#todo 의 아이템을 변경하기 위한 모델
class todoitem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
                "example": {
                    "item": "변경할 아이템 작성"
                }
        }