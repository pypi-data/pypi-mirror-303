import os
import pathlib

import hou

import ciocore.loggeria

from ciohoudini import (
    driver,
    frames,
)

LOGGER = ciocore.loggeria.get_conductor_logger()

ROP_PARMS = ("rop_checkbox_{index}", "rop_path_{index}", "rop_frame_range_{index}")

def add_one_render_rop(rop, node, next_index, network, render_rops_dict=None):
    """Add a render rop to the ui."""
    if not rop:
        return None
    rop_checkbox = True
    rop_path = rop.path() or "/{}/{}".format(network, rop.name())
    # print("Adding rop: {} at index: {}".format(rop_path, next_index))

    if rop.type().name() == 'usdrender_rop':
        #rop_frame_range = "{}-{}".format(int(rop.parm("f1").eval()), int(rop.parm("f2").eval()))
        rop_frame_range = frames.get_all_rop_frame_range(node, rop_path)
    else:
        #rop_frame_range = node.parm("frame_range").eval()
        rop_frame_range = frames.get_all_rop_frame_range(node, rop_path)

    if rop_path and render_rops_dict:
        key = rop_path.replace("/", "")
        if key in render_rops_dict:
            rop_frame_range = render_rops_dict[key].get('frame_range', '1-1')
            rop_checkbox = render_rops_dict[key].get('rop_checkbox', True)
            # print("Stored frame range: {}".format(rop_frame_range))

    # print("Adding rop frame range: {}".format(rop_frame_range))

    node.parm("render_rops").set(next_index)
    node.parm("rop_checkbox_{}".format(next_index)).set(rop_checkbox)
    node.parm("rop_path_{}".format(next_index)).set(rop_path)
    node.parm("rop_frame_range_{}".format(next_index)).set(rop_frame_range)

    #node.parm("rop_use_scout_frames_{}".format(next_index)).set(False)
    # Todo implement preview button for each rop


def get_render_rop_data(node):
    """Get the render rop data from the UI."""
    render_rops_data = []
    for i in range(1, node.parm("render_rops").eval() + 1):
        
        rop_checkbox = node.parm("rop_checkbox_{}".format(i))
        if ( rop_checkbox.eval() and not rop_checkbox.isDisabled()):
        
            render_rops_data.append({
                "path": node.parm("rop_path_{}".format(i)).evalAsString(),
                "frame_range": node.parm("rop_frame_range_{}".format(i)).evalAsString(),
                # "use_scout_frames": node.parm("rop_use_scout_frames_{}".format(i)).eval(),
            })
    return render_rops_data

def store_current_render_rop_data(node):
    """Store the current render rop data in the UI."""
    render_rops_dict = {}
    for i in range(1, node.parm("render_rops").eval() + 1):
        path = node.parm("rop_path_{}".format(i)).evalAsString()
        if path:
            key = path.replace("/", "")
            if key not in render_rops_dict:
                render_rops_dict[key] = {}
                render_rops_dict[key]["rop_checkbox"] = node.parm("rop_checkbox_{}".format(i)).eval()
                render_rops_dict[key]["frame_range"] = node.parm("rop_frame_range_{}".format(i)).evalAsString()
                # render_rops_dict[key]["use_scout_frames"] = node.parm("rop_use_scout_frames_{}".format(i)).eval()

    return render_rops_dict


def add_render_ropes(node, render_rops_dict=None):
    """
    Add all render rops to the UI.
    Currently only supports driver rop (out network)
    and usdrender_rop nodes (Stage network).
    """
    next_index = 1
    # Add the driver rop if it exists
    driver_rop = driver.get_driver_node(node)
    if driver_rop:
        # print("driver_rop: {}".format(driver_rop.name()))
        # Add the driver rop to the UI
        add_one_render_rop(driver_rop, node, next_index, "out", render_rops_dict=render_rops_dict)
   
    # Add all the render rops in the stage
    render_ropes = get_stage_render_rops()
    if render_ropes:
        for rop in render_ropes:
            next_index = node.parm("render_rops").eval() + 1
            # print("Adding rop: {}".format(rop.name()))
            # Add the rop to the UI
            add_one_render_rop(rop, node, next_index, "stage", render_rops_dict=render_rops_dict)
            
    # Disable the output folder parm if there are multiple ROPs
    node.parm("output_folder").disable(next_index > 2)


def get_stage_render_rops():
    """ Create a list all usdrender_rop nodes in the stage """
    stage_render_rops = []
    filtered_stage_render_rops = []
    stage_node_list = hou.node('/stage').allSubChildren()

    for rop in stage_node_list:
        if rop:
            if rop.type().name() in ('usdrender_rop', 'prism::LOP_Render::1.0'):
                if rop.isBypassed() is False:
                    stage_render_rops.append(rop)
                    
    # Remove any ROPs that might be a child of another ROP
    for needle_rop in stage_render_rops:
        ignore_rop = False
        for haystack_rop in stage_render_rops:
            if haystack_rop.path() in needle_rop.parent().path():
                ignore_rop = True
        if not ignore_rop:
            filtered_stage_render_rops.append(needle_rop)
    
    return filtered_stage_render_rops

