from fastapi import APIRouter, HTTPException
from models import StrictBaseModel
from db import db_open, df
from nodes_router import router2 as nodes_router
from questions_router import router3 as questions_router

router = APIRouter()
router.include_router(nodes_router, prefix="/{mindmap_id}/nodes", tags=["nodes"])
router.include_router(questions_router, prefix="/{mindmap_id}/questions", tags=["questions"])

class Mindmap(StrictBaseModel):
    name: str

@router.get('/')
async def get_mindmaps():
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM mindmaps")
        result = cur.fetchall()
    return result
@router.get('/{id}')
async def get_mindmap(id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM mindmaps WHERE id=?", (id,))
        result = cur.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Node not found.")
    return result
@router.post('/')
async def create_mindmap(item: Mindmap):
    columns, placeholders, values = df(item.dict()).insert_statement
    with db_open() as (conn, cur):
        cur.execute(f"INSERT INTO mindmaps ({columns}) VALUES ({placeholders})", values)
        lastid = cur.lastrowid
        cur.execute(f"INSERT INTO nodes (topic, mindmap_id, isroot) VALUES (?,?, 1)", (item.name, lastid))
        conn.commit()
    return {"success": True, "id": lastid}
@router.put('/{id}')
async def update_mindmap(id: int, item: Mindmap):
    columns_placeholders, values = df(item.dict()).update_statement
    with db_open() as (conn, cur):
        cur.execute(f"UPDATE mindmaps SET {columns_placeholders} WHERE id=?", values + (id,))
        conn.commit()
    return {"success": True}
@router.delete('/{id}')
async def remove_mindmap(id: int):
    with db_open() as (conn, cur):
        cur.execute("DELETE FROM mindmaps WHERE id=?", (id,))
        conn.commit()
    return {"success": True}