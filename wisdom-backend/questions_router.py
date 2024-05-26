import pprint
from fastapi import APIRouter, HTTPException
from models import StrictBaseModel
from db import db_open, df

class Question(StrictBaseModel):
    question: str

# /api/questions/
router1 = APIRouter()
@router1.get('/')
async def get_all_questions():
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM questions")
        result = cur.fetchall()
    return result
@router1.get('/{id}')
async def get_question(id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM questions WHERE id=?", (id,))
        result = cur.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Node not found.")
    return result
@router1.put('/{id}')
async def update_node(id: int, item: Question):
    columns_placeholders, values = df(item.dict()).update_statement
    with db_open() as (conn, cur):
        cur.execute(f"UPDATE questions SET {columns_placeholders} WHERE id=?", values + (id,))
        conn.commit()
    return {"success": True}
@router1.delete('/{id}')
async def remove_question(id: int):
    with db_open() as (conn, cur):
        cur.execute("DELETE FROM questions WHERE id=?", (id,))
        conn.commit()
    return {"success": True}

# /api/nodes/{node_id}/questions/
router2 = APIRouter()
@router2.get('/')
async def get_questions_node(node_id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM questions WHERE node_id=?", (node_id,))
        result = cur.fetchall()
    return result
@router2.post('/')
async def create_question(node_id: int, item: Question):
    columns, placeholders, values = df({'node_id': node_id, **item.dict()}).insert_statement
    with db_open() as (conn, cur):
        cur.execute(f"INSERT INTO questions ({columns}) VALUES ({placeholders})", values)
        conn.commit()
        lastid = cur.lastrowid
    return {"success": True, "id": lastid}

# /api/mindmaps/{mindmap_id}/questions/
router3 = APIRouter()
@router3.get('/')
async def get_questions_mindmap(mindmap_id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT questions.* FROM questions INNER JOIN nodes ON nodes.id = questions.node_id WHERE mindmap_id = ?", (mindmap_id,))
        result = cur.fetchall()
    return result