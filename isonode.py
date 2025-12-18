"""
    This tool recreates the isolation button from SoftImage or Maya in Houdini.
    It can be mapped to a hotkey to isolate selected nodes or restore previous visibility.
    Previous states are stored in each node's userData, avoiding global variables.
    Works on all nodes under /obj. """

import hou

ISO_KEY = "iso_prev_display"

def isoGeo():
    
    # Get root /obj node and all children
    obj = hou.node("/obj")
    nodes = obj.children()

    # Get currently selected nodes
    selected = hou.selectedNodes()

    # Check if we are in isolation mode
    in_iso = any(n.userData(ISO_KEY) is not None for n in nodes)

    if not in_iso:
        # Enter isolation: store visibility and show only selected
        for n in nodes:
            n.setUserData(ISO_KEY, str(n.isDisplayFlagSet()))
            n.setDisplayFlag(n in selected)
    else:
        # Exit isolation: restore previous visibility
        for n in nodes:
            prev = n.userData(ISO_KEY)
            if prev is not None:
                n.setDisplayFlag(prev == "True")
                n.destroyUserData(ISO_KEY)

# Run the isolation toggle
isoGeo()
