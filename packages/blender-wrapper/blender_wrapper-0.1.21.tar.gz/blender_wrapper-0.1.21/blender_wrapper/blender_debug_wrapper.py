

import importlib
import math
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import reduce, wraps
from re import X
from timeit import default_timer as timer
from typing import List

import bpy
import numpy as np
from bmesh.types import BMesh, BMVert
from mathutils import Vector, geometry

sys.path.append(r'P:\Dev\DeepTars\command_router\blender_app')

from blender_utils import blender_const as keys  # noqa
# from blender_utils.blender_resolve_bumpy_surface import select_bumpy_vertices  # noqa
from blender_utils.blender_context_manager import mesh_edit  # noqa

# force reload the imported modules
importlib.reload(keys)

# if "ConstKeys" in locals():
#     importlib.reload(blender_utils.blender_file_loader)

# else:
#     import blender_utils.blender_file_loader
# ConstKeys = blender_utils.blender_file_loader.ConstKeys


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        start_time = timer()
        result = f(*args, **kw)
        end_time = timer()
        print(f'elapsed time - {f.__name__}: {end_time - start_time}')
        return result
    return wrap


def calculate_point_assembles(arr: List[Vector]) -> List[List[Vector]]:
    """Calculate the point assemblies.
    The point assemblies are the groups of points that are close to each other.
    The point assemblies are used to calculate the surface area.

    Args:
        arr (List[Vector]): Represent the points of the model.

    Returns:
        List[List[Vector]]: Represent the point assemblies.
    """
    assemble_arr = []
    if len(arr) > 3:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for n in range(j+1, len(arr)):
                    assemble_arr.append([arr[i], arr[j], arr[n]])
    else:
        assemble_arr = [arr]
    return assemble_arr


def calculate_distance_np(p: Vector, plane_pts: List[Vector]):
    """Calculate the distance between the point and the line formed by the three points.
    We are given three points, and we seek the equation of the plane that goes through 
    them. The method is straight forward. A plane is defined by the equation:

    ax+by+cz=d

    Ref: https://kitchingroup.cheme.cmu.edu/blog/2015/01/18/Equation-of-a-plane-through-three-points/

    The above reference has a mistake in the formula. The correct formula(-d, not +d) is:
    Distance = (| a*x1 + b*y1 + c*z1 - d |) / (sqrt( a*a + b*b + c*c))

    Args:
        p (Vector): Represent the target point which is the point to be calculated the distance.
        plane_pts (Vector): Represent the three points of the plane.
    """
    p1 = plane_pts[0]
    p2 = plane_pts[1]
    p3 = plane_pts[2]

    # These two vectors are in the plane
    v1 = p3 - p1
    v2 = p2 - p1
    # the cross product is a vector normal to the plane
    cp = v1.cross(v2)
    a, b, c = cp
    # This evaluates a * x3 + b * y3 + c * z3 which equals d
    d = cp.dot(p3)

    d = abs((a * p.x + b * p.y + c * p.z - d))
    e = (math.sqrt(a * a + b * b + c * c))
    distance = d/e if e != 0 else 0
    area = geometry.area_tri(plane_pts[0], plane_pts[1], plane_pts[2])
    return distance, Vector(cp).normalized(), area


def calculate_distance(p: Vector, plane_pts: List[Vector]):
    if not plane_pts:
        return 0, Vector(), 0

    if 0 < len(plane_pts) < 3:
        raise ValueError('The number of points must be greater than 3.')

    p0 = plane_pts[0]
    p1 = plane_pts[1]
    p2 = plane_pts[2]

    U = Vector()
    V = Vector()
    normal = Vector()

    U.x = p1.x-p0.x
    V.x = p2.x-p0.x  # basis vectors on the plane
    U.y = p1.y-p0.y
    V.y = p2.y-p0.y
    U.z = p1.z-p0.z
    V.z = p2.z-p0.z

    normal.x = (U.y*V.z)-(U.z*V.y)      # plane normal
    normal.y = (U.z*V.x)-(U.x*V.z)
    normal.z = (U.x*V.y)-(U.y*V.x)

    dist = math.sqrt((normal.x*normal.x) + (normal.y*normal.y) + (normal.z*normal.z))  # normalized

    normal.x /= dist
    normal.y /= dist
    normal.z /= dist

    # calculate the area value of the triangle
    area = geometry.area_tri(p0, p1, p2)

    # calculate the distance from the point to the plane
    distance = abs((p.x-p0.x)*normal.x + (p.y-p0.y)*normal.y + (p.z-p0.z)*normal.z)

    return distance, normal, area


