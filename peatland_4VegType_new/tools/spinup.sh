#!/bin/bash

COUNT=1
NITER=3

while [ $COUNT -lt $NITER ]
do
	echo "Running iteration ${COUNT}"
	./ech2o_iso config_spinup.ini
	
	echo "finished run, copying files"
	"""
	cp -f ./Outputs/root0_.map   ./Spatial_50m/root_0.map #Report_Root_Mass
	cp -f ./Outputs/root1_.map   ./Spatial_50m/root_1.map
	cp -f ./Outputs/root2_.map   ./Spatial_50m/root_2.map
	cp -f ./Outputs/root3_.map   ./Spatial_50m/root_3.map
	cp -f ./Outputs/p0_.map      ./Spatial_50m/p_0.map    #Report_Veget_frac
	cp -f ./Outputs/p1_.map      ./Spatial_50m/p_1.map  
	cp -f ./Outputs/p2_.map      ./Spatial_50m/p_2.map  
	cp -f ./Outputs/p3_.map      ./Spatial_50m/p_3.map  
	cp -f ./Outputs/ntr0_.map    ./Spatial_50m/ntr_0.map  #Report_Stem_Density
	cp -f ./Outputs/ntr1_.map    ./Spatial_50m/ntr_1.map
	cp -f ./Outputs/ntr2_.map    ./Spatial_50m/ntr_2.map
	cp -f ./Outputs/ntr3_.map    ./Spatial_50m/ntr_3.map
	cp -f ./Outputs/lai0_000.365 ./Spatial_50m/lai_0.map  #Report_Leaf_Area_Index
	cp -f ./Outputs/lai1_000.365 ./Spatial_50m/lai_1.map
	cp -f ./Outputs/lai2_000.365 ./Spatial_50m/lai_2.map
	cp -f ./Outputs/lai3_000.365 ./Spatial_50m/lai_3.map
	cp -f ./Outputs/hgt0_.map    ./Spatial_50m/hgt_0.map  #Report_Tree_Height
	cp -f ./Outputs/hgt1_.map    ./Spatial_50m/hgt_1.map
	cp -f ./Outputs/hgt2_.map    ./Spatial_50m/hgt_2.map
	cp -f ./Outputs/hgt3_.map    ./Spatial_50m/hgt_3.map
	cp -f ./Outputs/bas0_000.365 ./Spatial_50m/bas_0.map  #Report_Basal_Area
	cp -f ./Outputs/bas1_000.365 ./Spatial_50m/bas_1.map
	cp -f ./Outputs/bas2_000.365 ./Spatial_50m/bas_2.map
	cp -f ./Outputs/bas3_000.365 ./Spatial_50m/bas_3.map
	cp -f ./Outputs/age0_000.365 ./Spatial_50m/age_0.map  #Report_Stand_Age
	cp -f ./Outputs/age1_000.365 ./Spatial_50m/age_1.map
	cp -f ./Outputs/age2_000.365 ./Spatial_50m/age_2.map
	cp -f ./Outputs/age3_000.365 ./Spatial_50m/age_3.map
	"""
	cp -f ./Outputs/SWE00000.365 ./Spatial_50m/swe.map    #Report_SWE
	cp -f ./Outputs/SWC1_000.365 ./Spatial_50m/SWC.L1.map  #Report_Soil_Water_Content_L1 = 1 
	cp -f ./Outputs/SWC2_000.365 ./Spatial_50m/SWC.L2.map  #Report_Soil_Water_Content_L2 = 1
	cp -f ./Outputs/SWC3_000.365 ./Spatial_50m/SWC.L3.map  #Report_Soil_Water_Content_L3 = 1
	cp -f ./Outputs/Ts000000.365 ./Spatial_50m/soiltemp.map  #Report_Soil_Temperature = 1
	cp -f ./Outputs/Q0000000.365 ./Spatial_50m/streamflow.map #Report_Streamflow = 1



	COUNT=$((COUNT+1))
done
	echo "Finished simulation\n"


