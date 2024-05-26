# Imports
from fastapi import FastAPI, Query
from mindmaps_router import router as mindmaps_router
from nodes_router import router1 as nodes_router
from attachments_router import router1 as attachments_router
from questions_router import router1 as questions_router
from db import db_open

# FastAPI
app = FastAPI(title='Wisdom App API', version='1.0', docs_url='/api/docs', openapi_url='/api/openapi.json')
app.include_router(mindmaps_router, prefix="/api/mindmaps", tags=["mindmaps"])
app.include_router(nodes_router, prefix="/api/nodes", tags=["nodes"])
app.include_router(attachments_router, prefix="/api/attachments", tags=["attachments"])
app.include_router(attachments_router, prefix="/a", tags=["attachments"])
app.include_router(questions_router, prefix="/api/questions", tags=["questions"])
@app.get('/api/search')
async def search(query: str = Query()):
    with db_open() as (conn, cur):
        cur.execute("SELECT * FROM nodes WHERE topic LIKE ? OR markdown LIKE ?;", (f'%{query}%', f'%{query}%'))
        result = cur.fetchall()
    return result