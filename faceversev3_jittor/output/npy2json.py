# :/app/faceversev3_jittor/output# python npy2json.py images/512/param/00_D_3.npy 

import numpy as np
import json
import sys
import os

# def change_ext(filename, new_extension):
#     file_root, _ = os.path.splitext(filename)
#     filenameos.path.basename
#     return f"{file_root}.{new_extension}"
def change_ext(path, new_extension):
    folder_name, file_name_with_ext = os.path.split(path)
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    return folder_name, f"{file_name}.{new_extension}"

if __name__== "__main__":
    args = sys.argv
    assert len(args)==2, f"Usage: python {args[0]} ###.npy"
    # npyファイルを読み込む
    npy_file = args[1]#'input_file.npy'
    # array_data = np.load(npy_file)
    array_data = np.load(npy_file, allow_pickle=True)

    # print(array_data)
    # print(type(array_data))
    # array_data_dict = array_data.to_dict()
    # print(type(array_data_dict))
    array_data_dict = array_data.item()
    print(type(array_data_dict))
    # numpy配列をリストに変換する
    array_data_list = array_data.tolist()
    # print(array_data_list)

    # JSONファイルに書き出す
    json_dir = "/json/"
    base_dir, json_tmp = change_ext(npy_file, "json")
    # json_file = json_dir + change_ext(npy_file, "json")#'output_file.json'
    # json_file = "./"+base_dir + json_dir + json_tmp#'output_file.json'
    json_file = "./"+ json_tmp#'output_file.json'
    # print(json_file)
    with open(json_file, 'w') as f:
        # json.dump(array_data_list, f)
        # json.dump(array_data, f)
        json.dump(array_data_dict["exp_name_list"], f)

    print(f'JSONファイルに書き出しました: {json_file}')