FROM nginx:alpine

RUN apk add bash python3 py3-pip yt-dlp ffmpeg
RUN pip install --break-system-packages --no-cache-dir generss

COPY yt2pod.py /
COPY start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
