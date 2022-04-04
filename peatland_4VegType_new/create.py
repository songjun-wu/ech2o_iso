import os
import shutil


localPath = os.getcwd()
outputPath = os.getcwd() + '/Spatial_initial'
dataPath = os.getcwd() + '/gis_peatland/Spatial'

os.chdir(dataPath)

print('******** Basic info ********')

os.system('asc2map -a --clone ./info/base.map ./info/dem.asc DEM.map')
os.system('asc2map -a --clone ./info/base.map ./info/chanmask.asc chanmask.map')
os.system('asc2map -a --clone ./info/base.map ./info/soil0.asc unit_soil0.map')
os.system('pcrcalc "unit_soil1.map = unit.map - unit_soil0.map"')
os.system('asc2map -a --clone ./info/base.map ./info/patches.asc patches.map')
os.system('asc2map -a --clone ./info/base.map ./info/p0.asc p_0.map')
os.system('asc2map -a --clone ./info/base.map ./info/p1.asc p_1.map')
os.system('asc2map -a --clone ./info/base.map ./info/p2.asc p_2.map')
os.system('asc2map -a --clone ./info/base.map ./info/p3.asc p_3.map')


os.system('col2map --clone ./info/base.map ./info/inflowMask.txt tmpmask.map')
os.system('pcrcalc "tmpmask1.map = cover(tmpmask.map, 0)"')
os.system('pcrcalc "ClimZones.map = tmpmask1.map + unit.map"')
os.system('rm tmpmask.map tmpmask1.map')

os.system('col2map --clone ./info/base.map ./info/swGaugeMask.txt Tsmask.map')


os.system('pcrcalc "unit.map = DEM.map/DEM.map"')
os.system('pcrcalc "ldd.map=lddcreate(DEM.map, 1e9,1e9,1e9,1e9)"')
os.system('pcrcalc "slope.map=slope(DEM.map)"')
os.system('pcrcalc "isohyet.map = unit.map * 1"')

print('******** Channel info ********')
os.system('asc2map -a --clone ./info/base.map ./info/chanwidth.asc chanwidth.map')
os.system('pcrcalc "chanparam.map=chanmask.map*2*1e-2"')
os.system('pcrcalc "chanmanningn.map=chanmask.map*1"')


print('******** Geophysics ********')
os.system('pcrcalc "albedo.map = unit.map * 3*1e-1"')
os.system('pcrcalc "emissivity.map = unit.map * 98*1e-2"')
os.system('pcrcalc "soilheatcap.map = unit.map * 2205*1e3"')
os.system('pcrcalc "soilthermalK.map = unit.map * 2 * 1e-1"')
os.system('pcrcalc "dampdepth.map = unit.map * 2"')
os.system('pcrcalc "temp_damp.map = unit.map * 10"')
os.system('pcrcalc "snowmeltCoeff.map = unit.map * 41 * 1e-9"')
os.system('pcrcalc "randrough.map = unit.map * 5 * 1e-2"')
os.system('pcrcalc "psi_ae.map = unit.map * 2*1e-1"')
os.system('pcrcalc "BClambda.map = unit.map * 53*1e-1"')


os.system('pcrcalc "KvKh.map = unit.map * 4 * 1e-1"')
os.system('pcrcalc "theta_r.map = unit.map * 5 * 1e-2"')
os.system('pcrcalc "Wc.map = unit.map * 7 * 1e-1"')
os.system('pcrcalc "Wp.map = unit.map * 9"')
os.system('pcrcalc "soildepth.L1.map = unit.map * 1 * 1e-1"')
os.system('pcrcalc "soildepth.L2.map = unit.map * 4 * 1e-1"')
os.system('pcrcalc "soildepth.L3.map = unit.map * 20 * 1e-1"') # or 2?
os.system('pcrcalc "Keff.map = unit.map * 1 * 1e-4"')

os.system('pcrcalc "kKsat.map = unit.map * 15 * 1e-2"')  # should be 10?? or 15 * 1e-2
os.system('pcrcalc "poros.map = unit.map * 75 * 1e-2"')  # 7
os.system('pcrcalc "kporos.map = unit.map * 8"')
os.system('pcrcalc "swe.map = unit.map * 0"')
os.system('pcrcalc "SWC.L1.map = poros.map * 75 * 1e-2"') #0.75 or 0.5
os.system('pcrcalc "SWC.L2.map = poros.map * 75 * 1e-2"') #0.75
os.system('pcrcalc "SWC.L3.map = poros.map * 75 * 1e-2"') #0.75
os.system('pcrcalc "soiltemp.map = unit.map * 10"')
os.system('pcrcalc "water_temp.map = chanmask.map * 8"')
os.system('pcrcalc "chanrough.map = chanmask.map * 1"')

os.system('pcrcalc "streamflow.map = unit.map * 0"')
os.system('pcrcalc "Kroot.map = unit.map * 10"')
os.system('pcrcalc "leakance.map = unit.map * 0"')

