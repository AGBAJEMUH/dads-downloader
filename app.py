import threading
import os
import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.utils import platform

import yt_dlp

class DadsDownloaderApp(App):
    def build(self):
        self.title = "Dad's Video Downloader"
        
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        # Title
        title_label = Label(
            text="🎥 Dad's Video Downloader", 
            font_size=dp(24), 
            bold=True,
            size_hint_y=None, 
            height=dp(50)
        )
        layout.add_widget(title_label)
        
        # Input Label
        input_label = Label(
            text="Paste Link Here:", 
            size_hint_y=None, 
            height=dp(30)
        )
        layout.add_widget(input_label)
        
        # Text Input
        self.url_input = TextInput(
            multiline=False, 
            size_hint_y=None, 
            height=dp(40)
        )
        layout.add_widget(self.url_input)
        
        # Download Button
        self.download_btn = Button(
            text="Download Video", 
            size_hint_y=None, 
            height=dp(50),
            background_color=(0.3, 0.7, 0.3, 1) # Greenish
        )
        self.download_btn.bind(on_press=self.start_download)
        layout.add_widget(self.download_btn)
        
        # Status Label
        self.status_label = Label(
            text="Ready", 
            color=(0.7, 0.7, 0.7, 1)
        )
        layout.add_widget(self.status_label)
        
        return layout

    def start_download(self, instance):
        url = self.url_input.text
        if not url:
            self.status_label.text = "Error: Please enter a URL"
            return

        self.status_label.text = "Processing..."
        self.download_btn.disabled = True
        
        # Request Android Permissions if needed
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

        # Run in thread
        threading.Thread(target=self.run_download, args=(url,), daemon=True).start()

    def run_download(self, url):
        try:
            # On Android, we should save to a visible folder
            # For this simple example, we'll try to save to the app's storage or generic storage
            # But standard yt-dlp might struggle with scoped storage without extra config.
            # We'll stick to basic implementation and refine if needed.
            
            # Use a generic path or current directory
            out_tmpl = '%(title)s.%(ext)s'
            if platform == 'android':
                from android.storage import primary_external_storage_path
                dir_path = primary_external_storage_path()
                download_dir = os.path.join(dir_path, 'Download')
                if not os.path.exists(download_dir):
                     # Try to create or fallback
                     pass 
                out_tmpl = os.path.join(download_dir, '%(title)s.%(ext)s')

            ydl_opts = {
                'format': 'best',
                'outtmpl': out_tmpl,
                # 'noplaylist': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get('title', 'video')

            Clock.schedule_once(lambda dt: self.update_status(f"Finished: {video_title}", success=True))
            
        except Exception as e:
            Clock.schedule_once(lambda dt: self.update_status(f"Error: {str(e)}", success=False))

    def update_status(self, message, success=True):
        self.status_label.text = message
        if success:
            self.status_label.color = (0, 1, 0, 1)
            self.url_input.text = "" # Clear input
        else:
            self.status_label.color = (1, 0, 0, 1)
        
        self.download_btn.disabled = False

if __name__ == "__main__":
    DadsDownloaderApp().run()
