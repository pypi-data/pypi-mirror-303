import numpy as np
import multiprocessing as mp
import csv
from scipy.optimize import least_squares
import numpy.random as rand



def ConversionTab(Photon, conversion):
    dim_x, dim_y = np.shape(Photon[0])
    pix, conv_wv, conv_phase = conversion
    convtab = np.zeros(shape = (dim_x, dim_y), dtype = object)
    for i in range(len(pix)):
        k, l = np.int64(pix[i].split(sep='_'))

        if k < dim_x and l < dim_y:
            convtab[k,l] = fit_parabola(conv_wv[i], conv_phase[i])

    return(convtab)



def photon2phase(Photon, curv, resolution):
    r"""Convert the wavelength in phase

    Parameters:
    -----------

    Photon: array
        Photon's wavelength on each pixel

    conv_wv: array
        Calibration's wavelength

    conv_phase: array
        Calibration's phase

    Output:
    -------

    signal: array
        Signal converted in phase 
    
    
    """

    
    dim_x, dim_y= np.shape(Photon[0])

    signal = np.copy(Photon)
    for i in range(dim_x):
        for j in range(dim_y):
       
                # for j in range(0,len(Photon[0][k,l])):

                ph = curv[i,j][0] * np.array(Photon[0][i,j]) ** 2 +  curv[i,j][1] * np.array(Photon[0][i,j]) + curv[i,j][2]
                sigma = ph / (2*resolution*np.sqrt(2*np.log10(2)))

                signal[0][i,j] = np.where(Photon[0][i,j]==0,0,np.random.normal(ph, sigma))
 
    return(signal)
    #         curv = fit_parabola(conv_wv,conv_phase)
    # ph = curv[0] * Photon[1] ** 2 +  curv[1] * Photon[1] + curv[2] #µ
    # sigma = ph / (2*resolution*np.sqrt(2*np.log10(2)))
    # signal[1] = np.where(Photon[1]==0,Photon[1],np.random.normal(ph, sigma))
    # return(inx,signal)

def PhaseNoise(photon, scale, baseline = None):

    dimx, dimy = np.shape(photon[0])
    sig = np.zeros(shape = 2, dtype = object)
    sig[0] = np.zeros(shape = (dimx, dimy), dtype = object)
    sig[1] = np.zeros(shape = (dimx, dimy), dtype = object)


    for i in range(dimx):
        for j in range(dimy):
            sig[0][i,j] = []
            sig[1][i,j] = []
            if len(photon[0][i,j]) >0:
                for k in range(len(photon[0][i,j])):
                    if baseline == None:
                        sig[0][i,j].append(rand.normal(loc = 0,scale = scale, size = len(photon[0][i,j][k] )) + photon[0][i,j][k])
                    else:
                        sig[0][i,j].append(rand.normal(loc = baseline[i,j],scale = scale, size = len(photon[0][i,j][k] )) + photon[0][i,j][k])
                    sig[1][i,j].append(np.copy(photon[1][i,j][k]))

    return(sig)



def exp_adding(photon,decay, exptime):
    r""" Add the exponential decay after the photon arrival

    Parameters:
    -----------

    sig: array
        Signal with the photon arrival

    decay: float
        The decay of the decreasing exponential
    
    Output:
    -------
    
    signal: array
        The signal with the exponential decrease
    
    """

    listph = np.zeros(np.shape(photon[0]), dtype = object)
    listtime = np.zeros(np.shape(photon[0]), dtype = object)
    dimx, dimy = np.shape(photon[0])
    
    for i in range(dimx):
        for j in range(dimy):
            listph[i,j] = []
            listtime[i,j] = []
            if len(photon[0][i,j])>0:
                for k in range(len(photon[0][i,j])):
                    if int(photon[1][i,j][k]) + 500 < exptime * 1e6:
                        listtime[i,j].append(np.linspace(0,499,500, dtype = int)+int(photon[1][i,j][k]))
                        listph[i,j].append(photon[0][i,j][k] * np.exp(decay * np.linspace(0,499,500, dtype = int)/1e6) )
                    else:
                        t = int( (int(photon[1][i,j][k]) + 500)- int(exptime*1e6))

                        listph[i,j].append(photon[0][i,j][k] * np.exp(decay * np.linspace(0,t-1,t)/1e6))
                        listtime[i,j].append(np.linspace(0,t-1,t, dtype = int)+int(photon[1][i,j][k]))


    return([listph, listtime])



def read_csv(Path,sep='/'):
    r"""Read the calibration file

    Parameters:
    -----------

    Path: string
        Path to the calibration file
    
    sep: string
        The delimiter

    Output:
    -------

    pix: array
        The pixel id

    wv: array
        Calibration wavelength

    phase: array
        Calibration phase          
    
    
    """
    pix = []
    wv = []
    phase = []
    with open(Path,'r') as file:
        data = csv.reader(file,delimiter = sep)
        for i in data:
            pix.append(i[0])
            wv.append(eval(i[2]))
            phase.append(eval(i[1]))
    return(pix,wv,phase)


def fit_parabola(wavelength, phase):
        def model(x,u):
            return(x[0]*u**2 + x[1]*u + x[2])     
        def fun(x,u,y):
            return(model(x,u) - y)
        def Jac(x,u,y):
            J = np.empty((u.size,x.size))
            J[:,0] = u**2
            J[:,1] = u
            J[:,2] = 1
            return(J)
        t = np.array(wavelength)
        dat = np.array(phase)
        x0 = [1,1,1]
        res = least_squares(fun, x0, jac=Jac, args=(t,dat)) 
        return res.x[0],res.x[1],res.x[2]
