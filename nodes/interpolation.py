#---------------------------------------------------------------------------------------------------------------------#
# CR Animation Nodes by RockOfFire and Akatsuzi              
# for ComfyUI                                    https://github.com/comfyanonymous/ComfyUI 
#---------------------------------------------------------------------------------------------------------------------#

import torch

#---------------------------------------------------------------------------------------------------------------------#
# FUNCTIONS
#---------------------------------------------------------------------------------------------------------------------#
#
#---------------------------------------------------------------------------------------------------------------------#
# NODES
#---------------------------------------------------------------------------------------------------------------------#
class CR_GradientInteger:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ["Lerp"]
       
        return {"required": {"start_value": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "end_value": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "start_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "frame_duration": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "gradient_profile": (gradient_profiles,) 
                },
        }
    
    RETURN_TYPES = ("INT", )
    RETURN_NAMES = ("INT", )
    FUNCTION = "gradient"
    CATEGORY = "CR Animation/Interpolate"

    def gradient(self, start_value, end_value, start_frame, frame_duration, current_frame, gradient_profile):
    
        if current_frame < start_frame:
            return (start_value,)

        if current_frame > start_frame + frame_duration:
            return (end_value,)
            
        step = (end_value - start_value) / frame_duration
        
        current_step = current_frame - start_frame
        
        int_out = start_value + int(current_step * step)
        
        return (int_out,)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------#
class CR_GradientFloat:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ["Lerp"]    
    
        return {"required": {"start_value": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "end_value": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "start_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "frame_duration": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "gradient_profile": (gradient_profiles,)                              
                },
        }
    
    RETURN_TYPES = ("FLOAT", )
    RETURN_NAMES = ("FLOAT", )    
    FUNCTION = "gradient"
    CATEGORY = "CR Animation/Interpolate"

    def gradient(self, start_value, end_value, start_frame, frame_duration, current_frame, gradient_profile):
    
        if current_frame < start_frame:
            return (start_value,)

        if current_frame > start_frame + frame_duration:
            return (end_value,)
            
        step = (end_value - start_value) / frame_duration
        
        current_step = current_frame - start_frame        
        
        float_out = start_value + current_step * step
        
        return (float_out,)

#---------------------------------------------------------------------------------------------------------------------#
class CR_IncrementFloat:

    @classmethod
    def INPUT_TYPES(s):
    
        return {"required": {"start_value": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.001,}),
                             "step": ("FLOAT", {"default": 0.1, "min": -9999.0, "max": 9999.0, "step": 0.001,}),
                             "start_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.00,}),
                             "frame_duration": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                },
        }
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    OUTPUT_NODE = True    
    FUNCTION = "increment"
    CATEGORY = "CR Animation/Interpolate"

    def increment(self, start_value, step, start_frame, frame_duration, current_frame):
  
        #print(f"current frame {current_frame}")
        if current_frame < start_frame:
            return (start_value,)
  
        current_value = start_value + (current_frame - start_frame) * step
        if current_frame <= start_frame + frame_duration:
            current_value += step
            #print(f"<current value {current_value}")    
            return (current_value,)
                
        return (current_value,)

#---------------------------------------------------------------------------------------------------------------------#
class CR_IncrementInteger:

    @classmethod
    def INPUT_TYPES(s):
    
        return {"required": {"start_value": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "step": ("INT", {"default": 1.0, "min": -9999.0, "max": 9999.0, "step": 1.0,}),
                             "start_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "frame_duration": ("INT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "current_frame": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                },
        }
    
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT",)
    OUTPUT_NODE = True    
    FUNCTION = "increment"
    CATEGORY = "CR Animation/Interpolate"

    def increment(self, start_value, step, start_frame, frame_duration, current_frame):
  
        #print(f"current frame {current_frame}")
        if current_frame < start_frame:
            return (start_value,)
  
        current_value = start_value + (current_frame - start_frame) * step
        if current_frame <= start_frame + frame_duration:
            current_value += step
            #print(f"<current value {current_value}")    
            return (current_value,)
                
        return (current_value,)
 
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 8 nodes
'''
    # Interpolate Anything
    "CR Gradient Float":CR_GradientFloat,
    "CR Gradient Integer":CR_GradientInteger,
    "CR Increment Float":CR_IncrementFloat,        
    "CR Increment Integer":CR_IncrementInteger,
}
'''

