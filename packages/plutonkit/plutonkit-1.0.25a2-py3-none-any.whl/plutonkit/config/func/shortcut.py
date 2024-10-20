def shortcut_ucfirst(val,_):
    return val.capitalize()

def shortcut_lower(val,_):
    return val.lower()

def shortcut_upper(val,_):
    return val.upper()

def shortcut_join_space(val,actions):
    return (actions[0]["arg"][0]).join(val.split(" "))

def shortcut_replace(val,actions):
    return val.replace(actions[0]["arg"][0], actions[0]["arg"][1])

def shortcut_if(val,actions):
    if str(actions[0]["arg"][0]) == str(val):
        val = actions[0]["arg"][1]
    return val