print('******** Vegetations ********')
os.system('pcrcalc "age_0.map =  if(p_0.map>0 then unit.map*1 else 0)"')
os.system('pcrcalc "age_1.map =  if(p_1.map>0 then unit.map*1 else 0)"')
os.system('pcrcalc "age_2.map =  if(p_2.map>0 then unit.map*1 else 0)"')
os.system('pcrcalc "age_3.map =  if(p_3.map>0 then unit.map*50 else 0)"')
os.system('pcrcalc "bas_0.map =  if(p_0.map>0 then unit.map*4*1e-2 else 0)"')
os.system('pcrcalc "bas_1.map =  if(p_1.map>0 then unit.map*4*1e-2 else 0)"')
os.system('pcrcalc "bas_2.map =  if(p_2.map>0 then unit.map*4*1e-2 else 0)"')
os.system('pcrcalc "bas_3.map =  if(p_3.map>0 then unit.map*1*1e-1 else 0)"')
os.system('pcrcalc "lai_0.map =  unit.map"')
os.system('pcrcalc "lai_1.map =  unit.map"')
os.system('pcrcalc "lai_2.map =  unit.map"')
os.system('pcrcalc "lai_3.map =  unit.map"')
os.system('pcrcalc "hgt_0.map =  unit.map*2*1e-1"')
os.system('pcrcalc "hgt_1.map =  unit.map*7*1e-1"')
os.system('pcrcalc "hgt_2.map =  unit.map*7*1e-1"')
os.system('pcrcalc "hgt_3.map =  unit.map*10"')
os.system('pcrcalc "ntr_0.map =  if(p_0.map>0 then unit.map*3 else 0)"')
os.system('pcrcalc "ntr_1.map =  if(p_1.map>0 then unit.map*3 else 0)"')
os.system('pcrcalc "ntr_2.map =  if(p_2.map>0 then unit.map*3 else 0)"')
os.system('pcrcalc "ntr_3.map =  if(p_3.map>0 then unit.map*15*1e-2 else 0)"')
os.system('pcrcalc "root_0.map =  if(p_0.map>0 then unit.map*250 else 0)"')
os.system('pcrcalc "root_1.map =  if(p_1.map>0 then unit.map*400 else 0)"')
os.system('pcrcalc "root_2.map =  if(p_2.map>0 then unit.map*400 else 0)"')
os.system('pcrcalc "root_3.map =  if(p_3.map>0 then unit.map*300 else 0)"')

print('******** Tracking ********')
os.system('pcrcalc "d2H_snowpack.map = unit.map * -57"')
os.system('pcrcalc "d2H_surface.map = unit.map * -57"')
os.system('pcrcalc "d2H_soilL1.map = unit.map * -57"')
os.system('pcrcalc "d2H_soilL2.map = unit.map * -57"')
os.system('pcrcalc "d2H_soilL3.map = unit.map * -57"')
os.system('pcrcalc "d2H_groundwater.map = unit.map * -57"')

"""
os.system('pcrcalc "Age_groundwater.map = unit.map * 0"')
os.system('pcrcalc "Age_snowpack.map = unit.map * 0"')
os.system('pcrcalc "Age_surface.map = unit.map * 0"')
os.system('pcrcalc "Age_soilL1.map = unit.map * 0"')
os.system('pcrcalc "Age_soilL2.map = unit.map * 0"')
os.system('pcrcalc "Age_soilL3.map = unit.map * 0"')
os.system('pcrcalc "d2O_groundwater.map = unit.map * -8"')
os.system('pcrcalc "d2O_snowpack.map = unit.map * -8"')
os.system('pcrcalc "d2O_soilL1.map = unit.map * -8"')
os.system('pcrcalc "d2O_soilL2.map = unit.map * -8"')
os.system('pcrcalc "d2O_soilL3.map = unit.map * -8"')
os.system('pcrcalc "d2O_surface.map = unit.map * -8"')
os.system('pcrcalc "dD_groundwater.map = unit.map * -8"')
os.system('pcrcalc "dD_snowpack.map = unit.map * -8"')
os.system('pcrcalc "dD_soilL1.map = unit.map * -8"')
os.system('pcrcalc "dD_soilL2.map = unit.map * -8"')
os.system('pcrcalc "dD_soilL3.map = unit.map * -8"')
os.system('pcrcalc "dD_surface.map = unit.map * -8"')
"""

print('******** New maps! ********')
os.system('pcrcalc "fcontrea.map = unit.map * 1"')
os.system('pcrcalc "fImperv.map = unit.map * 0"')
os.system('pcrcalc "chanlength.map = unit.map * 1"')
os.system('pcrcalc "chanDeepparam.map = chanparam.map"')

os.system('pcrcalc "GW_DeepStorage.map = unit.map * 1"')
os.system('pcrcalc "d2H_DeepGW.map = unit.map * -59"')
os.system('pcrcalc "fActive_DeepGW.map = if(chanmask.map>0 then unit.map*5*1e-1 else 0)"')
os.system('pcrcalc "KeffTopSoil.map = Keff.map"')


print('******** Test maps! ********')
os.system('pcrcalc "facc.map = accuflux(ldd.map, 1)"')








os.system('cp '+dataPath+'/info/SpeciesParams.tab '+dataPath+'/SpeciesParams.tab')

if os.path.exists(outputPath):
    os.system('rm -rf '+outputPath)
os.system('cp -r '+dataPath+' '+outputPath)





