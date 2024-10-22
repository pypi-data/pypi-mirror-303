#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# **************************************************
__author__  = "Teddy Chantrait"
__email__   = "teddy.chantrait@gmail.com"
__status__  = "Development"
__date__    = "2024-06-07 18:20:10.418626"
__version__ = 1.0
# **************************************************
import pyvista as pv
from mgmetis import metis
from mgmetis.enums import OPTION
import numpy as np
import inspect
from scipy.spatial import KDTree
import vtk
from . import utils as COUT


class meshIntersector(pv.UnstructuredGrid, COUT.utils):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self._kdt_elt_center: KDTree = None
        self._kdt_pts: KDTree = None

    def _build_kdt_elt_center(self):
        self._kdt_elt_center = KDTree(self.cell_centers().points)

        # mecanisme to call only once this fonction
        self_fct_name = inspect.currentframe().f_code.co_name
        self.__dict__[self_fct_name] = self.do_nothing

    def _build_kdt_pts(self):
        self._kdt_pts = KDTree(self.points)

        # mecanisme to call only once this fonction
        self_fct_name = inspect.currentframe().f_code.co_name
        self.__dict__[self_fct_name] = self.do_nothing

    def build_trace_at_elt_center(self, msh:pv.UnstructuredGrid=None, eps=1e-4,
                                  intersection_field_name=""):
        ifname = intersection_field_name
        self._build_kdt_elt_center()
        dd, ii = self._kdt_elt_center.query(msh.cell_centers().points, eps=eps)
        trace_in_given_mesh = np.argwhere(dd < 1e-7).flatten()
        trace_in_current_mesh = ii[trace_in_given_mesh]
        if ifname != "":
            c_keys = list(msh.cell_data.keys())
            if ifname in c_keys:
                print("WARNING intersection_field_name {} already exist in the \
                given mesh\nKnown cell data are {}".format(ifname, c_keys))
            tmp = np.ones(msh.number_of_cells, dtype=np.int32) * -1
            tmp[ifname] = 1
            msh.interface.cell_data[ifname] = tmp
        return trace_in_given_mesh, trace_in_current_mesh
        # for ifiled in fields_to_transfert["cell"]:
        #     test = np.ones(interface.number_of_cells, dtype=np.int32) * -1
        #     test[trace] = ifiled[1][ii]
        #     interface.cell_data[ifiled[0]] = test

    def build_trace_at_pts(self, pts, eps=1e-4):
        self._build_kdt_pts()
        dd, ii = self._kdt_pts.query(pts, eps=eps)
        trace_in_given_mesh = np.argwhere(dd < 1e-7).flatten()
        trace_in_current_mesh = ii[trace_in_given_mesh]
        return trace_in_given_mesh, trace_in_current_mesh


def build_map_eltype_dim(mesh: pv.UnstructuredGrid= None):
    """
    return a dictionnary containing for each element type a dictionnary.
    That one has 2 fields:
    dim : the geometrical dimmension of the element
    vtktype : the vtktype integer associated
    see https://docs.pyvista.org/version/stable/api/core/_autosummary/pyvista.UnstructuredGrid.celltypes.html
    """
    dims = {}
    for k in mesh.cells_dict.keys():
        cellType = pv.CellType(k)
        c = vtk.vtkCellTypeSource()
        c.SetCellType(cellType)
        dim = c.GetCellDimension()
        dims[cellType.name] = {"vtktype":k, "dim":dim}
        print("element: {}, space dimension: {}".format(cellType.name, dim))
    return dims


def build_bulk_and_interface_elt_fields(omega: pv.UnstructuredGrid= None,
                                        bulk_elt_name:str = "bulk_elt",
                                        interface_elt_name:str = "interface_elt"):
    c_keys = list(omega.cell_data.keys())
    if bulk_elt_name in c_keys:
        raise NotImplementedError("bulk_elt_name {} already exist in the \
        given mesh\nKnown cell data are {}".format(bulk_elt_name, c_keys))
    if interface_elt_name in c_keys:
        raise NotImplementedError("interface_elt_name {} already exist in the \
        given mesh\nKnown cell data are {}".format(interface_elt_name, c_keys))

    elt_dims = build_map_eltype_dim(omega)
    dims = []
    for elt, val in elt_dims.items():
        dims.append(val["dim"])
    bulk_dim = max(dims)
    elts = list(elt_dims.keys())
    elts.sort()
    print(bulk_dim)
    print(elt_dims)
    assert(bulk_dim > 0)
    interface_dim = bulk_dim-1
    if elts == ['LINE', 'VERTEX'] or elts == ['LINE']:
        print("1D mesh detected")
        bulk_dim = 1
        interface_dim = 3

    bulk_elt = np.zeros(omega.number_of_cells, dtype=np.int32)
    interf_elt = np.zeros(omega.number_of_cells, dtype=np.int32)
    celltypes = omega.celltypes
    for elt, val in elt_dims.items():
        if val["dim"] == bulk_dim:
            trace = np.argwhere(celltypes == val["vtktype"])
            bulk_elt[trace] = 1
        if val["dim"] == interface_dim:
            trace = np.argwhere(celltypes == val["vtktype"])
            interf_elt[trace] = 1

    omega.cell_data[bulk_elt_name] = bulk_elt
    omega.cell_data[interface_elt_name] = interf_elt
    return


