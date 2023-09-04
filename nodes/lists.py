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
class CR_TextList:

    @classmethod
    def INPUT_TYPES(cls):
  
        return {"required": {
                    "text_1": ("STRING", {"multiline": False, "default": ""}),
                    "alias1": ("STRING", {"multiline": False, "default": ""}),
                    "text_2": ("STRING", {"multiline": False, "default": ""}),
                    "alias2": ("STRING", {"multiline": False, "default": ""}),
                    "text_3": ("STRING", {"multiline": False, "default": ""}),
                    "alias3": ("STRING", {"multiline": False, "default": ""}),
                    "text_4": ("STRING", {"multiline": False, "default": ""}),
                    "alias4": ("STRING", {"multiline": False, "default": ""}),                    
                    "text_5": ("STRING", {"multiline": False, "default": ""}),
                    "alias5": ("STRING", {"multiline": False, "default": ""}),                    
                },
                "optional": {"text_list": ("text_LIST",)
                },
        }

    RETURN_TYPES = ("TEXT_LIST", "STRING", )
    RETURN_NAMES = ("TEXT_LIST", "show_text", )
    FUNCTION = "text_list"
    CATEGORY = "CR Animation/List"

    def text_list(self, text_1, alias1, text_2, alias2, text_3, alias3, text_4, alias4, text_5, alias5, text_list=None):

        # Initialise the list
        texts = list()
        showtext = list()
        
        # Extend the list for each text item in a connected list
        if text_list is not None:
            texts.extend([l for l in text_list])
        
        # Extend the list for each text item in the list
        if text_1 != "":
            text1_tup = [(alias1, text_1)]        
            texts.extend(text1_tup),
            showtext.extend([(alias1 + "," + text_1 + "\n")]),

        if text_2 != "":
            text2_tup = [(alias2, text_2)]        
            texts.extend(text2_tup),
            showtext.extend([(alias2 + "," + text_2 + "\n")]),

        if text_3 != "":
            text3_tup = [(alias3, text_3)]        
            texts.extend(text3_tup),
            showtext.extend([(alias3 + "," + text_3 + "\n")]),

        if text_4 != "":
            text4_tup = [(alias4, text_4)]        
            texts.extend(text4_tup),
            showtext.extend([(alias4 + "," + text_4 + "\n")]),
            
        if text_5 != "":
            text5_tup = [(alias5, text_5)]        
            texts.extend(text5_tup),
            showtext.extend([(alias5 + "," + text_5 + "\n")]),
            
        #print(f"[Debug] CR Text List: {texts}")

        show_text = "".join(showtext)
            
        return (texts, show_text, )

#---------------------------------------------------------------------------------------------------------------------#
class CR_TextListSimple:

    @classmethod
    def INPUT_TYPES(cls):
  
        return {"required": {            
                },
                "optional": {"text_1": ("STRING", {"multiline": False, "default": ""}),
                             "text_2": ("STRING", {"multiline": False, "default": ""}),
                             "text_3": ("STRING", {"multiline": False, "default": ""}),
                             "text_4": ("STRING", {"multiline": False, "default": ""}),                    
                             "text_5": ("STRING", {"multiline": False, "default": ""}),
                             "text_list_simple": ("TEXT_LIST_SIMPLE",)
                },
        }

    RETURN_TYPES = ("TEXT_LIST_SIMPLE", )
    RETURN_NAMES = ("TEXT_LIST_SIMPLE", )
    FUNCTION = "text_list_simple"
    CATEGORY = "CR Animation/List"

    def text_list_simple(self, text_1, text_2, text_3,  text_4, text_5, text_list_simple=None):

        # Initialise the list
        texts = list()
        
        # Extend the list for each text in the stack
        if text_list_simple is not None:
            texts.extend(l for l in text_list_simple)
        
        if text_1 != "" and text_1 != None:
            texts.append(text_1),

        if text_2 != "" and text_2 != None:
            texts.append(text_2)

        if text_3 != "" and text_3 != None:
            texts.append(text_3)

        if text_4 != "" and text_4 != None:
            texts.append(text_4),
            
        if text_5 != "" and text_5 != None:
            texts.append(text_5),
            
        return (texts,)
       
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 4 nodes
'''
NODE_CLASS_MAPPINGS = {
    ### Lists
    "CR Model List":CR_ModelList,
    "CR LoRA List":CR_LoRAList,    
    "CR Text List":CR_TextList,
    "CR Text List Simple":CR_TextListSimple,
}
'''

