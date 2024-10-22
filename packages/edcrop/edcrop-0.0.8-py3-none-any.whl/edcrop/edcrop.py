"""
Created on Fri Nov 27 16:53:52 2015

Finished March 2023.

@author: Steen Christensen, Geoscience, Aarhus University, Denmark,
         sc@geo.au.dk, or steen@grast.dk.
         
Full documentation: Christensen, S. (2023): 
    "Documentation of edcrop - version 1 - 
     A Python package to simulate field-scale evapotranspiration and drainage 
     from crop, wetland, or forest". Dept. of Geoscience, Aarhus University.


Edcrop is a python package to compute daily actual evapotranspiration from 
bare soil, crop,forest or wetland on basis of daily data on temperature, 
precipitation,and reference evapotranspiration as well as parameter values 
for soil, crop, and model. As a biproduct, the module also computes the daily
percolation (drainage) from the soil profile. 

Edcrop can either be run from own script by importing it as a module, or 
it can be run as a script.

All input to Edcrop, except the climate time series, is given in a required 
text file which by default is named edcrop.yaml. The file is named with the 
extension .yaml because it follows the YAML format and is processed using the 
Python YAML module. 

The daily climate data input is given in a CSV file.

By default, Edcrop generates a log file and two output files for each 
simulation, containing daily and yearly water balance results, respectively. 
The user is free to choose which results are printed. 
The users can also choose to plot some input data and simulation results and 
save them as PNG files.

A very brief summary of the simulation procedure in edcrop follows here:

Some of edcrop's models for simulating vegetation growth and water balance 
were taken and modified from

Jørgen E. Olesen and Tove Heidmann (2002). EVACROP
Et program til beregning af aktuel fordampning og afstrømning
fra rodzonen, Version 1.01. Afdeling for Plantevækst og Jord 
og Afdeling for Jordbrugssystemer, Forskningscenter Foulum,
Tjele, Denmark. 51 pp.

which for some part was taken from

Aslyng, H.C. & Hansen, S. (1982). Water Balance and Crop Production
Simulation. Hydrotechnical Laboratory. The Royal Veterinary and 
Agricultural University. Copenhagen, Denmark. 200 pp.

However, an alternative water balance model also implemented in edcrop is
described at the end of the summary.

In edcrop, potential evapotranspiration is calculated from input reference 
evapotranspiration. The calculation uses a seasonal crop coefficent, which is
computed using leaf area and a single coefficient method.

Plant growth is driven solely by daily temperature cummulated either from 
time of sowing or from end of winter.

In edcrop, the modified Evacrop model differs from the original Evacrop in 
different ways. First, it includes macropore drainage. Secondly, it includes 
growth and transpiration models for additional vegetation types (maize, 
deciduous forest, needleleaf forest, wetland, and wet meadow). Thirdly, 
irrigation can be applied either by specifying dates and rate, or by using 
automatic irrigation. Automatic irrigation is activated when the water content 
in the root zone becomes less than a minimum value. Irrigation only works 
for crops.

Like the original Evacrop, the Evacrop model in edcrop simulates flow through 
the soil profile as flow through two linear reservoirs using daily time steps.

The alternative water balance model simulates flow through the soil profile as 
flow through four linear or nonlinear reservoirs using daily or sub-daily 
time steps. For nonlinear reservoirs, Edcrop uses Mualem – van Genuchten like 
functions. It also simulates gravity driven macro-pore flow as well as loss 
of infiltration due to surface runoff.

"""

from datetime import datetime, timedelta, date
from os.path import isfile

import numpy as np
import pandas as pd
import yaml as yml
import matplotlib.pyplot
import matplotlib.dates as dates
# import matplotlib.ticker as ticker


"""
===============================================================================
class of funtions related to initializing, reading, computing, writing and 
plotting water balance time series
===============================================================================
"""
class TimeSeries:
    
    # def set_tick_labels_3(self, ax1, ax2, ax3):
    #     """ called by self.plot_time_series() """
        
    #     start_year=self.date[0].year
    #     end_year=self.date[self.nd-1].year
        
    #     ax1.xaxis.set_major_formatter(ticker.NullFormatter())
    #     ax2.xaxis.set_major_formatter(ticker.NullFormatter())
    #     ax1.tick_params(which='minor',labelcolor='w',length=0)
    #     ax2.tick_params(which='minor',labelcolor='w',length=0)
    #     # More than one year - yearly tick marks
    #     if end_year>start_year:        
    #         ax3.xaxis.set_major_locator(dates.YearLocator())
    #         ax3.xaxis.set_minor_locator(dates.YearLocator(1, month=7, day=3))
    #         ax3.xaxis.set_major_formatter(ticker.NullFormatter())
    #         ax3.xaxis.set_minor_formatter(dates.DateFormatter('%Y'))
    #         for tick in ax3.xaxis.get_minor_ticks():
    #             tick.tick1line.set_markersize(0)
    #             tick.tick2line.set_markersize(0)
    #             tick.label1.set_horizontalalignment('center')
    #         ax3.set_xlabel("Year")
    #     # Only one year - monthly tick marks
    #     else:
    #         ax3.xaxis.set_major_locator(dates.MonthLocator())
    #         ax3.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
    #         ax3.xaxis.set_major_formatter(ticker.NullFormatter())
    #         ax3.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
    #         for tick in ax3.xaxis.get_minor_ticks():
    #             tick.tick1line.set_markersize(0)
    #             tick.tick2line.set_markersize(0)
    #             tick.label1.set_horizontalalignment('center')
    #         ax3.set_xlabel(start_year)
            
    #     return(ax1,ax2,ax3)
    
    # def set_tick_labels_4(self, ax1, ax2, ax3, ax4):
    #     """ called by self.plot_time_series() """
        
    #     start_year=self.date[0].year
    #     end_year=self.date[self.nd-1].year
        
    #     ax1.xaxis.set_major_formatter(ticker.NullFormatter())
    #     ax2.xaxis.set_major_formatter(ticker.NullFormatter())
    #     ax3.xaxis.set_major_formatter(ticker.NullFormatter())
    #     ax1.tick_params(which='minor',labelcolor='w',length=0)
    #     ax2.tick_params(which='minor',labelcolor='w',length=0)
    #     ax3.tick_params(which='minor',labelcolor='w',length=0)
    #     # More than one year - yearly tick marks
    #     if end_year>start_year:        
    #         ax4.xaxis.set_major_locator(dates.YearLocator())
    #         ax4.xaxis.set_minor_locator(dates.YearLocator(1, month=7, day=3))
    #         ax4.xaxis.set_major_formatter(ticker.NullFormatter())
    #         ax4.xaxis.set_minor_formatter(dates.DateFormatter('%Y'))
    #         for tick in ax4.xaxis.get_minor_ticks():
    #             tick.tick1line.set_markersize(0)
    #             tick.tick2line.set_markersize(0)
    #             tick.label1.set_horizontalalignment('center')
    #         ax4.set_xlabel("Year")
    #     # Only one year - monthly tick marks
    #     else:
    #         ax4.xaxis.set_major_locator(dates.MonthLocator())
    #         ax4.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=15))
    #         ax4.xaxis.set_major_formatter(ticker.NullFormatter())
    #         ax4.xaxis.set_minor_formatter(dates.DateFormatter('%b'))
    #         for tick in ax4.xaxis.get_minor_ticks():
    #             tick.tick1line.set_markersize(0)
    #             tick.tick2line.set_markersize(0)
    #             tick.label1.set_horizontalalignment('center')
    #         ax4.set_xlabel(start_year)
            
    #     return(ax1,ax2,ax3,ax4)
    
    def plot_time_series(self, soilname, cropname, fn_begin):
        """ function to plot results; called from run_model() """
        
        plt=matplotlib.pyplot
        
        title=cropname+' on {0}'.format(soilname)
        f,(ax1,ax2,ax3)=plt.subplots(3,1,sharey=True,sharex=True)
        f.suptitle(title,fontsize=12)
        if self.I.sum() > 0.0:
            ax1.bar(self.date,self.P+self.I,color='b',edgecolor='k',width=0.8,
                    linewidth=0)
            ax1.set_ylabel("P+I [mm]")
        else:
            ax1.set_ylabel("P [mm]")
        ax1.bar(self.date,self.P,color='k',edgecolor='k',width=0.8,linewidth=0)
        ax2.bar(self.date,self.Ea,color='r',edgecolor='r',width=0.8,
                linewidth=0)
        ax2.set_ylabel("Ea [mm]")
        if self.Dmp.sum() > 0.0:
            ax3.bar(self.date,self.Dsum,color='b',edgecolor='b',width=0.8,
                    linewidth=0)
            ax3.set_ylabel("Db+Dmp [mm]")
        else:
            ax3.bar(self.date,self.Db,color='b',edgecolor='b',width=0.8,
                    linewidth=0)
            ax3.set_ylabel("Db [mm]")
        ax3.set_xlabel("Year")

        locator = dates.AutoDateLocator()#(minticks=3, maxticks=7)
        formatter = dates.ConciseDateFormatter(locator)
        ax1.xaxis.set_major_locator(locator)
        ax1.xaxis.set_major_formatter(formatter)
        ax2.xaxis.set_major_locator(locator)
        ax2.xaxis.set_major_formatter(formatter)
        ax3.xaxis.set_major_locator(locator)
        ax3.xaxis.set_major_formatter(formatter)
##  If matplot too old to contain ConciseDateFormatter
#        ax1,ax2,ax3=self.set_tick_labels_3(ax1,ax2,ax3)  
        plt.savefig(fn_begin+'_P_Ea_Db.png',dpi=600, facecolor='w', 
                    edgecolor='w', orientation='landscape', 
                    format=None, transparent=False, bbox_inches=None, 
                    pad_inches=0.1)
#        plt.savefig(fn_begin+'_P_Ea_Db.png',dpi=600, facecolor='w', 
#                    edgecolor='w', orientation='landscape', papertype=None, 
#                    format=None, transparent=False, bbox_inches=None, 
#                    pad_inches=0.1,\
#                    frameon=None) 
#        plt.show()
        plt.close()
        
        f2,(ax4,ax5,ax6,ax7)=plt.subplots(4,1,sharex=True)
        f2.suptitle(title,fontsize=12)
        ax4.plot(self.date,self.Tsum)
        ax4.set_ylabel("Tsum [C]")
        ax5.plot(self.date,self.zr)
        ax5.set_ylabel("zr [mm]")
        ax5.set_ylim(0, max(self.zr)+100) # 1100)
        ax6.plot(self.date,self.Lg,color='g')
        ax6.plot(self.date,self.L)
        ax6.set_ylabel("L [mm]")
        ax6.set_ylim(0, max(self.L)+1) #10)
        ax7.plot(self.date,self.kc)
        ax7.set_ylabel("kc [-]")
        ax7.set_ylim(min(self.kc)-0.1, max(self.kc)+0.1) # 1.2)

        locator = dates.AutoDateLocator()#(minticks=3, maxticks=7)
        formatter = dates.ConciseDateFormatter(locator)
        ax4.xaxis.set_major_locator(locator)
        ax4.xaxis.set_major_formatter(formatter)
        ax5.xaxis.set_major_locator(locator)
        ax5.xaxis.set_major_formatter(formatter)
        ax6.xaxis.set_major_locator(locator)
        ax6.xaxis.set_major_formatter(formatter)
        ax7.xaxis.set_major_locator(locator)
        ax7.xaxis.set_major_formatter(formatter)
##  If matplot too old to contain ConciseDateFormatter
#        ax4,ax5,ax6,ax7=self.set_tick_labels_4(ax4,ax5,ax6,ax7)  
        plt.savefig(fn_begin+'_T_zr_L_kc.png',dpi=600, facecolor='w', 
                    edgecolor='w', orientation='portrait', 
                    format=None, transparent=False, bbox_inches=None, 
                    pad_inches=0.1) 
#        plt.savefig(fn_begin+'_T_zr_L_kc.png',dpi=600, facecolor='w', 
#                    edgecolor='w', orientation='portrait', papertype=None, 
#                    format=None, transparent=False, bbox_inches=None, 
#                    pad_inches=0.1, frameon=None) 
        
#        plt.show()
        plt.close()
        
    def print_from_dictionary(self, fname):
        """ 
        Function to print daily and or yearly results; 
        the function is called from run_model(); 
        self.prlist is a list of items (names) found in the output
        dictionary, self.outdict, for which daily output 
        is printed;
        self.prlist_y is a similar list for printing of yearly results;
        self.prlist and self.prlist_y are set or read in function
        ModelParameters.read_initialize()
        """
        
        df=pd.DataFrame.from_dict(self.outdict)
        df.set_index(self.prlist[0],inplace=True,drop=False)
        dtformat = self.dtformat
        dtformat = "%Y-%m-%d"

        n=len(self.prlist)
        if n>1:
            colalias=[self.prlist[0].rjust(10)]
            for i in range(1,n):
                colalias.append(self.prlist[i].rjust(11))
            df.to_csv(fname+'_wb.out',index=False,columns=self.prlist,\
              float_format="%11.6f",date_format=dtformat,header=colalias)

        n=len(self.prlist_y)
        if n>0:
#            df2=df.resample('A',how=sum)
            df2=df.resample('A').sum()
            colalias=[]
            for i in range(0,len(self.prlist_y)):
                colalias.append(self.prlist_y[i].rjust(8))
            df2.to_csv(fname+'_y_wb.out',index=True,columns=self.prlist_y,\
               float_format="%8.1f",date_format="%Y",header=colalias)
        
    def forced_irrigation(self, mp):
        """ 
        Set time series of forced daily irrigation; 
        the days and rate of crop irrigation are set or read in function
        CropParameters.read_initilize();
        
        called from run_model().
        """
        for idate in mp.irrigationdate:
            for j in range(0, self.nd):
                if same_day_and_month(idate,self.date[j]):
                    self.I[j] = mp.irrigation
                    
    def irrigationmodel_Aslyng(self, i, mp):
        """ irrigation model taken from Aslyng and Hansen, 1982, Ch. 12. """
        if  i < self.nd-3 and mp.Vr < mp.clim*mp.cb*mp.Cr \
                and mp.irrdaycount > mp.tfreq:
            Psum = 0.0
            for isum in range(i+1,i+3):
                Psum = Psum + self.P[isum] + self.I[isum]
            if Psum < mp.Plim:
                Virr = mp.Cr - mp.Vr # Fill to field cap.
                Virr = min(Virr, mp.Imax)
                Virr = max(Virr, mp.Imin)
                self.I[i+1] = self.I[i+1] + Virr
                mp.irrdaycount = 0
        
    def read(self, name, cval, fl):
        """ 
        read as pandas csv-file with daily 
        date, temperature, precipitation, reference evapotranspiration;
        skip first line in reading;
        name should hold the climate loop name;
        cval['filename'] should hold file name; 
        
        called from run_model().
        """
        try:
            fname = cval['filename']
        except:
            print_msg(("\nError: For climate loop %s, filename not specified."
                  + "  Loop to next!")%name, fl)
            return(False)

        self.dtformat = "%Y-%m-%d"
        try:
            dtformat = cval['dtformat']
        except:
            dtformat = self.dtformat
            
        if not isfile(fname):
            print_msg("\n Climate data file %s does not exist.  Loop to next!"
                  %fname, fl)
            return(False)
        else: 
            print_msg("\n Climate data file: %s."%fname, fl)
    
        no_err=True
    
        # Time series is read as pandas data frame from CSV file 
        # with following columns:
        colnames=['Date','Temp','P','Er']
