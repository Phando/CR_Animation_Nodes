from .nodes.interpolation import *
from .io import *
from .nodes.prompt import *
#from .nodes.schedulers import *
from .nodes.lists import *
from .nodes.utils import *
#from .nodes.camera import *
from .nodes.cyclers import *

NODE_CLASS_MAPPINGS = {
    ### Drop 5 - 30 nodes
    # Prompt
    "CR Prompt List":CR_PromptList,
    "CR Prompt List Keyframes":CR_PromptListKeyframes,
    "CR Animation Stack":CR_AnimationStack,    
    "CR Animation Stack Keyframes":CR_AnimationStackKeyframes,
    "CR Keyframe List":CR_KeyframeList,    
    "CR Prompt Text":CR_PromptText,    
    # Interpolation
    "CR Gradient Float":CR_GradientFloat,
    "CR Gradient Integer":CR_GradientInteger,
    "CR Increment Float":CR_IncrementFloat,    
    "CR Increment Integer":CR_IncrementInteger,
    "CR Interpolate Latents":CR_InterpolateLatents,    
    ### Lists
    "CR Model List":CR_ModelList,
    "CR LoRA List":CR_LoRAList,
    "CR Text List":CR_TextList,
    "CR Text List Simple":CR_TextListSimple,
    "CR Image List":CR_ImageList,
    "CR Image List Simple":CR_ImageListSimple,      
    ### Cyclers
    "CR Cycle Models":CR_CycleModels,    
    "CR Cycle LoRAs":CR_CycleLoRAs,
    "CR Cycle Text":CR_CycleText,
    "CR Cycle Text Simple":CR_CycleTextSimple,
    "CR Cycle Images":CR_CycleImages,
    "CR Cycle Images Simple":CR_CycleImagesSimple,        
    # Utils
    "CR Index Increment":CR_IncrementIndex,
    "CR Index Multiply":CR_MultiplyIndex,
    "CR Index Reset":CR_IndexReset,      
    "CR Debatch Frames":CR_DebatchFrames,    
    "CR Text List To String":CR_TextListToString,    
    "CR Current Frame":CR_CurrentFrame,
    # IO
    "CR Load Animation Frames":CR_LoadAnimationFrames,
}

__all__ = ['NODE_CLASS_MAPPINGS']

print("\033[34mCR Animation Nodes: \033[92mLoaded\033[0m")
