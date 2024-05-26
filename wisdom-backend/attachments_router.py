from fastapi import APIRouter, HTTPException, File, Form, UploadFile
from fastapi.responses import StreamingResponse
from db import db_open
import io

# /a AND /api/attachments
router1 = APIRouter()
@router1.get('/{id}')
async def get_attachment(id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT mime_type, data FROM attachments WHERE id=?", (id,))
        result = cur.fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Node not found.")
    return StreamingResponse(io.BytesIO(result['data']), media_type=result['mime_type'])
@router1.delete('/{id}')
async def remove_attachment(id: int):
    with db_open() as (conn, cur):
        cur.execute("DELETE FROM attachments WHERE id=?", (id,))
        conn.commit()
    return {"success": True}

# /api/nodes/{node_id}/attachments/
router2 = APIRouter()
@router2.get('/')
async def get_attachments(node_id: int):
    with db_open() as (conn, cur):
        cur.execute("SELECT id, mime_type FROM attachments WHERE node_id=?", (node_id,))
        result = cur.fetchall()
    return result

@router2.post('/')
async def create_attachment(node_id: int, mime_type: str = Form(...), file: UploadFile = File(...)):
    contents = await file.read()
    with db_open() as (conn, cur):
        cur.execute(f"INSERT INTO attachments (node_id, data, mime_type) VALUES (?, ?, ?)", (node_id, contents, mime_type))
        conn.commit()
        lastid = cur.lastrowid
    return {"success": True, "id": lastid}