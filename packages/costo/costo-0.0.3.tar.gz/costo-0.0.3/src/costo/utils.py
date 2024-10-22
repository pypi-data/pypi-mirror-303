#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# **************************************************
__author__  = "Teddy Chantrait"
__email__   = "teddy.chantrait@gmail.com"
__status__  = "Development"
__date__    = "2024-05-31 09:39:36.902967"
__version__ = 1.0
# **************************************************
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import numpy as np
import pyvista as pv

colorama_init()

def check_inputs(c_data, used_keys):
    assert(type(c_data) == dict)
    input_keys = c_data.keys()
    for k in used_keys:
        if not(k in input_keys):
            raise ValueError("keys: {} is required, but not provied".format(k))
    return


class printer():
    def __init__(self, mention: str =""):
        self.old_print = print
        self.mention = mention
        self.Fore = Fore
        self.color = Fore.BLUE
        self.print = self._new_print

    def _new_print(self, *args, **kwargs):
        new_args = [self.color+str(self.mention)]
        for arg in args:
            new_args.append(arg)
        new_args.append(""+Fore.RESET)
        return self.old_print(*new_args, **kwargs)


class utils():
    def _init(self):
        return

    def do_nothing(self):
        return

    def do_nothing1(self,*args, **kwds):
        return

    def call_only_once(fct):
        def new_fct(*args, **kwds):
            print("Call function", fct.__name__)
            fct(*args, **kwds)
            return
        return new_fct
        # # mecanisme to call only once this fonction
        # self_fct_name = inspect.currentframe().f_code.co_name
        # self.__dict__[self_fct_name] = self.do_nothing

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

def FindAllSubclasses(classType):
    import sys
    import inspect
    subclasses = []
    callers_module = sys._getframe(1).f_globals['__name__']
    classes = inspect.getmembers(sys.modules[callers_module], inspect.isclass)
    for name, obj in classes:
        if (obj is not classType) and (classType in inspect.getmro(obj)):
            subclasses.append((obj, name))
    return subclasses

def compare_mesh(m1, m2, trace_cell_m1_to_m2=None, trace_point_m1_to_m2=None, use_fields_from_m1_only=False, verbose=0):
    import pyvista as pv
    assert(type(m1) == type(m2))
    assert(type(m1) in [pv.core.pointset.UnstructuredGrid,
                        pv.core.pointset.StructuredGrid,
                        pv.core.pointset.PolyData])
    assert(m1.number_of_points == m2.number_of_points)
    if trace_point_m1_to_m2 is None:
        trace_point_m1_to_m2 = np.arange(m1.number_of_points, dtype=np.int32)
    if not use_fields_from_m1_only:
        assert(len(m1.point_data) == len(m2.point_data))
        # assert(len(m1.cell_data) == len(m2.cell_data))
    assert(np.allclose(m1.points[trace_point_m1_to_m2], m2.points))
    if type(m1) is pv.core.pointset.UnstructuredGrid:
        assert(m1.number_of_cells == m2.number_of_cells)
        if trace_cell_m1_to_m2 is None:
            trace_cell_m1_to_m2 = np.arange(m1.number_of_cells, dtype=np.int32)
        if not use_fields_from_m1_only:
            assert(np.allclose(m1.cells, m2.cells))
    if type(m1) is pv.core.pointset.PolyData:
        assert(m1.number_of_cells == m2.number_of_cells)
        if trace_cell_m1_to_m2 is None:
            trace_cell_m1_to_m2 = np.arange(m1.n_cells, dtype=np.int32)
        assert(len(m1.faces) == len(m2.faces))
        if not use_fields_from_m1_only:
            assert(np.allclose(m1.faces, m2.faces))
    for k in m1.cell_data:
        k1 = k
        if verbose > 0:
            print("compare {} in cell_data".format(k))
        # if k == "rhoc" or k == "F" or k == "W" or k == "M_inv":
        #     continue
        # if k == "E":
        #     k1 = "total-energy"
        # assert(np.allclose(m1.cell_data[k][trace_cell_m1_to_m2], m2.cell_data[k1]))
    for k in m1.point_data:
        assert(np.allclose(m1.point_data[k][trace_point_m1_to_m2], m2.point_data[k]))
    return
