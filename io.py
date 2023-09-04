#---------------------------------------------------------------------------------------------------------------------#
# CR Animation Nodes by RockOfFire and Akatsuzi
# for ComfyUI                                    https://github.com/comfyanonymous/ComfyUI
#---------------------------------------------------------------------------------------------------------------------#

from PIL import Image, ImageSequence
import comfy.sd
import re
import torch
import numpy as np
import os
import sys
import folder_paths
import math
import json
from typing import List
from PIL.PngImagePlugin import PngInfo
from nodes import SaveImage

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

#---------------------------------------------------------------------------------------------------------------------#
# FUNCTIONS
#---------------------------------------------------------------------------------------------------------------------#
#
#---------------------------------------------------------------------------------------------------------------------#
# NODES
#---------------------------------------------------------------------------------------------------------------------#
class CR_LoadAnimationFrames:
    input_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'input')
    print(input_dir)
    @classmethod
    def INPUT_TYPES(s):
        #if not os.path.exists(s.input_dir):
            #os.makedirs(s.input_dir)
        image_folder = [name for name in os.listdir(s.input_dir) if os.path.isdir(os.path.join(s.input_dir,name)) and len(os.listdir(os.path.join(s.input_dir,name))) != 0]
        return {"required":
                    {"image_sequence_folder": (sorted(image_folder), ),
                     "start_index": ("INT", {"default": 1, "min": 1, "max": 10000}),
                     "max_frames": ("INT", {"default": 1, "min": 1, "max": 10000})
                     }
                }

    CATEGORY = "CR Animation/IO"

    RETURN_TYPES = ("IMAGE", "MASK", "INT")
    RETURN_NAMES = ("frames", "masks", "index")
    FUNCTION = "load_image_sequence"

    def load_image_sequence(self, image_sequence_folder, start_index, max_frames):
        image_path = os.path.join(self.input_dir, image_sequence_folder)
        file_list = sorted(os.listdir(image_path), key=lambda s: sum(((s, int(n)) for s, n in re.findall(r'(\D+)(\d+)', 'a%s0' % s)), ()))
        sample_frames = []
        sample_frames_mask = []
        sample_index = list(range(start_index-1, len(file_list), 1))[:max_frames]
        for num in sample_index:
            i = Image.open(os.path.join(image_path, file_list[num]))
            image = i.convert("RGB")
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            image = image.squeeze()
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")
            sample_frames.append(image)
            sample_frames_mask.append(mask)
        return (torch.stack(sample_frames), sample_frames_mask)

#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 1 node
'''
NODE_CLASS_MAPPINGS = {
    # IO
    "CR Load Animation Frames":CR_LoadAnimationFrames,
}
'''

