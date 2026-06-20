# YouTube Video Downloader

A Python-based YouTube Video Downloader that allows users to download videos directly from YouTube in multiple resolutions, including:

* 720p (HD)
* 1080p (Full HD)
* 1440p (2K)
* 2160p (4K)

The application automatically downloads the highest quality audio stream and merges it with the selected video quality using FFmpeg.

## Features

* Download videos using a YouTube URL
* Support for multiple resolutions
* Best available audio quality
* Automatic video/audio merging
* MP4 output format
* Command-line interface
* Fast and lightweight

## Technologies Used

* Python
* yt-dlp
* FFmpeg

## Requirements

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Install FFmpeg

#### macOS (Homebrew)

```bash
brew install ffmpeg
```

Verify installation:

```bash
ffmpeg -version
```

#### Windows

Download FFmpeg from:

https://ffmpeg.org/download.html

Add FFmpeg to your system PATH.

## Usage

Run:

```bash
python main.py
```

Example:

```text
Enter YouTube URL:
https://www.youtube.com/watch?v=example

Select Quality:
1. 720p
2. 1080p
3. 1440p (2K)
4. 2160p (4K)
```

The downloaded video will be saved in the project's Downloads folder (or the directory specified in the code).

## Supported Resolutions

| Resolution | Quality |
| ---------- | ------- |
| 720p       | HD      |
| 1080p      | Full HD |
| 1440p      | 2K      |
| 2160p      | 4K      |

## Project Structure

```text
youtube-downloader/
│
├── main.py
├── requirements.txt
├── README.md
└── Downloads/
```

## Future Improvements

* GUI Interface (Tkinter / PyQt)
* Playlist Download Support
* Download Progress Bar
* Audio-only Downloads (MP3)
* Batch Downloads
* Video Metadata Viewer

## Disclaimer

This project is intended for educational purposes only. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws when downloading content.

## Author

Ziyad Usman Khan
Python Developer
