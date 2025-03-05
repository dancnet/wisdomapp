== Building ==
1) Have nodejs and python3 installed.
2) Download w3css in wisdom-frontend/src from https://www.w3schools.com/w3css/4/w3.css
3) Build frontend: npm install && npm run build
4) If you are going to use uvicorn for serving static files, create a folder called static in wisdom-backend, copy there build wisdom-frontent. Edit main.py, add:
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="static", html=True), name="site")
5) install python dependencies and run with: uvicorn main:app
== For Docker ==
Follow building steps and ensure you have the files in this manner:
.
├── Dockerfile
├── requirements.txt
└── src
    ├── main.py
    ├── knowledge.sql
    ├── more .py files
    ├── data
    │   └── .keep
    └── static
        ├── assets
        │   └── fonts, js, css...
        ├── index.html
        └── manifest.json

then build: docker build -t wisdomapp .
and create a container: docker run -d -p 8000:8000 -v wisdomapp-data:/wisdomapp/data --name wisdomapp wisdomapp