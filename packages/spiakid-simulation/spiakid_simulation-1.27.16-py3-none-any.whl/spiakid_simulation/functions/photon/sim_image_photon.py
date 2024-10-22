import numpy as np
from scipy import interpolate
import numpy.random as rand
import csv
import multiprocessing as mp
from multiprocessing import shared_memory

def photon_nbr(wavelength,spectre,time,diam,transmission):
    if type(transmission) == str:
        func_trans = trans_read(transmission)
        value = func_trans(wavelength)
        spectre *= value
    spectre = spectre * wavelength * 10**-3 / (6.26*10**-34 *3*10**8) * np.pi * (diam/2)**2  * time
    nbr = spectre.max() * (wavelength[-1]-wavelength[0]) * 10**-6 

    return(int(nbr),spectre)



def photon(wavelength,spectre,time,diam,point_nb,transmission=False):
    ph = {}

    for st in range(len(spectre)): 

        ph_nbr,sp = photon_nbr(wavelength,spectre[st][:],time,diam,transmission)
        print(ph_nbr)
        lbd = rand.uniform(low = wavelength[0],high = wavelength[-1],size = ph_nbr)
        t=rand.uniform(low=0,high = time*point_nb,size = ph_nbr)
        intens=rand.uniform(low = 0,high = sp.max(),size = ph_nbr)
        sp_func = interpolate.interp1d(wavelength,sp)
        pop_list = []
        dic_list = []
        for i in range(ph_nbr):
            if intens[i] > sp_func(lbd[i]):
                pop_list.append(i)
            else:
                dic_list.append([lbd[i],t[i]])
        lbd = np.delete(lbd,pop_list)
        t = np.delete(t,pop_list)
        ph[st] = dic_list

    return(ph)

def trans_read(path,sep='/'):
    # Wavelength in µm ! 
    wv = []
    trans = []
    with open(path,'r') as file:
        data = csv.reader(file,delimiter = sep)
        for i in data:
            wv.append(eval(i[0]))
            trans.append(eval(i[1]))

    Trans_func = interpolate.interp1d(wv,trans)

    return(Trans_func)

def detector_scale(detector_dim,photon_dict):
    Wavelength = np.zeros(detector_dim,dtype = object)
    Time = np.zeros(detector_dim,dtype = object)

    x_det,y_det = detector_dim

    for i in range(x_det):
        for j in range(y_det):
            Wavelength[i,j] = []
            Time[i,j] = []


    for ph in range(len(photon_dict)):
        if int(photon_dict[ph][0]) < x_det and int(photon_dict[ph][1]) < y_det and int(photon_dict[ph][0]) >= 0 and int(photon_dict[ph][1]) >= 0 :
            Wavelength[int(photon_dict[ph][0]),int(photon_dict[ph][1])].append(photon_dict[ph][2])
            Time[int(photon_dict[ph][0]),int(photon_dict[ph][1])].append(photon_dict[ph][3])

    return(Wavelength,Time)


def rejct_filter(args):

    shm_name_pos,shm_name_energy = args[0][0],args[0][1]
    shm_shape_pos,shm_shape_energy = args[1][0],args[1][1]
    shm_dtype_pos,shm_dtype_energy = args[2][0],args[2][1]

    max_psf = args[3]
    lbd = args[4]
    time = args[5]
    PSF_size = args[6]
    WVarray = args[7]

    existing_smh_pos = shared_memory.SharedMemory(name = shm_name_pos)
    existing_smh_energy = shared_memory.SharedMemory(name = shm_name_energy)

    data_pos = np.ndarray(shm_shape_pos, dtype = shm_dtype_pos, buffer = existing_smh_pos.buf)
    data_energy = np.ndarray(shm_shape_energy, dtype = shm_dtype_energy, buffer = existing_smh_energy.buf)

    WVindx = (np.abs(WVarray-lbd)).argmin()
    stop = 0
    while stop == 0:

        pix = np.random.randint(len(data_pos[WVindx]))
        E = np.random.uniform(low = 0,high = max_psf[WVindx])
        if E<= data_energy[WVindx][pix]:
            x = data_pos[WVindx][pix][0]
            y = data_pos[WVindx][pix][1]
            stop += 1
            
    existing_smh_pos.close()
    existing_smh_energy.close()
    return([x-0.5*PSF_size,y-0.5*PSF_size, lbd,time])


