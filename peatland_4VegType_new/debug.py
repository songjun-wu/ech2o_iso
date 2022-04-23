import numpy as np
import matplotlib.pyplot as plt

def debug(path, STATION, plotFlag):
    STATION += 1
    # Water states
    SoilMoistureL1 = np.loadtxt(path+'SoilMoistureL1.tab', skiprows=12)[:, STATION]
    SoilMoistureL2 = np.loadtxt(path+'SoilMoistureL2.tab', skiprows=12)[:, STATION]
    GroundWater = np.loadtxt(path+'GroundWater.tab', skiprows=12)[:, STATION]

    # Water fluxes
    Precip = np.loadtxt(path+'Precip.tab', skiprows=12)[:, STATION]*86400  # (m/s to m/d; *86400)


    SrftoChn = np.loadtxt(path+'SrftoChn.tab', skiprows=12)[:, STATION] #(m to m/d; *1)
    ChnLatI = np.loadtxt(path+'ChnLatI.tab', skiprows=12)[:, STATION] #(m to m/d; *1)
    GWtoChn = np.loadtxt(path+'GWtoChn.tab', skiprows=12)[:, STATION] #(m to m/d; *1)
    DeepGWtoChn = np.loadtxt(path+'DeepGWtoChn.tab', skiprows=12)[:, STATION] #(m to m/d; *1)
    streamflow = np.loadtxt(path+'Streamflow.tab', skiprows=12)[:, STATION]*34.56 #(m3/s to m/d; *dt/dx^2, i.e., 34.56)

    # Isotopic balance
    d2precip = np.loadtxt(path+'d2H_precip.tab', skiprows=12)[:, STATION]
    d2H_surface = np.loadtxt(path+'d2H_surface.tab', skiprows=12)[:, STATION]
    d2SoilL1 = np.loadtxt(path+'d2H_soilL1.tab', skiprows=12)[:, STATION]
    d2SoilL2 = np.loadtxt(path+'d2H_soilL1.tab', skiprows=12)[:, STATION]
    d2GW = np.loadtxt(path+'d2H_groundwater.tab', skiprows=12)[:, STATION]
    d2Chan = np.loadtxt(path+'d2H_chan.tab', skiprows=12)[:, STATION]


    aspectRatio = 11
    if plotFlag:
        fig, ax = plt.subplots(6, 4, sharex=True, sharey=False, figsize=(15,6))
        ax[1,0].imshow(SoilMoistureL1.T, aspect=aspectRatio)
        ax[2,0].imshow(SoilMoistureL2.T, aspect=aspectRatio)
        ax[3,0].imshow(GroundWater.T, aspect=aspectRatio)

        ax[0,1].imshow(Precip.T, vmin=0, vmax=0.3, aspect=aspectRatio)
        ax[1,1].imshow(SrftoChn.T, vmin=0, vmax=0.3, aspect=aspectRatio)
        ax[2,1].imshow(ChnLatI.T, vmin=0, vmax=0.3, aspect=aspectRatio)
        ax[3,1].imshow(GWtoChn.T, vmin=0, vmax=0.3, aspect=aspectRatio)
        ax[4,1].imshow(DeepGWtoChn.T, vmin=0, vmax=0.3, aspect=aspectRatio)
        ax[5,1].imshow(streamflow.T, vmin=0, vmax=0.3, aspect=aspectRatio)

        ax[0,2].imshow(d2precip.T, vmin=-80, vmax=-30, aspect=aspectRatio)
        ax[1,2].imshow(d2H_surface.T, vmin=-80, vmax=-30, aspect=aspectRatio)
        ax[2,2].imshow(d2SoilL1.T, vmin=-80, vmax=-30, aspect=aspectRatio)
        ax[3,2].imshow(d2GW.T, vmin=-80, vmax=-30, aspect=aspectRatio)
        ax[5,2].imshow(d2Chan.T, vmin=-80, vmax=-30, aspect=aspectRatio)
        
        ax[0,3].imshow((Precip*d2precip).T, vmin=-80, vmax=0, aspect=aspectRatio)
        ax[1,3].imshow((SrftoChn*d2H_surface).T, vmin=-80, vmax=0, aspect=aspectRatio)
        ax[2,3].imshow((ChnLatI*d2Chan).T, vmin=-80, vmax=0, aspect=aspectRatio)
        ax[3,3].imshow((GWtoChn*d2GW).T, vmin=-80, vmax=0, aspect=aspectRatio)
        ax[5,3].imshow((streamflow*d2Chan).T, vmin=-80, vmax=0, aspect=aspectRatio)
        plt.savefig('debug.png', dpi=300)
        plt.show()


path = r'./Outputs/'
STATION = np.arange(0,9,1)
plotFlag = True
debug(path, STATION, plotFlag)




