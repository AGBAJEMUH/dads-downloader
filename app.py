import streamlit as st
import yt_dlp
import os

st.title("🎥 Dad's Video Downloader")

url = st.text_input("Paste Link Here (YouTube, Facebook, etc.):")

if st.button("Step 1: Process Video"):
    if url:
        try:
            with st.spinner("Processing... please wait."):
                # 1. Download settings (saves to a temp file on the server)
                save_name = "downloaded_video.mp4"
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': save_name,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # 2. Read the file into memory so Dad can download it
                with open(save_name, "rb") as f:
                    video_bytes = f.read()

                # 3. Show the final download button
                st.success("Video is ready!")
                st.download_button(
                    label="Step 2: Save to Phone",
                    data=video_bytes,
                    file_name="dad_video.mp4",
                    mime="video/mp4"
                )
                
                # Clean up the server
                os.remove(save_name)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a link first!")