def photon_pos_on_PSF(star_pos,photon_dic,POS, ENERGY, max_psf, PSF_size,WVarray, nb_process):
    dict_photon = {}

    # Going through the star list
    for st in range(len(star_pos)):
        args = []
        # Looking for all photon for this star

        shm_pos = shared_memory.SharedMemory(name='POS',create = True,size=POS.nbytes)
        shared_data_pos = np.ndarray(POS.shape,dtype = POS.dtype,buffer=shm_pos.buf)
        np.copyto(shared_data_pos,POS)

        shm_energy = shared_memory.SharedMemory(name='ENERGY',create = True,size=ENERGY.nbytes)
        shared_data_energy = np.ndarray(ENERGY.shape,dtype = ENERGY.dtype,buffer=shm_energy.buf)
        np.copyto(shared_data_energy,ENERGY)


        for ph in range(len(photon_dic[st])):

            args.append([[shm_pos.name,shm_energy.name],[POS.shape,ENERGY.shape],[POS.dtype,ENERGY.dtype],max_psf,photon_dic[st][ph][0],photon_dic[st][ph][1],PSF_size,WVarray])
  
       
        with mp.Pool(processes=nb_process) as pool:

            results = pool.map(rejct_filter, args)



        dict_photon[st] = results

        shm_pos.close()
        shm_pos.unlink()

        shm_energy.close()
        shm_energy.unlink()

    return(dict_photon)

def photon_proj(Photon_dict, star_pos, psf_to_detect,rot_func, alt_ev, size, FOV,lam0,point_nb):
    dict_photon = []
    pix_length = FOV/size

    for st in range(len(star_pos)):
        for ph in range(len(Photon_dict[st])):
            # Adding the star position taking account of rotation + ratio psf size to dectector size
            x_ph, y_ph = Photon_dict[st][ph][0] / psf_to_detect + rot_func[st][0](Photon_dict[st][ph][3]/point_nb), Photon_dict[st][ph][1] / psf_to_detect + rot_func[st][1](Photon_dict[st][ph][3]/point_nb)
            alt = alt_ev[st](Photon_dict[st][ph][3]/point_nb)  # photon altitude at t
   
            DR = dispersion(np.pi/2 - alt, lam0, Photon_dict[st][ph][2])

            y_ph = y_ph + DR * pix_length
            dict_photon.append([x_ph,y_ph,Photon_dict[st][ph][2],Photon_dict[st][ph][3]])
    return(dict_photon)


def dispersion(Z, Lam0, Lam, TC=11.5, RH=14.5, P=743):
    """
    The routine compute the Differential Atmospheric Dispersion
    for a given zenithal distance "Z" for different wavelengths "Lam"
    with respect to a reference wavelength "Lam0".

    The atmospheric parameters can be adjusted to those characterstic
    of the site the computation is made for.
    The parameters listed below refer to the average Paranal conditions.
    
    Routine from Enrico Marchetti, taken on eso.org website, translated from
    IDL by E Gendron.
    
    Parameters
    ----------
    Z       : float. The zenithal distance 
    Lam0 : float. The reference wavelength in microns.
    Lam  : float or array. Wavelength(s) in microns.
    TC      : float. Temperature at the ground [C°]
    RH      : flaot. Relative humidity at the ground [%]
    P       : float. Pressure at the ground [mbar]
    
    For La Silla site, the median params are TC=11.5, RH=14.5, P=743.
    For Armazones site, the median params are TC=7.5, RH=15, P=712.

    Returns
    -------
    DR : Same array as Lam. Amplitude of the differential atmospheric
    dispersion with respect to the reference wavelength Lam0.
    """
    T = TC + 273.16
    PS = -10474.0+116.43*T-0.43284*T**2+0.00053840*T**3
    P2 = RH/100.0*PS
    P1 = P-P2
    D1 = P1/T*(1.0+P1*(57.90*1.0E-8-(9.3250*1.0E-4/T)+(0.25844/T**2)))
    D2 = P2/T*(1.0+P2*(1.0+3.7E-4*P2)*(-2.37321E-3+(2.23366/T)-
            (710.792/T**2)+(7.75141E4/T**3)))
    S0 = 1.0/Lam0
    S = 1.0/Lam
    N0_1 = 1.0E-8*((2371.34+683939.7/(130-S0**2)+4547.3/(38.9-S0**2))*D1+
            (6487.31+58.058*S0**2-0.71150*S0**4+0.08851*S0**6)*D2)
    N_1 = 1.0E-8*((2371.34+683939.7/(130-S**2)+4547.3/(38.9-S**2))*D1+
            (6487.31+58.058*S**2-0.71150*S**4+0.08851*S**6)*D2)
    DR = np.tan(Z)*(N0_1-N_1)*206264.8
    return (DR)


def photon_calib(dim,wv):
    wv_len = len(wv)
    wv_step = np.linspace(start = wv[int(0.25*wv_len)],stop =wv[int(0.75*wv_len)], num = 3)

    x_det,y_det = dim
    dict_wv = []
    for wv in wv_step:

        Wavelength = np.zeros(dim,dtype = object)
        Time = np.zeros(dim,dtype = object)
        

        for i in range(x_det):
            for j in range(y_det):
             
                Wavelength[i,j] = np.ones(shape = 2000) * wv
                Time[i,j] = np.linspace(0,1,2000)
        dict_wv.append([wv,Wavelength,Time])

    # print(len(dict_wv))
    return(dict_wv)