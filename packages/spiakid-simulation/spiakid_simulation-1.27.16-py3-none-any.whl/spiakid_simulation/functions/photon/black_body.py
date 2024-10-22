import numpy as np
import numpy.random as rand
from astropy.modeling import models
from astropy import units as u
import matplotlib.pyplot as plt
from astropy.visualization import quantity_support
import multiprocessing
import time


def Black_Body_spectrum(Temperature,wv_min,wv_max):
    r"""Give photons with a random wavelength and radiance and sort them according to Black Body

    Parameters:
    -----------

    Temperature: float
        The temperature of the Black Body
    
    NbPhton: int
        How many photon to sort
    
    wv_min: float
        The minimum wavelength
    
    wv_max: float
        The maximum wavelength
    
    Output:
    -------

    wv_ok: array
        Wavelength of simulated photon which fit in the Black Body

    bb_ok: array
        Radiance of simulated photon which fit in the Black Body

    wv_out: array
        Wavelength of simulated photon which doesn't fit in the Black Body

    bb_out:
        Radiance of photon which doesn't fit in the Black Body

    """

    c = 299792458e6*u.um/u.s #µm.s-1
    array = np.linspace(wv_min,wv_max,100000)*u.um # Wavelength in µm
    nu = c/array
    bb = models.BlackBody(temperature=Temperature*u.K)
    Black_Body = bb(nu)  # erg.Hz-1.s-1.cm-2
    return (Black_Body.value)


def BB_filter(Temperature,FitsPhoton,wv_min=0.38,wv_max=1):
    r"""Give photons with a random wavelength and radiance and sort them according to Black Body for each pixel

    Parameters:
    -----------

    Temperature: float
        The temperature of the Black Body
    
    FitsPhoton: int
        How many photon to sort
    
    wv_min: float
        The minimum wavelength
    
    wv_max: float
        The maximum wavelength
    
    Output:
    -------

    wv_ok: array
        Wavelength of simulated photon which fit in the Black Body for each pixel

    bb_ok: array
        Radiance of simulated photon which fit in the Black Body for each pixel

    wv_out: array
        Wavelength of simulated photon which doesn't fit in the Black Body for each pixel

    bb_out:
        Radiance of simulated photon which doesn't fit in the Black Body for each pixel

    """
    BB_photon_ok = np.zeros(np.shape(FitsPhoton), dtype=object)
    BB_photon_out = np.zeros(np.shape(FitsPhoton), dtype=object)
    BB_radiance_ok = np.zeros(np.shape(FitsPhoton), dtype=object)
    BB_radiance_out = np.zeros(np.shape(FitsPhoton), dtype=object)


    for i in range(len(FitsPhoton[0])):
        for j in range(len(FitsPhoton[1])):

            wv_ok,bb_ok,wv_out,bb_out =Black_Body(Temperature=Temperature, NbPhoton=FitsPhoton[i,j],wv_min=wv_min,wv_max=wv_max)
            BB_photon_ok[i,j] = wv_ok
            BB_photon_out[i,j] = wv_out
            BB_radiance_ok[i,j] = bb_ok
            BB_radiance_out[i,j] = bb_out
    return(BB_photon_ok,BB_radiance_ok,BB_photon_out,BB_radiance_out)


# #Test
# Fits = [[300,500,200],
#         [100,405,200],
#         [102,807,51]]
# Fits = np.array(Fits)
# temperature = 5800
# a,b,c,d = BB_filter(temperature,Fits)
# print(len(a[2,1]))



# def func(n):
#     return(n**2)


# num_arr = range(10**7)

# st = time.time()
# res_1 = []
# for i in num_arr:
#     res_1.append(func(i))
# en=time.time()
# print('lin',en-st)


# num_process = 4
# st = time.time()
# with multiprocessing.Pool(processes=num_process) as pool:
#     res = pool.map(func, num_arr)
# pool.close()
# en=time.time()
# print('multi',en-st)