import numpy as np
import numpy.random as rand
from astropy.io import fits
from pathlib import Path
from scipy import interpolate
import matplotlib.pyplot as plt
import h5py
from scipy.signal import find_peaks

from spiakid_simulation.new_version.fun.PSF.turbulence import PSF_creation, PSF_creation_mult
from spiakid_simulation.new_version.fun.DataReading import data_check
from spiakid_simulation.new_version.fun.Photon.sim_image_photon import photon, photon_pos_on_PSF, photon_proj, detector_scale
from spiakid_simulation.new_version.fun.Rot.rot import EarthRotation

from spiakid_simulation.new_version.fun.Phase.phase_conversion import read_csv, photon2phase, exp_adding, PhaseNoise,  ConversionTab
from spiakid_simulation.new_version.fun.Calibration.Calib import exp_adding_calib , PhaseNoiseCalib, ConversionTabCalib, Photon2PhaseCalib, photon_calib
from spiakid_simulation.new_version.fun.Filter.filter import PSD, Template, FilterCreation

from spiakid_simulation.new_version.fun.output.HDF5_creation import recursively_save_dict_contents_to_group
import tracemalloc
import gc


class Simulation():
    __slots__ = ('detect', 'psf', 'stars')
    def __init__(self,file ):

        # Data reading
        tracemalloc.start()
        global DATA
        DATA = data_check(file)

        global path
        path = DATA['sim_file']

        global h5file
        h5file = h5py.File(path, 'w')

        global phgen
        phgen = DATA['Photon_Generation']

        global telescope
        telescope = phgen['telescope']
        global exptime 
        exptime = telescope['exposition_time']
        global diameter 
        diameter = telescope['diameter']
        global obscuration
        obscuration = telescope['obscuration']
        global latitude
        latitude = telescope['latitude'] * np.pi / 180 
        global transmittance
        transmittance = telescope['transmittance']
        global pxnbr
        pxnbr = telescope['detector']['pix_nbr']
        global pxsize 
        pxsize = telescope['detector']['pix_size']
        global baseline
        baseline =  telescope['detector']['baseline']

        if baseline =='random':
            global baselinepix
            baselinepix = np.random.uniform(low = 10, high = 20, size = (pxnbr, pxnbr))

            h5file['baseline/Baseline'] = baselinepix
            
        elif baseline == 'uniform':
            baselinepix = np.zeros(shape = (pxnbr, pxnbr))
    
        global weightmap
        weightmap = telescope['detector']['weightmap']

        global timelinestep 
        timelinestep = telescope['detector']['point_nb']
        global calibtype
        calibtype = telescope['detector']['calibration']
        # if calibtype =='import':
        #     global calibfile
        #     calibfile = telescope['detector']['calibfile']


        global nbwv
        nbwv = telescope['detector']['nbwavelength']

        st = phgen['star']
        global stnbr 
        stnbr = st['number']
        global stdistmin
        stdistmin = st['distance']['min']
        global stdistmax
        stdistmax = st['distance']['max']
        global wv
        wv = np.linspace(st['wavelength_array']['min'],
                        st['wavelength_array']['max'],
                        st['wavelength_array']['nbr'])
        global spectrum 
        spectrum = st['spectrum_folder']

        sky = phgen['sky']


        global rotation
        rotation = sky['rotation']
        global altguide 
        altguide = sky['guide']['alt'] * np.pi / 180 
        global azguide 
        azguide = sky['guide']['az'] * np.pi / 180 
        
        

  
        global spectrumlist 
        spectrumlist = []
        files = Path(spectrum).glob('*')
        for i in files:
            spectrumlist.append(i)

        
        
        try:
            global save_type
            save_type = DATA['Output']['save']
        except: pass

        try: DATA['Phase']
        except: pass
        else:
            global calibfile
            calibfile = DATA['Phase']['Calib_File']
            global conversion
            conversion = read_csv(calibfile)
            global nphase
            nphase = DATA['Phase']['Phase_Noise']
            global decay
            decay = - DATA['Phase']['Decay']
            global nreadoutscale
            nreadoutscale = DATA['Phase']['Readout_Noise']['scale']
            global nreadouttype
            nreadouttype = DATA['Phase']['Readout_Noise']['noise_type']

            

            global nperseg
            nperseg = DATA['Electronic']['nperseg']

            global templatetime
            templatetime = DATA['Electronic']['template_time']
            
            global trigerinx
            trigerinx = DATA['Electronic']['trigerinx']

            global pointnb
            pointnb = DATA['Electronic']['point_nb']



            # Detector Creation
            self.detect = self.Detector()
        recursively_save_dict_contents_to_group(h5file, '/', DATA)

        #PSF computing
        self.psf = self.PSF()

        self.stars = {}
        # Star and photon creation
        for i in range(0, stnbr):
            print('star %i'%i)
            self.stars['star_'+str(i)] = self.Star(self.psf,i)
            
        
        gc.collect()
        try: DATA['Phase']
        except: pass
        else:
            # Photon distribution on the detector 
            self.stars['Detector'] = self.PhotonDetection(self.stars, self.detect.noisetimeline, self.detect.wmap)
        print('End detector', flush = True)
        # try:
        #     self.Output(save_type)
        # except: 
        #     pass
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        

    class PSF():
            __slots__ = ('psfpxnbr', 'psfsize','psfenergy','psfpos','maxpsf','psf')
            def __init__(self):

        
                try: phgen['PSF']
                except:
                        self.gaussian_psf(pxnbr=pxnbr, pxsize=pxsize, wv=wv)
                else:
                        psf = phgen['PSF']
                        psfmeth = psf['method']
                        psffile = psf['file']
                        try: psfmeth == 'Download'
                        except:
                            self.defined_psf(psf=psf,psffile=psffile, wv=wv, diameter=diameter,
                                            obscuration=obscuration,exptime=exptime)
                        else:
                            file = fits.open(psffile)[0]
                            self.psf = file.data
                            list_axis = [file.header['NAXIS1'],file.header['NAXIS2'],file.header['NAXIS3']]
                            if (list_axis.count(file.header['NAXIS1']) == 2)  and (file.header['CUNIT1'] == 'arcsec'):
                                self.psfpxnbr = file.header['NAXIS1']
                                self.psfsize = self.psfpxnbr * file.header['CDELT1']
                            else:
                                if file.header['CUNIT2'] == 'arcsec':
                                    self.psfpxnbr =file.header['NAXIS2']
                                    self.psfsize = self.psfpxnbr * file.header['CDELT2']


                # Create a minimum of intensity on the psf to place a photon
                self.psfenergy = np.zeros(shape = np.shape(wv), dtype = object)
                self.psfpos = np.zeros(shape = np.shape(wv), dtype = object)
                self.maxpsf = []
         
                for wvl in range(len(wv)):
                    self.maxpsf.append(1.1 * np.max(self.psf[wvl]))
                    self.psfpos[wvl]  = []
                    self.psfenergy[wvl] = []
                    lim = np.max(self.psf[wvl])/100
                    data  = self.psf[wvl]
                    for i in range(self.psfpxnbr):
                        for j in range(self.psfpxnbr):
                            if self.psf[wvl][i,j]> lim: 
                                self.psfpos[wvl].append([i,j])
                                self.psfenergy[wvl].append(data[i,j])

                    

            def gaussian_psf(self, pxnbr, pxsize, wv):
                self.psfpxnbr = pxnbr
                psf_grid = np.zeros(shape = (pxnbr,pxnbr,len(wv)))
                psf_grid[np.int8(pxnbr/2),np.int8(pxnbr/2),:] = 1
                    # point = np.linspace(0,1,pix_nbr)
                    # psf = interpolate.RegularGridInterpolator((point,point,wavelength_array),psf_grid)
                    # psf_pix_nbr = pix_nbr
                self.psfsize = pxsize * pxnbr
                self.psf = psf_grid
             

            def defined_psf(self, psf, psffile, wv, diameter, obscuration, exptime):
                self.psfpxnbr = psf['pix_nbr']
                self.psfsize = psf['size']
                seeing = psf['seeing']
                wind = psf['wind']
                L0 = psf['L0']

                if type[wind] == list:
                    coeff = psf['coeff']
                    self.psf = PSF_creation_mult(fov_tot=self.psfsize, nb_pixels_img=self.psfpxnbr,
                                                wavelength_array=wv, seeing=seeing, wind=wind,
                                                D=diameter, obscuration=obscuration, L0=L0,
                                                obs_time=exptime, coeff=coeff,save_link=psffile)
                else:
                    self.psf = PSF_creation(fov_tot=self.psfsize, nb_pixels_img=self.psfpxnbr,
                                            wavelength_array=wv, seeing=seeing, wind=wind,
                                            D=diameter, obscuration=obscuration, L0=L0,
                                            obs_time=exptime, save_link=psffile)

    class Star():
            __slots__ = ('posx', 'posy', 'spectrumchoice', 'stardist', 'starintensity', 'spectrum', 'phase', 'alt_az_t', 'ra_dec_t', 'ang')
            def __init__(self, psf,i):
                
                self.posx  = rand.uniform(low =0, high= pxnbr)
                self.posy  = rand.uniform(low =0, high= pxnbr)
                print(self.posx,self.posy, flush = True)
                sp = np.loadtxt(spectrumlist[rand.randint(len(spectrumlist))])
                self.spectrumchoice = interpolate.interp1d(sp[:,0],sp[:,1])
                self.stardist = rand.uniform(stdistmin, stdistmax)
                self.starintensity = 1 * (10 / self.stardist**2)
                self.spectrum = (10 /self.stardist**2) * self.spectrumchoice(wv*10**3)

                rot, evalt = self.Rotation()
                photonlist = self.PhotonCreation(i)
                photonPSF = self.PSFDistribution(psf, photonlist)
                detectpos = self.PhotonProj(psf, rot,evalt, photonPSF)
                photondetect = self.DetectorProj(detectpos)
                h5file['Stars/'+str(i)+'/Spectrum'] = sp
                h5file['Stars/'+str(i)+'/Pos'] = [self.posx, self.posy]
                h5file['Stars/'+str(i)+'/Dist'] = self.stardist
                h5file['Stars/'+str(i)+'/Intensity'] = self.starintensity

                

                try: DATA['Phase']
                except: pass
                else:
                    # self.Calib()
                    phaseconv = self.PhaseConversion(photondetect)
                    expphase = self.PhaseExp(phaseconv)
                    nexpphase = self.PhaseExpNoise(expphase)
                    self.phase = np.zeros(shape = (pxnbr, pxnbr), dtype = object)
                    for i in range(0, pxnbr):
                        for j in range(0, pxnbr):
                            self.phase[i,j] = []
                            for ph in range(0, len(nexpphase[0][i,j])):
                                self.phase[i,j].append([nexpphase[1][i,j][ph],nexpphase[0][i,j][ph]])


            def Rotation(self):
                # print('Rot')
                if rotation == True:
                
                    # print('Earth rotation effect')
                    guide = [altguide,azguide]

                    rot,evalt,self.alt_az_t,self.ra_dec_t,self.ang = EarthRotation(lat_tel=latitude,coo_guide=guide,coo_star=[self.posx, self.posy],time = exptime,size=pxnbr)

                else:
                    t = np.linspace(0,exptime,exptime+1 )
                    rot = [interpolate.interp1d([0,exptime],[self.posx,self.posy]),
                                interpolate.interp1d([0,exptime],[t,t])]
                    evalt = interpolate.interp1d([0,exptime],[np.pi/2,np.pi/2])
                    self.alt_az_t =[altguide,azguide,0]
                    self.ra_dec_t = [0,0,0]
                    self.ang = 0
                return(rot, evalt)
            
            def PhotonCreation(self,i):
                # print('photon creation', flush = True)
                # dict with [wavelength (µm), time (µs)]
                photonlist = photon(wavelength=wv, spectre=self.spectrum, time=exptime,
                                    diam=diameter, point_nb=timelinestep, transmission=transmittance)
                print(len(photonlist), flush = True)
                h5file['Stars/'+str(i)+'/PhotonNumber'] = len(photonlist)
                h5file['Stars/'+str(i)+'/Photons'] = photonlist
                return(photonlist)

            def PSFDistribution(self,psf, photonlist):
                # print('PSFed', flush = True)
                photonPSF = photon_pos_on_PSF(photonlist, psf, wv)
                return(photonPSF)

            def PhotonProj(self,psf, rot, evalt,photonPSF):
                # print('photon pos on detector frame + rot', flush = True)
                lam0 = (max(wv)+min(wv))/2
                detectpos = photon_proj(photonPSF, psf, rot,evalt, pxnbr, pxsize, lam0, timelinestep)
                return(detectpos)

            def DetectorProj(self,detectpos):
                # print('Detector projection', flush = True)
                # [Wavelength[pix,pix], Time[pix,pix]]
                photondetect = detector_scale(pxnbr, detectpos)
                return(photondetect)

            def PhaseConversion(self,photondetect):
                # print('Phase conversion', flush = True)
                convtab = ConversionTab(photondetect,conversion)
                phaseconv = photon2phase(photondetect,convtab, nphase)
                return(phaseconv)
                
            def PhaseExp(self,phaseconv):
                # print('Phase exp', flush = True)
                expphase = exp_adding(phaseconv, decay, exptime)
                return(expphase)
        
            def PhaseExpNoise(self, expphase):
                #   [Wavelength[pix,pix][list],Time[pix,pix]]
                # print('Phase Exp Noise', flush = True)
                if baseline == 'uniform':
                    nexpphase = PhaseNoise(expphase, nreadoutscale)
                elif baseline == 'random':
                    nexpphase = PhaseNoise(expphase, nreadoutscale, baselinepix)
                return(nexpphase)
                
    class Detector():
        __slots__ = ('pixfilter', 'noisetimeline', 'photondetectcalib', 'wmap')
        def __init__(self,):

            
            print('Detector part', flush = True)
            # WeightMap creation 
            
            if weightmap == True:
                self.wmap = np.random.uniform(low = 0.5, high = 1, size = (pxnbr, pxnbr))
            # elif 
            else:

                self.wmap = np.ones(shape = (pxnbr, pxnbr))
            h5file['WeightMap'] = self.wmap
            self.pixfilter = np.zeros(shape = (pxnbr,pxnbr), dtype = object)
            
            psd = np.zeros(shape = (pxnbr,pxnbr), dtype = object)
            template = np.zeros(shape = (pxnbr,pxnbr), dtype = object)
            self.noisetimeline = np.zeros(shape = (pxnbr,pxnbr), dtype = object)
            
            print('Filter creation', flush = True)
            

                
            for i in range(pxnbr):
                for j in range(pxnbr):
               
                    if baseline == 'uniform':
                        self.noisetimeline[i,j] = [np.linspace(0,int(1e6),int(1e6)),np.random.normal(scale=nreadoutscale, loc = 0, size = int(1e6))]
                    elif baseline == 'random':
                        self.noisetimeline[i,j] = [np.linspace(0,int(1e6),int(1e6)),np.random.normal(scale=nreadoutscale, loc = baselinepix[i,j], size = int(1e6))]
                    self.Filter(self.noisetimeline[i,j], i, j,template,psd)
            self.Calib(self.noisetimeline)
      

        def Filter(self, noise, i, j,template,psd):
            #  Filter creation
            psd[i,j] = PSD(noise, nperseg)

            template[i,j] = Template(decay, templatetime, trigerinx, pointnb)

            self.pixfilter[i,j] = FilterCreation(template[i,j], psd[i,j][1])

        def CalibCompute(self, tab, wvcalib, phcalib, noisetimeline,output = False):
            phaseconvcalib = Photon2PhaseCalib(phcalib, tab, nphase)
            expphasecalib = exp_adding_calib(phaseconvcalib, decay, timelinestep)
            nexpphasecalib = PhaseNoiseCalib(expphasecalib, nreadoutscale, baselinepix)
            # try: calibfile
            # except: pass
            # else:
            #     calibhdf5 = h5py.open(calibfile, 'w')
            for i in range(pxnbr):
                for j in range(pxnbr):

                    peaks,_ = find_peaks(nexpphasecalib[i,j][1], prominence=10, height=max(noisetimeline[i,j][1]))
                    nbpeaks = int(len(peaks) * self.wmap[i,j])
                    peaks = peaks[:nbpeaks]
                    h5file['Calib/'+str(wvcalib)+'/'+str(i)+'_'+str(j)] = [peaks, nexpphasecalib[i,j][1][peaks]]
                    # calibhdf5['Calib/'+str(wvcalib)+'/'+str(i)+'_'+str(j)] = [peaks, nexpphasecalib[i,j][1][peaks]]


            if output == True:
                return(nexpphasecalib)

        def Calib(self,noisetimeline):
                print('Calibration', flush = True)
                # 3 list, each contain 1 detector with calibration on all pix
                wvcalib = np.linspace(wv[0],wv[-1],nbwv)
                self.photondetectcalib = photon_calib(pxnbr, wvcalib, calibtype)
             
                tab = ConversionTabCalib(self.photondetectcalib[0], conversion)
                if save_type == 'photon_list':
                    for i in range(len(wvcalib)):
                        self.CalibCompute(tab, wvcalib[i], self.photondetectcalib[i], noisetimeline)
                
                print('Calib done', flush = True)
   
    class PhotonDetection():
        __slots__ = ('detect')
        def __init__(self, stars, noisetimeline, wmap):
            print('Detector', flush = True)


            photons = np.zeros(shape = (pxnbr, pxnbr), dtype = object)

            for i in range(pxnbr):
                for j in range(pxnbr):
                    photons[i,j] = np.zeros(shape = exptime, dtype = object)
                    
                    for t in range(exptime):
                        photons[i,j][t] = []
                        
            pixdic = {}
            pixtot = []
            for st in range(len(stars)):
                listepixph = [
                    (k, l) for k, line in enumerate(stars['star_'+str(st)].phase)
                           for l, element in enumerate(line) if element
                ]
                pixdic['star_'+str(st)] = listepixph
                pixtot += listepixph
                # for (k,l) in listepixph:
                #     for ph in range(len(stars['star_'+str(st)].phase[k,l])):
                #         photons[k,l][int(stars['star_'+str(st)].phase[k,l][ph][0][0]/1e6)].append([stars['star_'+str(st)].phase[k,l][ph][1][0]])
                        # h5file['Photons/'+str(int(stars['star_'+str(st)].phase[k,l][ph][0][0]/1e6))+'/'+str(k)+'_'+str(l)].append(stars['star_'+str(st)].phase[k,l][ph][1][0]) 
            pixtot = list(set(pixtot))
            for pix in pixtot:
                m_noise = max(noisetimeline[pix[0],pix[1]][1])
                for t in range(exptime):
                    
                    # h5file['Photons/'+str(t)] = []
                    # del h5file['Photons/'+str(t)+'/'+str(pix[0])+'_'+str(pix[1])]
                    ntime = np.random.normal(loc = 0, scale = nreadoutscale, size = int(timelinestep))
                    compare = np.copy(ntime)
                    for st in range(len(stars)):

                        if pix in pixdic['star_'+str(st)]:
                            # print(wmap[pix[0],pix[1]],len(stars['star_'+str(st)].phase[pix[0],pix[1]]), int(wmap[pix[0],pix[1]] * len(stars['star_'+str(st)].phase[pix[0],pix[1]])))
                            for ph in range(int(wmap[pix[0],pix[1]] * len(stars['star_'+str(st)].phase[pix[0],pix[1]]))):
                                # print(int(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][0]/1e6))
                                if int(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][0]/1e6) == t:
                                    # print(t)
                                    # print(np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][0]),np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]))
                                    if np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][0]/1e6) == np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]/1e6): 

                                        inx = list(map(np.int32,stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0]-np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]/1e6)*1e6))
                                        ntime[inx] += stars['star_'+str(st)].phase[pix[0],pix[1]][ph][1]

                                    else:
                                        inx = abs(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0] - np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]/1e6)*1e6).argmin()
                                        inxa = list(map(np.int32, np.linspace(0,len(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0]) - inx - 1, len(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0]))))
                                        inxb = np.int32(np.linspace(0, len(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][inx:])-1, len(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][inx:])))
                                        # if stars['star_'+str(st)].phase[pix[0],pix[1]][ph][-1]/1e6 < exptime -1: 
                                        ntime[inxa] += stars['star_'+str(st)].phase[pix[0],pix[1]][ph][1][inxa]
                                        if np.int8(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]/1e6) < exptime - 1:
                                            stars['star_'+str(st)].phase[pix[0],pix[1]].append([inxb + + np.int32(stars['star_'+str(st)].phase[pix[0],pix[1]][ph][0][-1]/1e6)*1e6, stars['star_'+str(st)].phase[pix[0],pix[1]][ph][1][inxb]])

                    if (ntime == compare).all():
                        pass
                    else:
                        peaks, _ = find_peaks(ntime, prominence = 10, height=m_noise)
        
                        if save_type == 'photon_list':
                                # print(t)
                                h5file['Photons/'+str(t)+'/'+str(pix[0])+'_'+str(pix[1])] = [peaks, ntime[peaks]]


            # for i in range(pxnbr):
            #     for j in range(pxnbr):
            #         for t in range(exptime):
                        
            #             if len(photons[i,j][t]) > 0:
            #                 h5file['Photons/'+str(t)+'/'+str(i)+'_'+str(j)] = photons[i,j][t][:]
            #             else:
            #                 h5file['Photons/'+str(t)+'/'+str(i)+'_'+str(j)]= []

        # def phasedistrib(self, phase, i, j):
            
        #     if len(phase[i,j]) > 0:
        #         for ph in range(len(phase[i,j])): 
            
        #             if np.int8(phase[i,j][ph][0][0]/1e6) == np.int8(phase[i,j][ph][0][-1]/1e6):
           
                        # inx = list(map(np.int8,phase[i,j][ph][0] - np.int8(phase[i,j][ph][0][-1]/1e6)*1e6))
        #                 self.detect[int(phase[i,j][ph][0][-1]/1e6)][inx] += phase[i,j][ph][1]
        #                 print(max(phase[i,j][ph][1]))
        #                 print(max(self.detect[int(phase[i,j][ph][0][-1]/1e6)][inx]), len(self.detect[int(phase[i,j][ph][0][-1]/1e6)][inx] ))

        #             else: 
        #                 inx = abs(phase[i,j][ph][0] - np.int8(phase[i,j][ph][0][-1]/1e6)*1e6).argmin()
        #                 inxb = list(map(np.int8,phase[i,j][ph][0][:inx] - np.int8(phase[i,j][ph][0][0]/1e6)*1e6))
        #                 inxa = np.int8(np.linspace(0, len(phase[i,j][ph][0][inx:]) - 1, len(phase[i,j][ph][0][inx:])))
        #                 if np.int8(phase[i,j][ph][0][-1]/1e6) < exptime - 1:
        #                     self.detect[np.int8(phase[i,j][ph][0][0]/1e6)][inxb] += phase[i,j][ph][1][:inx]
        #                     self.detect[np.int8(phase[i,j][ph][0][-1]/1e6)][inxa] += phase[i,j][ph][1][inx:]
        #                 else: 
        #                     self.detect[np.int8(phase[i,j][ph][0][0]/1e6)][inxb] += phase[i,j][ph][1][:inx]
              
        #                 print('confirm'+' s: '+str(np.int8(phase[i,j][ph][0][0]/1e6)), flush = True)
        #         print(str(len(phase[i,j])) +' Photons placed for: '+str(i)+'_'+str(j), flush=True)
        #     print('max detect = ',np.max(self.detect))
 


            

    # def Output(self, savetype):

    #     print('output part', flush = True)
    #     if savetype == 'Simulation':
    #                 # print('Saving in HDF5 at: ' + str(path))
    #                 # save_dict_to_hdf5(self.config, path,self,pix_nbr)
    #         h5file = h5py.File(path, 'w') 
    #         recursively_save_dict_contents_to_group(h5file, '/', DATA)
    #         h5file['PSF'] = self.psf.psf
    #         # h5file['stars'] = {}
    #         for i in range(0, stnbr):
    #             # h5file['stars']['star_'+str(i)] = {}
    #             h5file['stars/star_'+str(i)+'/posx'] = self.stars['star_'+str(i)].posx
    #             h5file['stars/star_'+str(i)+'/posy'] = self.stars['star_'+str(i)].posy
          
    #             h5file['stars/star_'+str(i)+'/stardist'] = self.stars['star_'+str(i)].stardist
    #             h5file['stars/star_'+str(i)+'/spectrum'] = self.stars['star_'+str(i)].spectrum
                

    #         for k in range(pxnbr):
    #             for l in range(pxnbr):
    #                 for s in range(exptime):
    #                     # h5file['stars/star_'+str(i)+'/'+str(s)+'/'+str(k)+'_'+str(l)] = self.stars['detect_'+str(i)].detector[k,l][s]
    #                     h5file['Detector/' + str(s) + '/' + str(k)+'_'+str(l)] = self.stars['Detector'].detector[k,l][s]

    #         try: DATA['Phase']
    #         except: pass
    #         else:
    #             for k in range(pxnbr):
    #                 for l in range(pxnbr):
    #                     h5file['Filter/'+str(k)+'_'+str(l)] = self.detect.pixfilter[k,l]
                        
    #                     h5file['Calibration/'+str(0)+'/'+str(k)+'_'+str(l)] = self.detect.nexpphasecalib0[k,l]
    #                     h5file['Calibration/'+str(1)+'/'+str(k)+'_'+str(l)] = self.detect.nexpphasecalib1[k,l]
    #                     h5file['Calibration/'+str(2)+'/'+str(k)+'_'+str(l)] = self.detect.nexpphasecalib2[k,l]

    #     elif savetype == 'photon_list':

    #         h5file = h5py.File(path, 'w') 
    #         recursively_save_dict_contents_to_group(h5file, '/', DATA)
          
    #         for k in range(pxnbr):
    #             for l in range(pxnbr):
    #                 m_noise = max(self.detect.noisetimeline[k,l][1])
    #                 for s in range(exptime):
    #                     peaks, _ = find_peaks(self.stars['Detector'].detector[k,l][s],prominence = 10, height=m_noise)
    #                     h5file['Photons/'+str(s)+'/'+str(k)+'_'+str(l)] = [peaks, self.stars['Detector'].detector[k,l][s][peaks]]



# test = Simulation('/home/sfaes/sim_script_dev/new_version/Template_phase.yaml')
# print(test.star_1.nexpphase[0])
# plt.plot(test.star_1.nexpphase[1][0,0][1],test.star_1.nexpphase[0][0,0][1])
# plt.show()
# print(test.star_1.nexpphasecalib[0][0][0,0][0][500:1000])