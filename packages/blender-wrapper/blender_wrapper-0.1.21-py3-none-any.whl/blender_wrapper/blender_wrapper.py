"""Blender batch mode (CLI)

"""
import json
import os
import subprocess
import sys
from os.path import abspath, dirname
from .utils.singleton import singleton
import logging
from .utils.runtime import is_running_in_jupyter
from typing import List

SCRIPT_MAPPING = {
    'array_objects_by_curve': 'array_objects_by_curve.py',
    'blender_modifier_decimate': 'blender_modifier_decimate.py',
    'blender_remove_doubles': 'blender_remove_doubles.py',
    'blender_modifier': 'blender_modifier.py',
    'blender_file_converter': 'blender_file_converter.py',
    'blender_set_mesh_origin': 'blender_set_mesh_origin.py',
    'blender_set_mesh_uvmap': 'blender_set_mesh_uvmap.py',
    'blender_bake_texture': 'blender_bake_texture.py',
    'blender_resolve_bumpy_surface': 'blender_resolve_bumpy_surface.py',
    'blender_reconstruct_mesh': 'blender_reconstruct_mesh.py',
    'blender_separate_mesh': 'blender_separate_mesh.py',
    'blender_convert_textured_glb': 'blender_convert_textured_glb.py',
    'blender_simplify_mesh': 'blender_simplify_mesh.py',
    'blender_set_sharp_edge': 'blender_set_sharp_edge.py',
    'blender_generate_convex_hull': 'blender_generate_convex_hull.py'
}


def get_script_path(script_name: str):

    if script_name not in SCRIPT_MAPPING:
        script_path = os.path.join(
            dirname(abspath(__file__)), f'{script_name}.py')
        if os.path.exists(script_path):
            return script_path
        else:
            raise ValueError(f'Invalid script name: {script_name}')

    return os.path.join(dirname(abspath(__file__)), SCRIPT_MAPPING[script_name])


