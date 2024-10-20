def resolve(dtype, default = (None, None, None)):
    
    kwdict = { "required": True }
    
    if dtype in [int, float, str]:
        kwdict = { **kwdict, "type": dtype }
    
    elif dtype == list:
        kwdict = { **kwdict, "action": "store", "nargs": "*" }
        
    elif dtype == bool:
        kwdict = { **kwdict, "action": "store_true" }
        
    if default != (None, None, None):
        del kwdict["required"]
        kwdict = { **kwdict, 
            "default": default,
            "help": f"(default {default})",
        }
        
    return kwdict
