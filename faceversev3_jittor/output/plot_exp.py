

import numpy as np
import json
import sys
import os
import matplotlib.pyplot as plt


exp_name_list = ["browDownLeft", "browDownRight", "browInnerUp", "browOuterUpLeft", "browOuterUpRight", "cheekPuff", "cheekSquintLeft", "cheekSquintRight", "eyeBlinkLeft", "eyeBlinkRight", "eyeLookDownLeft", "eyeLookDownRight", "eyeLookInLeft", "eyeLookInRight", "eyeLookOutLeft", "eyeLookOutRight", "eyeLookUpLeft", "eyeLookUpRight", "eyeSquintLeft", "eyeSquintRight", "eyeWideLeft", "eyeWideRight", "jawForward", "jawLeft", "jawOpen", "jawRight", "mouthClose", "mouthDimpleLeft", "mouthDimpleRight", "mouthFrownLeft", "mouthFrownRight", "mouthFunnel", "MouthLeft", "mouthLowerDownLeft", "mouthLowerDownRight", "mouthPressLeft", "mouthPressRight", "mouthPucker", "MouthRight", "mouthRollLower", "mouthRollUpper", "mouthShrugLower", "mouthShrugUpper", "mouthSmileLeft", "mouthSmileRight", "mouthStretchLeft", "mouthStretchRight", "mouthUpperUpLeft", "mouthUpperUpRight", "noseSneerLeft", "noseSneerRight", "tongueOut"]

if __name__== "__main__":
    print(len(exp_name_list))
    args = sys.argv
    assert len(args)==2, f"Usage: python {args[0]} ./images/512/exp_00_D_3.png.txt"
    txt_file = args[1]#'input_file.npy
    folder_name, file_name_with_ext = os.path.split(txt_file)
    file_name, file_ext = os.path.splitext(file_name_with_ext)

    with open(txt_file) as f:
        # text = f.readlines().rstrip('\n')
        lines = f.read().splitlines()
        lines = [float(s) for s in lines]
        # print(text)
        print(lines)
        plt.plot(exp_name_list, lines, marker="o")
        plt.xticks(rotation=90)
        plt.xlabel("exp name")
        plt.ylabel("exp para")
        plt.title(f"{len(lines)}dim expression")
        plt.tight_layout()
        plt.ylim(-0.2,2)
        save_path = f"{folder_name}/plot_exp_{file_name}"#.png"
        plt.savefig(save_path)
        print(f"save: {save_path}")
        # plt.show()
