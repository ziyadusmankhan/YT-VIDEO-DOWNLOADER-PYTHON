from yt_dlp import YoutubeDL




url = input("Enter YouTube URL: ")

print("\nChoose Quality:")
print("1. 1080p")
print("2. 1440p (2K)")
print("3. 4K")

choice = input("Enter your choice: ")

# Quality selection
if choice == "1":
    video_format = "bv*[height<=1080]+ba/b"
    output_format = "mp4"


elif choice == "2":
    video_format = "bv*[height<=1440]+ba/b"
    output_format = "mkv"

elif choice == "3":
    video_format = "bv*[height<=2160]+ba/b"
    output_format = "mkv"

else:
    print("Invalid choice!")
    exit()

# yt-dlp options
ydl_opts = {
    'format': video_format,
    'merge_output_format': output_format,
    'outtmpl': '%(title)s.%(ext)s'
}

try:

    print("\nStarting download...\n")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nDownload completed successfully!")

except Exception as e:
    print("\nError:", e)
