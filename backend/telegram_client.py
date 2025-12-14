from pyrogram import Client
import os

api_id = 26704085         # aapka API ID
api_hash = "f150646c78f09b4f88bef191a22539c0"  # aapka API HASH

# Session name
app = Client(
    "session_by_rk",
    api_id=api_id,
    api_hash=api_hash
)
