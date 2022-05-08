#!/bin/bash
./asc2c "Tavg.txt" "Tavg.bin"
./asc2c "Tmin.txt" "Tmin.bin"
./asc2c "Tmax.txt" "Tmax.bin"
./asc2c "Precip.txt" "Precip.bin"
./asc2c "Sdown.txt" "Sdown.bin"
./asc2c "Ldown.txt" "Ldown.bin"
./asc2c "RH.txt" "RH.bin"
./asc2c "windspeed.txt" "windspeed.bin"
./asc2c "d2H.txt" "d2H.bin"
./asc2c "LAI_0.txt" "LAI_0.bin"
./asc2c "LAI_1.txt" "LAI_1.bin"
./asc2c "LAI_2.txt" "LAI_2.bin"
./asc2c "LAI_3.txt" "LAI_3.bin"

./asc2c "Pressure.txt" "Pressure.bin"

./asc2c "BCsurface.txt" "BCsurface.bin"
./asc2c "BCgroundwater.txt" "BCgroundwater.bin"
./asc2c "BCdeepgroundwater.txt" "BCdeepgroundwater.bin"

./asc2c "BCd2Hsurface.txt" "BCd2Hsurface.bin"
./asc2c "BCd2Hgroundwater.txt" "BCd2Hgroundwater.bin"
./asc2c "BCd2Hdeepgroundwater.txt" "BCd2Hdeepgroundwater.bin"

./asc2c "Height_0.txt" "Height_0.bin"
./asc2c "Height_1.txt" "Height_1.bin"
./asc2c "Height_2.txt" "Height_2.bin"
./asc2c "Height_3.txt" "Height_3.bin"

./asc2c "DeepGWlvl.txt" "DeepGWlvl.bin"


cp ../Spatial_50m/ClimZones.map "ClimZones.map"
cp ../Spatial_50m/isohyet.map "isohyet.map"

