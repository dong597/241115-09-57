from pydantic import BaseModel
from typing import List
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

# todo_list의 item만 리턴하기 위한 모델
class todoitems(BaseModel):
    todos: List[todoitem]  # 여러 개의 todoitem을 리스트로 저장

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "첫번째 아이템"
                    },
                    {
                        "item": "두번째 아이템"
                    }
                ]
            }
        }