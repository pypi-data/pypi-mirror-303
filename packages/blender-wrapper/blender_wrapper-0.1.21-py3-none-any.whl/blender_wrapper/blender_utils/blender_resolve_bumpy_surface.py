import bpy
import sys
import bmesh
import math
from bmesh.types import BMFace, BMVert
from dataclasses import dataclass
from typing import List


@dataclass
class GFace:
    normal: tuple
    index: int
    vertices: tuple
    degrees: float
    face: BMFace


def get_pyramid_faces(faces: dict, active_face_normal: tuple, threshold: int):
    # verts = [vert for face in faces for vert in face.vertices]
    # # spire_vert = Counter(verts)
    # print(Counter(verts))
    pyrimid_faces = []
    for index, face in faces.items():
        face_angle = math.degrees(face.normal.angle(active_face_normal))
        #print(f'index: {index} ,angle: {face_angle}')
        # face_angle equals to 0 means the face is the active face.
        if len(face.verts) == 3 and face_angle > threshold:
            gface = GFace(face.normal, index, tuple(v.index for v in face.verts), face_angle, face)
            pyrimid_faces.append(gface)

    return pyrimid_faces if len(pyrimid_faces) == 2 else []


def get_connected_faces(face: BMFace) -> dict:
    connected_faces = {}
    for edge in face.edges:
        for f in edge.link_faces:
            if f.index not in connected_faces and f.normal.length > 0:
                connected_faces[f.index] = f
    return connected_faces


def select_bumpy_faces(faces: List[BMFace], threshold: int):
    """The surface of the model genreated by the point cloud has some "pyiramid" shape faces.
    This function will select the faces that are considered as bumpy.
    The example image could be found from : doc/images/blender/blender_surface_remesh_001.png 

    Args:
        faces (List[BMFace]): Represent the faces of the model.
        threshold (int): Represent the angle threshold for the bumpy surfaces.
    """
    bpy.ops.mesh.select_all(action="DESELECT")
    for active_face in faces:
        if active_face.select and active_face.normal.length == 0:
            continue
        connected_faces = get_connected_faces(active_face)
        if len(connected_faces) == 4:
            pyrimid_faces = get_pyramid_faces(connected_faces, active_face.normal, 80)
            if pyrimid_faces:
                #print(f'matched faces: {len(pyrimid_faces)}')
                active_face.select = True
                for gface in pyrimid_faces:
                    # get the matched faces into selection
                    gface.face.select = True