def calculate_distance_on_vertices(target: BMVert, verts: List[BMVert], min_area_threshold=0.1):  # p0: Vector, p1: Vector, p2: Vector):
    """Calculate the distance between the point and the line formed by the three points.
    https://stackoverflow.com/questions/55189333/how-to-get-distance-from-point-to-plane-in-3d
    """
    p: Vector = target.co
    # represent the plane normal
    direction: Vector = Vector()
    # represent the max area of the triangle
    max_area: float = 0
    # represent the distance from the point to each vertice of the 'plane'
    distance_list: list[float] = []

    pts_groups = calculate_point_assembles(verts)

    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:

        dataset = [{'p': target.co,
                    'plane_pts': [p.co for p in pts_group]}
                   for pts_group in pts_groups]
        results = list(executor.map(lambda param: calculate_distance_np(**param), dataset))

    for (distance, normal, area) in results:

        # ignore the surface that 3 points are almost aligned in the line
        # 0.1 threshold could help filter the valid surfaces
        if area < min_area_threshold:
            continue
        # find the normal of the max area triangle
        elif area > max_area:
            max_area = area
            direction = normal

        distance_list.append(distance)

    return sorted(distance_list, reverse=True), direction


def flatten_bumpy_vertices(bm: BMesh, verts: List[BMVert], max_distance_threshold: int = 0.2):
    """The surface of the model genreated by the point cloud has some "pyiramid" shape faces.
    This function will select the vertices that are considered as bumpy.
    The example image could be found from : doc/images/blender/blender_surface_remesh_002.png

    Args:
        verts (List[BMVert]): Represent the vertices of the model.
        max_distance_threshold (int): Represent the angle threshold for the bumpy surfaces.
        is_dissolve (bool): If True, the vertices that are considered as bumpy will be removed, 
                            but keep the connected faces

    """
    print('====================')

    diversity_threshold: int = 0.03

    bpy.ops.mesh.select_all(action="DESELECT")

    selected_verts = []

    for progress_index, active_vert in enumerate(verts):

        connected_verts = []

        for ed in active_vert.link_edges:
            connected_verts.append(ed.other_vert(active_vert))

        # calculate the distance between the point and the planes formed by the all the vertices

        distance_list, direction = calculate_distance_on_vertices(active_vert, connected_verts)

        # remove the last shortest distance for getting better average value
        distance_list = [dist for dist in distance_list if dist > max_distance_threshold]

        # ignore invalid vector direction which is equal to zero
        # print(f'distance_list: {distance_list}')
        # print(f'direction: {direction}')
        if not direction.length or not len(distance_list):
            continue

        # reverse the direction if the angle is larger than 90 degrees
        normal_angle = math.degrees(active_vert.normal.angle(direction))
        # correct vector direction if the angle is larger than 90 degrees
        direction = direction * -1 if normal_angle > 90 else direction

        # calculate the standard deviation of the distance list
        distance_deviation = np.sqrt(np.var(distance_list))
        # calculate the average distance
        ave_distance = np.average(distance_list) if len(distance_list) > 1 else distance_list.pop()

        # print(f'{progress_index}/{len(verts)}: {active_vert.index} {ave_distance} {distance_deviation}')

        # print(f'ave_distance: {ave_distance} - distance_deviation: {distance_deviation}')
        # check the distance deviation and the average distance
        # it would skip if the distance doesn't meet the criteria
        if ave_distance < max_distance_threshold or distance_deviation > diversity_threshold:
            continue

        active_vert.select = True

        selected_verts.append([active_vert, direction*ave_distance])

        sys.stdout.write(f'\r{progress_index}/{len(verts)}')
        sys.stdout.flush()

    bpy.ops.mesh.dissolve_mode(use_verts=True)

    # batch translate the vertices
    # if is_dissolve:
    #     # remove the selected verts but keep the connected faces
    #     bpy.ops.mesh.dissolve_mode(use_verts=True)
    # else:
    #     with ThreadPoolExecutor(max_workers=10) as executor:

    #         dataset = [{'verts': [vert],
    #                     'vec': vec}
    #                    for (vert, vec) in selected_verts]
    #         list(executor.map(lambda param: bmesh.ops.translate(bm, **param), dataset))


def calculate_edges_angle(bm: BMesh, v0: BMVert, v1: BMVert, v2: BMVert):
    # find the vector representation of each edge
    # first get the indices of the vertices which represent the edge

    # now get the coordinates of those vertices and make a vector from them
    V0 = Vector(v1.co) - Vector(v0.co)
    V1 = Vector(v2.co) - Vector(v0.co)

    # find the angle between them
    return math.degrees(V0.angle(V1))


