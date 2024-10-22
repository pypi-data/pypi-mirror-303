import numpy as np
from scipy.optimize import least_squares
import numpy.random as rand

def photon_calib(dim,wv, typecalib):

    wv_len = len(wv)
    wv_step = np.linspace(start = wv[int(0.1*wv_len)],stop =wv[int(0.9*wv_len)], num = wv_len)
    wv_calib = np.zeros(shape = wv_len, dtype = object)
    x_det,y_det = dim, dim
   
    for wv in range(len(wv_step)):
        # print(wv)
        if typecalib == 'passband':
            Wavelength = np.ones([x_det,y_det, 2000]) * (wv_step[wv] + np.random.uniform(-0.005, 0.005, 2000))
        elif typecalib == 'laser':
            Wavelength = np.ones([x_det,y_det, 2000]) * wv_step[wv]
        Time = np.ones([x_det,y_det, 2000]) * np.linspace(0+500,1e6-500,2000, dtype = int)
        # detect = np.zeros([x_det,y_det],dtype = object)

        wv_calib[wv] = [Wavelength, Time]
    # print(len(dict_wv))
    return(wv_calib)


def ConversionTabCalib(Photon, conversion):
    dim_x, dim_y, _ = np.shape(Photon[0])
    pix, conv_wv, conv_phase = conversion
    convtab = np.zeros(shape = (dim_x, dim_y), dtype = object)
    for i in range(len(pix)):
        k, l = np.int64(pix[i].split(sep='_'))

        if k < dim_x and l < dim_y:
            convtab[k,l] = fit_parabola(conv_wv[i], conv_phase[i])

    return(convtab)

def PhaseNoiseCalib(photon, scale, baseline):

    dimx, dimy = np.shape(photon[0])
    sig = np.zeros(shape = (dimx, dimy), dtype = object)
    
    for i in range(dimx):
        for j in range(dimy):
            sig[i,j] = [photon[1][i,j], baseline[i,j] + photon[0][i,j] + rand.normal(loc = 0,scale = scale, size = len(photon[0][i,j] ))]
    
    return(sig)


def extractDigits(lst, decay):
    return list(map(lambda el:np.array(el * np.exp(decay * np.linspace(0,498,499) * 1e-6)).astype(np.float64), lst))


def AddingExp(ph, photonlist, time):
 
    addmatrix = np.zeros(shape = (len(ph)))
    for (t, photon) in zip(time, photonlist):

        addmatrix[int(t):int(t+len(photon))] = photon
    ph = ph + addmatrix
    return(ph)

def exp_adding_calib(photon,decay, exptime):

    # phasecalib = np.copy(photon)
    
    dimx, dimy,_ = np.shape(photon[0])
    phasecalib = np.zeros(shape=2, dtype = object)
    phasecalib[1] = np.zeros(shape=(dimx, dimy), dtype = object)
    phasecalib[0] = np.zeros(shape=(dimx, dimy), dtype = object)
    for i in range(dimx):
        for j in range(dimy):
            # print(time)
            
            photonlist = extractDigits(photon[0][i,j], decay)

            if photon[1][i,j][-1] + 500 > exptime:
                ph = np.zeros(shape= (photon[1][i,j][-1] + 500))
                
                extphoton = AddingExp(ph, photonlist, photon[1][i,j])
                phasecalib[0][i,j] = extphoton[:exptime]
                phasecalib[1][i,j] = np.linspace(0,exptime-1,exptime, dtype = int)
            
            else:
                ph = np.zeros(shape = exptime, dtype = int)

                phasecalib[0][i,j] = AddingExp(ph, photonlist, photon[1][i,j])
                phasecalib[1][i,j] = np.linspace(0,exptime-1,exptime, dtype = int)


    return(phasecalib)

def Photon2PhaseCalib(Photon, curv, resolution):
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

    
    dim_x, dim_y, _= np.shape(Photon[0])

    signal = np.copy(Photon)
    for i in range(dim_x):
        for j in range(dim_y):
       
                # for j in range(0,len(Photon[0][k,l])):

                ph = curv[i,j][0] * np.array(Photon[0][i,j]) ** 2 +  curv[i,j][1] * np.array(Photon[0][i,j]) + curv[i,j][2]
                sigma = ph / (2*resolution*np.sqrt(2*np.log10(2)))

                signal[0][i,j] = np.where(Photon[0][i,j]==0,0,np.random.normal(ph, sigma))
                signal[1][i,j] = Photon[1][i,j]
 
    return(signal)


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