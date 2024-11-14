from fastapi import APIRouter , Path
from model import todo,todoitem

todo_router = APIRouter()
todo_list = []

# 데이터 추가
@todo_router.post("/todo")
async def add_todo(todo:todo) -> dict:
    todo_list.append(todo)
    return {
            "message": "todo added successfilly"
    }

# 전체 데이터 확인
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
            "todos": todo_list
    }

#개별 데이터 확인 , title은 메타데이터로 동작하는것이다.
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="특정 todo를 확인하기 위한 ID", ge=1,le=1000)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo" : todo
            }
    return {
        "message": "todo with suppied ID doesn't exist" 
        }

# 개별 id 의 item 수정하기(PUT)
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: todoitem, todo_id: int = Path(...,title="변경할 아이템의 id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message" : "todo is update now"
            }
    return {
        "message": "todo with suppied ID doesn't exist"
    }

# 전체 목록 삭제하기
@todo_router.delete("/todo")
async def delete_all_todo(todo:todo) -> dict:
    todo_list.clear()
    return {
            "message": "all todo delete"
    }

# 특정 item 삭제하기
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(...,title="삭제될 아이템의 id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo_list.pop(todo_id)
            return {
                "message" : "this item is delete"
            }
    return {
        "message": "ID doesn't exist"
    }
