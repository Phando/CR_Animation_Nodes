#---------------------------------------------------------------------------------------------------------------------#
# CR Animation Nodes by RockOfFire and Akatsuzi     https://github.com/RockOfFire/CR-Animation-Nodes                                       
# for ComfyUI                                       https://github.com/comfyanonymous/ComfyUI
#---------------------------------------------------------------------------------------------------------------------#

import comfy.sd
import torch
import os
import sys
import folder_paths
import random

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

#---------------------------------------------------------------------------------------------------------------------# 
# NODES
#---------------------------------------------------------------------------------------------------------------------# 
class CR_CycleModels:

    @classmethod
    def INPUT_TYPES(s):
    
        modes = ["Off", "Sequential"]

    
        return {"required": {"mode": (modes,),
                             "model": ("MODEL",),
                             "clip": ("CLIP",),
                             "model_list": ("MODEL_LIST",),
                             "frame_interval": ("INT", {"default": 30, "min": 0, "max": 999, "step": 1,}),        
                             "loops": ("INT", {"default": 1, "min": 1, "max": 1000}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                },
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    RETURN_NAMES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "cycle_models"
    CATEGORY = "CR Animation/List"

    def cycle_models(self, mode, model, clip, model_list, frame_interval, loops, current_frame,):
            
        # Initialize the list
        model_params = list()

        # Extend lora_params with the lora_list items
        if model_list:
            for _ in range(loops):
                model_params.extend(model_list)
            #print(f"[Debug] CR Cycle Models:{model_params}")
                
        if mode == "Off":
            return (model, clip)               

        elif mode == "Sequential":
            if current_frame == 0:
                return (model, clip) 
            else:    
                # Calculate the index of the current model based on the current_frame and frame_interval
                current_model_index = (current_frame // frame_interval) % len(model_params)
                #print(f"[Debug] CR Cycle Models:{current_model_index}")
                
                # Get the parameters of the current model
                current_model_params = model_params[current_model_index]
                model_alias, ckpt_name = current_model_params
                print(f"[Info] CR Cycle Models: Current model is {ckpt_name}")
                
                # Load the current model
                ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
                out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, 
                embedding_directory=folder_paths.get_folder_paths("embeddings"))
                return out 
        #else:
        #    return (model, clip) 
 
#---------------------------------------------------------------------------------------------------------------------# 
class CR_CycleLoRAs:

    @classmethod
    def INPUT_TYPES(s):
        
        modes = ["Off", "Sequential"]
    
        return {"required": {"mode": (modes,),
                             "model": ("MODEL",),
                             "clip": ("CLIP",),
                             "lora_list": ("LORA_LIST",),
                             "frame_interval": ("INT", {"default": 30, "min": 0, "max": 999, "step": 1,}),
                             "loops": ("INT", {"default": 1, "min": 1, "max": 1000}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),                             
                },
        }
    
    RETURN_TYPES = ("MODEL", "CLIP", )
    RETURN_NAMES = ("MODEL", "CLIP", )
    FUNCTION = "cycle"
    CATEGORY = "CR Animation/List"

    def cycle(self, mode, model, clip, lora_list, frame_interval, loops, current_frame):
    
        # Initialize the list
        lora_params = list()

        # Extend lora_params with lora_list items
        if lora_list:
            for _ in range(loops):
                lora_params.extend(lora_list)
            #print(f"[Debug] CR Cycle LoRAs:{lora_params}")            
        else:
            return model, clip

        if mode == "Sequential":
            # Calculate the index of the current LoRA based on the current_frame and frame_interval
            current_lora_index = (current_frame // frame_interval) % len(lora_params)
            #print(f"[Debug] CR Cycle LoRAs:{current_lora_index}")
            
            # Get the parameters of the current LoRA
            current_lora_params = lora_params[current_lora_index]
            lora_alias, lora_name, model_strength, clip_strength = current_lora_params
            
            # Load the current LoRA
            lora_path = folder_paths.get_full_path("loras", lora_name)
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            print(f"[Info] CR_CycleLoRAs: Current LoRA is {lora_name}")

            # Apply the current LoRA to the model and clip
            model_lora, clip_lora = comfy.sd.load_lora_for_models(
            model, clip, lora, model_strength, clip_strength)
            return model_lora, clip_lora            
        else:
            return model, clip

#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 2 nodes
'''
NODE_CLASS_MAPPINGS = {  
    ### Cycle List
    "CR Cycle Models":CR_CycleModels,    
}
'''

