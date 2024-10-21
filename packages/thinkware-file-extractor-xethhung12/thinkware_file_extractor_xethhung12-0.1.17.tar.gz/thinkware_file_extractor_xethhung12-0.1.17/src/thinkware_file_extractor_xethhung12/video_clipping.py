import os
import re
import sys
from datetime import datetime
from typing import Union

import cv2
from pyasn1.type.char import VideotexString
from pytesseract import pytesseract
from dataclasses import dataclass

from thinkware_file_extractor_xethhung12.utils_tools import mp4view


def time_str_second(time_str)->int:
    matcher = re.match("(\d{2}):(\d{2}):(\d{2})",time_str)
    if matcher is None:
        raise ValueError(f"time string should be with format HH:mm:ss, but `{time_str}` provided")

    hh = int(matcher[1])
    mm = int(matcher[2])
    ss = int(matcher[3])

    return hh*3600+mm*60+ss


def jump_to_time(vidcap, time_str):
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, time_str_second(time_str)*fps)


def clip_screen_at(vidcap, time_str)->tuple[bool, cv2.typing.MatLike]:
    jump_to_time(vidcap, time_str)
    return vidcap.read()


def get_screen_time_on_video(vidcap, width) -> Union[None, "VideoClipping"]:
    start_row = 1400 if width == 2560 else 2125
    end_row = 1430 if width == 2560 else 2150
    start_col = 430 if width == 2560 else 430
    end_col = 600 if width == 2560 else 610
    success, image = vidcap.read()
    if success:
        time_image = image[start_row:end_row, start_col:end_col]
        gray_time_image = cv2.cvtColor(time_image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray_time_image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        im2 = gray_time_image.copy()
        for cnt in contours:

            x, y, w, h = cv2.boundingRect(cnt)
            cropped = im2[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)
            text = text if not text.endswith('\x0c') else text[0:-1]
            text = text if not text.endswith('\n') else text[0:-1]
            res = re.match("\d{4}\.\d{2}\.\d{2} \d{2}:\d{2}:\d{2}", text)
            if res is not None:
                h, m, s = get_video_time(vidcap)
                return VideoClipping(
                    text[0:10].replace(".", "-"),
                    text[11:13],
                    text[14:16],
                    text[17:19],
                    f"{h:02d}:{m:02d}:{s:02d}"
                )
            else:
                continue
    else:
        return None

    return None


def get_screen_time_on_video_by_time_str(vidcap, width, time_str):
    second = time_str_second(time_str)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    for i in range(0,fps):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, second * fps+i)
        res = get_screen_time_on_video(vidcap, width)
        if res is not None:
            return res
        else:
            continue
    raise ValueError(f"There is not time found in the video clip")


def get_video_time(vidcap):
    sec = int(vidcap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
    h = int(sec / 3600) % 3600
    m = int(sec / 60) % 60
    s = sec % 60

    return h, m, s


@dataclass
class VideoClipping:
    date: str
    hour: str
    minute: str
    second: str
    corresponding_timestamp: str

    def full_time_str(self):
        return f"{self.date} {self.hour}:{self.minute}:{self.second}"

    def as_datetime(self):
        return datetime.strptime(f"{self.date} {self.hour}:{self.minute}:{self.second}", "%Y-%m-%d %H:%M:%S")

def extract_time_list(p)->list[VideoClipping]:

    width = mp4view(p).get_width()
    if width not in [2560, 3840]:
        raise ValueError(f"width should be 2560 or 3840, but {width} provided")

    l = []
    vidcap = cv2.VideoCapture(p)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    fc = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    i = 0
    index=0
    pc = None
    while True:
        index+=1
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        res = get_screen_time_on_video(vidcap, width)


        if res is not None:
            l.append(res)

        i += (fps * 30)
        if pc is None or (not int(i/fc*100) == pc):
            pc = int(i/fc*100)
            sys.stderr.write(f"{i}/{fc} - {pc} %\n")

        if i > fc:
            break


    return l
