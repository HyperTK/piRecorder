import os
from glob import glob
import picamera
import datetime
import time
import sys

FILEPATH = "/mnt/ssd/"
EXT = '*.h264'
MAX_FILE_COUNT = 108
MOVIE_INTERVAL = 600

def main(now):
    filename = FILE_PATH + now + ".h264"
    file_remove()
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.brightness = 60
        camera.start_recording(output=filename)
        time.sleep(MOVIE_INTERVAL)
        camera.stop_recording()

def file_remove():
    files = glob(FILE_PATH + EXT)
    # check and remove
    if len(files) > MAX_FILE_COUNT:
        files.sort(key=os.path.getmtime, reverse=False)
        os.remove(files[0])

if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    now = dt_now.strftime("%Y-%m-%d_%H-%M-%S")
    main(now)
    print("Recording Stop")
