import sys
import numpy as np

# Local load of neutralNEMO
sys.path.append("../src/neutralNEMO/")
from grid import load_hgriddata, load_zgriddata
from grid import build_nemo_hgrid
from surf import load_tsdata, find_omega_surfs
from eos import calc_seos, calc_seos_s_t, NEMO_eos

# Package load of neutralNEMO
# from neutralNEMO.grid import load_hgriddata, load_zgriddata
# from neutralNEMO.grid import build_nemo_hgrid
# from neutralNEMO.surf import load_tsdata, find_omega_surfs

hgd = load_hgriddata( "mesh_mask.nc" )
zgd = load_zgriddata( "mesh_mask.nc", vert_dim="nav_lev")

neutral_grid = build_nemo_hgrid(hgd, iperio=False, jperio=False, gridtype="rectilinear")

tsd = load_tsdata("GYRE_1m_04110101_04201230_grid_T.nc", zgd, to_varname="votemper", so_varname="vosaline")

zpins = [ 100, 1000] 
ipins = [10, 15]
jpins = [ 5, 5 ]
tpins = [-1, -1]
ver_ipins = 10
ver_jpins = 10

# eos = NEMO_eos( 'teos10' )
# eos = NEMO_eos( 'eos80' )
eos = NEMO_eos( 'seos' , rn_a0 = 1.655e-1, rn_b0 = 7.655e-1,
               rn_nu = 0., rn_lambda1 = 0., rn_lambda2 = 0.,
               rn_mu1 = 0., rn_mu2 = 0. )


surf_dataset = find_omega_surfs( tsd, neutral_grid, zgd, zpins, ipins, jpins, tpins, eos=eos, eos_type='insitu', ITER_MAX=10, calc_veronis=True, ver_ipins=ver_ipins, ver_jpins=ver_jpins)

print(surf_dataset)

surf_dataset.to_netcdf("test_dataset.rect.nc")
