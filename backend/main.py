from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO

from video_fetcher import fetch_videos
from telegram_client import app

api = FastAPI(title="Online TG Video API")

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
def home():
    return {"status": "Backend running"}

@api.get("/videos")
def get_videos(limit: int = 50):
    videos = fetch_videos(limit)
    foldered_videos = {}
    for v in videos:
        main = v["main_folder"]
        foldered_videos.setdefault(main, []).append(v)
    return foldered_videos

@api.get("/video/{file_id}")
async def get_video(file_id: str):
    try:
        async with app:
            file = await app.get_file(file_id)
            data = await app.download_media(file.file_id, file_name=None)
            return StreamingResponse(BytesIO(data), media_type="video/mp4")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
