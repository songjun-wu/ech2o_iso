@echo off

set root=D:\OneDrive\Phd\WorkPackages\4\paper6\data\gis_peatland\spatial

echo call D:\miniconda3\Scripts\activate.bat
echo call conda activate py37
call D:\Programs\Miniconda3\Scripts\activate.bat
call conda activate python36




call d:
call cd %root%


echo ******** construct DEM.map
call asc2map -a --clone ./info/base.map ./info/dem.asc DEM.map

echo ******** Unit map
call pcrcalc "unit.map = DEM.map/DEM.map"

echo ******** construct ClimZones.map
call asc2map -a --clone ./info/base.map ./info/ClimZones.asc ClimZones.map

echo ******** construct ldd.map
call pcrcalc "ldd.map=lddcreate(DEM.map, 1e9,1e9,1e9,1e9)"

echo ******** construct slope.map
call pcrcalc "slope.map=slope(DEM.map)

call pcrcalc "isohyet.map = unit.map * 1"

echo ******** construct chanmask.map
call asc2map -a --clone ./info/base.map ./info/chanmask.asc chanmask.map
echo ******** construct chanwidth.map
call asc2map -a --clone ./info/base.map ./info/chanwidth.asc chanwidth.map


echo ******** construct chanmanningn.map
call pcrcalc "chanmanningn.map=chanmask.map*5"
echo ******** construct chanparam.map
call pcrcalc "chanparam.map=chanmask.map*0.02"





echo ******** Geophysics ********
echo ******** Albedo
call pcrcalc "albedo.map = unit.map * 0.3"

echo ******** Emissivity
call pcrcalc "emissivity.map = unit.map * 0.98"

echo ******** Soil heat capacity
call pcrcalc "soilheatcap.map = unit.map * 2.205e6"

echo ******** Soil thermal conductivity
call pcrcalc "soilthermalK.map = unit.map * 0.2"

echo ******** Soil depth with negligible heat exchange
call pcrcalc "dampdepth.map = unit.map * 2"

echo ******** Initial soil temperature
call pcrcalc "temp_damp.map = unit.map * 10"

echo ******** Snowmelt coefficient
call pcrcalc "snowmeltCoeff.map = unit.map * 4.1e-8"

echo ******** Terrain rugosity
call pcrcalc "randrough.map = unit.map * 0.05"

echo ******** Soil air entry pressure
call pcrcalc "psi_ae.map = unit.map * 0.2"

echo ******** Brooks and Corey lambda
call pcrcalc "BClambda.map = unit.map * 5.3"

echo ******** V-to-H hydraulic conductivity ratio
call pcrcalc "KvKh.map = unit.map * 0.4"

echo ******** Residual soil moisture
call pcrcalc "theta_r.map = unit.map * 0.05"

echo ******** Other soil parameters
call pcrcalc "Wc.map = unit.map * 0.7"
call pcrcalc "Wp.map = unit.map * 9"

echo ******** Topography index
call pcrcalc "topind.map = ln(accuflux(ldd.map,625000)/slope.map)"

echo ******** Soil depth
call pcrcalc "soildepth.map = topind.map/areaaverage(topind.map,nominal(unit.map))"

echo ******** Effective hydraulic conductivity (reference hydraulic conductiviti in m/s)
call pcrcalc "Keff.map = 1 / (soildepth.map * 36000)"


echo ******** Effective hydraulic conductivity 
call pcrcalc "kKsat.map = 0.15 * unit.map"

echo ******** Porosity
call pcrcalc "poros.map = 1 / (1 + exp(0.01 * topind.map))"

echo ******** Porosity
call pcrcalc "kporos.map = 2 * unit.map"

echo ******** Snow water equivalent
call pcrcalc "swe.map = unit.map * 0"

echo ******** Initial soil moisture in the three layers
call pcrcalc "SWC.L1.map = poros.map * 0.5"
call pcrcalc "SWC.L2.map = poros.map * 0.5"
call pcrcalc "SWC.L3.map = poros.map * 0.5"

echo ******** Initial soil temperature
call pcrcalc "soiltemp.map = unit.map * 10"

echo ******** Initial water temperature
call pcrcalc "water_temp.map = chanmask.map * 8"
call pcrcalc "chanrough.map = chanmask.map * 1"

echo ******** Initial soil temperature
call pcrcalc "streamflow.map = unit.map * 0"

echo ******** Depth of first two soil hydraulic layers
echo \(third is deduced from the total soil depth\)
call pcrcalc "soildepth.L1.map = unit.map * 0.1"
call pcrcalc "soildepth.L2.map = unit.map * 0.1"

echo ******** Exponential root profile
call pcrcalc "Kroot.map = unit.map * 10"

echo ******** Leakance through bedrock
call pcrcalc "leakance.map = unit.map * 0.0"

