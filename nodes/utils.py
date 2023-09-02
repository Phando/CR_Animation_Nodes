#---------------------------------------------------------------------------------------------------------------------#
# CR Animation Nodes by RockOfFire and Akatsuzi                                         
# for ComfyUI                                    https://github.com/comfyanonymous/ComfyUI
#---------------------------------------------------------------------------------------------------------------------#
#
#---------------------------------------------------------------------------------------------------------------------#
# FUNCTIONS
#---------------------------------------------------------------------------------------------------------------------#
#
#---------------------------------------------------------------------------------------------------------------------#
# NODES
#---------------------------------------------------------------------------------------------------------------------#
class CR_IncrementIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "index": ("INT", {"default": 1, "min": -10000, "max": 10000}),
                    "interval": ("INT", {"default": 1, "min": -10000, "max": 10000}),
                    }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("index", "interval")
    FUNCTION = "increment"
    CATEGORY = "CR Animation/Index"
    
    def increment(self, index, interval):
        index+=interval
        return (index, )

#---------------------------------------------------------------------------------------------------------------------#   
class CR_MultiplyIndex:

    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "index": ("INT", {"default": 1, "min": 0, "max": 10000}),
                    "factor": ("INT", {"default": 1, "min": 0, "max": 10000}),
                    }
        }


    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("index", "factor")
    FUNCTION = "multiply"
    CATEGORY = "CR Animation/Index"
    
    def multiply(self, index, factor):
        index = index * factor
        return (index, factor) 

#---------------------------------------------------------------------------------------------------------------------#   
class CR_IndexReset:

    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "index": ("INT", {"default": 1, "min": 0, "max": 10000}),
                    "reset_to": ("INT", {"default": 1, "min": 0, "max": 10000}),
                    }
        }


    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("index", "reset_to")
    FUNCTION = "reset"
    CATEGORY = "CR Animation/Index"
    
    def reset(self, index, reset_to):
        index = reset_to
        return (index, reset_to)    

#---------------------------------------------------------------------------------------------------------------------# 
class CR_DebatchFrames:
   # cloned from ltdrdata Image Batch To Image List node
   
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "frames": ("IMAGE",), } }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("debatched_frames",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "debatch"
    CATEGORY = "CR Animation/Utils"

    def debatch(self, frames):
        images = [frames[i:i + 1, ...] for i in range(frames.shape[0])]
        return (images, )

#---------------------------------------------------------------------------------------------------------------------# 
class CR_TextListToString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                "text_list": ("STRING", {"forceInput": True}),
                    },
                }

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("STRING", )
    FUNCTION = "joinlist"
    CATEGORY = "CR Animation/Utils"

    def joinlist(self, text_list):
    
        string_out = " ".join(text_list)
        
        return (string_out,)

#---------------------------------------------------------------------------------------------------------------------# 
class CR_CurrentFrame:

    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "index": ("INT", {"default": 1, "min": -10000, "max": 10000}),
                    "print_to_console": ([
                                "On",
                                "Off"],),
                    }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("index",)
    FUNCTION = "to_console"
    CATEGORY = "CR Animation/Utils"
    
    def to_console(self, index, ):
        if print_to_console == "On":
            print(f"[Info] CR Current Frame:{index}")
            
        return (index, )
        
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 5 nodes
'''
NODE_CLASS_MAPPINGS = {
    # Index
    "CR Index Increment":CR_IncrementIndex,
    "CR Index Multiply":CR_MultiplyIndex,
    "CR Index Reset":CR_IndexReset,    
    # Utils
    "CR Debatch Frames":CR_DebatchFrames,    
    "CR Text List To String":CR_TextListToString,
    "CR Current Frame":CR_CurrentFrame,
}
'''