#        df = pd.read_csv(fname,delim_whitespace=True, parse_dates=True,
#                         names=colnames,skiprows=1)
#        df = pd.read_csv(fname,delim_whitespace=True, 
#                         names=colnames,skiprows=1)
        df = pd.read_csv(fname,names=colnames,skiprows=1,
                          sep='\s+|,\s*|;\s*', engine='python')
        self.date=pd.to_datetime(df.Date,format=dtformat)
        self.T=np.float64(df.Temp)
        self.P=np.float64(df.P)
        self.Eref=np.float64(df.Er)
        self.nd=len(self.date)
        
    #   Check that sequence is daily
        for i in range(1,self.nd):
            d1=self.date[i-1]+timedelta(days=+1)
            d2=self.date[i]
            if (d1!=d2):
                print_msg("\n  Error: %s is not one day after %s"
                      %(self.date[i-1],self.date[i]), fl)
                no_err=False
                
        if not no_err: 
            print_msg("  Error in %s"%fname,fl)
    
        return(no_err)
        
    def initialize(self):
        """ 
        Initialize simulated time series variables before model run;
        also define dictionary, self.outdict, of possible output time series;
        
        called from run_model().
        """
        nd=self.nd
        self.Ep=np.zeros(nd,dtype=np.float64)
        self.Ea=np.zeros(nd,dtype=np.float64)
        self.Eas=np.zeros(nd,dtype=np.float64)
        self.Eae=np.zeros(nd,dtype=np.float64)
        self.Eai=np.zeros(nd,dtype=np.float64)
        self.Eaig=np.zeros(nd,dtype=np.float64)
        self.Eaiy=np.zeros(nd,dtype=np.float64)
        self.Eat=np.zeros(nd,dtype=np.float64)
        self.Ept=np.zeros(nd,dtype=np.float64)
        self.Epe=np.zeros(nd,dtype=np.float64)
        self.Epc=np.zeros(nd,dtype=np.float64)
        self.Epcg=np.zeros(nd,dtype=np.float64)
        self.Epcy=np.zeros(nd,dtype=np.float64)
        self.Dr=np.zeros(nd,dtype=np.float64)
        self.Db=np.zeros(nd,dtype=np.float64)
        self.Dmp=np.zeros(nd,dtype=np.float64)
        self.Dsum=np.zeros(nd,dtype=np.float64)
        self.Qro=np.zeros(nd,dtype=np.float64)
        self.I=np.zeros(nd,dtype=np.float64)
        self.Tsum=np.zeros(nd,dtype=np.float64)
        self.L=np.zeros(nd,dtype=np.float64)
        self.Lg=np.zeros(nd,dtype=np.float64)
        self.Ly=np.zeros(nd,dtype=np.float64)
        self.zr=np.zeros(nd,dtype=np.float64)
        self.Vsum=np.zeros(nd,dtype=np.float64)
        self.Vdel=np.zeros(nd,dtype=np.float64)
        self.Vs=np.zeros(nd,dtype=np.float64)
        self.Vr=np.zeros(nd,dtype=np.float64)
        self.Vb=np.zeros(nd,dtype=np.float64)
        self.Ve=np.zeros(nd,dtype=np.float64)
        self.Vu=np.zeros(nd,dtype=np.float64)
        self.Vi=np.zeros(nd,dtype=np.float64)
        self.Vsoil=np.zeros(nd,dtype=np.float64)
        self.Pm=np.zeros(nd,dtype=np.float64)
        self.Pr=np.zeros(nd,dtype=np.float64)
        self.Ps=np.zeros(nd,dtype=np.float64)
        self.Cr=np.zeros(nd,dtype=np.float64)
        self.Cb=np.zeros(nd,dtype=np.float64)
        self.Cu=np.zeros(nd,dtype=np.float64)
        self.kc=np.zeros(nd,dtype=np.float64)
        
        # Define dictionary if possible output time series
        self.outdict = {
            "Date": self.date,
            "P":    self.P,
            "Er":   self.Eref,
            "T":    self.T,
            "Ep":   self.Ep,
            "Ea":   self.Ea,
            "Eas":  self.Eas,
            "Eae":  self.Eae,
            "Eai":  self.Eai,
            "Eaig": self.Eaig,
            "Eaiy": self.Eaiy,
            "Eat":  self.Eat,
            "Ept":  self.Ept,
            "Epe":  self.Epe,
            "Epc":  self.Epc,
            "Epcg": self.Epcg,
            "Epcy": self.Epcy,
            "Dr":   self.Dr,
            "Db":   self.Db,
            "Dmp":  self.Dmp,
            "Dsum": self.Dsum,
            "Qro":  self.Qro,
            "I":    self.I,
            "Tsum": self.Tsum,
            "L":    self.L,
            "Lg":   self.Lg,
            "Ly":   self.Ly,
            "zr":   self.zr,
            "Vsum": self.Vsum,
            "Vdel": self.Vdel,
            "Vs":   self.Vs,
            "Vr":   self.Vr,
            "Vb":   self.Vb,
            "Ve":   self.Ve,
            "Vu":   self.Vu,
            "Vi":   self.Vi,
            "Vsoil":   self.Vsoil,
            "Pm":   self.Pm,
            "Pr":   self.Pr,
            "Ps":   self.Ps,
            "Cr":   self.Cr,
            "Cb":   self.Cb,
            "Cu":   self.Cu,
            "kc":   self.kc
            }
        

    def watbal_ed_step(self, mp, thf, cb, kqr, kqb, cd, i):
        """
        Computes water balance step "i" of the procedure of
        Olesen and Heidmann (2002, eqs. 2.14-2.55);
        besides computing time series variables, it is also updating
        some model parameter (mp) values;
        
        this version is modified, so water is routed through soil horizon
        elements;
        
        "Doc." is model docimentation.
        
        called from run_model().
        """
        
        # Compute Ep from Eref by use of crop coefficient; Doc. eq. 
        self.Ep[i] = max(0.0, self.kc[i]*self.Eref[i]) 

        # In storage at beginning of time step
        Vsum0 = mp.in_storage_ec()
        # Snow reservoir
        if self.T[i] > mp.Tm:
            self.Eas[i] = min(mp.Vs, self.Ep[i]) # (2.14)
            Pm = min(mp.Vs-self.Eas[i], mp.cm*(self.T[i]-mp.Tm))
            Pr = self.P[i]
            self.Pr[i] = Pr
            self.Ps[i] = 0.0
        else: # (2.25) and (2.26)
            mp.Vs = mp.Vs + self.P[i]
            Pm = 0.0
            Pr = 0.0
            self.Eas[i] = min(mp.Vs,self.Ep[i]) # (2.14)
            self.Pr[i] = Pr
            self.Ps[i] = self.P[i]
        mp.Vs = mp.Vs - Pm - self.Eas[i] # (2.27)
        # Soil potential evaporation
        self.Epe[i] = ((self.Ep[i]-self.Eas[i]) 
                       * np.exp(-mp.kp*self.L[i])) # (2.15)
        # Crop potential evaporation
        self.Epc[i] = ((self.Ep[i]-self.Eas[i]) 
                       * (1.0-np.exp(-mp.kp*self.L[i]))) # (2.16)
        self.Epcg[i] = ((self.Ep[i]-self.Eas[i])
                        * (1.0-np.exp(-mp.kp*self.Lg[i]))) # (2.17)
        self.Epcy[i] = self.Epc[i] - self.Epcg[i] # (2.18)
        if not cb < 0.0:  # Negative cb means bare soil and no transpiration
            self.Ept[i] = self.Epcg[i] - self.Eaig[i] # (2.41)
        # Update reservoir parameters and water contents
        mp.Capacities(self.zr[i], thf, self.L[i])
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            mp.Cr = mp.Cr_sat
        # Interception reservoir
        VI=mp.VI
        mp.VI = min(mp.CI, VI+Pr+self.I[i]+Pm) # (2.28, 2.30)
        # Evaporation from interception reservoir
        if self.L[i] > 0.:        # (2.38) and (2.39)
            self.Eaiy[i] = min(mp.VI*self.Ly[i]/self.L[i], self.Epcy[i])
            self.Eaig[i] = min(mp.VI*self.Lg[i]/self.L[i], self.Epcg[i])
        else:
            self.Eaiy[i] = 0.0
            self.Eaig[i] = 0.0
        self.Eai[i] = self.Eaig[i] + self.Eaiy[i] # (2.40)
        # Total volume of water into soil
        PI = Pr + self.I[i] + Pm - (mp.VI-VI) 
        # Final water in interception reservoir
        mp.VI = mp.VI - self.Eai[i] # (2.49)
        
        # Compute evaporation, transpiration and drainage for time step by 
        # looping through nstep smaller equal-size time steps using Euler 
        # forward solution.
        # Initialize:
        V0 = np.array(mp.V) # Water content in soil horizon elements
        nstep = mp.steps_per_day
        dfac = 1./float(nstep)
        PI = PI*dfac
        Epe = self.Epe[i]*dfac
        Ept = self.Ept[i]*dfac
        Eas = self.Eas[i]*dfac
        Eai = self.Eai[i]*dfac
        Eae = 0.0
        Eat = 0.0
        Ea = 0.0
        Db = 0.0
        Dmp = 0.0
        Qro = 0.0
        Ve0 = mp.Ve
        # Loop to compute evaporation, transpiration and drainage
        for istep in range(0,nstep):
            (Ve0, V0, Eae0) = mp.soil_evap(Ve0, V0, Epe, PI, 
                                            self.zr[i])
            if self.Ept[i] > 0.0:
                (Ve0, V0, Eat0) = \
                    mp.transpiration(Ve0, V0, Ept, self.zr[i], cb, 
                                     cd.crop_type)
            else:
                Eat0 = 0.0
            Ea0 = Eas + Eae0 + Eai + Eat0
            (Ve0, V0, Db0) = mp.soil_drainage(Ve0, V0, dfac, Ea0, PI, cd)
            (Ve0, V0, Dmp0) = mp.macropore_drainage(Ve0, V0, dfac, cd)
            (V0, Qro0) = mp.surface_runoff(V0, dfac, cd)
            Ve0 = min(mp.Ce, Ve0)
            Eae = Eae + Eae0
            Eat = Eat + Eat0
            Ea = Ea + Ea0
            Db = Db + Db0
            Dmp = Dmp + Dmp0
            Qro = Qro + Qro0
        # Update varaibles at end of time step
        mp.V = V0
        VSoil = mp.V.sum()
        mp.Vr = mp.root_zone_water(mp.V, self.zr[i])
        mp.Vb = VSoil - mp.Vr
        mp.Ve       = Ve0
        # Time series
        self.Eae[i]  = Eae
        self.Eat[i]  = Eat
        self.Ea[i]   = Ea
        self.Db[i]   = Db
        self.Dmp[i]  = Dmp
        self.Qro[i]  = Qro
        self.Dsum[i] = Db + Dmp
        # Time series from model variables
        self.Vsum[i] = mp.in_storage_ec()
        self.Vdel[i] = self.Vsum[i] - Vsum0
        self.Vsoil[i] = VSoil
        self.Vs[i] = mp.Vs
        self.Vr[i] = mp.Vr
        self.Vb[i] = mp.Vb
        self.Ve[i] = mp.Ve
        self.Vi[i] = mp.VI
        self.Pm[i] = Pm
        self.Cr[i] = mp.Cr
        self.Cb[i] = mp.Cb
        
        # Check whether to apply automatic irrigation in next time step
        mp.irrdaycount = mp.irrdaycount + 1
        if mp.autoirrigate and cd.within_irr_per(self.date[i]):
            mp.cb = cb
            mp.irrigationmodel(i, mp)
        
    def watbal(self, mp, thf, cb, kqr, kqb, cd, i):
        """
        Computes water balance step "i" of the procedure of
        Olesen and Heidmann (2002, eqs. 2.14-2.55);
        besides computing time series variables, it is also updating
        some model parameter (mp) values;
        
        called from run_model().
        """
        
        # Compute Ep from Eref by use of crop coefficient
        self.Ep[i] = max(0.0, self.kc[i]*self.Eref[i])

        # In storage at beginning of time step
        Vsum0 = mp.in_storage()
        # Snow reservoir
        if self.T[i] > mp.Tm:
            self.Eas[i] = min(mp.Vs, self.Ep[i]) # (2.14)
            Pm = min(mp.Vs-self.Eas[i], mp.cm*(self.T[i]-mp.Tm))
            Pr = self.P[i]
            self.Pr[i] = Pr
            self.Ps[i] = 0.0
        else: # (2.25) and (2.26)
            mp.Vs = mp.Vs + self.P[i]
            Pm = 0.0
            Pr = 0.0
            self.Eas[i] = min(mp.Vs,self.Ep[i]) # (2.14)
            self.Pr[i] = Pr
            self.Ps[i] = self.P[i]
        mp.Vs = mp.Vs - Pm - self.Eas[i] # (2.27)
        # Soil potential evaporation
        self.Epe[i] = ((self.Ep[i]-self.Eas[i]) 
                       * np.exp(-mp.kp*self.L[i])) # (2.15)
        # Crop potential evaporation
        self.Epc[i] = ((self.Ep[i]-self.Eas[i]) 
                       * (1.0-np.exp(-mp.kp*self.L[i]))) # (2.16)
        self.Epcg[i] = ((self.Ep[i]-self.Eas[i])
                        * (1.0-np.exp(-mp.kp*self.Lg[i]))) # (2.17)
        self.Epcy[i] = self.Epc[i] - self.Epcg[i] # (2.18)
        # Update reservoir parameters and water contents
        Cr = mp.Cr
        Cb = mp.Cb
        Vr = mp.Vr
        Vb = mp.Vb
        mp.Capacities(self.zr[i], thf, self.L[i])
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            mp.Cr = mp.Cr_sat
        if mp.Cr > Cr:                  # (2.19)
            mp.Vr = Vr + (mp.Cr-Cr)*Vb/Cb
        else:
            mp.Vr = Vr + (mp.Cr-Cr)*Vr/Cr
        mp.Vb = Vb - (mp.Vr-Vr) # (2.20, 2.24)
        # Relative water content in soil profile prior to infiltration and 
        # evaporation - to be used for computation of macropore flow:
        mp.Vrel = (mp.Vr + mp.Vb)/(mp.Cr + mp.Cb)
        # Upper rootzone reservoir
        Cu = mp.Cu
        Vu = mp.Vu
        mp.Cu = min(mp.Cr,Cu) # (2.22) Needed for shrinking rootzone
        if mp.Cu > 0.0:               # (2.23)
            mp.Vu = Vu - max(0.0,(Cu-mp.Cu)*Vu/Cu)
        else:
            mp.Vu = 0.0
        # Interception reservoir
        VI=mp.VI
        mp.VI = min(mp.CI, VI+Pr+self.I[i]+Pm) # (2.28, 2.30)
        # (2.29) Water to evaporat. and rootzone reservoirs:
        PI = Pr + self.I[i] + Pm - (mp.VI-VI) 
        # Evaporation and root zone reservoirs
        mp.Ve = mp.Ve + PI # (2.31)
        mp.Vr = mp.Vr + PI # (2.32)
