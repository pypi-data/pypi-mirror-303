from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from tkinter import *
from astropy.io import fits
from astropy.wcs import WCS




def interface(path_file):

    def PSF_plot(event):
       
        wv=int(var.get())
        Text["text"] = wavelength[wv]
        lines = int(var2.get())
        # axes_1.clear()
        axes_2.clear()

 
        axes_1.imshow(data[:,:,wv],cmap='gray_r',origin='lower')
        axes_1.set_title('PSF at '+str(wavelength[wv])+' µm')
        canvas_1.draw()

        axes_2.plot_wireframe(X, Y, data[:,:,wv],rcount=lines, ccount=lines)
        axes_2.set_title('3d PSF projection')
        canvas_2.draw()
        


    #file opening
    file = fits.open(path_file)[0]
    wcs = WCS(file.header)

    # Interface creation
    fenetre = Tk()
    fenetre.geometry("1250x600")
    fenetre.grid()

    

    start_wv = file.header['CRVAL1']
    wv_inter = file.header['CDELT1']
    nbr_wv = file.header['NAXIS1']-1
    end_wv = start_wv + wv_inter*nbr_wv
    data = file.data
    wavelength = np.linspace(start_wv,end_wv,nbr_wv+1)
    size = file.header['NAXIS2']
    point = np.linspace(0,1,size)
    X,Y = np.meshgrid(point,point)

    figure_1 = Figure(figsize=(6, 5), dpi=100)
    axes_1 = figure_1.add_subplot(111, projection=wcs,slices=(0,'y','x'))
    axes_1.imshow(data[:,:,0],cmap='gray_r',origin='lower')
    axes_1.set_title('PSF at 0.4 µm')
    
    canvas_1 = FigureCanvasTkAgg(figure_1,master = fenetre)  
    canvas_1.draw()
    toolbar_1 = NavigationToolbar2Tk(canvas_1,fenetre,pack_toolbar = False)
    toolbar_1.grid(column = 0,row = 1)
    canvas_1.get_tk_widget().grid(column = 0,row = 0)

    figure_2 = Figure(figsize=(6, 5), dpi=100)
    axes_2 = figure_2.add_subplot(projection = '3d')
    axes_2.plot_wireframe(X, Y, data[:,:,0])
    axes_2.set_title('3d PSF projection')
    canvas_2 = FigureCanvasTkAgg(figure_2,master = fenetre)  
    canvas_2.draw()
    toolbar_2 = NavigationToolbar2Tk(canvas_2,fenetre,pack_toolbar = False)
    toolbar_2.grid(column = 1,row = 1)
    canvas_2.get_tk_widget().grid(column = 1,row = 0)

    var = DoubleVar()
    scale = Scale(fenetre, variable=var,from_=0,to=nbr_wv,orient=HORIZONTAL,length=1000,showvalue=0)
    scale.grid(column = 0,row = 2,columnspan=2)    
    scale.bind("<ButtonRelease-1>",PSF_plot)

    var2 = DoubleVar()
    var2.set(size)
    scale_2 = Scale(fenetre,variable=var2,from_=1,to=50,orient=VERTICAL,length=500)
    scale_2.grid(column = 3,row =0)
    scale_2.bind("<ButtonRelease-1>",PSF_plot)    

    Text = Label(fenetre,text=0.4)
    Text.grid(column = 0, row = 3,columnspan=2)
    fenetre.mainloop()