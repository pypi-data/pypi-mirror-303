import numpy as np
import multiprocessing as mp
import spiakid_simulation.functions.utils as Ut

def phase_conv(Photon,pix,conv_wv,conv_phase,resolution, process_nb):
    r"""Convert the wavelength in phase on each pixel

    Parameters:
    -----------

    Photon: array
        Photon's wavelength on each pixel

    pix: array
        Pixel id

    conv_wv: array
        Calibration's wavelength

    conv_phase: array
        Calibration's phase

    resolution: float
        Spectrale resolution of the detector

    Output:
    -------

    signal: array
        Phase on each pixel 
    
    
    """
    dim = np.shape(Photon)
    signal = np.zeros(dim,dtype = object)

    args = []
    for i in range(len(pix)):
        k,l = np.int64(pix[i].split(sep='_'))
        if k < dim[0] and l < dim[1]:
            args.append([Photon[k,l],conv_wv[i],conv_phase[i],resolution,(k,l)])

    with mp.Pool(processes=process_nb) as pool : 
        res = pool.map(photon2phase,args)

    for r in res:
        signal[r[0][0],r[0][1]] = r[1]
 
    return(signal)


def phase_conv_calib(data,pix,conv_wv,conv_phase,resolution, process_nb):
    signal_calib = []

  
    for wv in range(len(data)):
       
        sig = phase_conv(data[wv][1],pix,conv_wv,conv_phase,resolution, process_nb)
        signal_calib.append([data[wv],sig])

    
    return(signal_calib)

def photon2phase(args):
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

    Photon,conv_wv,conv_phase, resolution, inx = args
    signal = np.copy(Photon)
    curv = Ut.fit_parabola(conv_wv,conv_phase)
    ph = curv[0] * Photon[1] ** 2 +  curv[1] * Photon[1] + curv[2] #µ
    sigma = ph / (2*resolution*np.sqrt(2*np.log10(2)))
    signal[1] = np.where(Photon[1]==0,Photon[1],np.random.normal(ph, sigma))
    return(inx,signal)

def exp_adding(phase,decay, process_nb):
    r""" Add the exponential decay after the photon arrival on each pixel

    Parameters:
    -----------

    phase: array
        Signal on each pixel

    decay: float
        The decay of the decreasing exponential
    
    Output:
    -------
    
    signal: array
        The signal with the exponential decrease on each pixel 
    
    """
    dim = np.shape(phase)
    signal = np.zeros(dim,dtype = object)
    pool = mp.Pool(process_nb)
    res = []
    for i in range(dim[0]):
          for j in range(dim[1]):
            #    print(i,j)
            results = pool.apply_async(exp, args=(phase[i,j],decay,i,j))
            res.append((i,j,results))
            #    signal[i,j] = exp(phase[i,j],decay,signal,i,j)
    for i,j,result in res:
        _,_,value = result.get()
        signal[i,j] = value
    pool.close()
    pool.join()
    return(signal)

def exp_adding_calib(data,decay,process_nb):
    signal_calib = []
    dim = np.shape(data[0][1])
    for wv in range(len(data)):
        pool = mp.Pool(process_nb)
        res = []
        signal = np.zeros(dim,dtype = object)
        for i in range(dim[0]):
            for j in range(dim[1]):
                results = pool.apply_async(exp, args=(data[wv][1][i,j],decay,i,j))
                res.append((i,j,results))
        for i,j,result in res:
            _,_,value = result.get()
            signal[i,j] = value
          
        pool.close()
        pool.join()
        signal_calib.append([data[wv][0],signal])
    return(signal_calib)

def exp(sig,decay,i,j):
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
    sig_time = np.copy(sig[0])
    sig_amp = np.zeros((len(sig_time)))
    
    phase_point = np.copy(sig[1])
    for i in range(len(sig[1])):
        if phase_point[i] !=0:
                if i+500 < len(sig[0]):
                    for j in range(0,500):
                        exp_time = sig[0][i:i+500]
                        sig_amp[i+j] += sig[1][i] * np.exp(decay * (exp_time[j]-exp_time[0])) 
                else:
                     for j in range(0,len(sig[1])-i):
                        exp_time = sig[0][i:len(sig[1])]
                        sig_amp[i+j] += sig[1][i] * np.exp(decay * (exp_time[j]-exp_time[0]))
    return(i,j,[sig_time,sig_amp])


