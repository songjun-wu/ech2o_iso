import os
import sys

localPath = os.getcwd()
parPath = os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))
os.chdir('../ech2o_iso/Release-Linux/')

try:
    os.system('make all')
except:
    print('Error in make')
    sys.exit()
else:

    os.system('cp '+parPath+'/ech2o_iso/Release-Linux/ech2o_iso '+localPath+'/ech2o_iso')
    os.chdir(localPath)
    #os.system('./ech2o_iso config_debug.ini')
    #os.system('python3 debug.py')




