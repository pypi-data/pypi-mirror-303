import bpy


def enable_gpus():
    pref = bpy.context.preferences
    cycles_addon = pref.addons["cycles"]
    cpref = cycles_addon.preferences
    cpref.compute_device_type = "CUDA"
    cpref.compute_device = "CUDA_0"

    # Enable and list all devices, or optionally disable CPU
    print("----------------------------------------------")
    cpref.get_devices()

    for d in cpref.devices:
        d.use = True
        if d.type == "CPU":
            d.use = False
        print(f"Device '{d.name}' type {d.type} : {d.use}")