#        # The following is modified compared to J.E. Olesen
#        self.Eae[i]=min(mp.Ve,self.Epe[i])
#        if (mp.Ve < self.Epe[i]):
#            if (self.Epe[i] < mp.Vr+mp.Vb):      
#                self.Eae[i]=self.Eae[i]+mp.ce*(self.Epe[i]-self.Eae[i])
        if mp.Ve < self.Epe[i]:     # Olesen's (2.33)
            if self.Epe[i] > mp.Vr + mp.Vb: # This deviates slightly from Olesen because the
                self.Eae[i] = 0.0  # evap. reservoir is a part of the rootzone reservoir
            else:
                self.Eae[i] = mp.ce*self.Epe[i]
        else:
            self.Eae[i] = self.Epe[i]
#        mp.Ve = min(mp.Ce, max(0.0, (mp.Ve-self.Eae[i]))) # (2.34)
        mp.Ve = max(0.0, (mp.Ve-self.Eae[i])) # (2.34)
        # Macropore drainage, which is new compared to J.E. Olesen:
        (mp.Ve, self.Dmp[i]) = mp.macropore_drainage_ec(mp.Ve, cd)
        mp.Ve = min(mp.Ce, mp.Ve) # (2.34)
        Vr = mp.Vr
        mp.Vr = max(Vr-self.Eae[i]-self.Dmp[i], 0.0) # (2.35, 2.37)
        mp.Vb = max(mp.Vb-self.Eae[i]-self.Dmp[i]+Vr-mp.Vr, 0.0) # (2.36)
        # Evaporation from interception reservoir
        if self.L[i] > 0.:        # (2.38) and (2.39)
            self.Eaiy[i] = min(mp.VI*self.Ly[i]/self.L[i], self.Epcy[i])
            self.Eaig[i] = min(mp.VI*self.Lg[i]/self.L[i], self.Epcg[i])
        else:
            self.Eaiy[i] = 0.0
            self.Eaig[i] = 0.0
        self.Eai[i] = self.Eaig[i] + self.Eaiy[i] # (2.40)
        # Transpiration
        if cb < 0.0: # Negative cb means bare soil
            mp.Vu = 0.0
            mp.Cu = 0.0
        else:            
            self.Ept[i] = self.Epcg[i] - self.Eaig[i] # (2.41)
            if  mp.Vr > cb*mp.Cr:
                mp.Vu = 0.0
                mp.Cu = 0.0
            else:
                mp.Vu = mp.Vu + PI - self.Eae[i] - self.Dmp[i]# (2.42)
                mp.Cu = min(mp.Cr, 
                            (mp.Cu+max(0.0, PI-self.Eae[i]-self.Dmp[i]))) # (2.43)
                if mp.Vu < cb*mp.Cu or mp.Vu < self.Ept[i]: # (2.44-2.45)
                    mp.Vu = 0.0
                    mp.Cu = 0.0
            # (2.46) follows:
            if mp.Vu > 0.0 or mp.Vr > cb*mp.Cr or cd.crop_type == "WM" \
                    or cd.crop_type == "WL": # (2.46)
                self.Eat[i] = self.Ept[i]        
            else:
                if mp.Vr > 0.0:
                    self.Eat[i] = self.Ept[i]*mp.Vr/(cb*mp.Cr)
                else:
                    self.Eat[i] = 0.0
            self.Eat[i] = max(0.0, min(mp.Vr, self.Eat[i])) # (2.47)
        # Actual evapotranspiration
        self.Ea[i] = self.Eas[i]+self.Eae[i]+self.Eai[i]+self.Eat[i] # (2.48)
        # Update water contents by subtracting actual evapo(transpi)ration
        mp.VI = mp.VI - self.Eai[i] # (2.49)
        mp.Vu = max(mp.Vu-self.Eat[i], 0.0) # (2.50)
        mp.Vr = mp.Vr - self.Eat[i] # (2.51)
        # If groundwater-fed wetland
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            self.Dr[i] = PI - self.Ea[i]
            self.Db[i] = self.Dr[i]
            if cd.crop_type == "WL": 
                mp.Ve = mp.Ce
            mp.Vr = mp.Cr_sat
            mp.Vb = 0.0
        # If water content exceeds field capacity, compute drainage
        else:
            if mp.Vr > mp.Cr:
                self.Dr[i] = ((kqr+(1.0-kqr) * (mp.zx-self.zr[i])/mp.zx)
                              * (mp.Vr-mp.Cr)) # (2.52)
            else:
                self.Dr[i] = 0.0
            if mp.Vb + self.Dr[i] > mp.Cb:
                self.Db[i] = ((kqb + (1.0-kqb)*self.zr[i]/mp.zx)
                              * (mp.Vb+self.Dr[i]-mp.Cb)) # (2.53)
            else:
                self.Db[i] = 0.0
            mp.Vr = mp.Vr - self.Dr[i] # (2.54)
            mp.Vb = mp.Vb + self.Dr[i] - self.Db[i] # (2.55)
    
        # In storage at end of time step
        self.Qro[i] = 0.0
        # self.Dmp[i] = 0.0
        self.Dsum[i] = self.Db[i] + self.Dmp[i]
        self.Vsum[i] = mp.in_storage()
        self.Vdel[i] = self.Vsum[i] - Vsum0
        self.Vsoil[i] = mp.Vr + mp.Vb
        self.Vs[i] = mp.Vs
        self.Vr[i] = mp.Vr
        self.Vb[i] = mp.Vb
        self.Ve[i] = mp.Ve
        self.Vu[i] = mp.Vu
        self.Vi[i] = mp.VI
        self.Pm[i] = Pm
        self.Cr[i] = mp.Cr
        self.Cb[i] = mp.Cb
        self.Cu[i] = mp.Cu
        
        # Check whether to apply automatic irrigation in next time step
        mp.irrdaycount = mp.irrdaycount + 1
        if mp.autoirrigate and cd.within_irr_per(self.date[i]):
            mp.cb = cb
            mp.irrigationmodel(i, mp)
        
    def update_tharvest_tsow(self, i, tharvest, tsow):
        """ 
        Update time of harvest and sowing to year of day 'i';
        
        called from growth function of winter or spring crop, self.gf_wc() 
        or self.gf_sc().
        """
        
        strn = '{0}{1}'.format(self.date[i].strftime('%Y'),tharvest.strftime('%m%d'))
        tharvest = datetime.strptime(strn,'%Y%m%d')
        strn = '{0}{1}'.format(self.date[i].strftime('%Y'),tsow.strftime('%m%d'))
        tsow = datetime.strptime(strn,'%Y%m%d')
        return(tharvest,tsow)

    def gf_bs(self, cd, mp): 
        """ 'Computes growth' time series for bare soil """
        
        mp.autoirrigate = False
        self.kc[:]=cd.kcmin
            
    def gf_gi(self, cd, mp): 
        """  Computes growth time series for grass with grazing """
        year = mp.winterperiod[0].year
        mp.sow = cd.sowdate.replace(year = year)
        mp.harvest = cd.harvestdate.replace(year = year)
        # Harvest must be later than sowing
        if mp.harvest <= mp.sow:
            mp.harvest = cd.harvestdate.replace(year = year + 1)
        mp.harvest0 = mp.harvest
       
#        cd.daygrowth = 0.0
        add_date = True
        for i in range(0,self.nd):
            idate = self.date[i]
            if idate > mp.irrigationperiod[1]: # Increment period to next year
                mp.irrigationperiod = add_year(mp.irrigationperiod)
            if iswinter(idate, mp):
                self.L[i] = cd.Lv
                self.Lg[i] = cd.Lv
                self.zr[i] = cd.zrv
#                self.kc[i] = cd.kcmin
                fac=min(1.0, cd.Lv/cd.Lm)
                self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                add_date = True
            else: # After winter period
                if add_date and mp.autoirrigate:
                    cd.autoirr_period.append(mp.irrigationperiod)
                    add_date = False
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                    zr = cd.zrv
                if self.Tsum[i] < cd.So:
                    self.L[i] = cd.Lv
                    self.Lg[i] = cd.Lv
                    self.zr[i] = cd.zrv
                    zr = self.zr[i]
#                    self.kc[i] = cd.kcmin
                    fac=min(1.0, cd.Lv/cd.Lm)
                    self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                else:
                    self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i] = \
                        cd.growfunc(self.Tsum[i], zr, cd.zrv, cd.cr, cd.Lv, 
                                    cd.Sf, cd.So)
                    zr = self.zr[i]
#                        cd.growfunc(self.Tsum[i])

    def gf_gii(self, cd, mp): 
        """ Computes growth time series for grass for hay harvesting """
        year = mp.winterperiod[0].year
        mp.sow = cd.sowdate.replace(year = year)
        n = len(cd.harvestdate)
        mp.harvest = cd.harvestdate[n-1].replace(year = year)
        # Harvest must be later than sowing
        if mp.harvest <= mp.sow:
            mp.harvest = cd.harvestdate.replace(year = year + 1)
        mp.harvest0 = mp.harvest
        
#        cd.daygrowth = 0.0
        add_date = True
        jo = -1
        cd.Lmin = cd.Lv
        for i in range(0,self.nd):
            idate = self.date[i]
            if idate > mp.irrigationperiod[1]: # Increment period to next year
                mp.irrigationperiod = add_year(mp.irrigationperiod)
            if iswinter(idate, mp):
                self.L[i] = cd.Lv
                self.Lg[i] = cd.Lv
                self.zr[i] = cd.zrv
                zr = self.zr[i]
#                self.kc[i] = cd.kcmin
                fac=min(1.0, cd.Lv/cd.Lm)
                self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                jo = -1
                cd.Lmin = cd.Lv
                add_date = True
            else: # After winter period
                if add_date and mp.autoirrigate:
                    cd.autoirr_period.append(mp.irrigationperiod)
                    add_date = False
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                if self.Tsum[i] < cd.So and jo < 0:
                    self.L[i] = cd.Lv
                    self.Lg[i] = cd.Lv
                    self.zr[i] = cd.zrv
                    zr = self.zr[i]
#                    self.kc[i] = cd.kcmin
                    fac=min(1.0, cd.Lv/cd.Lm)
                    self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                else: # Period of growth
                    jo = i
                    self.zr[i], self.L[i], self.Lg[i], self.Ly[i], self.kc[i] \
                        , self.Tsum[i] = \
                        cd.growcutfunc(self.Tsum[i], zr, cd.zrv, cd.cr, 
                                       cd.Lv, cd.Sf, cd.So, idate)
                    zr = self.zr[i]
                        
    def gf_wc(self, cd, mp):
        """  Computes growth time series for winter crop """
        
        year = mp.winterperiod[0].year
        # Sowing must be in the fall, before beginning of winter
        mp.sow = cd.sowdate.replace(year = year)
        if mp.sow  > mp.winterperiod[0]:
            year = year - 1 
            mp.sow = cd.sowdate.replace(year = year)
        # Harvest must be before sowing
        mp.harvest = cd.harvestdate.replace(year = year)
        if mp.harvest > mp.sow:
            mp.harvest = cd.harvestdate.replace(year = year-1)
        mp.harvest0 = mp.harvest
        add_date = True
        for i in range(0,self.nd):
            idate = self.date[i]
            if mp.autoirrigate and idate > mp.irrigationperiod[1]: # Increment period to next year
                mp.irrigationperiod = add_year(mp.irrigationperiod)
            # Winter - this may increment winter period, sow and harvest dates:
            if iswinter(idate, mp):
                self.L[i] = cd.Lv
                self.Lg[i] = cd.Lv
                self.zr[i] = cd.zrv
#                self.kc[i] = cd.kcmin
                fac=min(1.0, cd.Lv/cd.Lm)
                self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
            # From winter until harvest
            elif idate < mp.harvest:
                # Calculate temperature sum
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                    zr = cd.zrv
                if self.Tsum[i] < cd.So:
                    self.L[i] = cd.Lv
                    self.Lg[i] = cd.Lv
                    self.zr[i] = cd.zrv
                    zr = self.zr[i]
#                    self.kc[i] = cd.kcmin
                    fac=min(1.0, cd.Lv/cd.Lm)
                    self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                elif self.Tsum[i] < cd.Sr: # Growth period
                    self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i] = \
                        cd.growfunc(self.Tsum[i], zr, cd.zrv, cd.cr, cd.Lv, 
                                    cd.Sf, cd.So)
                    zr = self.zr[i]
                    add_date = True
                else: # Ripening period, until harvest
                    if add_date and mp.autoirrigate:
                        cd.irrigation_append(mp.sow, idate-mp.tlim,
                                          mp.irrigationperiod)
                        add_date = False
                    self.zr[i], self.L[i], self.Lg[i], self.Ly[i], self.kc[i] \
                        = cd.ripefunc(self.Tsum[i], zr)
                    if cd.autoharvest and self.Lg[i] < 0.001 and \
                    mp.harvest == mp.harvest0:
                        mp.harvest = idate + timedelta(days=+7)
            # From harvest to sowing, when soil is bare
            elif idate < mp.sow:
                    zr = self.zr[i]
                    self.kc[i] = cd.kcmin
            # From sowing until winter
            else:
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                if self.Tsum[i] > cd.Soe:
                    self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i] = \
                        cd.growfunc(self.Tsum[i], zr, 0.0, cd.cre, 0.0, cd.Sfe, 
                                    cd.Soe)
                    zr = self.zr[i]
                else:
                    zr = self.zr[i]
                    self.kc[i] = cd.kcmin

    def gf_sc(self, cd, mp): 
        """ Computes growth time series for spring crop """
        
        year = mp.winterperiod[0].year
        # Harvest must be in summer or fall, before beginning of winter
        mp.harvest = cd.harvestdate.replace(year = year)
        if mp.harvest > mp.winterperiod[0]:
            year = year - 1 
            mp.harvest = cd.harvestdate.replace(year = year)
        harvest = mp.harvest
        # Sowing must be before harvest
        mp.sow = cd.sowdate.replace(year = year)
        if mp.sow > mp.harvest:
            mp.sow = cd.sowdate.replace(year = year - 1)
            
        add_date = True
        for i in range(0,self.nd):
            idate = self.date[i]
            if idate > harvest: # Increment sow and harvest to next year
                [mp.sow, mp.harvest] = add_year([mp.sow, mp.harvest])
                harvest = mp.harvest
            if mp.autoirrigate and idate > mp.irrigationperiod[1]: # Increment period to next year
                mp.irrigationperiod = add_year(mp.irrigationperiod)
            # Before sowing or after harvest, when soil is bare
            if idate < mp.sow or idate >= harvest:
                self.kc[i] = cd.kcmin
            # From sowing to harvest
            else:
                # Calculate temperature sum
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                    zr = self.zr[i]
                if self.Tsum[i] < cd.So: # Until beginning of growth
                    self.kc[i] = cd.kcmin
                    zr = self.zr[i]
                    continue
                elif self.Tsum[i] < cd.Sr: # Growth until ripening
                    self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i] = \
                        cd.growfunc(self.Tsum[i], zr, cd.zrv, cd.cr, 0.0, 
                                    cd.Sf, cd.So)
                    zr = self.zr[i]
                    add_date = True
                else: # From beginning of ripening until harvest
                    if add_date and mp.autoirrigate:
                        cd.irrigation_append(mp.sow, idate-mp.tlim,
                                          mp.irrigationperiod)
                        add_date = False
                    self.zr[i], self.L[i], self.Lg[i], self.Ly[i], self.kc[i] \
                        = cd.ripefunc(self.Tsum[i], zr)
                    zr = self.zr[i]
                    if cd.autoharvest and self.Lg[i] < 0.001 and \
                    harvest == mp.harvest:
                        harvest = idate + timedelta(days=+7)
                        
       
    def gf_2c(self, cd, mp): 
        """ Computes growth time series for spring crop with grass as second
            crop
        """
        year = mp.winterperiod[0].year
        # Harvest must be in summer or fall, before beginning of winter
        mp.harvest = cd.harvestdate[0].replace(year = year)
        if mp.harvest > mp.winterperiod[0]:
            year = year - 1 
            mp.harvest = cd.harvestdate[0].replace(year = year)
        mp.harvest0 = mp.harvest
        # Sowing must be before harvest
        mp.sow = cd.sowdate.replace(year = year)
        if mp.sow > mp.harvest:
            mp.sow = cd.sowdate.replace(year = year - 1)
        
