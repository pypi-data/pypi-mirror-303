import sys
import numpy as np

# Local load of neutralNEMO
sys.path.append("../src/neutralNEMO/")
from grid import load_hgriddata, load_zgriddata
from grid import build_nemo_hgrid
from surf import load_tsdata, find_omega_surfs
from eos import NEMO_eos


# Package load of neutralNEMO
# from neutralNEMO.grid import load_hgriddata, load_zgriddata
# from neutralNEMO.grid import build_nemo_hgrid
# from neutralNEMO.surf import load_tsdata, find_omega_surfs

hgd = load_hgriddata( "domcfg_eORCA1v2.2x.nc" )
zgd = load_zgriddata( "domcfg_eORCA1v2.2x.nc" , infer_tmask3d=True, infer_tmask2d=True, infer_path="nemo_bu978o_1y_19771201-19781201_grid-T.nc", vert_dim="z")

neutral_grid = build_nemo_hgrid(hgd, iperio=True, jperio=False, gridtype="orca")

tsd = load_tsdata("nemo_bu978o_1y_19771201-19781201_grid-T.nc", zgd, to_varname="thetao")

zpins = [ 100, ]
ipins = [1,]
jpins = [90]
tpins = [-1]
ver_ipins = 1
ver_jpins = 90

# eos = NEMO_eos( 'teos10' )
eos = NEMO_eos( 'eos80' )
# eos = NEMO_eos( 'seos' , rn_a0 = 1.655e-1, rn_b0 = 7.655e-1,
#                rn_nu = 0., rn_lambda1 = 0., rn_lambda2 = 0.,
#                rn_mu1 = 0., rn_mu2 = 0. )

surf_dataset = find_omega_surfs( tsd, neutral_grid, zgd, zpins, ipins, jpins, tpins, eos=eos, eos_type='insitu', ITER_MAX=10, calc_veronis=True, ver_ipins=ver_ipins, ver_jpins=ver_jpins)

print(surf_dataset)

surf_dataset.to_netcdf("test_dataset.orca.nc")
