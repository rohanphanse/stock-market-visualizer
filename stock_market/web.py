import asyncio
import os
import pty
import subprocess
import sys

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as handle:
        return HTMLResponse(handle.read())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    master_fd, slave_fd = pty.openpty()
    env = os.environ.copy()
    env.setdefault("TERM", "xterm-256color")
    proc = subprocess.Popen(
        [sys.executable, "-m", "stock_market.main"],
        stdin=slave_fd,
        stdout=slave_fd,
        stderr=slave_fd,
        env=env,
        close_fds=True,
    )
    os.close(slave_fd)
    loop = asyncio.get_running_loop()

    async def read_pty():
        try:
            while True:
                data = await loop.run_in_executor(None, os.read, master_fd, 1024)
                if not data:
                    break
                await websocket.send_text(data.decode("utf-8", "ignore"))
        except Exception:
            pass

    async def read_ws():
        try:
            while True:
                data = await websocket.receive_text()
                if data:
                    os.write(master_fd, data.encode())
        except WebSocketDisconnect:
            pass

    tasks = [asyncio.create_task(read_pty()), asyncio.create_task(read_ws())]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()

    if proc.poll() is None:
        proc.terminate()
        try:
            await loop.run_in_executor(None, proc.wait, 2)
        except Exception:
            proc.kill()
    os.close(master_fd)


def main():
    uvicorn.run("stock_market.web:app", host="0.0.0.0", port=8000, log_level="info")