#        tsow = cd.sowdate
#        tharvest = cd.harvestdate[0]
        cd.harvestdate = cd.harvestdate[1:]
#        cd.daygrowth = 0.0
        add_date = True
        cd.Lmin = cd.Lv
        for i in range(0,self.nd):
            idate = self.date[i]
#            print(i,idate,harvest,mp.harvest)
#            if idate > harvest: # Increment sow and harvest to next year
#                [mp.sow, mp.harvest] = add_year([mp.sow, mp.harvest])
#                harvest = mp.harvest
            if mp.autoirrigate and idate > mp.irrigationperiod[1]: # Increment period to next year
                mp.irrigationperiod = add_year(mp.irrigationperiod)
            # Before sowing or after harvest, when soil is bare
            if iswinter(idate, mp):
                self.kc[i] = cd.kcmin
            elif idate < mp.sow:
#                print(i,idate,mp.sow)
                self.kc[i] = cd.kcmin
#                if harvest < mp.harvest:
#                    harvest = mp.harvest
#                zr = 0.0
            # From sowing to harvest
            else:
                # Calculate temperature sum
                if i > 0:
                    self.Tsum[i] = self.Tsum[i-1] + self.T[i]
                else:
                    self.Tsum[i] = self.T[i]
                    zr = self.zr[i]
                # First crop
                if idate <= mp.harvest:
                    if self.Tsum[i] < cd.So: # Until beginning of growth
                        self.kc[i] = cd.kcmin
                        zr = self.zr[i]
                        continue
                    elif self.Tsum[i] < cd.Sr: # Growth until ripening
                        self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i] = \
                            cd.growfunc(self.Tsum[i], zr, 0.0, cd.cr, 0.0, 
                                        cd.Sf, cd.So)
                        zr = self.zr[i]
                        add_date = True
                    else: # From beginning of ripening until harvest
                        if add_date and mp.autoirrigate:
                            cd.irrigation_append(mp.sow, idate-mp.tlim,
                                              mp.irrigationperiod)
                            add_date = False
                        self.zr[i], self.L[i], self.Lg[i], self.Ly[i], self.kc[i] \
                            = cd.ripefunc(self.Tsum[i], zr)
                        zr = self.zr[i]
                        if cd.autoharvest and self.Lg[i] < 0.001 and \
                        mp.harvest == mp.harvest0:
                            mp.harvest = idate + timedelta(days=+7)
                        if idate == mp.harvest:
                            self.Tsum[i] = 0.0
                            self.L[i] = cd.Lc
                            self.Lg[i] = cd.Lc
                            self.zr[i] = cd.zrv
                            zr = self.zr[i]
                            fac=min(1.0, cd.Lc/cd.Lm)
                            self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
#                            self.kc[i] = cd.kcmin
                            add_date = True
                        elif self.Lg[i] < cd.Lc:
                            fac=min(1.0, cd.Lc/cd.Lm)
                            self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
                            self.Lg[i] = cd.Lc
                # Second grop (grass that is cut)
                else:
                    if add_date and mp.autoirrigate:
                        cd.autoirr_period.append(
                                (idate, mp.irrigationperiod[1]))
                        add_date = False
                    if self.Tsum[i] < cd.Soe:# and jo < 0:
                        zr = zr + cd.cre
                        self.zr[i] = min(zr, cd.zrx)
                        zr = self.zr[i]
                        self.L[i] = cd.Lc
                        self.Lg[i] = cd.Lc
                        fac=min(1.0, cd.Lc/cd.Lm)
                        self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
#                        self.kc[i] = cd.kcmin
                    else: # Period of growth
                        self.zr[i],self.L[i],self.Lg[i],self.Ly[i],self.kc[i],\
                        self.Tsum[i] = \
                            cd.growcutfunc(self.Tsum[i], zr, cd.zrv, 
                                           cd.cre, cd.Lc, cd.Sfe, cd.Soe, idate)
                        zr = self.zr[i]
       
    def gf_df(self , cd, mp):
        """ Computes growth time series for decidious forest """
        
        mp.autoirrigate = False
        idate = self.date[0]
        (t1, t2) = set_period("Leaf_out", (cd.leaflife[0], cd.leaflife[1]), 
                              idate)
        (t3, t4) = set_period("Leaf_loss", (cd.leaflife[2], cd.leaflife[3]),
                             idate)
        for i in range(0,self.nd):
            idate = self.date[i]
            if idate > t4:
               [t1, t2] = add_year([t1, t2]) 
               [t3, t4] = add_year([t3, t4]) 
            self.zr[i] = cd.zrx
            # Before leaves come out, or after they have wilted
            if idate < t1 or idate >= t4:
                self.L[i] = cd.Lv
                self.kc[i] = cd.kcmin
            # During coming out of leaves
            elif idate < t2:
                fac = (idate-t1).days / (t2-t1).days
                self.L[i] = cd.Lv + (cd.Lm-cd.Lv)*fac
                self.kc[i] = cd.kcmin + (cd.kcmax-cd.kcmin)*fac
#                self.kc[i] = cd.kcw + (cd.kcs-cd.kcw)*fac
            # During summer
            elif idate < t3:
                self.L[i] = cd.Lm
                self.kc[i] = cd.kcmax
            # During wilting
            else:
                fac = (idate-t3).days / (t4-t3).days
                self.L[i] = cd.Lm - (cd.Lm-cd.Lv)*fac
                self.kc[i] = cd.kcmax - (cd.kcmax-cd.kcmin)*fac
            self.Lg[:] = self.L[:]

    def gf_nf(self,cd, mp):
        """  Computes growth time series for needleleaf forest """
        
        mp.autoirrigate = False
        for i in range(0,self.nd):
            self.L[i]=cd.Lm
            self.Lg[i]=cd.Lm
            self.zr[i]=cd.zrx
            self.kc[i]=cd.kcmin
    

"""    
===============================================================================
class of funtions to initialize, read, and compute crop parameter values
===============================================================================
"""
class CropParameters:
    
#    def growfunc(self, Tsum):
    def growfunc(self, Tsum, zr, zrmin, cr, Lmin, Sf, So):
        """
        computes root depth, leaf areas, and kc during spring;
        returns these values;
        
        called from class TimeSeries growth function.
        """
        
        zr = min(zr + cr, self.zrx)
        zr = max(zrmin, zr)
        fac = (np.exp(2.3979*(Tsum-So)/(Sf-So)) - 1.0) / 10.0
#        L = self.Lm*fac
        L = Lmin + (self.Lm-Lmin)*fac
        L = min(self.Lm, L)
#        L = max(Lmin, L)
        Lg = L
        Ly = 0.0
        fac=min(1.0, Lg/self.Lm)
        kc = self.kcmin + (self.kcmax-self.kcmin)*fac
        
        return(zr, L, Lg, Ly, kc)
        
    def growcutfunc(self,Tsum, zr, zrmin, cr, Lmin, Sf, So, idate):
        """
        computes root depth, leaf areas, and kc for grass that is 
        cut/harvested; returns these values and Tsum, which is set to 0 when
        grass is cut;
        
        called from class TimeSeries growth function.
        """
        zr = min(zr + cr, self.zrx)
        zr = max(zrmin, zr)
        # Check if day of harvest
        for hdate in self.harvestdate:
            if same_day_and_month(idate, hdate):
                Tsum = 0.0
                continue
        if Tsum > So:
            L = Lmin + ((self.Lm-Lmin)
                 * (np.exp(2.3979*(Tsum - So)/(Sf - So)) - 1.0)
                 / 10.0)
        else:
            L = 0.0
        L = max(Lmin, L)
        L = min(self.Lm, L)
        Lg = L
        Ly = 0.0
        fac=min(1.0, Lg/self.Lm)
        kc = self.kcmin + (self.kcmax-self.kcmin)*fac
        
        return(zr, L, Lg, Ly, kc, Tsum)
        

    def ripefunc(self,Tsum, zr):
        """
        computes root depth, leaf areas, and kc during ripening;
        returns these values;
        
        called from class TimeSeries growth function.
        """
        zr = zr + self.cr
        zr = max(self.zrv, min(zr,self.zrx))
        Lg = max(0, self.Lm*(1.0 - (Tsum-self.Sr)/(self.Sm-self.Sr)))
        L = max(self.Lym, 
                self.Lm-(self.Lm-self.Lym)*(Tsum-self.Sr)/(self.Sm-self.Sr))
        Ly = L - Lg
        fac = min(1.0, Lg/self.Lm)
        kc = self.kcmin + (self.kcmax-self.kcmin)*fac
        
        return(zr, L, Lg, Ly, kc)

    def irrigation_append(self, sow, harvestmature, irrigationperiod):
        """ appends irrigation period adjusted to crop growth """
        if sow < irrigationperiod[0] or sow > harvestmature:
            d1 = irrigationperiod[0]
        else:
            d1 = sow
        if harvestmature < irrigationperiod[1]:
            d2 = harvestmature
        else:
            d2 = irrigationperiod[1]
        self.autoirr_period.append((d1,d2))
        
    def within_irr_per(self, d):
        """ 
        checks if date d is within crop dependent irrigation period.
        """
        n = len(self.autoirr_period)
        if n < 1:
            return(False)
        if d <= self.actualirr_per[0]:
            return(False)
        elif d < self.actualirr_per[1]:
            return(True)
        if self.irr_per < n-1:
            self.irr_per = self.irr_per + 1
            self.actualirr_per = self.autoirr_period[self.irr_per]
        return(False)

    def initialize(self, ctype, cval, ts, sd, fl):
        """
        Initialize crop parameter values by use of dictionaries;
        also set t.plant_growth, the time series plant growth function;
        crop_type, which is either ctype or cval['croptype'], is used as 
        'key' for dictionaries;
        
        called from self.read_initialize().
        """
        
        self.L=0.0
        self.zr=0.0

        # Predefined crops        
        cropname = {
                    "BS": 'Bare soil',
                    "G1": 'Grass with grazing',
                    "G2": 'Grass for hay', 
                    "WW": 'Winter wheat', 
                    "SB": 'Spring barley',
                    "POT": 'Potato',
                    "FB": 'Fodder beet',
                    "SR": 'Spring rape',
                    "PEA": 'Pea',
                    "SBG": 'Spring barley with grass',
                    "MZ": 'Maize',
                    "DF": 'Deciduous forest',
                    "NF": 'Needleleaf forest',
                    "WL": 'Wetland',
                    "WM": 'Wet meadow'
                    }
