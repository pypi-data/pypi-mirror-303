import numpy as np
import numpy.random as rand

from pathlib import Path

from astropy.io import fits
from scipy import interpolate

import multiprocessing as mp

def image_sim(pix_nb,pix_size, object_number, distance,Path_file,Wavelength,spectrum,save = False):  # Wavelength in µm
    r""" Simulate an image of the sky night and save the datacube in WCS compatible format.

        Parameters:
        -----------

        Image_size: int
            Size of the image (number of pixel on the column/row)

        object_number: int
            Number of stars on the sky
        
        distance: couple
            Distance of simulated stars in parsec

        Path_file: str
            Path to save the datacube
        
        Output:
        -------

        None
        
        """
    # Image Creation

    image = []
    Image_size = int(pix_nb)
    # importing spectrums
    files = Path(spectrum).glob('*')
    Spectrum_path = []
    Point = len(Wavelength)
    Object_dict = {}
    posx = []
    posy = []
    dist = []
    pos = []
    for i in files:
        Spectrum_path.append(i)

    # Object creation (position + spectrum path)
    for i in range(object_number):
        pos_x = rand.uniform(low =int(-0.25*Image_size), high= int(1.25*Image_size))
        pos_y = rand.uniform(low = int(-0.25*Image_size), high= (1.25*Image_size))
        print(pos_x,pos_y)
        Object_dict[i] = {}
        Object_dict[i]['Position'] = [pos_x,pos_y]
        data_init = np.loadtxt(Spectrum_path[rand.randint(len(Spectrum_path))])
        Object_dict[i]['Spectrum'] = interpolate.interp1d(data_init[:,0],data_init[:,1])   #nm
        Object_dict[i]['Distance'] =  rand.randint(distance[0], distance[1]) # Distance Parsec
        dist.append(Object_dict[i]['Distance'])
        Object_dict[i]['Intensity'] = 1 * (10 / dist[-1]**2)
        posx.append(pos_x)
        posy.append(pos_y)
        pos.append([i,pos_x,pos_y])

    Spec = []

    
    for obj in range(object_number):
        spectrum = []
        for i in range(Point):
            spectrum.append((10 / dist[obj]**2) * Object_dict[obj]['Spectrum'](Wavelength[i]*10**3))
        Spec.append(spectrum)



    image = np.zeros([int(1.25*Image_size) - int(-0.25*Image_size), int(1.25*Image_size)- int(-0.25*Image_size),len(Wavelength)])
    for i in range(Point):
         for obj in range(object_number):
              image[int(posx[obj]),int(posy[obj]),i] = Object_dict[obj]['Intensity']


    if save == True:
        hdr = fits.Header()
        hdr['CTYPE3'] = 'RA---CAR'
        hdr['CTYPE2'] = 'DEC--CAR'
        hdr['CTYPE1'] = 'WAVE'
        hdr['CUNIT3'] = 'deg'
        hdr['CUNIT2'] = 'deg'
        hdr['CUNIT1'] = 'nm'
        hdr['CRVAL3'] = 0
        hdr['CRVAL2'] = 0
        hdr['CRVAL1'] = Wavelength[0]*10**3
        hdr['CDELT1'] = (Wavelength[1]-Wavelength[0])*10**3
        hdr['CDELT3'] = 1.0e-4
        hdr['CDELT2'] = 1.0e-4
        primary_hdu = fits.PrimaryHDU(image,header=hdr)

        hdul = fits.HDUList([primary_hdu])
        hdul.writeto(Path_file,overwrite=True)
    return(pos,Spec)