def separate_looping_vertces(verts: List[List[int]]):
    full_verts = [v for f_verts in verts for v in f_verts]
    # Get the first group of face vertices for finding the looping vertices
    f_indexes = verts.pop(0)
    # represent the loop vertices
    loop_verts = []

    for f_index in f_indexes:
        # add the vertice to the loop vertices
        loop_verts.append(f_index)

        near_f_indexes = next(iter([f_idx for f_idx in verts if f_index in f_idx]), None)
        while near_f_indexes:
            # remove the previous face index from the list
            near_f_indexes.remove(f_index)
            # remove the matched group from the list, so that it won't be matched again
            verts.remove(near_f_indexes)
            # get the next face index for finding the matched group
            f_index = near_f_indexes[0]
            # add the vertice to the loop vertices
            loop_verts.append(f_index)
            # prepare vertices group for finding the next matched group
            near_f_indexes = next(iter([f_idx for f_idx in verts if near_f_indexes[0] in f_idx]), None)

    the_other_loop_list = list(set(full_verts) - set(loop_verts))
    return sorted([list(set(loop_verts)), the_other_loop_list], key=len)


def find_distinct_vertices(bm: BMesh, vert: BMVert):
    """Find the distinct vertices in the given list of vertices.
    The coherent looping vertices will be put into a same group.

    Args:
        verts (List[BMVert]): Represent the vertices of the model.

    Returns:
        List[BMVert]: Represent the distinct vertices.

    """
    linked_edge_indexes = set([e.index for e in vert.link_edges])
    all_edges = set([e.index for f in vert.link_faces for e in f.edges])

    outter_edges = [bm.edges[i] for i in all_edges.difference(linked_edge_indexes)]
    outter_verts = {v.index: v for e in outter_edges for v in e.verts}

    start_edge = outter_edges.pop(0)
    selected_edge_group = [start_edge]
    shared_vert = None
    for loop_vert in start_edge.verts:
        while matched := list(e for e in outter_edges if loop_vert in e.verts):
            if len(matched) > 1:
                shared_vert = loop_vert
                break
            next_edge = matched.pop()
            selected_edge_group.append(next_edge)
            outter_edges.remove(next_edge)
            loop_vert = next_edge.other_vert(loop_vert)

    selected_vert_group = {v.index: v for e in selected_edge_group for v in e.verts}

    others_verts = set(outter_verts.values()).difference(set(selected_vert_group.values()))
    # added the shared vertices
    if shared_vert:
        others_verts.add(shared_vert)

    return list(selected_vert_group.values()), list(others_verts)


def merge_vertices(bm: BMesh, verts: List[BMVert], min_distance_threshold: float = 0.2):
    """Merge the vertices that are close to each other.

    Args:
        verts (List[BMVert]): Represent the vertices of the model.
    """
    # print('====================')
    bpy.ops.mesh.select_all(action="DESELECT")
    for progress_index, active_vert in enumerate(verts):
        if active_vert.select:
            continue
        # represnt the index of the connected vertices
        conn_vert_indexes = []
        # represent the vertices that are connected to the active vertice
        conn_verts = {}
        for f in active_vert.link_faces:
            for v in f.verts:
                conn_verts[v.index] = v

        for f in active_vert.link_faces:
            conn_vert_indexes.append([v.index for v in f.verts if v.index != active_vert.index])

        # represent the vertice indexes group that are looping (i.e., [[1,2,3], [4,5,6]])
        (vert_group_0, vert_group_1) = find_distinct_vertices(bm, active_vert)
        if len(vert_group_0) < 3 or len(vert_group_1) < 3:
            continue

        distance_list_0, _ = calculate_distance_on_vertices(active_vert, vert_group_0)
        distance_list_1, _ = calculate_distance_on_vertices(active_vert, vert_group_1)

        # calculate the average distance for both groups
        # the following code would pick up the larger average distance group to process
        g_0_ave_distance = np.average(distance_list_0)
        g_1_ave_distance = np.average(distance_list_1)

        # if the distance can't meet the criteria, skip the processing
        if not distance_list_0 or max(g_0_ave_distance, g_1_ave_distance) < min_distance_threshold:
            continue

        active_vert.select = True

        sys.stdout.write(f'\r{progress_index}/{len(verts)}')
        sys.stdout.flush()

    bpy.ops.mesh.dissolve_mode(use_verts=True)


@timing
def separate_chaos_vertices(bm, is_selected_only: bool = False, max_linked_face_num: int = 6):
    verts = [v for v in bm.verts if v.select == is_selected_only and len(v.link_faces) > max_linked_face_num]
    merge_vertices(bm, verts=verts)


cfg = {
    keys.ARG_FILE: 'test'
}
print(cfg)

# meshes = {}
# for index, obj in enumerate(bpy.data.objects):
#     dimension = reduce(lambda x, y: x*y, obj.dimensions)
#     if dimension < 800:
#         bpy.data.objects.remove(obj, do_unlink=True)
#     else:
#         meshes[obj.name] = reduce(lambda x, y: x*y, obj.dimensions)
# print(len(bpy.data.objects))
# meshes = {}
# for obj in bpy.data.objects:

#     with mesh_edit(mesh_name=obj.name, is_force_deselect=True, is_clean_up_mesh=False) as bm:
#         bm.faces.ensure_lookup_table()
#         meshes[obj.name] = len(bm.faces)
