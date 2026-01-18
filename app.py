import streamlit as st
import yt_dlp
import os
import re

# Function to make the filename safe for phones
def clean_filename(title):
    return re.sub(r'[^a-zA-Z0-9 ]', '', title)

st.title("🎥 Dad's Video Downloader")
url = st.text_input("Paste Link Here:")

if st.button("Step 1: Process Video"):
    if url:
        try:
            with st.spinner("Processing..."):
                temp_file = "temp_video.mp4"
                ydl_opts = {'format': 'best', 'outtmpl': temp_file}

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_title = info.get('title', 'video')
                    ydl.download([url])
                
                with open(temp_file, "rb") as f:
                    video_bytes = f.read()

                st.success(f"Ready: {video_title}")
                st.download_button(
                    label="Step 2: Save to Phone",
                    data=video_bytes,
                    file_name=f"{clean_filename(video_title)}.mp4",
                    mime="video/mp4"
                )
                os.remove(temp_file)
        except Exception as e:
            st.error(f"Error: {e}")
