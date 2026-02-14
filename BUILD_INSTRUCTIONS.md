# How to Build the APK (Android App)

Since creating an Android APK requires a Linux environment, the easiest way for you to build this app is using **Google Colab** (a free online coding tool from Google).

## Steps

1.  **Download your files**:
    - Download `app.py`, `buildozer.spec`, and `requirements.txt` from this project to your computer.

2.  **Open Google Colab**:
    - Go to [Google Colab](https://colab.research.google.com/).
    - Click "New Notebook".
    - On the left sidebar, click the folder icon ("Files").
    - **Upload** your `app.py`, `requirements.txt` and `buildozer.spec` files.

3.  **Run Build Commands**:
    - Copy and paste the following commands into a code cell in the notebook and run it (click the Play button):

```bash
!pip install buildozer cython==0.29.33
!sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good

# Install Java (required for buildozer)
!apt-get install -y openjdk-8-jdk
!update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

!buildozer init
# (Wait for prompt, then confirm 'y' if asked)

!buildozer android debug
```

4.  **Accept License**:
    - During the build (which takes ~15 mins), it might ask you to accept licenses. Type `y` and Enter in the output box.

5.  **Download APK**:
    - Once finished, verify the `bin` folder in the Files sidebar.
    - You will see a file ending in `.apk`.
    - Right-click it and "Download".

6.  **Install on Phone**:
    - Send the `.apk` file to your Android phone.
    - Open it and allow "Install from unknown sources" if prompted.
    - Enjoy "Dad's Downloader"!
