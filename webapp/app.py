from dataclasses import dataclass
from typing import List, Optional, Dict

from litestar import Litestar, get, post, put
from litestar.exceptions import NotFoundException


@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: List[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]

STATUS = {
    "value1": False,
    "value2": True
}


def get_todo_by_title(todo_name) -> TodoItem:
    for item in TODO_LIST:
        if item.title == todo_name:
            return item
    raise NotFoundException(detail=f"TODO {todo_name!r} not found")


@get("/")
async def get_list(done: Optional[bool] = None) -> List[TodoItem]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]


@post("/")
async def add_item(data: TodoItem) -> List[TodoItem]:
    TODO_LIST.append(data)
    return TODO_LIST


@put("/{item_title:str}")
async def update_item(item_title: str, data: TodoItem) -> List[TodoItem]:
    todo_item = get_todo_by_title(item_title)
    todo_item.title = data.title
    todo_item.done = data.done
    return TODO_LIST


@get("/status/{key:str}")
async def get_status(key: str) -> bool:
    return STATUS[key]

@get("/post/{key:str}/{value:str}")
async def set_status(key:str, value:str) -> Dict[str,str]:
    if value.strip().lower() == "true":
        STATUS[key] = True
    elif value.strip().lower() == "false":
        STATUS[key] = False
    return STATUS


app = Litestar([get_list, add_item, update_item, get_status, set_status])