def build_graph_partitionning(omega:pv.UnstructuredGrid = None, nb_part=2, nb_node_by_elt=3, part_name="part", part_name_at_node=""):
    assert(nb_part > 1)
    assert(type(omega) == pv.UnstructuredGrid)
    # --------------------------------------------------
    # use metis to do a graph partitionning
    # --------------------------------------------------
    # ON support qu'il y a qu'in
    cells = omega.cells.reshape(-1, nb_node_by_elt+1)[:, 1:]
    objval, epart, npart = metis.part_mesh_dual(nb_part, cells)

    # --------------------------------------------------
    omega.cell_data[part_name] = epart
    if part_name_at_node != "":
        omega.point_data[part_name_at_node] = npart
    return


def map_data_on_local_BC(kdt, interface, fields_to_transfert: list=[]):
    pts = interface.cell_centers().points

    dd, ii = kdt.query(pts, eps=1e-3)
    # print(kdt.n)
    # print(dd)
    # print(pts.shape[0])
    # print(ii)
    # trace = np.argwhere( ii != kdt.n).flatten()
    trace = np.argwhere(dd < 1e-7).flatten()
    ii = ii[trace]
    for ifiled in fields_to_transfert["cell"]:
        test = np.ones(interface.number_of_cells, dtype=np.int32) * -1
        test[trace] = ifiled[1][ii]
        interface.cell_data[ifiled[0]] = test


def extract_subdomains(omega:pv.UnstructuredGrid = None, part_name="epart"):
    assert(type(omega) == pv.UnstructuredGrid)
    c_keys = list(omega.cell_data.keys())
    if part_name not in c_keys:
        raise RuntimeError("fielf {} (part_name attribute) is not in the mesh (attribute omega)\n\
        known fields ares:\n{}".format(part_name, c_keys))
    parts = np.unique(omega.cell_data[part_name])

    eps = 1e-7
    omegas = []

    for ipart in parts:
        omega_p = omega.threshold([ipart - eps, ipart + eps],
                                  scalars=part_name)

        # surf_p = omega_p.extract_surface()
        # gamma_p = surf_p.extract_feature_edges()
        # # print(gamma_p.cell_data["cell_ids"])
        # # print(gamma1.cell_data["cell_ids"])
        # BC_nodes, x_ind, y_ind = np.intersect1d(gamma_p.cell_data["cell_ids"],
        #                                         gamma.cell_data["cell_ids"],
        #                                         return_indices=True)

        # npts = gamma_p.number_of_cells
        # BC = np.ones(npts, dtype=np.int32)*-1
        # BC[x_ind] = gamma.cell_data["gmsh:physical"][y_ind]
        # gamma_p.cell_data["gmsh:physical"] = BC

        omegas.append(omega_p)
        # gammas.append(gamma_p)
    # --------------------------------------------------
    return omegas


class Imesh(pv.UnstructuredGrid, COUT.utils):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.msh_dim = None
        self.interface = None
        self.interface_pts = None
        self._field_ids_name = "TMP_CONNECTOR_IDS"
        # self._bb_center = None
        # self._bound = None
        self._init_mesh()

    def _init_mesh(self):
        self._compute_mesh_dim()

    def _compute_mesh_dim(self):
        elt_dims = build_map_eltype_dim(self)

        dims = []
        for elt, val in elt_dims.items():
            dims.append(val["dim"])
        dims = np.unique(np.array(dims, dtype=np.int32))
        if (len(dims) != 1): raise NotImplementedError("Mesh contains element with different dimension")
        self.msh_dim = dims[0]

        # mecanisme to call only once this fonction
        self_fct_name = inspect.currentframe().f_code.co_name
        self.__dict__[self_fct_name] = self.do_nothing


    def add_local_fields(self, name="connector_ids"):
        c_keys = self.cell_data.keys()
        p_keys = self.point_data.keys()
        if (name in c_keys) or (name in p_keys):
            raise NotImplementedError("field name {} already exist in the mesh. Known fields are\n:@point:\n{}\n@cell:\n{}".format(name, p_keys, c_keys))
        self.point_data[name] = np.arange(self.number_of_points,dtype=np.int32)
        self.cell_data[name] = np.arange(self.number_of_cells, dtype=np.int32)


    def build_skin(self):
        self.add_local_fields(self._field_ids_name)
        match self.msh_dim:
            case 1:
                conn = self.cells_dict[pv.CellType.LINE].flatten()
                unique_pts_ids, count = np.unique(conn, return_counts=True)
                trace = np.argwhere(count == 1).flatten()
                self.interface = self.extract_points(ind=trace, include_cells=False)
            case 2:
                surf = self.extract_surface()
                self.interface = surf.extract_feature_edges()
            case 3:
                self.interface = self.extract_surface()
            case _:
                raise RuntimeError
        # mecanisme to call only once this fonction
        self_fct_name = inspect.currentframe().f_code.co_name
        self.__dict__[self_fct_name] = self.do_nothing

    def compute_interface_cell_centers(self, ):
        self.build_skin()
        # self.bounds = self.intef_cell_centers.bounds
        # TO DO voir sir il y a moyen de faire un premier try avoir la bounding_box
        self.interface_pts = self.interface.cell_centers().points

        # mecanisme to call only once this fonction
        self_fct_name = inspect.currentframe().f_code.co_name
        self.__dict__[self_fct_name] = self.do_nothing
