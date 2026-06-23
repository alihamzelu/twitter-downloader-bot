import os
import yt_dlp

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)

DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_video(link, quality, output_path="downloads/%(id)s.%(ext)s"):
    meta_opts = {
        "format": f"bestvideo[height<={quality}]+bestaudio/best",
        "quiet": True,
        "noproxy": True
    }

    with yt_dlp.YoutubeDL(meta_opts) as ydl:
        info = ydl.extract_info(link, download=False)
        file_size_bytes = info.get('filesize') or info.get('filesize_approx')
        
        if file_size_bytes:
            file_size_mb = file_size_bytes / (1024 * 1024)
            if file_size_mb > 300:
                raise ValueError(f"File size exceeds the 300MB limit ({file_size_mb:.1f}MB).")

    ydl_opts = {
        "outtmpl": output_path,
        "format": f"bestvideo[height<={quality}]+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "noproxy": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info)

    return filename