@singleton
class BlenderWrapper():
    def __init__(self, blender_path: str = None):
        if not os.path.isfile(blender_path):
            raise FileNotFoundError('Invalid blender executable path')

        self.blender_path = blender_path

    def run(self, *args, scene_path=None):
        params = list(['--background'])
        if scene_path:
            params.append(f'"{scene_path}"')
        params += ['--python', *args]
        params.insert(0, os.path.join(self.blender_path))
        logging.debug(
            f'Running command: {os.path.basename(self.blender_path)}')
        logging.debug(f'parameters: {params}')

        if is_running_in_jupyter():
            process = subprocess.Popen(
                ' '.join(params), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()
        else:
            process = subprocess.Popen(' '.join(params), stdout=sys.stdout)
            output, error = process.communicate()

        if process.returncode != 0:
            raise SystemError(error, os.path.basename(self.blender_path))

        return output


def array_objects_by_curve(config_path: str):
    param = [get_script_path('array_objects_by_curve'),
             '--', config_path]
    BlenderWrapper().run(*param)


def modifier_decimate(file_path: str, output: str = None, decimate_ratio: float = 0.4):
    """The Decimate modifier allows you to reduce the vertex/face count
    of a mesh with minimal shape changes.

    Args:
        file_path (str): represent the file path
        output (str, optional): represent the output file path
        decimate_ratio (float, optional): represent the factor of the decimate level. Defaults to 0.4.
    """
    if not (0 < decimate_ratio < 1):
        logging.debug(
            f'Skip processing the decimate modifier, as the ratio ({decimate_ratio}) is not in the range of [0, 1]')
        return

    param = [get_script_path('blender_modifier_decimate'),
             '--', file_path, output or file_path, str(decimate_ratio)]
    BlenderWrapper().run(*param)


def blender_remove_doubles(file_path: str, output: str = None, is_smooth: bool = True):
    output = output or file_path
    param = [get_script_path('blender_remove_doubles'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             str(is_smooth)]
    BlenderWrapper().run(*param)


def blender_set_sharp_edge(file_path: str, output: str = None, angle: float = 60):
    output = output or file_path
    param = [get_script_path('blender_set_sharp_edge'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             str(angle)]
    BlenderWrapper().run(*param)


def blender_modifier(file_path: str, output: str = None, modifiers: list = None):
    """Batch process modifiers.

    Args:
        file_path (str): Represent the import ply file path.
        output (str): Represent the output ply file path.
        modifiers (list, optional): Represent the modifiers to be processed. Defaults to None.
                                    (i.e. ['decimate,0.2,True,COLLAPSE', 'remesh,SMOOTH,9,True,True', 'smooth,0.3,3'])
    """
    if not modifiers:
        logging.warning(f'[Blender] Skip batch processing modifiers')
        return
    output = output or file_path
    param = [get_script_path('blender_modifier'),
             '--',
             f'"{file_path}"',
             f'"{output}"']
    param += modifiers
    BlenderWrapper().run(*param)


def blender_file_converter(file_path: str, output: str = None, scale_factor: float = 1.0):
    output = output or file_path
    param = [get_script_path('blender_file_converter'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             f'"{scale_factor}"']
    BlenderWrapper().run(*param)


def blender_set_mesh_origin(file_path: str, output: str = None, origin=[0, 0, 0]):
    """Set new origin by moving vertex positions.

    Args:
        file_path (str): Represent the import ply file path.
        output (str): Represent the output ply file path.
        origin (list, optional): Represent the new origin location. Defaults to [0, 0, 0].
    """
    output = output or file_path

    if not any(x != 0 for x in origin):
        logging.warning(f'[Blender] Skip setting new origin to {origin}')

    param = [get_script_path('blender_set_mesh_origin'),
             '--',
             f'"{file_path}"',
             f'"{output}"']
    param += list(map(lambda x: str(x), origin))
    BlenderWrapper().run(*param)


def blender_set_mesh_uvmap(file_path: str, output: str, iterations: int = 12):
    param = [get_script_path('blender_set_mesh_uvmap'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             str(iterations)]
    BlenderWrapper().run(*param)


def blender_bake_textures(
        scene_path: str,
        file_path: str,
        output: str,
        material: str,
        mode: str,
        model_scale: float = 1.0,
        texture_size: int = 512,
        environment_texture: str = None,
        lighting_strength: float = 0.4,
        output_scene: str = ''
):
    param = [get_script_path('blender_bake_texture'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             material,
             mode,
             str(model_scale),
             str(texture_size),
             environment_texture,
             str(lighting_strength),
             output_scene]
    BlenderWrapper().run(*param, scene_path=scene_path)


def blender_resolve_bumpy_surface(file_path: str, output: str = None):
    output = output or file_path
    param = [get_script_path('blender_resolve_bumpy_surface'),
             '--',
             f'"{file_path}"',
             f'"{output}"']
    BlenderWrapper().run(*param)


def blender_reconstruct_mesh(file_path: str, output: str = None):
    output = output or file_path
    param = [get_script_path('blender_reconstruct_mesh'),
             '--',
             f'"{file_path}"',
             f'"{output}"']
    BlenderWrapper().run(*param)


def blender_separate_mesh(file_path: str, output: str = None, min_volume_threshold: int = 0.0001):
    """_summary_

    Args:
        file_path (str): represent the file path
        output (str, optional): represent the output path. Defaults to None.
        min_volume_threshold (int, optional): represent the volume threshold. Defaults to 0.0001 m3.
                                              the mesh will be ignored if the volume is smaller 
                                              than this threshold.

    Returns:
        dict: represent the separated mesh. below is the example:
        {
            "sample1": {
                "path": "P:\\pwh\\sample1.ply",
                "volume": 0.0006
        }
        note: the volume is calculated by the object dimensions x*y*z
    """
    output = output or file_path
    output_config_path = f'{file_path[:-4]}_sub_meshes.json'
    param = [get_script_path('blender_separate_mesh'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             output_config_path,
             str(min_volume_threshold)]
    BlenderWrapper().run(*param)
    return json.load(open(output_config_path))


def blender_export_textured_glb(file_path: str, output: str, texture: str):
    if output[-3:].lower() != 'glb':
        raise ValueError(f"Output path is not GLB format.")
    param = [get_script_path('blender_convert_textured_glb'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             f'"{texture}"']
    BlenderWrapper().run(*param)


def blender_simplify_mesh(file_path: str, output: str, threshold: float = 0):
    param = [get_script_path('blender_simplify_mesh'),
             '--',
             f'"{file_path}"',
             f'"{output}"',
             str(threshold)]
    BlenderWrapper().run(*param)


def blender_generate_convex_hull(output: str, input_files: List[str]):
    param = [get_script_path('blender_generate_convex_hull'),
             '--',
             f'"{output}"',
             *input_files]
    BlenderWrapper().run(*param)
