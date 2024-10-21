import json
import os
import sys
from xml.etree.ElementTree import indent

import yaml

is_debug = True if os.environ.get("dev", default='false') == "true" else False

width_for_4k="3840"
width_for_2k="2560"

def get_scale(val) -> str:
  if val == width_for_4k:
    return "940"
  elif val == width_for_2k:
    return "740"
  else:
    return "UNKNOWN"

def  get_x(val) -> str:
  if val == width_for_4k:
    return "420"
  elif val == width_for_2k:
    return "350"
  else:
    return "UNKNOWN"

def get_y(val) -> str:
  if val == width_for_4k:
    return "1500"
  elif val == width_for_2k:
    return "980"
  else:
    return "UNKNOWN"


class MP4View:
  def __init__(self, map):
    self.map = map

  def get_width(self)->int:
    return self.map["width"]

  def get_height(self)->int:
    return self.map["height"]

  def get_codec(self)->str:
    return self.map["codec_name"]

  def get_codec_long_name(self)->str:
    return self.map["codec_long_name"]

def mp4view(f_name)->MP4View:
  abs_file_name = str(os.path.abspath(f_name))
  cmd = f"ffprobe -v error -select_streams v -show_streams -of json {abs_file_name}"
  out = os.popen(cmd).read()
  d = json.loads(out)
  return MP4View(d["streams"][0])


def target_file(path, prefix, mode) -> [str]:
    path = os.path.abspath(path)
    f = []
    for (_, _, files) in os.walk(path):
        for filename in files:
            if filename.startswith(prefix) and filename.endswith(mode + ".MP4"):
                f.append(filename)
    return f


def target_file_count(path, prefix, mode) -> int:
    return len(target_file(path, prefix, mode))


def has_target_file(path, prefix, mode) -> bool:
    return target_file_count(path, prefix, mode) > 0


def cal_size(size)->str:
    if size > 1024:
        if size > 1024 * 1024:
            if size > 1024 * 1024 * 1024:
                return f"{size / (1024 * 1024):.2f} GB"
            else:
                return f"{size / (1024*1024):.2f} MB"
        else:
            return f"{size/1024:.2f} KB"
    else:
        return f"{size} bytes"


def summary(path):
    path=str(os.path.abspath(path))
    dList = ["cont_rec","evt_rec","manual_rec","motion_timelapse_rec","parking_rec"]
    d = {}
    for dir in os.listdir(path):
        if dir in dList:
            d.update({
                dir: {
                    "name": dir,
                    "path": str(os.path.abspath(os.path.join(path, dir))),
                    "size": 0,
                    "file_count": 0,
                    "dates":[]
                }
            })

    for k, v in d.items():
        size = os.popen(f"du -h -d 0 {v['path']}").read().split("\t")[0]
        for _, _, fs in os.walk(v["path"]):
            v["file_count"] += len(fs)
            v["dates"]=list(set(map(lambda x: x[4:14], fs)))
            v["size"]=size
    return d
