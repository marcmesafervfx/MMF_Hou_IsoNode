""" The intention of this tool is to recreate the isolation button from
SoftImage or Maya in Houdini. The script can be mapped to a hotkey to 
perform quickly. The magic comes with the houdini session module stored 
in the current scene, which allows the script to store the previous 
flags of each node.

For now, the intention is to work only with the geo nodes, but it is 
possible to add extra nodes on the list."""


import hou

def isoGeo():
    """ Isolate or unhide objects. """
    
    # Check if variable is in the current houdini session file.
    try:
        hou.session.ISO_MODE
    except:
        hou.session.ISO_MODE = "OFF"
    
    # Initialize the Root object node and its children    
    OBJ_ROOT = hou.node("/obj/")
    children = OBJ_ROOT.children()
    
    child_nodes = []
    
    for child in children:
        try:
            if not "light" in child.type().name(): 
                child.isDisplayFlagSet()
                child_nodes.append(child)
        except:
            pass
      
    
    # Initialize current visible nodes.
    visible = []
    
    # Check which nodes are visible and append them to the list.
    for node in child_nodes:
        if node.isDisplayFlagSet():
            visible.append(node)
    
    # Get the selected nodes.        
    selected = hou.selectedNodes()

    sel_nodes = []

    for sel in selected:
        try:
            if not "light" in child.type().name(): 
                sel.isDisplayFlagSet()
                sel_nodes.append(sel)
        except:
            pass
    
    # Check if the isolation mode and set flags based on response.
    if hou.session.ISO_MODE == "OFF":
        hou.session.PREV_ISO = visible
        hou.session.ISO_MODE = "ON"
        for node in child_nodes:
            node.setDisplayFlag(0)
        for select in selected:
            select.setDisplayFlag(1)
    else:
        for node in child_nodes:
            node.setDisplayFlag(0)
        for node in hou.session.PREV_ISO:
            node.setDisplayFlag(1)
        hou.session.ISO_MODE = "OFF"
        
isoGeo()
