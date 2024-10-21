import argparse
import json
import sys

import yaml

import thinkware_file_extractor_xethhung12.automating
from thinkware_file_extractor_xethhung12.script_gen import gen_merge_script, gen_copy_script, clear_script_gen

import thinkware_file_extractor_xethhung12 as thinkwareExtractor


def main():
    parser = argparse.ArgumentParser(
        prog='thinkware_file_extractor_xethhung12',
        description='extract thinkware data',
    )

    level_1_subparser=parser.add_subparsers(help="utils", dest="level1")
    level_1_subparser_utils_parser = level_1_subparser.add_parser(
        "utils", description="utils for querying information"
    )
    utils_parser_level_2=level_1_subparser_utils_parser.add_subparsers(help="when-x", dest="level2")

    utils_parser_level_2_view_fs=utils_parser_level_2.add_parser("view-fs")
    utils_parser_level_2_view_fs.add_argument(
        "--path", type=str, help="path to view"
    )

    utils_parser_level_2_when_x=utils_parser_level_2.add_parser("when-x")
    utils_parser_level_2_when_x.add_argument(
        "--value","-v", type=str, help="x value"
    )

    utils_parser_level_2_when_x=utils_parser_level_2.add_parser("when-y")
    utils_parser_level_2_when_x.add_argument(
        "--value","-v", type=str, help="y value"
    )

    utils_parser_level_2_scale=utils_parser_level_2.add_parser("scale")
    utils_parser_level_2_scale.add_argument(
        "--value","-v", type=str, help="scale value"
    )

    utils_parser_level_2_timeline_scan=utils_parser_level_2.add_parser("timeline-scan")
    utils_parser_level_2_timeline_scan.add_argument(
        "--path", type=str, help="path to test",
    )

    utils_parser_level_2_has_target_file=utils_parser_level_2.add_parser("has-target-file")
    utils_parser_level_2_has_target_file.add_argument(
        "--path", type=str, help="path to test"
    )

    utils_parser_level_2_backup_files=utils_parser_level_2.add_parser("backup-files")
    utils_parser_level_2_backup_files.add_argument(
        "--from", type=str, help="path of source"
    )
    utils_parser_level_2_backup_files.add_argument(
        "--to", type=str, help="path of dest"
    )

    utils_parser_level_2_has_target_file.add_argument(
        "--prefix", type=str, help="prefix of file", choices = ["EVT", "REC", "MOT", "PAK"]
    )
    utils_parser_level_2_has_target_file.add_argument(
        "--mode", type=str, help="front or rear", choices = ["F", "R"]
    )

    utils_parser_level_2_target_file_count=utils_parser_level_2.add_parser("target-file-count")
    utils_parser_level_2_target_file_count.add_argument(
        "--path", type=str, help="path to test"
    )
    utils_parser_level_2_target_file_count.add_argument(
        "--prefix", type=str, help="prefix of file", choices = ["EVT", "REC", "MOT", "PAK"]
    )
    utils_parser_level_2_target_file_count.add_argument(
        "--mode", type=str, help="front or rear", choices = ["F", "R"]
    )

    level_1_subparser_mp4_parser = level_1_subparser.add_parser(
        "mp4", description="mp4 related"
    )
    level_1_subparser_mp4_parser_level_2 = level_1_subparser_mp4_parser.add_subparsers(help="mp4 related", dest="level2")
    level_1_subparser_mp4_parser_level_2_all_parser=level_1_subparser_mp4_parser_level_2.add_parser("all")
    level_1_subparser_mp4_parser_level_2_all_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_width_parser=level_1_subparser_mp4_parser_level_2.add_parser("width")
    level_1_subparser_mp4_parser_level_2_width_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_height_parser=level_1_subparser_mp4_parser_level_2.add_parser("height")
    level_1_subparser_mp4_parser_level_2_height_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_mp4_parser_level_2_codec_parser=level_1_subparser_mp4_parser_level_2.add_parser("codec")
    level_1_subparser_mp4_parser_level_2_codec_parser.add_argument(
        "--file-name","-f", type=str, help="view file"
    )

    level_1_subparser_script_gen_parser = level_1_subparser.add_parser(
        "script-gen", description="generate scripts"
    )
    level_1_subparser_script_gen_parser_level_2=level_1_subparser_script_gen_parser.add_subparsers(help="merge-script", dest="level2")
    level_1_subparser_script_gen_parser_level_2_parser=level_1_subparser_script_gen_parser_level_2.add_parser("merge-script")
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--source", type=str, help="source path"
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--dest", type=str, help="destination path"
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--prefix", type=str, help="prefix of file", choices = ["EVT", "REC", "MOT", "PAK"]
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--mode", type=str, help="front or rear", choices = ["F", "R"]
    )
    level_1_subparser_script_gen_parser_level_2_parser.add_argument(
        "--dest-file-name", type=str, help="destination file name", default="merge"
    )

    level_1_subparser_script_gen_parser_level_2_clear_script_parser=level_1_subparser_script_gen_parser_level_2.add_parser("clear-script")
    level_1_subparser_script_gen_parser_level_2_clear_script_parser.add_argument(
        "--path", type=str, help="path to clear"
    )

    level_1_subparser_script_gen_parser_level_2_copy_script_parser=level_1_subparser_script_gen_parser_level_2.add_parser("copy-script")
    level_1_subparser_script_gen_parser_level_2_copy_script_parser.add_argument(
        "--source", type=str, help="source path"
    )
    level_1_subparser_script_gen_parser_level_2_copy_script_parser.add_argument(
        "--dest", type=str, help="destination path"
    )

    level_1_subparser_script_gen_parser_level_2_split_and_merge_parser=level_1_subparser_script_gen_parser_level_2.add_parser("split-and-merge-script")
    level_1_subparser_script_gen_parser_level_2_split_and_merge_parser.add_argument(
        "--yaml", type=str, help="cut config in yaml"
    )
    level_1_subparser_script_gen_parser_level_2_split_and_merge_parser.add_argument(
        "--front", type=str, help="front movie"
    )
    level_1_subparser_script_gen_parser_level_2_split_and_merge_parser.add_argument(
        "--rear", type=str, help="rear movie"
    )

    x = parser.parse_args(sys.argv[1:])
    if x.level1 == "utils":
        if x.level2 == "view-fs":
            return print(yaml.safe_dump(thinkwareExtractor.utils.summary(x.path)))
        if x.level2 == "when-x":
            val = x.value
            return print(thinkwareExtractor.utils.get_x(val))
        elif x.level2 == "when-y":
            val = x.value
            return print(thinkwareExtractor.utils.get_y(val))
        elif x.level2 == "scale":
            val = x.value
            return print(thinkwareExtractor.utils.get_scale(val))
        elif x.level2 == "target-file-count":
            path = x.path
            prefix = x.prefix
            mode = x.mode
            return print(thinkwareExtractor.utils.target_file_count(path, prefix, mode))
        elif x.level2 == "has-target-file":
            path = x.path
            prefix = x.prefix
            mode = x.mode
            return print("yes" if thinkwareExtractor.utils.has_target_file(path, prefix, mode) else "no")
        elif x.level2 == "timeline-scan":
            path = x.path
            extracted = thinkwareExtractor.video_vision.extract_time_list(path)
            l = list(set([line.date for line in extracted]))
            d=[]
            for i in l:
                time_list=sorted(set([line.hour for line in extracted if line.date == i]))
                dd = {
                    "date": i,
                    "hour": time_list
                }
                d.append(dd)
            print(yaml.safe_dump(d))
        elif x.level2 == "backup-files":
            _from = x.__dict__['from']
            _to = x.to
            thinkware_file_extractor_xethhung12.automating.copy_all_file(_from, _to)
        else:
            print(x)
    elif x.level1 == "mp4":
        if x.level2 == "all":
            print(json.dumps(thinkwareExtractor.utils_tools.mp4view(x.file_name).map, indent=2))
        elif x.level2 == "width":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_width())
        elif x.level2 == "height":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_height())
        elif x.level2 == "codec":
            print(thinkwareExtractor.utils_tools.mp4view(x.file_name).get_codec())
        else:
            print(x)
    elif x.level1 == "script-gen":
        if x.level2 == "merge-script":
            print(gen_merge_script(x.source, x.dest, x.prefix, x.mode, x.dest_file_name if x.dest_file_name is not None else "merge"))
        elif x.level2 == "copy-script":
            print(gen_copy_script(x.source, x.dest))
        elif x.level2 == "clear-script":
            print(clear_script_gen(x.path))
        elif x.level2 == "split-and-merge-script":
            print(thinkwareExtractor.cut_lib.cut(x.yaml, x.front, x.rear))
        else:
            print(x)
    else:
        print(x)


if __name__ == '__main__':
    main()