echo ****** Tsmask
call col2map --clone ./info/base.map ./info/swGaugeMask.txt Tsmask.map

echo ****** inflowMask
call col2map --clone ./info/base.map ./info/inflowMask.txt inflowMask.map

echo ************   Soil Type ***************
call asc2map -a --clone ./info/base.map ./info/soil0.asc unit_soil0.map
call pcrcalc "unit_soil1.map = unit.map - unit_soil0.map"

echo ************   Veg   ***************
call asc2map -a --clone ./info/base.map ./info/patches.asc patches.map

call asc2map -a --clone ./info/base.map ./info/p0.asc p_0.map
call asc2map -a --clone ./info/base.map ./info/p1.asc p_1.map
call asc2map -a --clone ./info/base.map ./info/p2.asc p_2.map
call asc2map -a --clone ./info/base.map ./info/p3.asc p_3.map


call pcrcalc "age_0.map =  if(p_0.map>0 then unit.map*4 else 0)"
call pcrcalc "age_1.map =  if(p_1.map>0 then unit.map*4 else 0)"
call pcrcalc "age_2.map =  if(p_2.map>0 then unit.map*4 else 0)"
call pcrcalc "age_3.map =  if(p_3.map>0 then unit.map*50 else 0)"

call pcrcalc "bas_0.map =  if(p_0.map>0 then unit.map*0.04 else 0)"
call pcrcalc "bas_1.map =  if(p_1.map>0 then unit.map*0.04 else 0)"
call pcrcalc "bas_2.map =  if(p_2.map>0 then unit.map*0.04 else 0)"
call pcrcalc "bas_3.map =  if(p_3.map>0 then unit.map*0.04 else 0)"

call pcrcalc "lai_0.map =  unit.map"
call pcrcalc "lai_1.map =  unit.map"
call pcrcalc "lai_2.map =  unit.map"
call pcrcalc "lai_3.map =  unit.map"

call pcrcalc "hgt_0.map =  unit.map*0.5"
call pcrcalc "hgt_1.map =  unit.map*0.5"
call pcrcalc "hgt_2.map =  unit.map*0.5"
call pcrcalc "hgt_3.map =  unit.map*10"

call pcrcalc "ntr_0.map =  if(p_0.map>0 then unit.map*0.15 else 0)"
call pcrcalc "ntr_1.map =  if(p_1.map>0 then unit.map*0.15 else 0)"
call pcrcalc "ntr_2.map =  if(p_2.map>0 then unit.map*0.15 else 0)"
call pcrcalc "ntr_3.map =  if(p_3.map>0 then unit.map*0.15 else 0)"

call pcrcalc "root_0.map =  if(p_0.map>0 then unit.map*300 else 0)"
call pcrcalc "root_1.map =  if(p_1.map>0 then unit.map*300 else 0)"
call pcrcalc "root_2.map =  if(p_2.map>0 then unit.map*300 else 0)"
call pcrcalc "root_3.map =  if(p_3.map>0 then unit.map*300 else 0)"


echo ************Tracking*************
echo ************   Age     *************
call pcrcalc "Age_groundwater.map = unit.map * 0.0"
call pcrcalc "Age_snowpack.map = unit.map * 0.0"
call pcrcalc "Age_soilL1.map = unit.map * 0.0"


echo ************   d2H     *************
call pcrcalc "d2H_groundwater.map = unit.map * -60.0"
call pcrcalc "d2H_snowpack.map = unit.map * -60.0"
call pcrcalc "d2H_soilL1.map = unit.map * -60.0"
call pcrcalc "d2H_soilL2.map = unit.map * -60.0"
call pcrcalc "d2H_soilL3.map = unit.map * -60.0"
call pcrcalc "d2H_surface.map = unit.map * -60.0"

echo ************   d2O     *************
call pcrcalc "d2O_groundwater.map = unit.map * -8.0"
call pcrcalc "d2O_snowpack.map = unit.map * -8.0"
call pcrcalc "d2O_soilL1.map = unit.map * -8.0"
call pcrcalc "d2O_soilL2.map = unit.map * -8.0"
call pcrcalc "d2O_soilL3.map = unit.map * -8.0"
call pcrcalc "d2O_surface.map = unit.map * -8.0"

echo ************   dD    ***************
call pcrcalc "dD_groundwater.map = unit.map * -8.0"
call pcrcalc "dD_snowpack.map = unit.map * -8.0"
call pcrcalc "dD_soilL1.map = unit.map * -8.0"
call pcrcalc "dD_soilL2.map = unit.map * -8.0"
call pcrcalc "dD_soilL3.map = unit.map * -8.0"
call pcrcalc "dD_surface.map = unit.map * -8.0"

call conda deactivate
call conda deactivate
