#*******************************************************************************
# CONFIGURATION FILE
#*******************************************************************************

import numpy as np
from datetime import datetime, timedelta


arr = np.fromfile('./outputs.1/OutletDischarge_all.tab')

print(arr.shape)
