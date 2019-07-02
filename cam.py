import picamera
import datetime
import time
import sys

FILEPATH = "/media/pi/raspi/"
MOVIE_INTERVAL = 600


def main(now):
    filename = FILEPATH + now + ".h264"
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.brightness = 60
        camera.start_recording(output=filename)
        time.sleep(MOVIE_INTERVAL)
        camera.stop_recording()

if __name__ == "__main__":
    dt_now = datetime.datetime.now()
    now = dt_now.strftime("%Y-%m-%d_%H-%M-%S")
    main(now)
    print("Recording Stop")
