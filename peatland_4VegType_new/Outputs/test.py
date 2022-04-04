import os


localPath = os.getcwd()
dataPath = os.getcwd() + '/gis_peatland/Spatial'
outputPath = os.getcwd() + '/Spatial'





#print('cp '+dataPath+'/info/SpeciesParams.tab '+dataPath+'/SpeciesParams.tab')
#print('cp -a '+dataPath+'/. '+outputPath)

os.system('cp '+dataPath+'/info/SpeciesParams.tab '+dataPath+'/SpeciesParams.tab')

if os.path.exists(outputPath):
    os.system('rm -rf '+outputPath)
#os.system('ls '+dataPath)
print('cp -r '+dataPath+' '+outputPath)
os.system('cp -r '+dataPath+' '+outputPath)