#        self.cropname = cropname[crop_type]
#        self.crop_type = crop_type
        
        try:
            # Check for correct definition of cropname or croptype; 
            # if incorrect, raise Exception.
            if ctype in cropname.keys():
                self.cropname = cropname[ctype]
                self.crop_type = ctype
            elif cval != None and 'croptype' in cval.keys():
                self.cropname = ctype
                self.crop_type = cval['croptype']
                if not self.crop_type in cropname.keys():
                    ctype = ctype + "/" + self.crop_type
                    raise Exception
            else:
                raise Exception
            crop_type = self.crop_type

            
            # Function to compute time series for plant growth
            gf = {
            "BS": ts.gf_bs, 
            "G1": ts.gf_gi, 
            "G2": ts.gf_gii, 
            "WW": ts.gf_wc, 
            "SB": ts.gf_sc, 
            "POT": ts.gf_sc, 
            "FB": ts.gf_sc, 
            "SR": ts.gf_sc, 
            "PEA": ts.gf_sc, 
            "SBG": ts.gf_2c,
            "MZ": ts.gf_sc, 
            "DF": ts.gf_df, 
            "NF": ts.gf_nf,
            "WL": ts.gf_gi,
            "WM": ts.gf_gi
            }
            try:
                ts.plant_growth = gf[crop_type]
            except:
                print_msg('  Growth function for crop type %s is not '
                      + 'implemented yet!'%self.crop_type, fl)
                return(False)

            # Break points for water use function
            #                    Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
            cb = {
            "BS":  np.array([-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.]),
            "G1":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "G2":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "WW":  np.array([0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2]),
            "SB":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "POT": np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "FB":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "SR":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "PEA": np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "SBG": np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "MZ":  np.array([0.2, 0.2, 0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3, 0.2, 0.2]),
            "DF":  np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]),
            "NF":  np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]),
            "WL":  np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
            "WM":  np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
            }
            self.cb = cb[crop_type]
    
            # Root growth parameters: tupple (cr, cre).
            cr = {
            "BS":  (0.,0.),  
            "G1":  (12.,0.),  
            "G2": (12.,0.), 
            "WW": (15.,15.),
            "SB": (15.,0.),  
            "POT": (15.,0.),  
            "FB": (15.,0.), 
            "SR": (15.,0.),
            "PEA": (15.,0.), 
            "SBG": (15.,12.), 
            "MZ": (15.,0.), 
            "DF":  (0.,0.), 
            "NF": (0.,0.),
            "WL": (12.,0.),
            "WM": (12.,0.)
            }
            self.cr = cr[crop_type][0]
            self.cre = cr[crop_type][1]
    
            # Root depth winter, millimeter
            zrv = {
            "BS": 0., 
            "G1": 200., 
            "G2": 200., 
            "WW": 150., 
            "SB": 0., 
            "POT": 0., 
            "FB": 0., 
            "SR": 0., 
            "PEA": 0., 
            "SBG": 200., 
            "MZ": 0., 
            "DF": 1000., 
            "NF": 1000.,
            "WL": 1000.,
            "WM": 1000.
            }
            self.zrv = zrv[crop_type] # Root depth during winter
        
            # Max effective root depth, millimeter
            zrx = {
            "BS":  {"JB1":  0.0, "JB2":  0.0, "JB3":  0.0, "JB4":  0.0, "JB5":  0.0, "JB6":  0.0, "JB7":  0.0},
            "G1":  {"JB1": 500., "JB2": 500., "JB3": 500., "JB4":  500.,"JB5": 500., "JB6": 500., "JB7": 500.},
            "G2":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "WW":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "SB":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "POT": {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 750., "JB5": 750., "JB6": 750., "JB7": 750.},
            "FB":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "SR":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "PEA": {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "SBG": {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "MZ":  {"JB1": 500., "JB2": 750., "JB3": 500., "JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "DF":  {"JB1": 1000.,"JB2": 1000.,"JB3": 1000.,"JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "NF":  {"JB1": 1000.,"JB2": 1000.,"JB3": 1000.,"JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "WL":  {"JB1": 1000.,"JB2": 1000.,"JB3": 1000.,"JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.},
            "WM":  {"JB1": 1000.,"JB2": 1000.,"JB3": 1000.,"JB4": 1000.,"JB5": 1000.,"JB6": 1000.,"JB7": 1000.}
            }
            self.zrx = zrx[crop_type][sd.soil_type] # Maximum root depth
    
            # Leaf area parameters
            L = {
            "BS":  {"Lm": 0.0, "Lv": 0.0, "Lc": 0.0, "Lym": 0.0},
            "G1":  {"Lm": 2.0, "Lv": 1.0, "Lc": 0.5, "Lym": 0.0},
            "G2":  {"Lm": 5.0, "Lv": 1.0, "Lc": 0.5, "Lym": 0.0},
            "WW":  {"Lm": 5.0, "Lv": 0.5, "Lc": 0.0, "Lym": 2.0},
            "SB":  {"Lm": 5.0, "Lv": 0.0, "Lc": 0.0, "Lym": 2.0},
            "POT": {"Lm": 5.0, "Lv": 0.0, "Lc": 0.0, "Lym": 0.0},
            "FB":  {"Lm": 5.0, "Lv": 0.0, "Lc": 0.0, "Lym": 0.0},
            "SR":  {"Lm": 5.0, "Lv": 0.0, "Lc": 0.0, "Lym": 2.0},
            "PEA": {"Lm": 5.0, "Lv": 0.0, "Lc": 0.0, "Lym": 2.0},
            "SBG": {"Lm": 5.0, "Lv": 0.0, "Lc": 0.5, "Lym": 2.0},
            "MZ":  {"Lm": 3.5, "Lv": 0.0, "Lc": 0.0, "Lym": 1.0},
            "DF":  {"Lm": 6.0, "Lv": 0.5, "Lc": 0.0, "Lym": 0.5},
            "NF":  {"Lm": 8.0, "Lv": 8.0, "Lc": 0.0, "Lym": 8.0},
            "WL":  {"Lm": 3.0, "Lv": 1.0, "Lc": 0.0, "Lym": 0.0},
            "WM":  {"Lm": 3.0, "Lv": 1.0, "Lc": 0.0, "Lym": 0.0}
            }
            self.Lm = L[crop_type]["Lm"] # Maximum leaf area
            self.Lv = L[crop_type]["Lv"] # Leaf area during winter
            self.Lc = L[crop_type]["Lc"] # Leaf area after cutting
            self.Lym= L[crop_type]["Lym"] # Yellow leaf area at maturity
        
            # Temperature sums
            Tsum = {
            "BS":  {"So":   0., "Sf":   0., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "G1":  {"So": 125., "Sf": 425., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "G2":  {"So": 125., "Sf": 425., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "WW":  {"So": 125., "Sf": 425., "Sr":  1425., "Sm":  1750., "Soe": 140., "Sfe": 600.},
            "SB":  {"So": 110., "Sf": 510., "Sr":  1200., "Sm":  1525., "Soe":   0., "Sfe":   0.},
            "POT": {"So": 300., "Sf": 900., "Sr":  1650., "Sm":  2050., "Soe":   0., "Sfe":   0.},
            "FB":  {"So": 200., "Sf":1100., "Sr": np.inf, "Sm": np.inf, "Soe":   0., "Sfe":   0.},
            "SR":  {"So": 140., "Sf": 540., "Sr":  1600., "Sm":  1750., "Soe":   0., "Sfe":   0.},
            "PEA": {"So": 150., "Sf": 550., "Sr":  1250., "Sm":  1600., "Soe":   0., "Sfe":   0.},
            "SBG": {"So": 110., "Sf": 510., "Sr":  1200., "Sm":  1525., "Soe": 125., "Sfe": 425.},
            "MZ":  {"So": 110., "Sf": 800., "Sr":  1500., "Sm":  2000., "Soe":   0., "Sfe":   0.},
            "DF":  {"So":   0., "Sf":   0., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "NF":  {"So":   0., "Sf":   0., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "WL":  {"So": 125., "Sf": 425., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.},
            "WM":  {"So": 125., "Sf": 425., "Sr":     0., "Sm":     0., "Soe":   0., "Sfe":   0.}
            }
            self.So = Tsum[crop_type]["So"]
            self.Sf = Tsum[crop_type]["Sf"]
            self.Sr = Tsum[crop_type]["Sr"]
            self.Sm = Tsum[crop_type]["Sm"]
            self.Soe = Tsum[crop_type]["Soe"]
            self.Sfe = Tsum[crop_type]["Sfe"]
        
            """
             Crop Eref to Ep coefficient;
             Forest values taken from Refgaard et al., GEUS Rapport 2011/77;
             Summer values, kcmax, taken from Daisy/Agro and Kjaersgaard et al.
             (2008) and Allen et al. (1998).
             kcmin values taken from Stisen et al. (2011).
             kcmin1 values taken from Daisy/Agro.
            """
            k = {
            "BS":  {"kcmin": 1.0, "kcmax": 1.00,"kcmin1": 0.6, "kcmax1": 0.6},
            "G1":  {"kcmin": 1.0, "kcmax": 1.00,"kcmin1": 0.9, "kcmax1": 0.90},
            "G2":  {"kcmin": .9625, "kcmax": 1.15,"kcmin1": .9625, "kcmax1": 1.15},
            "WW":  {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "SB":  {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "POT": {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "FB":  {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "SR":  {"kcmin": 1.0, "kcmax": 1.10,"kcmin1": 0.6, "kcmax1": 1.10},
            "PEA": {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "SBG": {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "MZ":  {"kcmin": 1.0, "kcmax": 1.15,"kcmin1": 0.6, "kcmax1": 1.15},
            "DF":  {"kcmin": .85, "kcmax": 1.05,"kcmin1": .85, "kcmax1": 1.05},
            "NF":  {"kcmin": 1.4, "kcmax":  1.5,"kcmin1": 1.4, "kcmax1":  1.5},
            "WL":  {"kcmin": 0.9, "kcmax": 1.20,"kcmin1": 0.75, "kcmax1": 1.20},
            "WM":  {"kcmin": 0.9, "kcmax": 1.20,"kcmin1": 0.75, "kcmax1": 1.20}
            }
            self.kcmin = k[crop_type]["kcmin1"]
            self.kcmax = k[crop_type]["kcmax1"]
#            self.kcmin = 1.0
#            self.kcmax = 1.0
        
            # Sow and harvest dates
            d = {
            "BS":  {"sow": '19000101', "harv": '19010101'},
            "G1":  {"sow": '19000101', "harv": '19010101'},
            "G2":  {"sow": '19000101', "harv": '19010101'},
            "WW":  {"sow": '19000915', "harv": '19000817'},
            "SB":  {"sow": '19000415', "harv": '19000817'},
            "POT": {"sow": '19000501', "harv": '19000930'},
            "FB":  {"sow": '19000501', "harv": '19001015'},
            "SR":  {"sow": '19000415', "harv": '19000901'},
            "PEA": {"sow": '19000415', "harv": '19000815'},
            "SBG": {"sow": '19000415', "harv": '19001031'},
            "MZ":  {"sow": '19000415', "harv": '19001001'},
            "DF":  {"sow": '19000101', "harv": '19010101'},
            "NF":  {"sow": '19000101', "harv": '19010101'},
            "WL":  {"sow": '19000101', "harv": '19010101'},
            "WM":  {"sow": '19000101', "harv": '19010101'}
            }
            self.sowdate = datetime.strptime(
                    d[crop_type]["sow"],'%Y%m%d')#.date()
            self.harvestdate = datetime.strptime(
                    d[crop_type]["harv"],'%Y%m%d')#.date()
            self.autoharvest = False
        
            # Hay harvest dates
            if crop_type == "G2":
                Hdatetxt=['19000525','19000630','19000805','19000915',
                          '19001025']
                self.harvestdate = []
                for Hdate in Hdatetxt:
                    self.harvestdate.append(
                            datetime.strptime(Hdate,'%Y%m%d'))#.date()
        
            # Spring barley with grass harvest dates
            if crop_type == "SBG":
                Hdatetxt=['19000817','19001001']
                self.harvestdate = []
                for Hdate in Hdatetxt:
                    self.harvestdate.append(
                            datetime.strptime(Hdate,'%Y%m%d'))#.date()
                    
            self.autoirr_period = [] # Appended with crop dependent autoirrigation dates
            self.irr_per = 0 # Counter for irrigation periods
            
            # Leaf life of deciduous forest
            if crop_type == "DF":
                leaf_out_begin = "19000501" # May 1st
                leaf_out_end  = "19000520" # May 20th
                leaf_loss_begin = "19000901" # Sep 1st
                leaf_loss_end  = "19000930" # Sep 30th
                t1 = datetime.strptime(leaf_out_begin,'%Y%m%d')#.date()
                t2 = datetime.strptime(leaf_out_end,'%Y%m%d')#.date()
                t3 = datetime.strptime(leaf_loss_begin,'%Y%m%d')#.date()
                t4 = datetime.strptime(leaf_loss_end,'%Y%m%d')#.date()
                self.leaflife = [t1, t2, t3, t4]
                
            return(True)
            
        except:
            print_msg(("Error: Crop type = %s cannot be recognized."
                       + " Loop to next!"%(ctype)), fl)
            return(False)
   
    def read_initialize(self, ctype, cval, ts, sd, fl):
        """
        Initialize crop parameter values in self.initialize(); 
        if specified by parameter key in input dictionary sval, replace 
        default value;
        ts is TimeSeries class for which function ts.plant_growth is set;
        
        below datadict is dictionary for crop parameters for which it is
        possible to replace default value by input value in cval; its 'key' 
        is case sensitive; its 'value' is a tupple defined in function 
        replace_default_values();
        
        called from run_model().
        """
        
        if self.initialize(ctype, cval, ts, sd, fl):
            crop_type = self.crop_type
            if cval != None and 'croptype' in cval.keys():
                cval.pop('croptype') # Remove item that will no longer be used
            if cval != None:
                print_msg("\n Crop parameter values:  update from input file.",
                          fl)
                # fl.write("\n  %s"%ctype)
                print_msg("  %s:"%ctype, fl)
                print_dump(cval, fl) 
                datadict = {
                            "name": (self.cropname, "s", 1),
                            "cb": (self.cb, "f", 12, (0., 1.)),
                            "cr": (self.cr, "f", 1, (0, np.inf)),
                            "cre":  (self.cre, "f", 1, (0, np.inf)),
                            "zrv":  (self.zrv, "f", 1, (0, np.inf)),
                            "zrx":  (self.zrx, "f", 1, (0, np.inf)),
                            "Lm":  (self.Lm, "f", 1, (0, np.inf)),
                            "Lv":  (self.Lv, "f", 1, (0, np.inf)),
                            "Lc":  (self.Lc, "f", 1, (0, np.inf)),
                            "Lym":  (self.Lym, "f", 1, (0, np.inf)),
                            "So":  (self.So, "f", 1, (0, np.inf)),
                            "Sf":  (self.Sf, "f", 1, (0, np.inf)),
                            "Sr":  (self.Sr, "f", 1, (0, np.inf)),
                            "Sm":  (self.Sm, "f", 1, (0, np.inf)),
                            "Soe":  (self.Soe, "f", 1, (0, np.inf)),
                            "Sfe":  (self.Sfe, "f", 1, (0, np.inf)),
                            "kcmin":  (self.kcmin, "f", 1, (0, np.inf)),
                            "kcmax":  (self.kcmax, "f", 1, (0, np.inf)),
                            "autoharvest": (self.autoharvest, "b", 1)
                            }
                if crop_type == "DF":
                    datadict.update({"leaflife": (self.leaflife,"d",4)})
                elif crop_type == 'G2':
                    datadict.update({"harvestdate": (self.harvestdate,"d",-1)})
                elif crop_type == 'SBG':
                    datadict.update({"sowdate":  (self.sowdate,"d",1),
                                     "harvestdate": (self.harvestdate,"d",-1)})
                else:
                    datadict.update({"sowdate":  (self.sowdate,"d",1),
                                     "harvestdate":  (self.harvestdate,"d",1)})
                    
                # Read vales from fname
                update, datadict = replace_default_values(cval, datadict, fl)
                
                if update:
                    self.cropname = datadict['name'][0]
                    self.cb = datadict['cb'][0]
                    self.cr = datadict['cr'][0]
                    self.cre = datadict['cre'][0]
                    self.zrv = datadict['zrv'][0]
                    self.zrx = datadict['zrx'][0]
                    self.Lm = datadict['Lm'][0]
                    self.Lv = datadict['Lv'][0]
                    self.Lc = datadict['Lc'][0]
                    self.Lym = datadict['Lym'][0]
                    self.So = datadict['So'][0]
                    self.Sf = datadict['Sf'][0]
                    self.Sr = datadict['Sr'][0]
                    self.Sm = datadict['Sm'][0]
                    self.Soe = datadict['Soe'][0]
                    self.Sfe = datadict['Sfe'][0]
                    self.kcmin = datadict['kcmin'][0]
                    self.kcmax = datadict['kcmax'][0]
                    if crop_type == 'DF':
                        leaflife = datadict['leaflife'][0]
                        if leaflife[0] > leaflife[1]:
                            print_msg('  "leaf_out_begin > leaf_out_end;"'
                                  + '  input line ignored.', fl)
                        elif leaflife[2] > leaflife[3]:
                            print_msg('  "leaf_loss_begin > leaf_loss_end;"'
                                  + '  input line ignored.', fl)
                        else:
                            self.leaflife = leaflife
                    elif crop_type == 'G2': # Hay harvest dates
                        self.harvestdate = datadict['harvestdate'][0]
                    else:
                        self.sowdate = datadict['sowdate'][0]
                        self.harvestdate = datadict['harvestdate'][0]
                    self.autoharvest = datadict['autoharvest'][0]
            else:
                print_msg("\n Crop parameter values:  use default.", fl)
                
            return(True)
            
        else:
            return(False)
                

"""        
===============================================================================
class of funtions to initialize, read, and compute soil parameter values
===============================================================================
"""
class SoilParameters:  
    
    def initialize(self,stype,sval,fl):
        """
        Initialize soil parameter values by use of dictionaries;
        stype, or sval['soiltype'] is used as 'key' for dictionaries;
        
        called from self.read_initialize().
        """
        
        # Predifined soils with default values given below
        soilname = {'JB1':'Coarse sandy soil (JB1)',
                    'JB2':'Fine sandy soil (JB2)',
                    'JB3':'Coarse sandy soil with clay (JB3)',
                    'JB4':'Fine sandy soil with clay (JB4)',
                    'JB5':'Clayey soil with coarse sand (JB5)',
                    'JB6':'Clayey with fine sand (JB6)',
                    'JB7':'Clayey soil (JB7)'
                    }
            
        try:
            # Check for correct definition of soilname or soiltype; 
            # otherwise, raise Exception.
            if stype in soilname.keys():
                self.soilname = soilname[stype]
                self.soil_type = stype
            elif sval != None and 'soiltype' in sval.keys():
                self.soilname = stype
                self.soil_type = sval['soiltype']
                if not self.soil_type in soilname.keys():
                    stype = stype + "/" + self.soil_type
                    raise Exception
            else:
                raise Exception

            ### Default values for Linear model / Evacrop ###

            thf = {"JB1": np.array([.16, .08, .08, .08]),
                   "JB2": np.array([.20, .18, .18, .18]),
                   "JB3": np.array([.20, .12, .09, .09]),
                   "JB4": np.array([.20, .13, .09, .09]),
                   "JB5": np.array([.20, .16, .12, .12]),
                   "JB6": np.array([.20, .16, .16, .16]),
                   "JB7": np.array([.20, .16, .16, .16])
                   }
            self.thf = thf[self.soil_type]

            kq = {"JB1": (0.6,0.6),
                  "JB2": (0.3,0.3),
                  "JB3": (0.5,0.5),
                  "JB4": (0.3,0.3),
                  "JB5": (0.3,0.3),
                  "JB6": (0.3,0.3),
                  "JB7": (0.3,0.3)
                  }
            self.kqr = kq[self.soil_type][0]
            self.kqb = kq[self.soil_type][1]
            
            # Macro-pore flow parameters
            self.Kmp = 0.0
            # self.thmp = self.thf[0] #0.15
            self.Cmp = self.thf[0]*50. #0.15
            self.Vmprel = np.inf
            
            # Surface runoff parameters (from Daisy 5.93 dk-horizon.dai)
            ths = {"JB1": 0.395,
                   "JB2": 0.412,
                   "JB3": 0.406,
                   "JB4": 0.420,
                   "JB5": 0.391,
                   "JB6": 0.386,
                   "JB7": 0.386}
            self.Kro = 0.0
            self.thsat = ths[self.soil_type]
            
            self.Ce = 10.
            
            ### Mualem-van Genuchten / Daisy 5.93 dk-horizon.dai ###
            # Tht_s, Tht_r, n, l are dimensionless, 
            # K_sat in mm/d,
            # a in cm-1.
            #                                  Tht_s  Tht_r  a      n    K_sat     l
            self.horizon = {"A_JB1": np.array([0.395, 0.0, 0.062, 1.445, 1209., -0.973]),
                            "B_JB1": np.array([0.377, 0.0, 0.082, 1.580,  901., -0.335]),
                            "C_JB1": np.array([0.355, 0.0, 0.085, 1.721,  971.,  1.180]),
                            "A_JB2": np.array([0.412, 0.0, 0.054, 1.382,  843., -0.922]),
                            "B_JB2": np.array([0.405, 0.0, 0.069, 1.458,  639., -0.300]),
                            "C_JB2": np.array([0.370, 0.0, 0.080, 1.557,  549.,  1.188]),
                            "A_JB3": np.array([0.406, 0.0, 0.057, 1.337,  752., -1.461]),
                            "B_JB3": np.array([0.409, 0.0, 0.071, 1.388,  584., -0.937]),
                            "C_JB3": np.array([0.354, 0.0, 0.075, 1.370,  291.,  0.240]),
                            "A_JB4": np.array([0.420, 0.0, 0.048, 1.304,  593., -1.492]),
                            "B_JB4": np.array([0.395, 0.0, 0.058, 1.349,  417., -0.717]),
                            "C_JB4": np.array([0.354, 0.0, 0.056, 1.325,  259., -0.191]),
                            "A_JB5": np.array([0.391, 0.0, 0.050, 1.251,  425., -2.386]),
                            "B_JB5": np.array([0.362, 0.0, 0.066, 1.274,  268., -1.504]),
                            "C_JB5": np.array([0.317, 0.0, 0.043, 1.187,  113., -1.605]),
                            "A_JB6": np.array([0.386, 0.0, 0.044, 1.246,  353., -2.365]),
                            "B_JB6": np.array([0.360, 0.0, 0.054, 1.249,  230., -1.574]),
                            "C_JB6": np.array([.3382, 0.0, 0.046, 1.223,  150., -0.983]),
                            "A_JB7": np.array([0.386, 0.0, 0.048, 1.204,  324., -3.197]),
                            "B_JB7": np.array([0.352, 0.0, 0.053, 1.169,  148., -2.809]),
                            "C_JB7": np.array([0.3385,0.0, 0.047, 1.16 ,  110., -2.255])
                            }
            MvG_soilhorizons = {"JB1": ["A_JB1", "B_JB1","B_JB1","C_JB1"],
                                "JB2": ["A_JB2", "B_JB2","B_JB2","C_JB2"],
                                "JB3": ["A_JB3", "B_JB3","B_JB3","C_JB3"],
                                "JB4": ["A_JB4", "B_JB4","B_JB4","C_JB4"],
                                "JB5": ["A_JB5", "B_JB5","B_JB5","C_JB5"],
                                "JB6": ["A_JB6", "B_JB6","B_JB6","C_JB6"],
                                "JB7": ["A_JB7", "B_JB7","B_JB7","C_JB7"]
                                }
            self.MvG_soilhorizons = MvG_soilhorizons[self.soil_type]

        except:
            strn = "Error: Soil type = %s cannot be recognized. Loop to next!" 
            print_msg(strn%(stype), fl)
            return(False)
            
        self.soil_model = "lin" # "mvg" # or "lin"
        
        return(True)
            
            
    def read_initialize(self,stype,sval,fl):
        """
        Initialize soil parameter values; 
        if specified by parameter key in input dictionary sval, replace 
        default value;
        
        below datadict is dictionary for soil parameters for which it is
        possible to replace default value by input value in sval; its 'key' 
        is case sensitive; its 'value' is a tupple defined in function 
        replace_default_values();
        
        called from run_model().
        """
        
        if self.initialize(stype, sval, fl):
            if sval != None and 'soiltype' in sval.keys():
                sval.pop('soiltype') # Remove item that will no longer be used
            if sval != None:
                print_msg("\n Soil parameter values:  update from input file.",
                          fl)
                # fl.write("\n  %s"%stype)
                print_msg("  %s:"%stype, fl)
                print_dump(sval,fl)
                datadict={"thf": (self.thf, "f", 4, (0, np.inf)),
                          "kqr": (self.kqr, "f", 1, (0, np.inf)),
                          "kqb": (self.kqb, "f", 1, (0, np.inf)),
                          "Kmp": (self.Kmp, "f", 1, (0, np.inf)),
                          "Cmp": (self.Cmp, "f", 1, (0, np.inf)),
                          "Vmprel": (self.Vmprel, "f", 1, (0, np.inf)),
                          "Kro": (self.Kro, "f", 1, (0, np.inf)),
                          "ths": (self.thsat, "f", 1, (0, np.inf)),
                          "Ce":  (self.Ce, "f", 1, (0, np.inf)),
                          "name": (self.soilname, "s", 1),
                          "soilmodel": (self.soil_model, "s", 1),
                          "horizon": (self.horizon, "df", 6),
                          "soilhorizons": (self.MvG_soilhorizons, "s", 4)
                          }

                # Read values from file
                update, datadict = replace_default_values(sval, datadict, fl)
                if update:
                    self.thf = datadict['thf'][0]
                    self.kqr = datadict['kqr'][0]
                    self.kqb = datadict['kqb'][0]
                    self.Kmp = datadict['Kmp'][0]
                    self.Cmp = datadict['Cmp'][0]
                    self.Vmprel = datadict['Vmprel'][0]
                    self.Kro = datadict['Kro'][0]
                    self.thsat = datadict['ths'][0]
                    self.Ce = datadict['Ce'][0]
                    self.soilname = datadict['name'][0]
                    self.soil_model = datadict['soilmodel'][0].lower()
                    self.horizon = datadict['horizon'][0]
                    self.MvG_soilhorizons = datadict['soilhorizons'][0]

            else:
                print_msg("\n Soil parameter values:  use default.", fl)
                
            self.hydpar = []
            nlay = len(self.thf)

            if self.soil_model == "mvg":
                # Compute plant-available water content from van Genuchten,
                # Macro 5.0 Tech. Rep., eq. 21.
                # Also make layer list with Mualam parameter values and
                # array with difference between water content at saturation
                # and water content at field capacity.
##                sfc = 0.33 # Absolute value of suction at field capacity in bar
##                sfc = sfc * 1019.716 # in cm water column
                pF20 = 100.
                pF42 = 16000.
                self.ths = np.empty(nlay, dtype=float)
                for i in range(0, nlay):
                    horizon = self.MvG_soilhorizons[i]
                    try:
                        par = self.horizon[horizon]
                        ths = par[0]
                        thr = par[1]
                        a = par[2]
                        n = par[3]
                        Ks = par[4]
                        l = par[5]
                        m = 1.-1./n
##                        fac = pow((1. + pow((a*sfc), n)), -m)
##                        self.thf[i] = (ths - thr) * fac
                        fac_pF20 = pow((1. + pow((a*pF20), n)), -m)
                        fac_pF42 = pow((1. + pow((a*pF42), n)), -m)
                        self.thf[i] = (ths - thr) * (fac_pF20-fac_pF42)
                        self.hydpar.append((Ks, l, m))
                        self.ths[i] = ths - thr
                    except:
                        strn = ("  Error: Horizon name = \"%s\" cannot be "+
                                "recognized. Loop to next soil!")%(horizon)
                        print_msg(strn, fl)
                        return(False)
    
            elif self.soil_model == "lin":
                self.hydpar = np.ones(nlay, dtype = float)* self.kqr
                
            else:
                strn = ("  Error: soilmodel = \"%s\" is not "+
                        "recognized. Loop to next soil!")%(self.soil_model)
                print_msg(strn, fl)
                return(False)
                
            return(True)
            
        else:
            
            return(False)

"""        
===============================================================================
class of funtions to initialize, read, and compute model parameter values
===============================================================================
"""
class ModelParameters:

    def soil_evap(self, Ve, V, Epe, PI, zr):
        """ 
        Computes actual evaporation from soil, Eae,
        water volume of evaporation zone, Ve,
        and water volume of soil horizons after evaporation, V;
        
        called from Timeseries.watbal_ed_step().
        """
        
        Ve = Ve + PI
        V[0] = V[0] + PI
        VSoil = V.sum()
        if Ve < Epe:
            if Epe > VSoil:
                Eae = 0.0
            else:
                Eae = self.ce*Epe
#                V0 = V[0]
                # Subtract evaporation from all soil horizons
                V = self.reduce_water_vol(V, zr, Eae, "Eae")
                Ve = Ve*(1.-Eae/VSoil)
#                Ve = min(mp.Ce, Ve*(1.-Eae/VSoil))
#                Ve = min(mp.Ce, max(0.0, Ve*(1.-Eae/VSoil)))
#                Ve = min(mp.Ce, max(0.0, (Ve-V0+V[0])))
        else:
            Eae = Epe
            V[0] = V[0] - Eae
            Ve = max(0.0, (Ve - Eae))
#            Ve = min(self.Ce, max(0.0, (Ve - Eae)))
        return(Ve, V, Eae)
        
    def Lin_rel_transp(self, x, n):
        """
        Computes relative transpiration from linear model; 
        
        called from self.transpiration().
        """
        
        return(min([1., x]))

    def Pow_rel_transp(self, x, n):
        """
        Computes relative transpiration from power like model;
        n = 2 computes quadratic model; n = 3 computes spherical model; 
        and any n > 1 similarly;
        
        called from self.transpiration().
        """
        
        if n > 1.:
            a = n/(n-1.)
            b = a - 1.
            if x < 1.:
                Etrel = a*x - b*pow(x,n)
            else:
                Etrel = 1.
        else:
            Etrel = min([1., x])
        return(Etrel)

    def transpiration(self, Ve, V, Ept, zr, cb, crop_type):
        """ 
        Returns actual transpiration, Eat,
        and water volume of soil horizons after transpiration, V;
        
        called from Timeseries.watbal_ed_step().
        """
        
        # Compute absolute and relative water volume in root zone
        Vr = self.root_zone_water(V, zr)
        den = cb*self.Cr
        if den > 0.0:
            Vrel = Vr/den
        else:
            Vrel = np.inf
#            Vb = VSoil - Vr
        # Transpiration
        if Vrel >= 1.0 or crop_type == "WM" or crop_type == "WL":
            Eat = Ept
        else:
            if Vrel < 0.0:
                Eat = 0.0
            else:
                Eat = Ept * self.rel_transp(Vrel, 2)
        Eat = max(0.0, min(Vr, Eat))
        # Subtract transpiration from soil horizons within toot zone
        V0 = V[0]
        V = self.reduce_water_vol(V, zr, Eat, "Eat")
#        Ve = max(0.0, (Ve-V0+V[0]))
        Ve = max(0.0, Ve*(1.-(V0-V[0])/V0))
        return(Ve, V, Eat)
        
    def macropore_drainage_ec(self, Ve, cd):
        """ 
        Computes macropore flow, which is directly from top layer to beneath 
        soil profile; flow depends on relative water content in soil profile
        
        called from Timeseries.watbal_ed_step.
        """

        if cd.crop_type == "WL" or cd.crop_type == "WM":
            Dmp = 0.0
        else:
            if self.Kmp > 0.0:
                Vmp = Ve - self.Cmp
                # self.Vmprel = np.inf#0.5 + np.
                # self.Vmprel = 0.5
                if Vmp > 0.0 and self.Vrel < self.Vmprel:
                    Dmp = np.min([self.Kmp, Vmp])
                    if Dmp > Ve:
                        Dmp = Ve
                        Ve = 0.0
                    else:
                        Ve = Ve - Dmp
                else:
                    Dmp = 0.0
            else:
                Dmp = 0.0
        return(Ve, Dmp)

    def macropore_drainage(self, Ve, V, dfac, cd):
        """ 
        Computes macropore flow, which is directly from top layer to beneath 
        soil profile;
        
        called from Timeseries.watbal_ed_step.
        """

        if cd.crop_type == "WL" or cd.crop_type == "WM":
            Dmp = 0.0
        else:
            if self.Kmp > 0.0:
                Vmp = V[0] - self.Cmp
                Vrel = np.sum(V)/(self.Cr+self.Cb)
                if Vmp > 0.0 and Vrel < self.Vmprel:
                    Dmp = np.min([self.Kmp, Vmp])*dfac
                    Ve = max(0.0, Ve*(1.-(Dmp/V[0])))
                    V[0] = V[0] - Dmp
                else:
                    Dmp = 0.0
            else:
                Dmp = 0.0
        return(Ve, V, Dmp)

    def surface_runoff(self, V, dfac, cd):
        """ 
        Computes surface runoff occuring when the water content of the 
        top soil layer exceeds saturation;
        
        called from Timeseries.watbal_ed_step.
        """

        if cd.crop_type == "WL" or cd.crop_type == "WM":
            Qro = 0.0
        else:
            if self.Kro > 0.0:
                Vsat = V[0] - self.Csat
                if Vsat > 0.0:
                    Qro = self.Kro*Vsat*dfac
                    Qro = min(Vsat, Qro)
                    V[0] = V[0] - Qro
                else:
                    Qro = 0.0
            else:
                Qro = 0.0
        return(V, Qro)
        
    def Lin_drainage(self, V, C, K, dfac, cd):
        """
        Computes drainage using linear model;
        
        called from self.soil_drainage() and self.soil_water_routing().
        """

        if V > C:
            Dr = K * (V - C) * dfac
            Dr = min(V, Dr)
        else:
            Dr = 0.0
        return(Dr)
    
    def MvG_drainage(self, V, C, hydpar, dfac, cd):
        """
        Computes drainage using Mualem - van Genuchten hydraulic conductivity
        function;
        
        called from self.soil_drainage() and self.soil_water_routing().
        """
        
        Vr = V/C
        Ks = hydpar[0]
        l = hydpar[1]
        m = hydpar[2]
        if Vr > 1.0:
            Dr = Ks * dfac
        elif Vr > 0.0:
            Kd = Ks * pow(Vr, l)
            Dr = 1. - pow(Vr, 1./m)
            Dr = pow(Dr, m)
            Dr = Kd * pow((1. - Dr), 2) * dfac
        else:
            Dr = 0.0
        if Dr > V:
            Dr = V
        return(Dr)
    
    def soil_drainage(self, Ve, V, dfac, Ea, PI, cd):
        """ 
        Computes drainage from horizon to horizon, drainage from subzone, Db,
        water volume of soil horizons after drainage, V,
        and for wetland sets max water volume in evaporation reservoir, Ve;
        
        called from Timeseries.watbal_ed_step.
        """
            
        # If groundwater-fed wetland
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            Db = PI - Ea
            if cd.crop_type == "WL": 
                Ve = self.Ce
            V[:] = self.Cr_sat * self.dz/self.zx
        # If crop or forest
        else:
            # Soil drainage
            V0 = V[0]
            for i in range(0, self.ndz):
                Dr = self.drainage_func(V[i], self.C[i], self.hydpar[i], dfac,
                                        cd)
                V[i] = V[i] - Dr
                if i < self.ndz - 1:
                    V[i+1] = V[i+1] + Dr
                else:
                    Db = Dr
            Ve = max(0.0, Ve*(1.-(V0-V[0])/V0))
        return(Ve, V, Db) 
    
    def reduce_water_vol(self, V, zr, loss, loss_type):
        """
        Reduce water volume by "loss", either 
        - in entire soil profile (loss_type = "Eae"), or
        - in root zone (loss_type = "Eat")
        
        
        called from TimeSeries.watbal_ed_step().
        """
        
        if loss_type == "Eae": # Soil evaporation
            VSoil = V.sum()
            for i in range(0, self.ndz):
                V[i] = V[i] - loss * V[i]/VSoil
        elif loss_type == "Eat": # Transpiration
            Vr = self.root_zone_water(V, zr)
            l = 0
            z = max(0.0, zr)
            for i in range(0, self.ndz):
                if z > self.dz:
                    l = l + 1
                    z = z - self.dz
                    V[i] = V[i] - loss * V[i]/Vr
            if z > 0.0: 
                V[l] = V[l] - loss * (V[l]/Vr) * (z/self.dz)
        
        return(V)
    
    def root_zone_water(self, V, z):
        """
        Computes volume of water in root zone and sub zone;
        
        called from TimeSeries.watbal_ed_step().
        """
        
        Vr = 0.0
        j = 0
        z = max(0.0, z)
        for i in range(0, self.ndz):
            if z > self.dz:
                j = j + 1
                z = z - self.dz
                Vr = Vr + V[i]
            else:
                break
        if z > 0.0: 
            Vr = Vr + V[j] * z/self.dz
            
        return(Vr)
        
#    def soil_water_routing(self, V):
#        """
#        Route water through elements, as for series of linear reservoirs;
#        
#        called from TimeSeries.watbal_ed_step().
#        """
#        
#        for i in range(0, self.ndz-1):
#            dV = self.Lin_drainage(V[i], self.C[i], self.kq[i], cd)
#            V[i] = V[i] - dV
#            V[i+1] = V[i+1]  + dV
##            if V[i] > self.C[i]:
##                dV = self.kq[i] * (V[i] - self.C[i])
##                V[i] = V[i] - dV
##                V[i+1] = V[i+1]  + dV
#        return(V)
    
    
    def in_storage_ec(self):
        """ 
        compute sum of water stored as snow, intercepted water, and in 
        root and sub zones;
        
        called from TimeSeries.watbal_ed_step().
        """

        return(self.Vs + self.VI + self.V.sum())
        
    def in_storage(self):
        """ 
        compute sum of water stored as snow, intercepted water, and in 
        root and sub zones;
        
        called from TimeSeries.watbal().
        """

        return(self.Vs + self.VI + self.Vr + self.Vb)
        
    def Capacities(self,z,thf,L):
        """ 
        Initialize or compute capacities of root zone, sub zone, and
        interception;
        
        called from self.initialize(), TimeSeries.watbal(), and 
        TimeSeries.watbal_ed_step().
        """

        Cr = 0.0
        Cb = 0.0
        l = 0
        z = max(0.0, z)
        for i in range(0, self.ndz):
            dC = self.dz*thf[i]
            if z > self.dz:
                l = l + 1
                z = z - self.dz
                Cr = Cr + dC
            Cb = Cb + dC
        if z > 0.0: 
            Cr = Cr + z*thf[l]
        self.Cr = max(self.Ce, Cr)
        self.Cb = Cb - self.Cr
        self.CI = self.ci*L

    def wb_func(self, ts, fl):
        """
        Sets water balance function;
        
        called from self.read_initialize().
        """
        func = {"ed": ts.watbal_ed_step, 
                "evacrop": ts.watbal
                }
        default = "ed"
        
        name = self.wbfunc.lower()
        
        try:
            wbfunc = func[name]
        except:
            print_msg(("Error: wbfunc = %s cannot be recognized. "
                  + "Use \"%s\"!")%(name, default), fl)
            wbfunc = func[default]
            
        return(wbfunc)
        
    def initialize(self, model, sd, cd, ts):
        """
        Initialize model parameter values;
        initialize TimeSeries (ts) list defining output values to be printed;
        uses soil and crop parameter values;
        
        called from self.read_initialize().
        """
        self.modelname = model
        
        # Water balance function
        self.wbfunc = "ed" # or "evacrop"
        self.steps_per_day = 6
#        self.MaxIter = 00 # Used by TimeSeries.watbal_ed_step()
#        self.tol = 0.001 # Used by TimeSeries.watbal_ed_step()
        
        # Drainage function
        dfunc = {"lin": self.Lin_drainage,
                 "mvg": self.MvG_drainage}
        self.drainage_func = dfunc[sd.soil_model]
        self.hydpar = sd.hydpar
        
        # Relative transpiration function
        tfunc =  {"lin": self.Lin_rel_transp,
                  "pow": self.Pow_rel_transp}
        self.rel_transp = tfunc["lin"]

        # Dates of beginning and ending of winter period; the year is 
        # adjusted by set_period() to correspond to beginning of simulation
        dfmt = '%Y%m%d'
        winterperiod = [datetime.strptime('15001031', dfmt),
                        datetime.strptime('15010301', dfmt)]#.date()]
        self.winterperiod = set_period("Winter", winterperiod, 
                                       ts.date[0])#.date())

        self.zx = 1000.           # Max root zone depth and max sub zone depth 
        self.ndz = 4              # Number of depth intervals
        self.dz = self.zx/float(self.ndz) # Interval depth
        self.ci = 0.5             # Capacity constant for interception
        # Root depth:
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            cd.zr = self.zx
        else:
            cd.zr = 0.0
        cd.L = 0.0                # Leaf area
        self.Cu = 0.0             # Upper reservoir capacity
        self.Ce = sd.Ce           # Evaporation reservoir capacity     
        self.Capacities(cd.zr, sd.thf, cd.L) # Root zone, sub zone, and interception capacities
        self.porosity = 0.3
        self.Cr_sat = self.zx * self.porosity
        if cd.crop_type == "WL" or cd.crop_type == "WM":
            self.Cr = self.Cr_sat
        self.Vs = 0.0             # Snow content
        self.Vr = self.Cr         # Root zone content
        self.Vb = self.Cb         # Sub zone content
        self.Ve = self.Ce         # Evaporation reservoir content
        self.Vu = 0.0             # Upper reservoir content
        self.VI = self.CI         # Interception resercoir content
        self.ci = 0.5         # Interception capacity constant
        self.Tm = 0.0         # Threshold temperature for snow melt
        self.cm = 2.0         # Day degree factor for snow melt
        self.ce = 0.15        # Evaporation constant for dry soil
        self.kp = 0.6         # Extinction coefficient
        
        # Irrigation
        # Dates of beginning and ending of irrgation period; the year is 
        # adjusted by set_period() to correspond to beginning of simulation
        irrigationperiod = [datetime.strptime('18000430', dfmt),
                            datetime.strptime('18000901', dfmt)]#.date()]
        self.irrigationperiod = set_period("Irrigation", irrigationperiod, 
                                           ts.date[0])#.date())
        autoirrigationmodel = [ts.irrigationmodel_Aslyng]
        self.irrigationmodel = autoirrigationmodel[0]
        self.irrigationdate = [] # List of dates with forced irrigation
        self.irrigation = 25. # Amount of forced irrigation
        self.autoirrigate = False
        self.tlim = 20 # Do not irrigate less than tlim from crop maturity
        self.tfreq = 5 # Minimum number of days between irrigation
        self.clim = 0.8 # Defines water content below which to irrigate
        self.Plim = 5.  # Only irrigation when three days of precip. < Plim
        self.Imin = 25. # Minimum amount of irrigation
        self.Imax = 35. # Maximum amount of irrigation
        self.irrdaycount = 0 # Count days since last auto irrigation
        
        self.plotseries = False   # Plot option for daily time series
        
        ts.prlist = ["Date", "T", "P", "Ep", "I", "Ea", "Dsum"]
        ts.prlist_y = ["P", "Ep", "I", "Ea", "Dsum"]

    def read_initialize(self, model, mval, sd, cd, ts, fl):
        """
        Initialize model parameter values, in self.initialize(); 
        if specified by parameter key in input dictionary sval, replace 
        default value;
        also initialize or read TimeSeries (ts) list defining output to print;
        
        below datadict is dictionary for model parameters for which it is
        possible to replace default value by input value in mval; its 'key' 
        is case sensitive; its 'value' is a tupple defined in function 
        replace_default_values();
        
        called from run_model().
        """
        
        self.initialize(model, sd, cd, ts)
        
#        if isfile(fname):
        if mval != None:
            msg = "\n Model parameter values:  update from input file."
            print_msg(msg, fl)
            # fl.write("\n  %s"%model)
            print_msg("  %s:"%model, fl)
            print_dump(mval, fl)
            datadict={"Cr":         (self.Cr, "f", 1, (0, np.inf)),
                      "Cb":         (self.Cb, "f", 1, (0, np.inf)),
                      "Cu":         (self.Cu, "f", 1, (0, np.inf)),
                      "Vs":         (self.Vs, "f", 1, (0, np.inf)),
                      "Vr":         (self.Vr, "f", 1, (0, np.inf)),
                      "Vb":         (self.Vb, "f", 1, (0, np.inf)),
                      "Ve":         (self.Ve, "f", 1, (0, np.inf)),
                      "Vu":         (self.Vu, "f", 1, (0, np.inf)),
                      "VI":         (self.VI, "f", 1, (0, np.inf)),
                      "ci":         (self.ci, "f", 1, (0, np.inf)),
                      "Tm":         (self.Tm, "f", 1, (0, np.inf)),
                      "cm":         (self.cm, "f", 1, (0, np.inf)),
                      "ce":         (self.ce, "f", 1, (0, np.inf)),
                      "kp":         (self.kp, "f", 1, (0, np.inf)),
                      "zmax":       (self.zx, "f", 1, (0, np.inf)),
                      "iprnd":      (0, "i", 1, (1,4)),
                      "winterperiod": (self.winterperiod, "d", 2),
                      "irrigationperiod": (self.irrigationperiod, "d", 2),
                      "irrigationdate": (self.irrigationdate, "d", -1),
                      "irrigation": (self.irrigation, "f", 1, (0, np.inf)),
                      "autoirrigate": (self.autoirrigate, "b", 1),
                      "tlim":       (self.tlim,  "i", 1, (0, 366)),
                      "tfreq":      (self.tfreq, "i", 1, (0, 366)),
                      "clim":       (self.clim,  "f", 1, (0., 1.)),
                      "Plim":       (self.Plim,  "f", 1, (0, np.inf)),
                      "Imin":       (self.Imin,  "f", 1, (0, np.inf)),
                      "Imax":       (self.Imax,  "f", 1, (0, np.inf)),
                      "prlistd":    ("", "s", 1),
                      "prlisty":    ("", "s",1),
                      "plotseries": (self.plotseries, "b", 1),
                      "wbfunc":     (self.wbfunc, "s", 1),
                      "stepsperday":(self.steps_per_day,  "i", 1, (1, np.inf))
                      }

            # Read values from file
            update, datadict = replace_default_values(mval, datadict, fl)
            if update:
                self.Cr = datadict["Cr"][0]
                self.Cb = datadict["Cb"][0]
                self.Cu = datadict["Cu"][0]
                self.Vs = datadict["Vs"][0]
                self.Vr = datadict["Vr"][0]
                self.Vb = datadict["Vb"][0]
                self.Ve = datadict["Ve"][0]
                self.Vu = datadict["Vu"][0]
                self.VI = datadict["VI"][0]
                self.ci = datadict["ci"][0]
                self.Tm = datadict["Tm"][0]
                self.cm = datadict["cm"][0]
                self.ce = datadict["ce"][0]
                self.kp = datadict["kp"][0]
                self.zx = datadict["zmax"][0]
                self.dz = self.zx/float(self.ndz) # Interval depth
                winterperiod = datadict["winterperiod"][0]
                self.winterperiod = set_period("Winter", winterperiod,
                                               ts.date[0])#.date())
                irrigationperiod = datadict["irrigationperiod"][0]
                self.irrigationperiod = set_period("Irrigation",
                                            irrigationperiod,ts.date[0])#.date())
                self.irrigationdate = datadict['irrigationdate'][0]
                self.irrigation = datadict['irrigation'][0]
                self.autoirrigate = datadict['autoirrigate'][0]
#                autoirrigate = datadict['autoirrigate'][0]
#                if autoirrigate.lower() == "yes":
#                    self.autoirrigate = True
                self.tlim = datadict["tlim"][0]
                self.tfreq = datadict["tfreq"][0]
                self.clim = datadict["clim"][0]
                self.Plim = datadict["Plim"][0]
                self.Imin = datadict["Imin"][0]
                self.Imax = datadict["Imax"][0]
                self.wbfunc = datadict["wbfunc"][0]
                self.steps_per_day = datadict["stepsperday"][0]
                self.plotseries = datadict["plotseries"][0]
#                plotseries = datadict["plotseries"][0]
#                if plotseries.lower() == "yes":
#                    self.plotseries=True
                iprnd = datadict["iprnd"][0]
                prlistd = datadict["prlistd"][0].split()
                if iprnd == 1:
                    ts.prlist = ["Date","T","P","Ep","I","Ea","Dsum","Qro"]
                elif iprnd == 2:
                    ts.prlist = ["Date","T","P","Ep","I","Ea","Dsum","Qro",
                                 "Eas","Eae","Eai","Eat","Dr", "Db", "Dmp"]
                elif iprnd==3:
                    ts.prlist = ["Date","T","P","Ep","I","Ea","Dsum","Qro",
                                 "Eas","Eae","Eai","Eat","Dr","Db","Dmp","Ps",
                                 "Pr","Pm","Epe","Epcg","Epcy","Ept","Lg","Ly",
                                 "zr","kc","Tsum"]
                elif iprnd==4:
                    ts.prlist = ["Date","T","P","Er","Ep","I","Ea","Dsum",
                                 "Qro","Eas","Eae","Eai","Eaig","Eaiy","Eat",
                                 "Dr","Db","Dmp","Ps","Pr","Pm","Epe","Epc",
                                 "Epcg","Epcy","Ept","L","Lg","Ly","zr","kc",
                                 "Tsum","Cr","Cb","Cu","Vsum","Vdel","Vs","Vr",
                                 "Vb","Ve","Vu","Vi"]
                elif len(prlistd)>0: 
                    # Read string and use names from time series dictionary
                    ts.prlist = ["Date"]
                    for i in range(0, len(prlistd)):
                        try:
                            ts.outdict[prlistd[i]]
                            if prlistd[i] != "Date":
                                ts.prlist.append(prlistd[i])
                        except KeyError:
                            print_msg("  Could not recognize this as "
                                  + "a time series variable for daily print:"
                                  + " %s  -  Ignored"%prlistd[i], fl)
                
                prlisty = datadict["prlisty"][0].split()
                if len(prlisty) > 0:
                    ts.prlist_y = []
                    for i in range(0, len(prlisty)):
                        try:
                            ts.outdict[prlisty[i]]
                            if prlisty[i] != "Date":
                                ts.prlist_y.append(prlisty[i])
                        except KeyError:
                            print_msg(("Could not recognize this as "
                                  + "a time series variable for yearly print:"
                                  + " %s  -  "%prlisty[i]), fl)
                
        else:
            print_msg("\n Model parameter values:  use default.", fl)
            
        # Macropore flow and surface runoff parameters
        self.Kmp = sd.Kmp
        # self.Cmp = sd.thmp * self.dz
        self.Cmp = sd.Cmp
        self.Vmprel = sd.Vmprel
        self.Kro =sd.Kro
            
        # Set water balance function and initialize some parameters
        if self.wbfunc == "ed": # or "evacrop"
            if sd.soil_model == 'lin':
                self.C = np.array(sd.thf*self.dz) # Water content at field capacity
                self.Csat = sd.thsat*self.dz
            elif sd.soil_model == 'mvg':
                self.C = np.array(sd.ths*self.dz) # Water content at saturation
                self.Csat = self.C[0]
            self.V = np.array(sd.thf*self.dz) # As default, wat. cont. at field cap.
            self.Ve = self.V[0]
        self.wbfunc = self.wb_func(ts, fl)
        self.tlim = timedelta(days=int(self.tlim))

"""    
===============================================================================
Various functions used to read input data
===============================================================================
"""

def same_day_and_month(d1, d2):
    """ check if day and month of dates d1 and d2 are identical """
    if d1.day==d2.day and d1.month==d2.month:
        return(True)
    return(False)
    
def set_period(name, period, d0):
    """ 
    period is a list of two dates d1 (beginning) and d2 (end);
    these dates are adjusted so that d2 has same year as input date d0, or
    is a year later; d1 is adjusted by the same number of years.
    """
    d1 = period[0]
    d2 = period[1]
    if d1 > d2:
        msg = name + " period input error: date_1 > date_2"
        raise RuntimeError(msg)
    elif d2 - d1 >= timedelta(days = 365):
        msg = name + " period input error: date_2 - date_1 >= 365 days"
        raise RuntimeError(msg)
    yeardel = d0.year - d2.year
    if d2.replace(year = d2.year + yeardel) < d0:
        yeardel = yeardel + 1
    d1 = d1.replace(year = d1.year + yeardel)
    d2 = d2.replace(year = d2.year + yeardel)
    if isinstance(period, tuple):
        return((d1,d2))
    else:
        return([d1,d2])
    
def add_year(d):
    """ 
    d is a list or tuple with two dates; 
    the dates are increased by a year 
    """
    d0 = d[0].replace(year = d[0].year + 1)
    d1 = d[1].replace(year = d[1].year + 1)
    if isinstance(d,tuple):
        return((d0,d1))
    else:
        return([d0,d1])

def iswinter(d, mp):
    """ 
    checks if date d is within winter period; if d is later than winter period,
    winter period, sow and harvest are made to be a year later.
    """
    if d <= mp.winterperiod[0]:
        return(False)
    elif d < mp.winterperiod[1]:
        return(True)
    mp.winterperiod = add_year(mp.winterperiod)
    [mp.sow, mp.harvest0] = add_year([mp.sow, mp.harvest0])
    mp.harvest = mp.harvest0
    return(False)

def right_instance(inpval, defval, typ, nvar):
    """
    checks whether inpval is same instance as defval;
    typ and nvar is type and number of variables in defval;
    if nvar > 0, number of elements in inpvar must be at least nvar;
    
    returns True or False;
    
    called from replace_default_values().
    """
    
    # For dictionary
    if isinstance(defval,dict):
        if isinstance(inpval,dict):
            for key in inpval:
                if isinstance(inpval[key],(list,np.ndarray)):
                    for val in inpval[key]:
                        if typ == float and type(val) == int:
                            continue
                        elif not isinstance(val, typ):
                            return(False)
                    n = len(inpval[key])
                else:
                    if typ == float and type(val) == int:
                        pass
                    elif not isinstance(val, typ):
                        return(False)
                    n = 1
                if  n < nvar:
                    return(False)
            return(True)
        else:
            return(False)
        
    # For list or numpy array
    elif isinstance(defval,(list, np.ndarray)):
        if len(inpval) < nvar:
            return(False)
        else:
            for val in inpval:
                if typ == float and type(val) == int:
                    continue
                elif not isinstance(val, typ):
                    return(False)
        return(True)
        
    # For single variable
    else:
        if typ == float and type(inpval) == int:
            return(True)
        return(isinstance(inpval, typ))
        
def within_bounds(x,xlim,key,inpval,fl):
    """
    checks if x falls within bounds given by tuple xlim;
    key and inpval are only used to generate error message;
    
    returns True or False;
    
    called from replace_default_values().
    """
    if x < xlim[0] or x > xlim[1]:
        line = "  " + key +": " + str(inpval)
        print_msg("%s"%line, fl)
        print_msg(("  Value, %f, is outside "
              + "min/max-limits = (%f,%f);"
              +" input ignored!")
              %(x,xlim[0],xlim[1]), fl)
        return(False)
    return(True)
    
def date_to_datetime(d):
    return(datetime.combine(d, datetime.min.time()))

def replace_default_values(inpdict, datadict, fl):
    """
    Replace default values with values from input dictionary for either model, 
    soil, or crop;
    inpdict is dictionary of new values previously read from edcrop.py input 
    file; datadict is dictionary of parameters for which read value can be 
    used; datadict is defined in the calling function (see below);
    the 'value' in datadict is a tupple, (variable, type, number, xlim), where 
    allowed 'type's are defined by dictionary fdic below, number > 0 is number
    of values to be read, and the optional xlim is itself a tuple defining
    the minimum and maximum value that is accepted;
    if a key in inpdict does not match a key in datadict, this key and value 
    are ignored (not used);

    returns reply and datadict, where reply = True if at least one 'value' 
    in datadict has been updated;
    
    called from .read_initialize() of either of the classes 
    ModelParameters, SoilParameters, or CropParameters.
    """
    
    fdic = {"i": int, "f": float, "s": str, "b": bool,
            "d": (date,datetime), "df": float, "di": int, "ds": str}
    fnam = {"i": "int()", "f": "float()", "s": "str()", "d": "Date (%Y-%m-%d)",
            "df": "dict. w/ float()", "di": "dict. w/ int()", 
            "ds": "dict. w/ str()", "b": "bool"}
    
    reply = False
    
    for key in inpdict:
        try:
            inpval = inpdict[key]
            defval = datadict[key][0]
            typ = datadict[key][1]
            func = fdic[typ]
            ftyp = fnam[typ]
            nvar = datadict[key][2]
            # Check for right instance, then update
            if right_instance(inpval, defval, func, nvar):
                # Bounds on valukeyes
                if len(datadict[key]) == 4:
                    lim = True
                    xlim = datadict[key][3]
                else:
                    lim = False

                if isinstance(defval,dict):
                    for key2 in inpval:
                        inplst = inpval[key2]
                        if nvar < 1:
                            n = len(inplst)
                        else:
                            n = nvar
                        update = True
                        for i in range(0,n):
                            if not isinstance(inplst[i], (date,datetime)):
                                inplst[i] = func(inplst[i])
                            elif not isinstance(inplst[i], datetime):
                                inplst[i] = date_to_datetime(inpval[i])
                            if lim and not within_bounds(inplst[i],xlim,key,inpval,fl):
                                update = False
                                break
                        if update:
                            if func == float or func == int:
                                defval[key2] = np.array(inplst[0:n], dtype=func)
                            else:
                                defval[key2] = inplst[0:n]

                elif isinstance(defval,(list,np.ndarray)):
                    if nvar < 1:
                        n = len(inpval)
                    else:
                        n = nvar
                    update = True
                    for i in range(0,n):
                        if not isinstance(inpval[i], (date,datetime)):
                            inpval[i] = func(inpval[i])
                        elif not isinstance(inpval[i], datetime):
                            inpval[i] = date_to_datetime(inpval[i])
                        if lim and not within_bounds(inpval[i],xlim,key,inpval,fl):
                            update = False
                            break
                    if update:
                        inpval = inpval[0:n]
                        if func == float or func == int:
                            inpval = np.array(inpval, dtype=func)

                else:
                    if not isinstance(inpval,(date,datetime)):
                        inpval = func(inpval)
                    elif not isinstance(inpval, datetime):
                        inpval = date_to_datetime(inpval)
                    update = True
                    if lim and not within_bounds(inpval,xlim,key,inpval,fl):
                        update = False
                        break
               
                if update:
                    if isinstance(defval,dict):
                        datadict[key] = (defval,typ,nvar)
                    else:
                        datadict[key] = (inpval,typ,nvar)
                    reply = True
                continue
            else:
                line = "  " + key +": " + str(inpval)
                print_msg("%s"%line, fl)
                print_msg("  Input not of right type, %s; input ignored!"%ftyp,
                          fl)
                if nvar > 1:
                    print_msg(("  Number of elements in list or array should"
                               " be %d; input ignored!"%nvar), fl)
        except:
            line = "  " + key +": " + str(inpval)
            print_msg("%s"%line, fl)
            print_msg("  Unknown variable name: %s; input ignored!"%key, fl)
                
    return(reply, datadict)

    
def print_msg(msg, fl):
    """ prints msg on screen and in log file """
    print(msg)
    fl.write("\n"+msg)
    
def print_dump(val, fl):
    msg = (yml.dump(val, indent=2, width=120)).split('\n')
    for i in range(0,len(msg)):
        print_msg("    "+msg[i], fl)

def mandatory_inp_docs(docs, fl):
    """
    checks that docs contains three proper blocks (dictionaries), i.e. that
    are not empty; the blocks are in this order for Crops, Soils,
    and Climates, respectively;
    
    returns True or False;
    
    called from run_model().
    """
    
    name = ['Crops', 'Soils', 'Climates']
    alldocs = True
    i = -1
    for doc in docs:
        i += 1
        if doc == None or len(doc) < 1:
            line = ("  Error!  No \"%s\" document specified in input file" +
                    " - simulation will fail!")%name[i]
            print_msg("%s"%line, fl)
            alldocs = False
    if alldocs:
        print_msg("Loop through simulations.", fl)
    return(alldocs)

def read_yaml_file(fname,fi,fl):
    """
    Reads YAML input file; only stores information contained in blocks
    named 'Models', 'Crops', 'Soils', and 'Climates'; each block contains
    input information for model setups, crops, soils, and climate data sets,
    respectively, that simulation is going to loop through;
    
    it is ok that the file does not contain a 'Models' block in which 
    case simulation will use the default model set up;
    
    returns block (dictionary) for Models, Crops, Soils and Climates, 
    respectively;
    
    called from run_model().
    """

    models = {'Default': None}
    soils = {}
    crops = {}
    climates = {}
    
    print_msg("Read input file %s."%fname,fl)
    try:
        data = yml.load_all(fi, Loader=yml.FullLoader)
    except:
        print_msg("Error: Cannot load yaml input file: %s"
                  %fname, fl)
        return(False, models, soils, crops, climates)
    
    for doc in data:
        for key, value in doc.items():
            if key == 'Models':
                models = value
            elif key == 'Crops':
                crops = value
            elif key == 'Soils':
                soils = value
            elif key == 'Climates':
                climates = value
            else:
                msg = "  Unknown input block name: %s; input ignored!"%key
                print_msg(msg,fl)
    print_msg("",fl)
    return(True, models, soils, crops, climates)
    
def run_model(yaml='edcrop.yaml', log='edcrop.log'):
    """
    Initializes and runs edcrop by looping through reading input, 
    running model, and (if instructed to) plotting results.
    Keyword arguments:
    yaml is the name of the YAML input file (default is 'edcrop.yaml')
    log  is the name of the log file (default is 'edcrop.log')
    """
#    from .version import __version__
#    from version import __version__
    from edcrop import version
    __version__ = version.__version__
    
    try:
        fl = open(log,'w') # Log file
    except:
        print("Error: Cannot open logfile: %s"%log, fl)
        return
    try:
        fi = open(yaml,'r')
    except:
        print_msg("Error: Cannot open yaml input file: %s"
                  %yaml, fl)
        return

    print_msg("\nRunning edcrop version %s\n"%__version__, fl)
    
    # Read input file
    bool, models, soils, crops, climates = read_yaml_file(yaml,fi,fl)
    if not bool:
        return
    
    ts = TimeSeries()
    sd = SoilParameters()
    cd = CropParameters()
    mp = ModelParameters()
    
    # Check for mandatory inputs
    if mandatory_inp_docs((models, soils, crops, climates), fl):
        # Loop through all combinations of model, crop, soil, and climate
        for clim in climates:
            if not ts.read(clim, climates[clim], fl):
                continue
            for soil in soils:
                if not sd.read_initialize(soil, soils[soil], fl):
                    continue
                for crop in crops:
                    if not cd.read_initialize(crop, crops[crop], ts, 
                                              sd, fl):
                        continue
                    for model in models:
                        ts.initialize() # Initialize time series variables
                        # Set up model amd set model parameter values
                        mp.read_initialize(model, models[model],sd,cd,ts,fl)
                        msg = ("===> Run " + clim + "_" + soil + "_" + crop + 
                               "_" + model + "\n")
                        print_msg(msg, fl)
    
                        ts.plant_growth(cd, mp) # Time series for plant growth
                        
                        if mp.autoirrigate: # Set first period of automatic irrig.
                            cd.actualirr_per = cd.autoirr_period[0]
            
                        ts.forced_irrigation(mp) # Time series for forced irrigation
                        
                        # Loop to compute time series for daily water balance
                        for i in range(0,ts.nd): 
                            month = ts.date[i].month - 1
                            cb = cd.cb[month]
                            mp.wbfunc(mp, sd.thf, cb, sd.kqr, sd.kqb, cd, 
                                      i)
            
                        # Write and plot output
                        begin_name = (clim + "_" + soil + "_" + crop + "_"
                                      + model)
                        ts.print_from_dictionary(begin_name)
                        if mp.plotseries:
                            ts.plot_time_series(sd.soilname, cd.cropname, 
                                                begin_name)
    fl.close() # Close log file
