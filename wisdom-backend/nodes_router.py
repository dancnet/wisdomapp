from fastapi import APIRouter, HTTPException
from models import StrictBaseModel
from attachments_router import router2 as attachments_router
from questions_router import router2 as questions_router
from db import db_open, df

class Node(StrictBaseModel):
    parentid: int
    topic: str = None
    parentid: int = None
    direction: int = None
    expanded: int = None
    markdown: str = None
    background_color: str = None
    text_color: str = None

router1 = APIRouter()
router2 = APIRouter()
router1.include_router(attachments_router, prefix="/{node_id}/attachments", tags=["attachments"])
router1.include_router(questions_router, prefix="/{node_id}/questions", tags=["questions"])

# /api/mindmaps/{mindmap_id}/nodes/
@router2.get('/')
async def get_nodes(mindmap_id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM nodes_short WHERE mindmap_id=?", (mindmap_id,))
        result = cur.fetchall()
    return result

@router2.post('/')
async def create_node(mindmap_id: int, item: Node):
    columns, placeholders, values = df({'mindmap_id': mindmap_id, **item.dict()}).insert_statement
    with db_open() as (conn, cur):
        cur.execute(f"INSERT INTO nodes ({columns}) VALUES ({placeholders})", values)
        conn.commit()
        lastid = cur.lastrowid
    return {"success": True, "id": lastid}

# /api/nodes/
@router1.get('/{id}')
async def get_node(id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM nodes WHERE id=?", (id,))
        result = cur.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Node not found.")
    return result

@router1.put('/{id}')
async def update_node(id: int, item: Node):
    columns_placeholders, values = df(item.dict()).update_statement
    with db_open() as (conn, cur):
        cur.execute(f"UPDATE nodes SET {columns_placeholders} WHERE id=?", values + (id,))
        conn.commit()
    return {"success": True}

@router1.delete('/{id}')
async def delete_node(id: int):
    with db_open() as (conn, cur):
        cur.execute(f"DELETE FROM nodes WHERE id=?", (id,))
        conn.commit()
    return {"success": True}