""" Install fake-bpy-module-latest to assist the code completion of blender APIs
"""
from enum import Enum
import os
import sys
from dataclasses import dataclass
from os.path import dirname
from typing import List
import argparse

import bmesh
import bpy
from bmesh.types import BMFace


from blender_utils.blender_context_manager import mesh_edit  # noqa

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')


class ConstKeys:
    path = 'path'
    file = 'file'
    volume = 'volume'
    texture = 'texture'


@dataclass
class BParams:
    file_path: str
    export_path: str
    argv: List[str]
    _ext_name: str = ""
    _export_ext_name: str = ""
    mesh_name: str = ""

    def __post_init__(self):
        self.ext_name = self.file_path[-3:].lower()
        self.export_ext_name = self.export_path[-3:].lower()
        self.mesh_name = os.path.basename(self.file_path[:-4])
        self.load()

    def load(self):
        try:
            # clean up default cube mesh
            cube_ob = bpy.data.objects.get('Cube')
            if cube_ob:
                bpy.data.objects.remove(cube_ob, do_unlink=True)

            print(f'Loading file: {self.file_path}')

            if self.ext_name == 'ply':
                bpy.ops.wm.ply_import(filepath=self.file_path)
            elif self.ext_name == 'obj':
                bpy.ops.wm.obj_import(
                    filepath=self.file_path, forward_axis='Y', up_axis='Z')
            elif self.ext_name == 'fbx':
                bpy.ops.import_scene.fbx(filepath=self.file_path)
            elif self.ext_name == 'stl':
                bpy.ops.import_mesh.stl(
                    filepath=self.file_path, axis_forward='Y', axis_up='Z')
            elif self.ext_name in ['glb', 'gltf']:
                bpy.ops.import_scene.gltf(
                    filepath=self.file_path, import_shading='NORMALS')
            else:
                print(f'Unsupported file: {self.file_path}')
                sys.exit(1)
            print(f'Loaded file: {self.file_path}')

            # active the imported mesh
            bpy.ops.object.select_all(action='DESELECT')
            obj = bpy.data.objects[self.mesh_name]
            # ensure loaded object data is a single user
            obj.data = obj.data.copy()
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

        except Exception as e:
            print(f'Error: {e}')
            sys.exit(1)

    def export(self, mesh_name=None):
        """Export the specified mesh to a file.

        Args:
            mesh_name (str, optional): Represent the specific mesh name. Defaults will be using the import mesh name.
        """
        # merge vertices before exporting
        with mesh_edit(mesh_name=mesh_name or self.mesh_name):
            print(f'Merged vertices:[{mesh_name or self.mesh_name}]')
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.mesh.remove_doubles()

        print(
            f'Export selected mesh:[{mesh_name or self.mesh_name}] to {self.export_path}')

        if self.export_ext_name == 'stl':
            bpy.ops.export_mesh.stl(filepath=self.export_path,
                                    use_selection=True,
                                    use_mesh_modifiers=True,
                                    axis_forward='Y',
                                    axis_up='Z')
        elif self.export_ext_name == 'ply':
            bpy.ops.wm.ply_export(filepath=self.export_path,
                                  export_selected_objects=True,
                                  export_colors='NONE',
                                  export_normals=True,
                                  export_uv=True,
                                  apply_modifiers=True)
        elif self.export_ext_name == 'obj':
            bpy.ops.wm.obj_export(filepath=self.export_path,
                                  export_selected_objects=True,
                                  apply_modifiers=True,
                                  forward_axis='Y',
                                  export_uv=True,
                                  up_axis='Z')
        elif self.export_ext_name == 'fbx':
            bpy.ops.export_scene.fbx(filepath=self.export_path,
                                     use_selection=True,
                                     use_mesh_modifiers=True,
                                     axis_forward='Y',
                                     axis_up='Z')
        elif self.export_ext_name == 'glb':
            bpy.ops.export_scene.gltf(
                filepath=self.export_path,
                export_format='GLB',
                export_normals=True,
                export_materials='EXPORT',
                export_copyright='Syngular Technology',
                export_all_vertex_colors=False,
                use_selection=True
            )
        else:
            print(f'unsupported file extension: {self.export_ext_name}')
            sys.exit(1)


def parse_args() -> BParams:
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    file_path = argv.pop(0)
    output_path = argv.pop(0)
    return BParams(file_path, output_path, [*argv])
