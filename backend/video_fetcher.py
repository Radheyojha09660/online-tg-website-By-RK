from telegram_client import app

def fetch_videos(limit=50):
    """
    Fetch latest videos from your public Telegram group
    """
    videos = []
    with app:
        messages = app.get_chat_history("@YOUR_PUBLIC_GROUP", limit=limit)
        for msg in messages:
            if msg.video:
                # Folder logic based on hashtags in caption
                caption = msg.caption or ""
                main_folder = "General"
                sub_folder = "General"
                if "#" in caption:
                    parts = caption.split("#")
                    if len(parts) > 1:
                        main_folder = parts[1].split()[0]

                videos.append({
                    "message_id": msg.message_id,
                    "file_id": msg.video.file_id,
                    "caption": caption,
                    "main_folder": main_folder,
                    "sub_folder": sub_folder
                })
    return videos
