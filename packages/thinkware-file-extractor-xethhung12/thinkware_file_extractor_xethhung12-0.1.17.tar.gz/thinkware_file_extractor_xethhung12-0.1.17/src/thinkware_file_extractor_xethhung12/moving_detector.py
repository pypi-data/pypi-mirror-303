import os
from datetime import datetime, timedelta
from typing import Generator
import cv2
from collections import deque
from numpy.ma.extras import average

from thinkware_file_extractor_xethhung12.utils_tools import mp4view
from thinkware_file_extractor_xethhung12.video_clipping import get_video_time, get_screen_time_on_video

class M():
    def __init__(self, size: int):
        self.size = size
        self.queue = deque([], maxlen=size)

    def move(self):
        if len(self.queue) == self.size:
            self.queue.pop()
        self.queue.appendleft(True)

    def stay(self):
        if len(self.queue) == self.size:
            self.queue.pop()
        self.queue.appendleft(False)

    def is_moving(self)->True:
        return sum(map(lambda x: 1 if x else 0, self.queue)) / self.size > 0.7

    def is_staying(self)->True:
        return not self.is_moving()








def resize_and_show(im):
    # height, width, channel = im.shape
    # cv2.imshow("img", cv2.resize(im, (int(width/5), int(height/5))))
    cv2.imshow("img", im)


def cap_screen(path):
    vidcap = cv2.VideoCapture(path)
    os.makedirs("../../test-data", exist_ok=True)
    p = os.path.abspath("../../test-data")
    fps = vidcap.get(cv2.CAP_PROP_FPS)

    for i in range(10):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES,i * fps * 10)
        success, image = vidcap.read()
        cv2.imwrite(f"{p}/img-{i:02d}.jpg", image)

def image_canny(image):
    height, width,channels = image.shape
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image = cv2.resize(image, (int(width/5), int(height/5)))
    image = cv2.GaussianBlur(image, (3,3),0)
    image = cv2.Canny(image=image, threshold1=100, threshold2=200)
    return image

def extract_ref(img):
    def gen_list_of_clip():
        gap = 40
        def yield_index(range_size, count)->Generator[int, None, None]:
            for i in range(count):
                yield i * range_size + int(range_size / 2)
        listData = list([[i,i+gap, gap, gap+gap, [0,255,0]]for i in yield_index(320, 5)]) \
                   + list([[gap, gap+gap, i, i+gap, [255,0,0]] for i in yield_index(768, 5)]) \
                   + list([[i, i + gap, 3840-gap-gap, 3840-gap, [0,0,255]] for i in yield_index(320, 5)])

        return listData

    imgs=[]
    for y1,y2,x1,x2,rgb in gen_list_of_clip():
        # cv2.imwrite(os.path.join(p2,f"img-00-quoted-{i:02d}.jpg"),img[y1:y2,x1:x2])
        # img = cv2.rectangle(img, (x1,y1), (x2,y2), (rgb`jj[0], rgb[1], rgb[2]), 2)
        temp_img = img[y1:y2,x1:x2]
        imgs.append(temp_img)

    # for index,i in enumerate(imgs):
    #     cv2.imwrite(f"../../test-data/crop/{index:02d}.jpg", image_canny(i))
    return imgs


class MovingDetector:
    def __init__(self):
        self.pre = None

    def digest(self, digest_list):
        if self.pre is None:
            self.pre = digest_list
            return None

        r=[]
        pre_list = self.pre

        def hist_img(img):
            hist_img1 = cv2.calcHist([img],[0],None,[256],[0,256])
            cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
            return hist_img1

        for index, preImg in enumerate(pre_list):
            preImg = image_canny(preImg)
            cv2.imwrite(f"../../test-data/crop/preImg-{index:02d}.jpg", preImg)
            preImgH = hist_img(preImg)
            curImg = image_canny(digest_list[index])
            cv2.imwrite("../../test-data/crop/preImg-{index:02d}.jpg", preImg)
            curImgH = hist_img(curImg)
            v = cv2.compareHist(preImgH, curImgH, cv2.HISTCMP_CORREL)
            r.append(v)


        return r

    def rate(self, data):
        return average(data)

    def moving(self, data, threshold):
        return self.rate(data) < threshold




if __name__ == '__main__':
    p = "/home/xeth/PycharmProjects/xhThinkwareFileExtractor/REC_front_merge.mp4"
    # p = "/home/xeth/PycharmProjects/xhThinkwareFileExtractor/2560.mp4"
    # p = "/home/xeth/PycharmProjects/xhThinkwareFileExtractor/3840.mp4"
    vidcap = cv2.VideoCapture(p)
    width = mp4view(p).get_width()

    print(datetime.now())

    p2 = os.path.abspath("../../test-data")
    p3 = os.path.abspath(f"{p2}/canny")
    os.makedirs(p3, exist_ok=True)

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    detector = MovingDetector()
    i = 0
    car_status = "init"

    change_list = []
    def get_new_rec():
        return {"start": None, "end": None}

    cur_rec = get_new_rec()
    moving = M(6)
    while True:
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i * fps * 10)
        i+=1
        success, image = vidcap.read()
        if not success:
            print("Done")
            break

        h,m,s = get_video_time(vidcap)
        if i % 12 == 0:
            print(f"processing: {h:02d}:{m:02d}:{s:02d}")

        videoTime = get_screen_time_on_video(vidcap, width)
        ii = 0
        while videoTime is None and ii < 20:
            ii+=1
            vidcap.set(cv2.CAP_PROP_POS_FRAMES, i * fps * 10+ii*(fps/3))
            videoTime = get_screen_time_on_video(vidcap, width)

        ref_imgs = extract_ref(image)
        rs = detector.digest(ref_imgs)

        if rs is not None:
            now_moving =True if detector.rate(rs) < 0.995 else False

            if now_moving:
                moving.move()
            else:
                moving.stay()

            if car_status != "moving" and moving.is_moving():
                car_status = "moving"
                cur_rec["start"] = videoTime.as_datetime()
                cur_rec["start_r"] = f"{h:02d}:{m:02d}:{s:02d}"
                print(f"start: {cur_rec['start']} << {h:02d}:{m:02d}:{s:02d}")

            if car_status != "stay" and moving.is_staying():
                car_status = "stay"
                cur_rec["end"] = videoTime.as_datetime()
                cur_rec["end_r"] = f"{h:02d}:{m:02d}:{s:02d}"

                if cur_rec["start"] is not None:
                    change_list.append(cur_rec)
                    print(f"end: {cur_rec['end']} << {h:02d}:{m:02d}:{s:02d}")
                    cur_rec = get_new_rec()
                else:
                    cur_rec = get_new_rec()

    if cur_rec["start"] is not None:
        cur_rec["end"] = videoTime.as_datetime()
        cur_rec["end_r"] = f"{h:02d}:{m:02d}:{s:02d}"
        change_list.append(cur_rec)

    for x in change_list:
        print(x)
    print(datetime.now())


