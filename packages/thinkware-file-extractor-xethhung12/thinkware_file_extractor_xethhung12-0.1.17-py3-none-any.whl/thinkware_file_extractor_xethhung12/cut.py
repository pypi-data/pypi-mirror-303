import yaml

import thinkware_file_extractor_xethhung12.utils_tools

def cut(yaml_file, front_movie_file, rear_movie_file):
    tmp_front_movie_file = f"{front_movie_file[:-4]}_tmp.mp4"
    tmp_rear_movie_file = f"{rear_movie_file[:-4]}_tmp.mp4"
    mute = True
    width = str(thinkware_file_extractor_xethhung12.utils_tools.mp4view(front_movie_file).get_width())
    new_scale = thinkware_file_extractor_xethhung12.utils_tools.get_scale(width)
    new_x = thinkware_file_extractor_xethhung12.utils_tools.get_x(width)
    new_y = thinkware_file_extractor_xethhung12.utils_tools.get_y(width)

    s=""

    d = dict()
    with open(yaml_file, "r") as f:
        d = yaml.safe_load(f)
    for data in d:
        date_str = data['date']
        trips = data['trip']
        for trip in trips:
            hour = int(trip['hour'])
            start = trip['start']
            end = trip['end']
            dest_naming = []
            from_loc = trip['from']
            dest_naming.append(from_loc)
            for x in trip['through']:
                dest_naming.append(x)
            to_loc = trip['to']
            dest_naming.append(to_loc)

            dest_name = "_to_".join(map(lambda x: x.replace(' ', '-'), dest_naming))
            dest_name = f"{date_str}_{hour:02}_{dest_name}.mp4"

            cmd = f"""
rm -f {tmp_front_movie_file} {tmp_rear_movie_file} {dest_name}
ffmpeg -ss {start} -to {end} -i {front_movie_file} -c copy {"-an" if mute else ""} {tmp_front_movie_file}
ffmpeg -ss {start} -to {end} -i {rear_movie_file} -c copy {"-an" if mute else ""} {tmp_rear_movie_file}
ffmpeg -i {tmp_front_movie_file} -vf \"movie={tmp_rear_movie_file}, scale={new_scale}:-1 [inner]; [in] [inner] overlay={new_x}:{new_y} [out]\" -preset ultrafast {dest_name}
rm -f {tmp_front_movie_file} {tmp_rear_movie_file}
"""
            s=s+cmd
    return s