def remove_rop_row(node):
    """Remove a variable from the UI.

    Remove the entry at the given index and shift all subsequent entries down.
    """
    curr_count = node.parm("render_rops").eval()
    node.parm("rop_checkbox_{}".format(curr_count)).set(False)
    node.parm("rop_path_{}".format(curr_count)).set("")
    node.parm("rop_frame_range_{}".format(curr_count)).set("")
    # node.parm("rop_use_scout_frames_{}".format(curr_count)).set(False)
    node.parm("render_rops").set(curr_count - 1)

def remove_all_rop_rows(node):
    """Remove all the render rop rows from the UI."""
    curr_count = node.parm("render_rops").eval()
    for i in range(1, curr_count + 1):
        node.parm("rop_checkbox_{}".format(i)).set(False)
        node.parm("rop_path_{}".format(i)).set("")
        node.parm("rop_frame_range_{}".format(i)).set("")
        # node.parm("rop_use_scout_frames_{}".format(i)).set(False)
    node.parm("render_rops").set(0)


def select_all_render_rops(node, **kwargs):
    """Select all the render rops in the UI."""
    curr_count = node.parm("render_rops").eval()
    for i in range(1, curr_count + 1):
        node.parm("rop_checkbox_{}".format(i)).set(True)


def deselect_all_render_rops(node, **kwargs):
    """Deselect all the render rops in the UI."""
    curr_count = node.parm("render_rops").eval()
    for i in range(1, curr_count + 1):
        node.parm("rop_checkbox_{}".format(i)).set(False)


def reload_render_rops(node, **kwargs):
    """Reload the render rop data from the UI."""

    # Remove all the render rops rows from the UI
    remove_all_rop_rows(node)
    # Add all the render rops to the UI
    add_render_ropes(node, render_rops_dict=None)

def update_render_rops(node, **kwargs):
    """Update the render rop data from the UI."""

    render_rops_dict = store_current_render_rop_data(node)
    # Remove all the render rops rows from the UI
    remove_all_rop_rows(node)
    # Add all the render rops to the UI
    add_render_ropes(node, render_rops_dict=render_rops_dict)


def apply_script_to_all_render_rops(node, **kwargs):
    """Apply the given script to all render rops."""
    script = node.parm("override_image_output").evalAsString()
    # print("script: {}".format(script))

    curr_count = node.parm("render_rops").eval()
    for i in range(1, curr_count + 1):
        rop_path = node.parm("rop_path_{}".format(i)).evalAsString()
        driver.apply_image_output_script(rop_path, script)


def resolve_payload(node, path):
    """Resolve the output path for the given node."""

    output_path = ""
    
    LOGGER.debug("RENDER_ROPS path: '%s'", path)
    # Parm gets disabled if multiple ROP are activated
    # Temporarily testing if this logic should be consistent
    if node.parm('output_folder').isDisabled() or True:
        rop_node = hou.node(path)
        
        if rop_node.type().name() == 'usdrender_rop':
            output_parm = rop_node.parm("outputimage")
            
        elif rop_node.type().name() == 'Redshift_ROP':
             output_parm = rop_node.parm("RS_outputFileNamePrefix")
             
        elif rop_node.type().name() == 'arnold':
             output_parm = rop_node.parm("ar_picture")
             
        elif rop_node.type().name() == 'karma':
             output_parm = rop_node.parm("picture")

        # Mantra
        elif rop_node.type().name() == 'ifd':
             output_parm = rop_node.parm("vm_picture")               
        
        else:
            output_parm = rop_node.parm("outputPath")
            
            if output_parm is None:
                raise Exception("Unrecognized ROP: {}".format(path))

        output_image = pathlib.Path(output_parm.eval())
        
        output_path = output_image.parent.as_posix()
        LOGGER.debug('Output path from ROP: "%s"', output_path)
            
    else:
        try:
            output_path = node.parm('output_folder').eval()
            output_path = os.path.expandvars(output_path)
            if output_path and not os.path.exists(output_path):
                os.makedirs(output_path)
            LOGGER.debug("Output path: %s", output_path)
        except Exception as err_msg:
            LOGGER.warning("Unable to set output dir (%s)", err_msg)

    return {"output_path": output_path}

def update_render_with_husk(node, **kwargs):
    
    
    render_with_husk_enabled = bool(kwargs['parm'].eval())
    
    # Iterate through all the nodes and disable/enable if they are compatible
    # with Husk
    curr_count = node.parm("render_rops").eval()
    for i in range(1, curr_count + 1):
        rop_parm = node.parm("rop_path_{}".format(i))

        # Disable ROP if Husk is enabled but ROP can't be rendered in Husk
        disable_rop_in_submitter = not ( not render_with_husk_enabled or
                                        can_render_with_husk(hou.node(rop_parm.evalAsString())))

        [ node.parm(parm.format(index=i)).disable(disable_rop_in_submitter) for parm in ROP_PARMS ]

def can_render_with_husk(node):

    return node.type().name() in ('usdrender_rop', 'prism::LOP_Render::1.0')
