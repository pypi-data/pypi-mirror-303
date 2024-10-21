import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from os import listdir
from os.path import isfile

from thinkware_file_extractor_xethhung12.utils_tools import summary


class AtomicInt():
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def get(self)->int:
        with self.lock:
            return self.value

    def inc(self)->int:
        with self.lock:
            self.value += 1
            return self.value



FILE_LIST=["cont_rec","evt_rec","manual_rec","parking_rec","motion_timelapse_rec"]
def if_found(path)->bool:
    if len(list(filter(lambda x: x in FILE_LIST,listdir(path)))) == 5:
        return True
    else:
        return False

def scan_file(path):
    for i in os.listdir(path):
        print(i)

def rm_path_suffix(path):
    if path.endswith("/"):
        return path[:-1]
    else:
        return path


def copy_all_file(_from, _to):
    start_time = datetime.now()
    base_path=rm_path_suffix(_from)
    dest_path=rm_path_suffix(_to)

    if not if_found(base_path):
        print("not found")
        exit(0)
    else:
        d = sorted(summary(base_path)["cont_rec"]["dates"])
        dest_folder_name = f"{dest_path}/gen_{d[0]}-to-{d[-1]}/data"
        if not os.path.exists(dest_folder_name):
            os.makedirs(dest_folder_name, exist_ok=True)

        flist = [
            (f"{base_path}/{dn}",f"{dest_folder_name}/{dn}", fn)
            for dn in FILE_LIST
            for fn in listdir(f"{base_path}/{dn}") if isfile(os.path.join(f"{base_path}/{dn}", fn))
        ]

        folder_list = list([os.path.join(dest_folder_name,f) for f in FILE_LIST])
        for folder in folder_list:
            if not os.path.exists(f"{folder}"):
                os.makedirs(folder, exist_ok=True)
                print(f"created: {folder}")

        for folder in folder_list:
            for fn in listdir(f"{folder}"):
                if os.path.isfile(os.path.join(folder,fn)):
                    os.remove(os.path.join(folder,fn))
                    print(f"[Removed] {folder}/{fn}")

        # index = 0
        lock = threading.Lock()
        executor = ThreadPoolExecutor(max_workers=10)
        ai = AtomicInt()



        def copy_internal(fs):
            source, dest, filename = fs
            shutil.copy2(os.path.join(source,filename), os.path.join(dest,filename))

            with lock:
                index=ai.inc()
                now_time= datetime.now()
                elapsed = now_time - start_time
                time_used = f"00m{int(elapsed.total_seconds()):02}" if elapsed.total_seconds() < 60 else f"{int(elapsed.total_seconds()/60):02}m{int(elapsed.total_seconds()%60):02}s"
                print(f"[COPY - {time_used} {index}/{len(flist)}] `{filename}` from `{source}` to `{dest}`", flush=True)

        items = [ executor.submit(copy_internal, f) for f in flist]

        for item in items:
            item.result()


        executor.shutdown(wait=True)

        end_time = datetime.now()
        elapsed = end_time - start_time
        time_used = f"00m{int(elapsed.total_seconds()):02}" if elapsed.total_seconds() < 60 else f"{int(elapsed.total_seconds() / 60):02}m{int(elapsed.total_seconds() % 60):02}s"
        print(f"[Done] used {time_used} {{`{start_time}` `{end_time}`}} ")

if __name__ == '__main__':
    base_path=rm_path_suffix("/media/xeth/U1000")
    dest_path=rm_path_suffix("/media/xeth/My Passport")
    copy_all_file(base_path,dest_path)
