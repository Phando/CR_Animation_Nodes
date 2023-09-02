#---------------------------------------------------------------------------------------------------------------------#
# CR Animation Nodes by RockOfFire and Akatsuzi                                         
# for ComfyUI                                    https://github.com/comfyanonymous/ComfyUI
#---------------------------------------------------------------------------------------------------------------------#

import comfy.sd
import torch
import os
import sys
import folder_paths

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

#---------------------------------------------------------------------------------------------------------------------# 
# NODES
#---------------------------------------------------------------------------------------------------------------------# 
class CR_ModelList:

    @classmethod
    def INPUT_TYPES(cls):
    
        checkpoint_files = ["None"] + folder_paths.get_filename_list("checkpoints")
        
        return {"required": {
                    "ckpt_name1": (checkpoint_files,),
                    "alias1": ("STRING", {"multiline": False, "default": ""}),
                    "ckpt_name2": (checkpoint_files,),
                    "alias2": ("STRING", {"multiline": False, "default": ""}),
                    "ckpt_name3": (checkpoint_files,),
                    "alias3": ("STRING", {"multiline": False, "default": ""}),
                    "ckpt_name4": (checkpoint_files,),
                    "alias4": ("STRING", {"multiline": False, "default": ""}),                    
                    "ckpt_name5": (checkpoint_files,),
                    "alias5": ("STRING", {"multiline": False, "default": ""}),                    
                },
                "optional": {"model_list": ("MODEL_LIST",)
                },
        }

    RETURN_TYPES = ("MODEL_LIST", "STRING", )
    RETURN_NAMES = ("MODEL_LIST", "show_text", )
    FUNCTION = "model_list"
    CATEGORY = "CR Animation/List"

    def model_list(self, ckpt_name1, alias1, ckpt_name2, alias2, ckpt_name3, alias3, ckpt_name4, alias4,
        ckpt_name5, alias5, model_list=None):

        # Initialise the list
        models = list()
        model_text = list()
        
        # Extend the list for each model in the stack
        if model_list is not None:
            models.extend([l for l in model_list if l[0] != None]) #"None"
            model_text += "\n".join(map(str, model_list)) + "\n"

        if ckpt_name1 != "None":
            model1_tup = [(alias1, ckpt_name1)]
            models.extend(model1_tup),        
            model_text += "\n".join(map(str, model1_tup)) + "\n"

        if ckpt_name2 != "None":
            model2_tup = [(alias2, ckpt_name2)]
            models.extend(model2_tup),
            model_text += "\n".join(map(str, model2_tup)) + "\n"

        if ckpt_name3 != "None":
            model3_tup = [(alias3, ckpt_name3)]
            models.extend(model3_tup),
            model_text += "\n".join(map(str, model3_tup)) + "\n"

        if ckpt_name4 != "None":
            model4_tup = [(alias4, ckpt_name4)]
            models.extend(model4_tup),
            model_text += "\n".join(map(str, model4_tup)) + "\n"
            
        if ckpt_name5 != "None":
            model5_tup = [(alias5, ckpt_name5)]       
            models.extend(model5_tup),
            model_text += "\n".join(map(str, model5_tup)) + "\n"
            
        #print(f"[TEST] CR Model List: {models}")

        show_text = "".join(model_text)
            
        return (models, show_text, )

#---------------------------------------------------------------------------------------------------------------------#  
class CR_LoRAList:
    
    @classmethod
    def INPUT_TYPES(cls):
    
        lora_files = ["None"] + folder_paths.get_filename_list("loras")
        
        return {"required": {                    
                    "lora_name1": (lora_files,),
                    "alias1": ("STRING", {"multiline": False, "default": ""}),                    
                    "model_strength_1": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                    "clip_strength_1": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                    
                    "lora_name2": (lora_files,),
                    "alias2": ("STRING", {"multiline": False, "default": ""}),
                    "model_strength_2": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                    "clip_strength_2": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                    
                    "lora_name3": (lora_files,),
                    "alias3": ("STRING", {"multiline": False, "default": ""}),                       
                    "model_strength_3": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),
                    "clip_strength_3": ("FLOAT", {"default": 1.0, "min": -10.0, "max": 10.0, "step": 0.01}),  
                },
                "optional": {"lora_list": ("lora_LIST",)
                },
        }

    RETURN_TYPES = ("LORA_LIST", "STRING", )
    RETURN_NAMES = ("LORA_LIST", "show_text", )
    FUNCTION = "lora_list"
    CATEGORY = "CR Animation/List"

    def lora_list(self, lora_name1, model_strength_1, clip_strength_1, alias1,
    lora_name2, model_strength_2, clip_strength_2, alias2,
    lora_name3, model_strength_3, clip_strength_3, alias3, lora_list=None):

        # Initialise the list
        loras = list()
        lora_text = list()
        
        # Extend the list for each lora in the stack
        if lora_list is not None:
            loras.extend([l for l in lora_list if l[0] != None]) #"None"
            lora_text += "\n".join(map(str, lora_list)) + "\n"
        
        if lora_name1 != "None":
            lora1_tup = [(alias1, lora_name1, model_strength_1, clip_strength_1)]
            loras.extend(lora1_tup),
            lora_text += "\n".join(map(str, lora1_tup)) + "\n"
            
        if lora_name2 != "None":
            lora2_tup = [(alias2, lora_name2, model_strength_2, clip_strength_2)]        
            loras.extend(lora2_tup),
            lora_text += "\n".join(map(str, lora2_tup)) + "\n"

        if lora_name3 != "None":
            lora_tup3 = [(alias3, lora_name3, model_strength_3, clip_strength_3)]          
            loras.extend(lora3_tup),        
            lora_text += "\n".join(map(str, lora3_tup)) + "\n"
           
        #print(f"[DEBUG] CR Lora List: {lora_text}")

        show_text = "".join(lora_text)
            
        return (loras, show_text, )
 
       
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 2 nodes
'''
NODE_CLASS_MAPPINGS = {
    ### Lists
    "CR Model List":CR_ModelList,
    "CR LoRA List":CR_LoRAList,
'''

