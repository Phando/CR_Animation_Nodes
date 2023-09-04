from .nodes.interpolation import *
from .io import *
from .nodes.prompt import *
#from .nodes.schedulers import *
from .nodes.lists import *
from .nodes.utils import *
#from .nodes.camera import *
from .nodes.cyclers import *

NODE_CLASS_MAPPINGS = {
    ### Drop 4 - 25 nodes
    # Prompt Keyframes
    "CR Prompt List":CR_PromptList,
    "CR Prompt List Keyframes":CR_PromptListKeyframes,
    "CR Animation Stack":CR_AnimationStack,    
    "CR Animation Stack Keyframes":CR_AnimationStackKeyframes,
    "CR Keyframe List":CR_KeyframeList,    
    "CR Prompt Text":CR_PromptText,    
    # Interpolate
    "CR Gradient Float":CR_GradientFloat,
    "CR Gradient Integer":CR_GradientInteger,
    "CR Increment Float":CR_IncrementFloat,    
    "CR Increment Integer":CR_IncrementInteger,   
    ### Lists
    "CR Model List":CR_ModelList,
    "CR LoRA List":CR_LoRAList,
    "CR Text List":CR_TextList,
    "CR Text List Simple":CR_TextListSimple,    
    ### Cyclers
    "CR Cycle Models":CR_CycleModels,    
    "CR Cycle LoRAs":CR_CycleLoRAs,
    "CR Cycle Text":CR_CycleText,
    "CR Cycle Text Simple":CR_CycleTextSimple,     
    # Index
    "CR Index Increment":CR_IncrementIndex,
    "CR Index Multiply":CR_MultiplyIndex,
    "CR Index Reset":CR_IndexReset,      
    # Utils
    "CR Debatch Frames":CR_DebatchFrames,    
    "CR Text List To String":CR_TextListToString,    
    "CR Current Frame":CR_CurrentFrame,
    # IO
    "CR Load Animation Frames":CR_LoadAnimationFrames,
}

__all__ = ['NODE_CLASS_MAPPINGS']

print("\033[34mCR Animation Nodes: \033[92mLoaded\033[0m")
