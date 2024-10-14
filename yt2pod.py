from config import *
import os
import time

HTML_DIR = os.path.join("/usr/share/nginx/html/", NAME)
CACHE_FILE = os.path.join(os.path.expanduser("~"), f".cache/yt-dlp-{NAME}-archive")

# Function to run a shell command
def run_command(command):
    os.system(command)

# Download channel avatar
def download_avatar():
    command = f'yt-dlp {YT_CHANNEL} --write-thumbnail --playlist-items 0 --output {HTML_DIR}/avatar.jpg'
    run_command(command)

# Download audio from YouTube channel
def download_audio():
    command = f'yt-dlp --playlist-end {NUM_EPISODES} --extract-audio --output "{HTML_DIR}/%(title)s.%(ext)s" {YT_CHANNEL} --yes-playlist --download-archive {CACHE_FILE}'
    run_command(command)

# Remove old audio files
def remove_old_files():
    # Find and remove files older than 90 days
    cutoff_time = time.time() - (30 * 24 * 60 * 60)  # 30 days in seconds
    for root, dirs, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith('.opus') or file.endswith('.m4a'):
                file_path = os.path.join(root, file)
                if os.path.getmtime(file_path) < cutoff_time:
                    os.remove(file_path)

# Generate RSS feed
def generate_rss():
    command = f'genRSS --metadata --sort-creation --host http://{HOSTNAME}/ --dirname {HTML_DIR} --out {HTML_DIR}/index.html --image http://${HOSTNAME}/${NAME}/avatar.jpg --title "{DESCRIPTION}" --extensions opus,m4a'
    run_command(command)

# Main function to orchestrate the tasks
def main():
    download_avatar()
    download_audio()
    remove_old_files()
    generate_rss()
    #time.sleep(43200)
    time.sleep(60)

if __name__ == "__main__":
    while 1 > 0:
        main()
