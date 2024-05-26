#!/bin/bash
cd wisdom-backend
venv/bin/uvicorn main:app --reload --uds /tmp/wisdom.sock &
cd ../wisdom-frontend
npm run dev &
sleep infinity