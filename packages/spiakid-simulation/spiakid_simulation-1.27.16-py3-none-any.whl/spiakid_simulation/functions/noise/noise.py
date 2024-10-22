# import numpy as np
# import numpy.random as rand
# import multiprocessing as mp

# def gaussian(x,scale=4):
#     r""" Add Gaussian noise on the signal

#     Parameters:
#     -----------

#     x: array
#         Signal on each pixel
    
#     location: float
#         Expected value of the guassian noise
    
#     scale: float
#         Standard deviation of the gaussian noise
    
#     Output:
#     -------

#     signal: array
#         The signal with the Gaussian noise
#     """
#     dim = np.shape(x)
#     if (type(x[0,0]) == np.int16) | (type(x[0,0]) == np.float64):
#         signal = np.zeros(dim,dtype = float)
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 signal[i,j] = x[i,j] +  rand.normal(loc = 0,scale = scale)
#     else:
#         signal = np.zeros(dim,dtype = object)
#         pool = mp.Pool(5)
#         res = []
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 results = pool.apply_async(apply_gauss,args=(x,i,j,scale))
#                 res.append((i,j,results))
#         for i,j,result in res:
#             _,_,value = result.get()
#             signal[i,j] = [x[i,j][0],value]
#         pool.close()
#         pool.join()
#     return(signal)

# def apply_gauss(x, i, j, scale):

#     signal = np.zeros(shape=len(x[i,j][0]))
#     for k in range(len(x[i,j][0])):
#         signal[k] = x[i,j][1][k] +  rand.normal(loc = 0,scale = scale)
        
#     return(i,j,signal)

# def poisson(x):
#     r""" Add Poisson noise on the signal

#     Parameters:
#     -----------

#     x: array
#         Signal on each pixel
    
#     Output:
#     -------

#     signal: array
#         The signal with the Poisson noise
#     """
#     rng = rand.default_rng()
#     dim = np.shape(x)
#     if (type(x[0,0]) == np.int16) | (type(x[0,0]) == np.float64):
#         signal = np.zeros(dim,dtype = float)
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 signal[i,j] = float(rng.poisson(x[i,j]))
#     else:
#         signal = np.zeros(dim,dtype = object)
#         pool = mp.Pool(5)
#         res = []
#         for i in range(dim[0]):
#             for j in range(dim[1]):
#                 results = pool.apply_async(apply_poisson,args=(x,i,j))
#                 res.append((i,j,results))
#         for i,j,result in res:
#             _,_,value = result.get()
#             signal[i,j] = value
#         pool.close()
#         pool.join()
#     return(signal)

# def apply_poisson(x,i,j):
#     time = x[i,j][0]
#     rng = rand.default_rng()
#     signal = np.zeros(shape=len(x[i,j][0]))
#     for k in range(len(x[i,j][0])):
#         signal[k] = rng.poisson(x[i,j][1][k])
#     return(i,j,[time,signal])


import numpy as np
import numpy.random as rand


def gaussian(x,scale=4):
    r""" Add Gaussian noise on the signal

    Parameters:
    -----------

    x: array
        Signal on each pixel
    
    location: float
        Expected value of the guassian noise
    
    scale: float
        Standard deviation of the gaussian noise
    
    Output:
    -------

    signal: array
        The signal with the Gaussian noise
    """
    dim = np.shape(x)
    if (type(x[0,0]) == np.int16) | (type(x[0,0]) == np.float64):
        signal = np.zeros(dim,dtype = float)
        for i in range(dim[0]):
            for j in range(dim[1]):
                signal[i,j] = x[i,j] +  rand.normal(loc = 0,scale = scale)
    else:
        signal = np.zeros(dim,dtype = object)
        for i in range(dim[0]):
            for j in range(dim[1]):
                signal[i,j] = np.zeros(np.shape(x[i,j]))
                signal[i,j][0] = x[i,j][0]
                signal[i,j][1] = x[i,j][1] + rand.normal(loc = 0,scale = scale, size = len(x[i,j][1]))
    return(signal)

def gaussian_calib(data,scale):
    
    dim = np.shape(data[0][1])
    for wv in range(len(data)):
        for i in range(dim[0]):
            for j in range(dim[1]):
                data[wv][1][i,j][1] = np.array(data[wv][1][i,j][1]) + rand.normal(loc = 0,scale = scale, size = len(data[wv][1][i,j][1]))

    return(data)

def poisson(x):
    r""" Add Poisson noise on the signal

    Parameters:
    -----------

    x: array
        Signal on each pixel
    
    Output:
    -------

    signal: array
        The signal with the Poisson noise
    """
    rng = rand.default_rng()
    dim = np.shape(x)
    if (type(x[0,0]) == np.int16) | (type(x[0,0]) == np.float64):
        signal = np.zeros(dim,dtype = float)
        for i in range(dim[0]):
            for j in range(dim[1]):
                signal[i,j] = float(rng.poisson(x[i,j]))
    else:
        signal = np.zeros(dim,dtype = object)
        for i in range(dim[0]):
            for j in range(dim[1]):
                signal[i,j] = np.zeros(np.shape(x[i,j]))
                signal[i,j][0] = x[i,j][0]
                for k in range (len(signal[i,j][0])):
                    signal[i,j][1][k] = rng.poisson(x[i,j][1][k])
    return(signal)
