import os
import pathlib
import re

import hou

import ciocore.loggeria

from ciohoudini import frames, context

LOGGER = ciocore.loggeria.get_conductor_logger()

CMD_TEMPLATES = {'hython': "{hserver}hython \"{script}\" -f {first} {last} {step} -d {driver} \"{hipfile}\"",
                 #'husk':   "husk --make-output-path --no-mplay --threads 0 --verbose 9aC --fast-exit 0 -s {render_settings} -R {hydra_delegate} --frame {first} --frame-count {count} --frame-inc {step} -o {output_path} {usd_file}"
                 'husk':   "husk --make-output-path --no-mplay --threads 0 --verbose 9aC -s {render_settings} -R {hydra_delegate} --frame {first} --frame-count {count} --frame-inc {step} -o {output_path}.{first}.{output_ext} {usd_file}"
                }

def get_task_cmd(node, cmd_template_name='hython', task_template_override_value=None, **kwargs):
    """Get the task template from the node."""
        
    rop_path = kwargs.get("rop_path", None)
    
    render_script = node.parm("render_script").eval()
    render_scene = node.parm("render_scene").eval()
    host_version = node.parm("host_version").eval()
    usd_render_settings = None
    hydra_delegate = None
    usd_file = None
    output_path = None
    output_ext = ""

    try:
        rop_path = os.path.expandvars(rop_path)
    except Exception as e:
        raise Exception("Error expanding rop path {}: {}".format(rop_path, e))

    try:
        render_scene = os.path.expandvars(render_scene)
    except Exception as e:
        raise Exception("Error expanding render scene {}: {}".format(render_scene, e))
    
    rop_node = hou.node(rop_path)
    LOGGER.debug("Looking at LOP ROP: %s (%s)", rop_node, rop_node.type())
    
    if rop_node.type().name() == 'usdrender_rop': 
        usd_render_settings = rop_node.parm("rendersettings").eval()
        hydra_delegate = rop_node.parm("renderer").eval()
        output_image_path = pathlib.Path(rop_node.parm("outputimage").eval())
        
        try:
            new_output_image_name = output_image_path.name.split(".")[0]
            output_path = output_image_path.with_name(new_output_image_name).as_posix()
            
            output_ext = output_image_path.suffix
            LOGGER.debug("output_image: %s", output_path)
        
        except Exception as err_msg:
            raise Exception("Please set the parm Override Output Image on the node '{}'.\n  ({}):\n{}".format(rop_node, err_msg))
            
        output_usd_path = pathlib.Path(rop_node.parm("lopoutput").eval())
        usd_file = pathlib.Path(rop_node.parm("lopoutput").eval().replace("__render__", output_image_path.as_posix()))
        usd_file = usd_file.as_posix().replace(usd_file.drive, "")
        LOGGER.debug("usd_file1: %s", usd_file)
    
    elif rop_node.type().name() == 'prism::LOP_Render::1.0':
        usd_render_settings = rop_node.parm("renderSettings").eval()
        hydra_delegate = rop_node.parm("renderer").eval()
        
        # Strip the drive letters
        usd_path = pathlib.Path(rop_node.parm("outputPathCache").eval())
        if usd_path:
            usd_file = usd_path.as_posix().replace(usd_path.drive, "")

        output_path =  pathlib.Path(rop_node.parm("outputPath").eval())        
        output_ext = output_path.suffix
        if output_path:
            output_path = output_path.as_posix().replace(output_path.drive, "")

        output_path = ".".join(output_path.split(".")[0:-2])
        
                                    
    else:
        usd_render_settings = None  
        hydra_delegate = None
        usd_file = None

    data = {
        "script": re.sub("^[a-zA-Z]:", "", render_script).replace("\\", "/"),
        "first": kwargs.get("first", 1),
        "last":  kwargs.get("last", 1),
        "step": kwargs.get("step", 1),
        "count":  kwargs.get("last", 1) -  kwargs.get("first", 1) + 1,
        "driver": rop_path, # Use the rop path instead of the driver path.
        "hipfile": render_scene,
        "hserver": "",
        "render_settings": usd_render_settings,
        "hydra_delegate": hydra_delegate,
        "usd_file": usd_file,
        "output_path": output_path,
        "output_ext": output_ext
    }

    LOGGER.debug("Using data for task_template: %s", data)

    try:
        host_version = int(host_version.split()[1].split(".")[0])
    except:
        host_version = 19

    if host_version < 19:
        data["hserver"] = "/opt/sidefx/houdini/19/houdini-19.0.561/bin/hserver --logfile /tmp/hserver.log -C -D; "

    task_cmd_template = task_template_override_value or CMD_TEMPLATES[cmd_template_name]

    LOGGER.debug("-----TASK_TEMPLATE: '%s' ", task_cmd_template)
    
    return task_cmd_template.format(**data)

def resolve_payload(node, **kwargs):
    """
    Resolve the task_data field for the payload.

    If we are in sim mode, we emit one task.
    """
    task_limit = kwargs.get("task_limit", -1)
    frame_range = kwargs.get("frame_range", None)
    
    if node.parm("is_sim").eval():
        cmd = node.parm("task_template").eval()
        tasks = [{"command": cmd, "frames": "0"}] 
        return {"tasks_data": tasks}
    
    tasks = []
    resolved_chunk_size = frames.get_resolved_chunk_size(node, frame_range=frame_range)
    sequence = frames.main_frame_sequence(node, frame_range=frame_range, resolved_chunk_size=resolved_chunk_size)
    chunks = sequence.chunks()
    
    if node.parm("render_with_husk").eval():
        cmd_template_name = "husk"
        
    else:
        cmd_template_name = "hython"
    
    for i, chunk in enumerate(chunks):
        
        if task_limit > -1 and i >= task_limit:
            break
        
        # Get the frame range for this chunk.
        kwargs["first"] = chunk.start
        kwargs["last"] = chunk.end
        kwargs["step"] = chunk.step
        
        # Get the task command - ignores the value in the parm `task_template`
        task_template_override_value = None

        if not node.parm("task_template").isAtDefault():
            task_template_override_value = node.parm("task_template").eval()
        
        cmd = get_task_cmd(node, cmd_template_name, task_template_override_value=task_template_override_value, **kwargs)
        
        #######################################################################
        # Due to changes necessary to support multiple ROPs, the Task template
        # parameter is never used. This needs to be resolved.
        #######################################################################
        #
        # Set the context for this chunk.
        #context.set_for_task(first=chunk.start, last=chunk.end, step=chunk.step)
        #cmd = node.parm("task_template").eval()

        tasks.append({"command": cmd, "frames": str(chunk)})        

    return {"tasks_data": tasks}