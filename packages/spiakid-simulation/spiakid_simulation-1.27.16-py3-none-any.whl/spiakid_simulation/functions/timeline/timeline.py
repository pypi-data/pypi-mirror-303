import numpy as np
import multiprocessing as mp


def pixel_sorting(args):
        r""" Sort value according to the time

        Parameters:
        -----------

        time: float
            Time of observation

        data: array
            Photon's wavelength
        
        point_nb: int
            Number of point we want
        
        Output:
        -------

        signal: array
            Arrival time and wavelength of photons randomly spread
        
        """
        time = args[0]
        data = args[1]
        point_nb = args[2]
        time_data = args[3]
        inx = args[4]
        point_nb = int(point_nb)
        sig = list(np.zeros([2,point_nb]))

        if type(data) == list:
            if len(data)>0 : 
                sig[0] = np.linspace(0,time,point_nb)
    
                sig[1][time_data] = data

            else:
                sig = list(np.zeros([2,point_nb]))
                sig[0] = np.linspace(0,time,point_nb)

        
        
        else:
             sig = list(np.zeros([2,point_nb]))
             sig[0] = np.linspace(0,time,point_nb)

        return(inx,sig)
        


def sorting(time,data,point_nb, time_data, process_nb):
    r""" Sort value according to the time on each pixel

        Parameters:
        -----------

        time: float
            Time of observation

        data: array
            Photon's wavelength
        
        point_nb: int
            Number of point we want
        
        Output:
        -------

        signal: array
            Arrival time and wavelength of photons randomly spread on each pixel
        
        """
    dim = np.shape(data)
    

    signal = np.zeros(dim,dtype = object)
    Point_number = point_nb * time
  

    args = []
    res = []
    for i in range(dim[0]):
          for j in range(dim[1]):
          
            
            args.append([time,data[i,j],Point_number,np.int64(time_data[i,j]),(i,j)])

    with mp.Pool(processes=process_nb) as pool:
        res = pool.map(pixel_sorting,args)
    for r in res:
        signal[r[0][0],r[0][1]] = r[1]

    return(signal)



def sorting_calib(dim, point_number,wv_inter):
    inter = wv_inter[1]-wv_inter[0]
    wv_step = np.linspace(start = wv_inter[0]+0.25*inter,stop = wv_inter[0] + 0.75*wv_inter[1], num = 3)
    x_det,y_det = dim
    element = 300
    signal_calib = []
    
    for wv in wv_step:
        signal = np.zeros(shape=dim,dtype = object)
        for i in range(x_det):
             for j in range(y_det):
                time = np.linspace(0,1,point_number)
                wv_list = np.zeros(shape = point_number)
                indx = np.round(np.linspace(element-1,len(wv_list)-1,int(len(wv_list-element)/element))).astype(int)
                wv_list[indx] = wv
                signal[i,j] = [time,wv_list]
        
        signal_calib.append([wv,signal])

    return(signal_calib)