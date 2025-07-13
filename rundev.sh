#!/bin/bash
cd wisdom-backend
venv/bin/uvicorn main:app --reload --port 8000 &
cd ../wisdom-frontend
npm run dev &
sleep infinity