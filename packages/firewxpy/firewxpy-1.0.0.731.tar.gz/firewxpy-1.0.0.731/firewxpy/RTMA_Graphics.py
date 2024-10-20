import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import metpy.plots as mpplots
import metpy.calc as mpcalc
import numpy as np
import firewxpy.parsers as parsers
import firewxpy.geometry as geometry
import firewxpy.colormaps as colormaps
import pandas as pd
import matplotlib.gridspec as gridspec
import firewxpy.settings as settings
import firewxpy.standard as standard
import firewxpy.dims as dims


from matplotlib.patheffects import withStroke
from metpy.plots import USCOUNTIES
from datetime import datetime, timedelta
from dateutil import tz
from firewxpy.calc import scaling, Thermodynamics, unit_conversion
from firewxpy.utilities import file_functions
from metpy.units import units
from firewxpy.data_access import RTMA_CONUS

mpl.rcParams['font.weight'] = 'bold'

mpl.rcParams['font.weight'] = 'bold'

def plot_relative_humidity(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    contourf = np.arange(0, 101, 1)
    if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
        contours = [0, 10, 20, 30, 40, 60, 80, 100]
        linewidths = 1
        clabel_fontsize = 12
    else:
        contours = np.arange(0, 110, 10)
        linewidths = 0.5

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)
            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.relative_humidity_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            print("Unpacked the data successfully!")
            
        except Exception as e:

            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
            
            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
                
                rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                            
                print("Unpacked the data successfully!")

            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Relative Humidity (%)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, rtma_data[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        rtma_data = rtma_data[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', rtma_data, color='blue', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA RH', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA RH')


def plot_low_and_high_relative_humidity(low_rh_threshold=15, high_rh_threshold=80, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9, x1=None, x2=None, y=None, x_size=None, colorbar_fontsize=None, labels_low_increment=None, labels_high_increment=None):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    low_rh_thresh = low_rh_threshold + 1


    contourf_low = np.arange(0, low_rh_thresh, 1)
    contourf_high = np.arange(high_rh_threshold, 101, 1)
    
    if low_rh_threshold <= 15:
        labels_low = contourf_low
    elif low_rh_threshold > 15 and low_rh_threshold < 40:
        if (low_rh_threshold % 2) == 0:
            labels_low = contourf_low[::2]
        else:
            labels_low = contourf_low[::5]
    else:
        labels_low = contourf_low[::5]

    if high_rh_threshold >= 80:
        labels_high = contourf_high
    elif high_rh_threshold >= 60 and high_rh_threshold < 80:
        if (high_rh_threshold % 2) == 0:
            labels_high = contourf_high[::4]
        else:
            labels_high = contourf_high[::5]
    else:
        labels_high = contourf_high[::5]


    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, 'Low and High RH')
            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        x1, x2, y, x_size, colorbar_fontsize = dims.get_colorbar_coords(state, gacc_region)


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, 'Low and High RH')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        x1, x2, y, x_size, colorbar_fontsize = dims.get_colorbar_coords(state, gacc_region)


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        x1 = x1 
        x2 = x2
        y = y
        x_size = x_size
        colorbar_fontsize = colorbar_fontsize
        labels_low = contourf_low[::labels_low_increment]
        labels_high = contourf_high[::labels_high_increment]
    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap_low = colormaps.low_relative_humidity_colormap()
    cmap_high = colormaps.excellent_recovery_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            print("Unpacked the data successfully!")
            
        except Exception as e:

            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
            
            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
                
                rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                            
                print("Unpacked the data successfully!")

            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Low and High Relative Humidity\n[RH <= "+str(low_rh_threshold)+" (%) & RH >= "+str(high_rh_threshold)+" (%)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    if x_size <= 0.25:
        labels_low = contourf_low[::5]
        labels_high = contourf_high[::5]
    else:
        labels_low = labels_low
        labels_high = labels_high

    x_cbar_0, y_cbar_0, x_cbar_size, y_cbar_size = x1, y, x_size, 0.02
    x_cbar2_0, y_cbar2_0, x_cbar2_size, y_cbar2_size = x2, y, x_size, 0.02
    
    cs_low = ax.contourf(lon, lat, rtma_data[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf_low, cmap=cmap_low, alpha=alpha, zorder=2)

    cs_high = ax.contourf(lon, lat, rtma_data[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf_high, cmap=cmap_high, alpha=alpha, zorder=2)

    ax_cbar = plt.gcf().add_axes([x_cbar_0, y_cbar_0, x_cbar_size, y_cbar_size])
    ax_cbar_2 = plt.gcf().add_axes([x_cbar2_0, y_cbar2_0, x_cbar2_size, y_cbar2_size])
    cbar_low = plt.gcf().colorbar(cs_low, cax=ax_cbar, orientation='horizontal',
     label='Low Relative Humidity (%)', pad=0.01, ticks=labels_low)
    cbar_high = plt.gcf().colorbar(cs_high, cax=ax_cbar_2, orientation='horizontal',
     label='High Relative Humidity (%)', pad=0.01, ticks=labels_high)

    cbar_low.set_label(label="Low Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    cbar_high.set_label(label="High Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        rtma_data = rtma_data[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', rtma_data, color='blue', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA LOW AND HIGH RH', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA LOW AND HIGH RH')

def plot_24_hour_relative_humidity_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-50, 51, 1)

    linewidths = 1

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour RH Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, '24 Hour RH Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.relative_humidity_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15

            temp_24 = ds_24['tmp2m']
            dwpt_24 = ds_24['dpt2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = temp_24 - 273.15
            dwpt_24 = dwpt_24 - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            rtma_data_24 = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp_24, dwpt_24)

            diff = rtma_data[0, :, :] - rtma_data_24[0, :, :]
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24
    
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
    
            temp_24 = ds_24['tmp2m']
            dwpt_24 = ds_24['dpt2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = temp_24 - 273.15
            dwpt_24 = dwpt_24 - 273.15
            
            rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            rtma_data_24 = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp_24, dwpt_24)
    
            diff = rtma_data[0, :, :] - rtma_data_24[0, :, :]

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
    
                temp_24 = ds_24['tmp2m']
                dwpt_24 = ds_24['dpt2m']
                lat_24 = ds_24['lat']
                lon_24 = ds_24['lon']
                temp_24 = temp_24 - 273.15
                dwpt_24 = dwpt_24 - 273.15
                
                rtma_data = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                rtma_data_24 = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp_24, dwpt_24)
    
                diff = rtma_data[0, :, :] - rtma_data_24[0, :, :]
                            
                print("Unpacked the data successfully!")

            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA 24-Hour Relative Humidity Comparison (Δ%)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        diff = diff[::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', diff, color='blue', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Relative Humidity Trend (Δ%)", size=colorbar_fontsize, fontweight='bold')

    path, gif_path = file_functions.check_file_paths(state, gacc_region, '24HR RTMA RH COMPARISON', reference_system)
    file_functions.update_images(fig, path, gif_path, '24HR RTMA RH COMPARISON')


def plot_temperature(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    if month >= 5 and month <= 9:
        contourf = np.arange(30, 111, 1)
    if month == 4 or month == 10:
        contourf = np.arange(10, 91, 1)
    if month >= 11 or month <= 3:
        contourf = np.arange(-10, 71, 1)

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)


        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.temperature_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")   

            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Temperature (\N{DEGREE SIGN}F)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, temp[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Temperature (\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        temp = temp[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', temp, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA TEMPERATURE', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA TEMPERATURE')


def plot_temperature_advection(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(-20, 21, 1)

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.temperature_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            lat = ds['lat']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")

            except Exception as e:
                pass
                
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Temperature Advection [\N{DEGREE SIGN}F/Hour]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    dx = units('meters') * 2500
    dy = units('meters') * 2500
    temp = units('degF') * temp
    u = units('m/s') * u
    v = units('m/s') * v

    advection = mpcalc.advection(temp[0, :, :], u[0, :, :], v[0, :, :], dx=dx, dy=dy)

    advection = advection * 3600

    cs = ax.contourf(lon, lat, advection[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Temperature Advection (\N{DEGREE SIGN}F/Hour)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize


    stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                 transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)

    stn.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='darkgreen', label=rtma_time.strftime('%m/%d %H:00'), alpha=1, zorder=9, linewidth=2)


    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA TEMPERATURE ADVECTION', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA TEMPERATURE ADVECTION')


def plot_dew_point_advection(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(-20, 21, 1)

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)


        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.dew_point_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['dpt2m']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['dpt2m']
            lat = ds['lat']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['dpt2m']
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
                 
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Dew Point Advection [\N{DEGREE SIGN}F/Hour]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    dx = units('meters') * 2500
    dy = units('meters') * 2500
    temp = units('degF') * temp
    u = units('m/s') * u
    v = units('m/s') * v

    advection = mpcalc.advection(temp[0, :, :], u[0, :, :], v[0, :, :], dx=dx, dy=dy)

    advection = advection * 3600

    cs = ax.contourf(lon, lat, advection[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Dew Point Advection (\N{DEGREE SIGN}F/Hour)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize


    stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                 transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)

    stn.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='darkred', label=rtma_time.strftime('%m/%d %H:00'), alpha=1, zorder=9, linewidth=2)

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA DEW POINT ADVECTION', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA DEW POINT ADVECTION')


def plot_relative_humidity_advection(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(-30, 31, 1)

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.relative_humidity_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lat = ds['lat']
            lon = ds['lon']
      
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            lat = ds['lat']
            lon = ds['lon']
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
                rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                lat = ds['lat']
                lon = ds['lon']
    
                print("Unpacked the data successfully!")

            except Exception as e:
                pass

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Relative Humidity Advection [%/Hour]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    dx = units('meters') * 2500
    dy = units('meters') * 2500
    rh = units('percent') * rh
    u = units('m/s') * u
    v = units('m/s') * v

    advection = mpcalc.advection(rh[0, :, :], u[0, :, :], v[0, :, :], dx=dx, dy=dy)

    advection = advection * 3600

    cs = ax.contourf(lon, lat, advection[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Relative Humidity Advection (%/Hour)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                 transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)

    stn.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='blue', label=rtma_time.strftime('%m/%d %H:00'), alpha=1, zorder=9, linewidth=2)
    
    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA RH ADVECTION', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA RH ADVECTION')

def plot_frost_freeze(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(-10, 33, 1)

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.cool_temperatures_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Frost Freeze Areas\n[Temperature <= 32 (\N{DEGREE SIGN}F)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, temp[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='min', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Temperature (\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        temp = temp[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', temp, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA FROST FREEZE', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA FROST FREEZE')

def plot_extreme_heat(temperature_threshold=100, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(temperature_threshold, 121, 1)

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.cool_temperatures_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Extreme Heat Areas\n[Temperature >= "+str(temperature_threshold)+" (\N{DEGREE SIGN}F)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, temp[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap='hot', alpha=alpha, extend='max', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Temperature (\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        temp = temp[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', temp, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA EXTREME HEAT', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA EXTREME HEAT')

def plot_24_hour_temperature_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-25, 26, 1)

    linewidths = 1

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour Temperature Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.temperature_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)

            temp_24 = ds_24['tmp2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp_24)

            diff = temp[0, :, :] - temp_24[0, :, :]
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24

            temp = ds['tmp2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15

            temp_24 = ds_24['tmp2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = temp_24 - 273.15

            diff = temp[0, :, :] - temp_24[0, :, :]

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                temp = ds['tmp2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
    
                temp_24 = ds_24['tmp2m']
                lat_24 = ds_24['lat']
                lon_24 = ds_24['lon']
                temp_24 = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp_24)
    
                diff = temp[0, :, :] - temp_24[0, :, :]
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA 24-Hour Temperature Comparison (Δ\N{DEGREE SIGN}F)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        diff = diff[::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', diff, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Temperature Trend (Δ\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    path, gif_path = file_functions.check_file_paths(state, gacc_region, '24HR RTMA TEMPERATURE COMPARISON', reference_system)
    file_functions.update_images(fig, path, gif_path, '24HR RTMA TEMPERATURE COMPARISON')

def plot_dew_point(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    if month >= 5 and month <= 9:
        contourf = np.arange(10, 71, 1)
    if month == 4 or month == 10:
        contourf = np.arange(0, 61, 1)
    if month >= 11 or month <= 3:
        contourf = np.arange(-10, 51, 1)

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.dew_point_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            temp = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['dpt2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Dew Point (\N{DEGREE SIGN}F)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, temp[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Dew Point (\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        temp = temp[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', temp, color='darkred', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA DEW POINT', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA DEW POINT')

def plot_24_hour_dew_point_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-25, 26, 1)

    linewidths = 1

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour Dewpoint Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.dew_point_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            temp = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)

            temp_24 = ds_24['dpt2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp_24)

            diff = temp[0, :, :] - temp_24[0, :, :]
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24

            temp = ds['dpt2m']
            lat = ds['lat']
            lon = ds['lon']
            temp = temp - 273.15

            temp_24 = ds_24['dpt2m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            temp_24 = temp_24 - 273.15

            diff = temp[0, :, :] - temp_24[0, :, :]

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                temp = ds['dpt2m']
                lat = ds['lat']
                lon = ds['lon']
                temp = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp)
    
                temp_24 = ds_24['dpt2m']
                lat_24 = ds_24['lat']
                lon_24 = ds_24['lon']
                temp_24 = unit_conversion.Temperature_Data_or_Dewpoint_Data_Kelvin_to_Fahrenheit(temp_24)
    
                diff = temp[0, :, :] - temp_24[0, :, :]
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA 24-Hour Dew Point Comparison (Δ\N{DEGREE SIGN}F)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        diff = diff[::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', diff, color='darkred', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Dew Point Trend (Δ\N{DEGREE SIGN}F)", size=colorbar_fontsize, fontweight='bold')

    path, gif_path = file_functions.check_file_paths(state, gacc_region, '24HR RTMA DEW POINT COMPARISON', reference_system)
    file_functions.update_images(fig, path, gif_path, '24HR RTMA DEW POINT COMPARISON')

def plot_total_cloud_cover(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(0, 101, 1)

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.cloud_cover_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            lat = ds['lat']
            lon = ds['lon']
            tcdcclm = ds['tcdcclm']
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            tcdcclm = ds['tcdcclm']
            lat = ds['lat']
            lon = ds['lon']
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                lat = ds['lat']
                lon = ds['lon']
                tcdcclm = ds['tcdcclm']
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Total Cloud Cover (% Of Sky)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, tcdcclm[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Total Cloud Cover (% Of Sky)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        tcdcclm = tcdcclm[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', tcdcclm, color='red', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA TOTAL CLOUD COVER', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA TOTAL CLOUD COVER')

def plot_24_hour_total_cloud_cover_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-60, 61, 1)

    linewidths = 1

    labels = contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour Total Cloud Cover Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.cloud_cover_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            tcdcclm= ds['tcdcclm']
            lat = ds['lat']
            lon = ds['lon']

            tcdcclm_24 = ds_24['tcdcclm']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']

            diff = tcdcclm[0, :, :] - tcdcclm_24[0, :, :]
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24

            tcdcclm= ds['tcdcclm']
            lat = ds['lat']
            lon = ds['lon']

            tcdcclm_24 = ds_24['tcdcclm']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']

            diff = tcdcclm[0, :, :] - tcdcclm_24[0, :, :]

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                tcdcclm= ds['tcdcclm']
                lat = ds['lat']
                lon = ds['lon']
    
                tcdcclm_24 = ds_24['tcdcclm']
                lat_24 = ds_24['lat']
                lon_24 = ds_24['lon']
    
                diff = tcdcclm[0, :, :] - tcdcclm_24[0, :, :]
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA 24-Hour Total Cloud Cover Comparison (Δ% Of Sky)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        diff = diff[::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', diff, color='red', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Total Cloud Cover Trend (Δ% Of Sky)", size=colorbar_fontsize, fontweight='bold')

    path, gif_path = file_functions.check_file_paths(state, gacc_region, '24HR RTMA TOTAL CLOUD COVER COMPARISON', reference_system)
    file_functions.update_images(fig, path, gif_path, '24HR RTMA TOTAL CLOUD COVER COMPARISON')


def plot_wind_speed(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(0, 61, 1)

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            lat = ds['lat']
            lon = ds['lon']
            ws = ds['wind10m']
            ws = unit_conversion.meters_per_second_to_mph(ws)
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            ws = ds['wind10m']
            lat = ds['lat']
            lon = ds['lon']
            ws = unit_conversion.meters_per_second_to_mph(ws)
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                lat = ds['lat']
                lon = ds['lon']
                ws = ds['wind10m']
                ws = unit_conversion.meters_per_second_to_mph(ws)
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Wind Speed (MPH)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, ws[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='max', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Speed (MPH)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        ws = ws[0, ::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', ws, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA WIND SPEED', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA WIND SPEED')

def plot_24_hour_wind_speed_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-20, 21, 1)

    linewidths = 1

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour Wind Speed Comparison')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            ws = ds['wind10m']
            lat = ds['lat']
            lon = ds['lon']
            ws = unit_conversion.meters_per_second_to_mph(ws)

            ws_24 = ds_24['wind10m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)

            diff = ws[0, :, :] - ws_24[0, :, :]
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24

            ws = ds['wind10m']
            lat = ds['lat']
            lon = ds['lon']
            ws = unit_conversion.meters_per_second_to_mph(ws)

            ws_24 = ds_24['wind10m']
            lat_24 = ds_24['lat']
            lon_24 = ds_24['lon']
            ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)

            diff = ws[0, :, :] - ws_24[0, :, :]

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                ws = ds['wind10m']
                lat = ds['lat']
                lon = ds['lon']
                ws = unit_conversion.meters_per_second_to_mph(ws)
    
                ws_24 = ds_24['wind10m']
                lat_24 = ds_24['lat']
                lon_24 = ds_24['lon']
                ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)
    
                diff = ws[0, :, :] - ws_24[0, :, :]
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Wind Speed Comparison (ΔMPH)", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    plot_lon, plot_lat = np.meshgrid(lon[::decimate], lat[::decimate])

    if show_sample_points == True:

        stn = mpplots.StationPlot(ax, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        diff = diff[::decimate, ::decimate].to_numpy().flatten()
    
        stn.plot_parameter('C', diff, color='darkred', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Speed Difference (ΔMPH)", size=colorbar_fontsize, fontweight='bold')

    path, gif_path = file_functions.check_file_paths(state, gacc_region, '24HR RTMA WIND SPEED COMPARISON', reference_system)
    file_functions.update_images(fig, path, gif_path, '24HR RTMA WIND SPEED COMPARISON')


def plot_wind_speed_and_direction(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, barbs_or_quivers='barbs', barb_quiver_alpha=1, barb_quiver_fontsize=7, barb_linewidth=1, quiver_linewidth=0.5, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if barbs_or_quivers == 'barbs' or barbs_or_quivers == 'Barbs' or barbs_or_quivers == 'BARBS' or barbs_or_quivers == 'B' or barbs_or_quivers == 'b':

        barbs = True

    if barbs_or_quivers == 'quivers' or barbs_or_quivers == 'Quivers' or barbs_or_quivers == 'QUIVERS' or barbs_or_quivers == 'Q' or barbs_or_quivers == 'q':

        barbs = False

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    local_time, utc_time = standard.plot_creation_time()

    month = utc_time.month

    contourf = np.arange(0, 61, 1)

    labels = contourf[::4]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            ws = ds['wind10m']
            lon = ds['lon']
            lat = ds['lat']
            ws = unit_conversion.meters_per_second_to_mph(ws)
            lon_2d, lat_2d = np.meshgrid(lon, lat)
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)    
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time

            u = ds['ugrd10m']
            v = ds['vgrd10m']
            ws = ds['wind10m']
            lon = ds['lon']
            lat = ds['lat']
            ws = unit_conversion.meters_per_second_to_mph(ws)
            lon_2d, lat_2d = np.meshgrid(lon, lat)
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)         
            
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                ws = ds['wind10m']
                lon = ds['lon']
                lat = ds['lat']
                ws = unit_conversion.meters_per_second_to_mph(ws)
                lon_2d, lat_2d = np.meshgrid(lon, lat)
                u = unit_conversion.meters_per_second_to_mph(u)
                v = unit_conversion.meters_per_second_to_mph(v)    
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.patch.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    if barbs == True:
    
        plt.title("RTMA Wind Speed & Direction\n[MPH (Shaded) + Wind Barbs]", fontsize=title_fontsize, fontweight='bold', loc='left')

    if barbs == False:

        plt.title("RTMA Wind Speed & Direction\n[MPH (Shaded) + Wind Vectors]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, ws[0, :, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='max', zorder=2)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Speed (MPH)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    if barbs == True:

        stn = mpplots.StationPlot(ax, lon_2d[::decimate, ::decimate], lat_2d[::decimate, ::decimate],
                         transform=ccrs.PlateCarree(), zorder=9, fontsize=barb_quiver_fontsize, clip_on=True)

        stn.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='lime', label=rtma_time.strftime('%m/%d %H:00'), alpha=barb_quiver_alpha, zorder=9, linewidth=barb_linewidth)

        file_name_end = ' WIND BARBS'

    if barbs == False:

        minshaft, headlength, headwidth = dims.get_quiver_dims(state, gacc_region)

        ax.quiver(lon_2d[::decimate, ::decimate], lat_2d[::decimate, ::decimate], u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='lime', minshaft=minshaft, headlength=headlength, headwidth=headwidth, alpha=barb_quiver_alpha, label=rtma_time.strftime('%m/%d %H:00'), zorder=9, linewidth=quiver_linewidth, transform=ccrs.PlateCarree())

        file_name_end = ' WIND VECTORS'

    fname = 'RTMA WIND SPEED & DIRECTION'+ file_name_end

    path, gif_path = file_functions.check_file_paths(state, gacc_region, fname, reference_system)
    file_functions.update_images(fig, path, gif_path, fname)

def plot_24_hour_wind_speed_and_direction_comparison(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', alpha=0.5, data=None, data_24=None, time=None, time_24=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, barbs_or_quivers='barbs', barb_quiver_alpha=1, barb_quiver_fontsize=6, barb_linewidth=0.5, quiver_linewidth=0.5, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    data_24 = data_24
    time_24 = time_24
    state = state
    gacc_region = gacc_region

    if gacc_region != None:
        state = None
    else:
        state = state

    if gacc_region == 'OSCC' or gacc_region == 'oscc' or gacc_region == 'SOPS' or gacc_region == 'sops' or gacc_region == 'RMCC' or gacc_region == 'rmcc' or gacc_region == 'RM' or gacc_region == 'rm':
        if barb_quiver_fontsize <= 6:
            barb_quiver_fontsize = 8
    else:
        pass


    if barbs_or_quivers == 'barbs' or barbs_or_quivers == 'Barbs' or barbs_or_quivers == 'BARBS' or barbs_or_quivers == 'B' or barbs_or_quivers == 'b':

        barbs = True

    if barbs_or_quivers == 'quivers' or barbs_or_quivers == 'Quivers' or barbs_or_quivers == 'QUIVERS' or barbs_or_quivers == 'Q' or barbs_or_quivers == 'q':

        barbs = False


    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    contourf = np.arange(-20, 21, 1)

    linewidths = 1

    labels = contourf[::2]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, '24 Hour Wind Speed & Direction Comparison')


        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_change_colormap()

    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False

    if test == True and time == None:
        
        try:
            ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            u_24 = ds_24['ugrd10m']
            v_24 = ds_24['vgrd10m']
            ws = ds['wind10m']
            ws_24 = ds_24['wind10m']
            lon = ds['lon']
            lat = ds['lat']
            lon_24 = ds_24['lon']
            lat_24 = ds_24['lat']
            ws = unit_conversion.meters_per_second_to_mph(ws)
            ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)
            diff = ws[0, :, :] - ws_24[0, :, :]
            lon_2d, lat_2d = np.meshgrid(lon, lat)
            lon_24_2d, lat_24_2d = np.meshgrid(lon_24, lat_24)
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)
            u_24 = unit_conversion.meters_per_second_to_mph(u_24)
            v_24 = unit_conversion.meters_per_second_to_mph(v_24)            
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            ds_24 = data_24
            rtma_time_24 = time_24

            u = ds['ugrd10m']
            v = ds['vgrd10m']
            u_24 = ds_24['ugrd10m']
            v_24 = ds_24['vgrd10m']
            ws = ds['wind10m']
            ws_24 = ds_24['wind10m']
            lon = ds['lon']
            lat = ds['lat']
            lon_24 = ds_24['lon']
            lat_24 = ds_24['lat']
            ws = unit_conversion.meters_per_second_to_mph(ws)
            ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)
            diff = ws[0, :, :] - ws_24[0, :, :]
            lon_2d, lat_2d = np.meshgrid(lon, lat)
            lon_24_2d, lat_24_2d = np.meshgrid(lon_24, lat_24)
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)
            u_24 = unit_conversion.meters_per_second_to_mph(u_24)
            v_24 = unit_conversion.meters_per_second_to_mph(v_24)     

            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, ds_24, rtma_time, rtma_time_24 = RTMA_CONUS.get_RTMA_24_hour_comparison_datasets(utc_time)
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                u_24 = ds_24['ugrd10m']
                v_24 = ds_24['vgrd10m']
                ws = ds['wind10m']
                ws_24 = ds_24['wind10m']
                lon = ds['lon']
                lat = ds['lat']
                lon_24 = ds_24['lon']
                lat_24 = ds_24['lat']
                ws = unit_conversion.meters_per_second_to_mph(ws)
                ws_24 = unit_conversion.meters_per_second_to_mph(ws_24)
                diff = ws[0, :, :] - ws_24[0, :, :]
                lon_2d, lat_2d = np.meshgrid(lon, lat)
                lon_24_2d, lat_24_2d = np.meshgrid(lon_24, lat_24)
                u = unit_conversion.meters_per_second_to_mph(u)
                v = unit_conversion.meters_per_second_to_mph(v)
                u_24 = unit_conversion.meters_per_second_to_mph(u_24)
                v_24 = unit_conversion.meters_per_second_to_mph(v_24)            
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    
    rtma_time_24 = rtma_time_24.replace(tzinfo=from_zone)
    rtma_time_24 = rtma_time_24.astimezone(to_zone)
    rtma_time_utc_24 = rtma_time_24.astimezone(from_zone)   

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.patch.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    if barbs == True:
    
        plt.title("RTMA Wind Speed & Direction Comparison\n[ΔMPH (Shaded) + Wind Barbs]", fontsize=title_fontsize, fontweight='bold', loc='left')

    if barbs == False:

        plt.title("RTMA Wind Speed & Direction Comparison\n[ΔMPH (Shaded) + Wind Vectors]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Current: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")\n[Current - 24HRS]: " + rtma_time_24.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc_24.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    cs = ax.contourf(lon, lat, diff[:, :], 
                     transform=ccrs.PlateCarree(), levels=contourf, cmap=cmap, alpha=alpha, extend='both', zorder=2)

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    if barbs == True:

        stn = mpplots.StationPlot(ax, lon_2d[::decimate, ::decimate], lat_2d[::decimate, ::decimate],
                         transform=ccrs.PlateCarree(), zorder=9, fontsize=barb_quiver_fontsize, clip_on=True)
    
        stn1 = mpplots.StationPlot(ax, lon_24_2d[::decimate, ::decimate], lat_24_2d[::decimate, ::decimate],
                         transform=ccrs.PlateCarree(), zorder=9, fontsize=barb_quiver_fontsize, clip_on=True)

        stn.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='red', label=rtma_time.strftime('%m/%d %H:00'), alpha=barb_quiver_alpha, zorder=9, linewidth=barb_linewidth)

        stn1.plot_barb(u_24[0, :, :][::decimate, ::decimate], v_24[0, :, :][::decimate, ::decimate], color='blue', label=rtma_time_24.strftime('%m/%d %H:00'), alpha=barb_quiver_alpha, zorder=9, linewidth=barb_linewidth)

        file_name_end = ' WIND BARBS'

    if barbs == False:

        minshaft, headlength, headwidth = dims.get_quiver_dims(state, gacc_region)

        ax.quiver(lon_2d[::decimate, ::decimate], lat_2d[::decimate, ::decimate], u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='red', minshaft=minshaft, headlength=headlength, headwidth=headwidth, alpha=barb_quiver_alpha, label=rtma_time.strftime('%m/%d %H:00'), zorder=9, linewidth=quiver_linewidth, transform=ccrs.PlateCarree())
    
        ax.quiver(lon_24_2d[::decimate, ::decimate], lat_24_2d[::decimate, ::decimate], u_24[0, :, :][::decimate, ::decimate], v_24[0, :, :][::decimate, ::decimate], color='blue', minshaft=minshaft, headlength=headlength, headwidth=headwidth, alpha=barb_quiver_alpha, label=rtma_time_24.strftime('%m/%d %H:00'), zorder=9, linewidth=quiver_linewidth, transform=ccrs.PlateCarree())

        file_name_end = ' WIND VECTORS'

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Speed Difference (ΔMPH)", size=colorbar_fontsize, fontweight='bold')

    x_loc, y_loc = dims.get_label_coords(state, gacc_region)
    
    leg = ax.legend(loc=(x_loc, y_loc), framealpha=1, fontsize='x-small')
    leg.set_zorder(12)

    fname = '24HR RTMA WIND SPEED & DIRECTION COMPARISON'+ file_name_end
    
    path, gif_path = file_functions.check_file_paths(state, gacc_region, fname, reference_system)
    file_functions.update_images(fig, path, gif_path, fname)


def plot_dry_and_windy_areas(low_rh_threshold=15, high_wind_threshold=25, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, sample_point_type='barbs', barb_quiver_linewidth=1, barb_fontsize=10, row1=None, row2=None, row3=None, row4=None, row5=None, row6=None, col1=None, col2=None, col3=None, col4=None, col5=None, col6=None, tick=9, aspect=30):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region
    low_rh_threshold = low_rh_threshold
    high_wind_threshold = high_wind_threshold

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    low_rh_thresh = low_rh_threshold + 1

    rh_contourf = np.arange(0, low_rh_thresh, 1)

    high_wind = high_wind_threshold + 36
    
    wind_speed_contourf = np.arange(high_wind_threshold, high_wind, 1)

    if low_rh_threshold <= 15:
        rh_labels = rh_contourf
    elif low_rh_threshold > 15 and low_rh_threshold < 40:
        if (low_rh_threshold % 2) == 0:
            rh_labels = rh_contourf[::2]
        else:
            rh_labels = rh_contourf[::5]
    else:
        rh_labels = rh_contourf[::5]
        
    wind_labels = wind_speed_contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', True, 'Dry and Windy Areas')
            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        row1, row2, row3, row4, row5, row6, col1, col2, col3, col4, col5, col6 = dims.get_gridspec_dims(state, gacc_region)


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', True)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        row1, row2, row3, row4, row5, row6, col1, col2, col3, col4, col5, col6 = dims.get_gridspec_dims(state, gacc_region)


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        row1 = row1
        row2 = row2 
        row3 = row3
        row4 = row4 
        row5 = row5
        row6 = row6 
        col1 = col1 
        col2 = col2
        col3 = col3 
        col4 = col4 
        col5 = col5 
        col6 = col6

    fig_x_length = fig_x_length + 2
    fig_y_length = fig_y_length + 2
    sample_point_fontsize = sample_point_fontsize - 2

    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.red_flag_warning_criteria_colormap()

    low_rh_cmap = colormaps.low_relative_humidity_colormap()

    wind_cmap = colormaps.wind_speed_colormap()
    
    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rtma_wind = ds['wind10m']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)
            rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
            rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
    
            rtma_rh = rtma_rh[0, :, :]
            rtma_wind = rtma_wind[0, :, :] 
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rtma_wind = ds['wind10m']
            u = ds['ugrd10m']
            v = ds['vgrd10m']
            u = unit_conversion.meters_per_second_to_mph(u)
            v = unit_conversion.meters_per_second_to_mph(v)
            rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
            rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
    
            rtma_rh = rtma_rh[0, :, :]
            rtma_wind = rtma_wind[0, :, :] 
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
                rtma_wind = ds['wind10m']
                u = ds['ugrd10m']
                v = ds['vgrd10m']
                u = unit_conversion.meters_per_second_to_mph(u)
                v = unit_conversion.meters_per_second_to_mph(v)
                rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
                rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
        
                rtma_rh = rtma_rh[0, :, :]
                rtma_wind = rtma_wind[0, :, :] 
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    mask = (rtma_rh <= low_rh_threshold) & (rtma_wind >= high_wind_threshold)
    lon = mask['lon']
    lat = mask['lat']

    lons = ds['lon']
    lats = ds['lat']

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')
    
    gs = gridspec.GridSpec(10, 10)

    ax1 = fig.add_subplot(gs[row1:row2, col1:col2], projection=ccrs.PlateCarree())
    ax1.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax1.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax1.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax1.add_feature(cfeature.OCEAN, color='lightcyan', zorder=8)
    ax1.add_feature(cfeature.LAKES, color='lightcyan', zorder=4)
    if show_rivers == True:
        ax1.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax1.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax1.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax1.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax1.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax1.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax1.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax1.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Dry & Windy Areas\n[Relative Humidity <= "+str(low_rh_threshold)+" (%) & Wind Speed >= "+str(high_wind_threshold)+" (MPH)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax1.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax1.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    try:
        ax1.pcolormesh(lon,lat,mask, transform=ccrs.PlateCarree(),cmap=cmap, zorder=2, alpha=alpha)

    except Exception as e:
        pass   

    ax2 = fig.add_subplot(gs[row3:row4, col3:col4], projection=ccrs.PlateCarree())
    ax2.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax2.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax2.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax2.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax2.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax2.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax2.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax2.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax2.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax2.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax2.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax2.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax2.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs1 = ax2.contourf(lons, lats, rtma_rh[:, :], 
                     transform=ccrs.PlateCarree(), levels=rh_contourf, cmap=low_rh_cmap, alpha=alpha)

    cbar1 = fig.colorbar(cs1, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=rh_labels)
    cbar1.set_label(label="Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    decimate = decimate *2

    plot_lon, plot_lat = np.meshgrid(lons[::decimate], lats[::decimate])
    plot_lons, plot_lats = np.meshgrid(lons, lats)

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn1 = mpplots.StationPlot(ax2, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        rtma_rh = rtma_rh[::decimate, ::decimate].to_numpy().flatten()
    
        stn1.plot_parameter('C', rtma_rh, color='blue', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    ax3 = fig.add_subplot(gs[row5:row6, col5:col6], projection=ccrs.PlateCarree())
    ax3.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax3.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax3.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax3.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax3.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax3.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax3.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax3.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax3.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax3.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax3.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax3.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax3.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs2 = ax3.contourf(lons, lats, rtma_wind[:, :], 
                     transform=ccrs.PlateCarree(), levels=wind_speed_contourf, cmap=wind_cmap, alpha=alpha, extend='max', zorder=2)

    cbar2 = fig.colorbar(cs2, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=wind_labels)
    cbar2.set_label(label="Wind Speed (MPH)", size=colorbar_fontsize, fontweight='bold')

    plot_lon, plot_lat = np.meshgrid(lons[::decimate], lats[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        if sample_point_type == 'points':

            stn2 = mpplots.StationPlot(ax3, plot_lon.flatten(), plot_lat.flatten(),
                                         transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
        
            rtma_wind = rtma_wind[::decimate, ::decimate].to_numpy().flatten()
        
            stn2.plot_parameter('C', rtma_wind, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

        fname_end = ' SAMPLE POINTS'

        if sample_point_type == 'barbs':

            if state != None and gacc_region != None:

                barb_fontsize = settings.get_gridspec_barb_dims(state, gacc_region)

            if state == None and gacc_region == None:

                barb_fontsize = barb_fontsize

            stn2 = mpplots.StationPlot(ax3, plot_lons[::decimate, ::decimate], plot_lats[::decimate, ::decimate],
                             transform=ccrs.PlateCarree(), zorder=11, fontsize=barb_fontsize, clip_on=True)
    
            stn2.plot_barb(u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='lime', label=rtma_time.strftime('%m/%d %H:00'), zorder=11, linewidth=barb_quiver_linewidth)
    
            fname_end = ' WIND BARBS'

        if sample_point_type == 'quivers' or sample_point_type == 'vectors':

            minshaft, headlength, headwidth = dims.get_quiver_dims(state, gacc_region)
    
            ax3.quiver(plot_lons[::decimate, ::decimate], plot_lats[::decimate, ::decimate], u[0, :, :][::decimate, ::decimate], v[0, :, :][::decimate, ::decimate], color='lime', minshaft=minshaft, headlength=headlength, headwidth=headwidth, zorder=11, linewidth=barb_quiver_linewidth, transform=ccrs.PlateCarree())
    
            fname_end = ' WIND VECTORS'            
            
    else:
        pass

    fname = 'RTMA DRY & WINDY AREAS' + fname_end

    path, gif_path = file_functions.check_file_paths(state, gacc_region, fname, reference_system)
    file_functions.update_images(fig, path, gif_path, fname)


def plot_dry_and_gusty_areas(low_rh_threshold=15, high_wind_threshold=25, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, time=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, row1=None, row2=None, row3=None, row4=None, row5=None, row6=None, col1=None, col2=None, col3=None, col4=None, col5=None, col6=None, tick=9, aspect=30):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()
    data = data
    time = time
    state = state
    gacc_region = gacc_region
    low_rh_threshold = low_rh_threshold
    high_wind_threshold = high_wind_threshold

    reference_system = reference_system
    mapcrs = ccrs.PlateCarree()
    datacrs = ccrs.PlateCarree()

    if gacc_region != None:
        state = None
    else:
        state = state

    if sample_point_fontsize != 8:
        sp_font_default = False
        sp_fontsize = sample_point_fontsize
    else:
        sp_font_default = True

    low_rh_thresh = low_rh_threshold + 1

    rh_contourf = np.arange(0, low_rh_thresh, 1)

    high_wind = high_wind_threshold + 36
    wind_speed_contourf = np.arange(high_wind_threshold, high_wind, 1)

    if low_rh_threshold <= 15:
        rh_labels = rh_contourf
    elif low_rh_threshold > 15 and low_rh_threshold < 40:
        if (low_rh_threshold % 2) == 0:
            rh_labels = rh_contourf[::2]
        else:
            rh_labels = rh_contourf[::5]
    else:
        rh_labels = rh_contourf[::5]
        
    wind_labels = wind_speed_contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', True, 'Dry and Gusty Areas')
            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        row1, row2, row3, row4, row5, row6, col1, col2, col3, col4, col5, col6 = dims.get_gridspec_dims(state, gacc_region)


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', True)

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick

        row1, row2, row3, row4, row5, row6, col1, col2, col3, col4, col5, col6 = dims.get_gridspec_dims(state, gacc_region)


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        row1 = row1
        row2 = row2 
        row3 = row3
        row4 = row4 
        row5 = row5
        row6 = row6 
        col1 = col1 
        col2 = col2
        col3 = col3 
        col4 = col4 
        col5 = col5 
        col6 = col6

    fig_x_length = fig_x_length + 2
    fig_y_length = fig_y_length + 2
    sample_point_fontsize = sample_point_fontsize - 2

    
    local_time, utc_time = standard.plot_creation_time()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.red_flag_warning_criteria_colormap()

    low_rh_cmap = colormaps.low_relative_humidity_colormap()

    wind_cmap = colormaps.wind_speed_colormap()
    
    try:
        if data == None:
            test = True
        if data != None:
            test = False
    except Exception as a:
        test = False


    if test == True and time == None:
        
        try:
            ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rtma_wind = ds['gust10m']
            rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
            rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
    
            rtma_rh = rtma_rh[0, :, :]
            rtma_wind = rtma_wind[0, :, :] 
                        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif test == False and time != None:
        try:
            ds = data
            rtma_time = time
            temp = ds['tmp2m']
            dwpt = ds['dpt2m']
            temp = temp - 273.15
            dwpt = dwpt - 273.15
            rtma_wind = ds['gust10m']
            rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
            rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
    
            rtma_rh = rtma_rh[0, :, :]
            rtma_wind = rtma_wind[0, :, :] 
            print("Unpacked the data successfully!")
        except Exception as e:
            print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")

            try:
                ds, rtma_time = RTMA_CONUS.get_RTMA_dataset(utc_time)
                temp = ds['tmp2m']
                dwpt = ds['dpt2m']
                temp = temp - 273.15
                dwpt = dwpt - 273.15
                rtma_wind = ds['gust10m']
                rtma_wind = unit_conversion.meters_per_second_to_mph(rtma_wind)
                rtma_rh = Thermodynamics.relative_humidity_from_temperature_and_dewpoint_celsius(temp, dwpt)
        
                rtma_rh = rtma_rh[0, :, :]
                rtma_wind = rtma_wind[0, :, :] 
                            
                print("Unpacked the data successfully!")
            except Exception as e:
                pass    
        
    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)

    mask = (rtma_rh <= low_rh_threshold) & (rtma_wind >= high_wind_threshold)
    lon = mask['lon']
    lat = mask['lat']

    lons = ds['lon']
    lats = ds['lat']

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    gs = gridspec.GridSpec(10, 10)

    ax1 = fig.add_subplot(gs[row1:row2, col1:col2], projection=ccrs.PlateCarree())
    ax1.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax1.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax1.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax1.add_feature(cfeature.OCEAN, color='lightcyan', zorder=8)
    ax1.add_feature(cfeature.LAKES, color='lightcyan', zorder=4)
    if show_rivers == True:
        ax1.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax1.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax1.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax1.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax1.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax1.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax1.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax1.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass
    
    plt.title("RTMA Dry & Gusty Areas\n[Relative Humidity <= "+str(low_rh_threshold)+" (%) & Wind Gust >= "+str(high_wind_threshold)+" (MPH)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Analysis Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    ax1.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: NOAA/NCEP/NOMADS\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax1.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    try:
        ax1.pcolormesh(lon,lat,mask, transform=ccrs.PlateCarree(),cmap=cmap, zorder=2, alpha=alpha)

    except Exception as e:
        pass   

    ax2 = fig.add_subplot(gs[row3:row4, col3:col4], projection=ccrs.PlateCarree())
    ax2.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax2.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax2.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax2.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax2.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax2.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax2.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax2.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax2.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax2.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax2.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax2.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax2.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs1 = ax2.contourf(lons, lats, rtma_rh[:, :], 
                     transform=ccrs.PlateCarree(), levels=rh_contourf, cmap=low_rh_cmap, alpha=alpha)

    cbar1 = fig.colorbar(cs1, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=rh_labels)
    cbar1.set_label(label="Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    decimate = scaling.get_nomads_decimation(western_bound, eastern_bound, southern_bound, northern_bound, True)

    decimate = decimate * 2

    plot_lon, plot_lat = np.meshgrid(lons[::decimate], lats[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn1 = mpplots.StationPlot(ax2, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        rtma_rh = rtma_rh[::decimate, ::decimate].to_numpy().flatten()
    
        stn1.plot_parameter('C', rtma_rh, color='blue', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    ax3 = fig.add_subplot(gs[row5:row6, col5:col6], projection=ccrs.PlateCarree())
    ax3.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax3.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75, zorder=9)
    ax3.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax3.add_feature(cfeature.OCEAN, color='lightcyan', zorder=1)
    ax3.add_feature(cfeature.LAKES, color='lightcyan', zorder=1)
    if show_rivers == True:
        ax3.add_feature(cfeature.RIVERS, color='lightcyan', zorder=4)
    else:
        pass

    if show_gacc_borders == True:
        ax3.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax3.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax3.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax3.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax3.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax3.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax3.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs2 = ax3.contourf(lons, lats, rtma_wind[:, :], 
                     transform=ccrs.PlateCarree(), levels=wind_speed_contourf, cmap=wind_cmap, alpha=alpha, extend='max', zorder=2)

    cbar2 = fig.colorbar(cs2, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=wind_labels)
    cbar2.set_label(label="Wind Gust (MPH)", size=colorbar_fontsize, fontweight='bold')

    plot_lon, plot_lat = np.meshgrid(lons[::decimate], lats[::decimate])

    if sp_font_default == False:
        sample_point_fontsize = sp_fontsize
    else:
        sample_point_fontsize = sample_point_fontsize

    if show_sample_points == True:

        stn2 = mpplots.StationPlot(ax3, plot_lon.flatten(), plot_lat.flatten(),
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        rtma_wind = rtma_wind[::decimate, ::decimate].to_numpy().flatten()
    
        stn2.plot_parameter('C', rtma_wind, color='lime', path_effects=[withStroke(linewidth=1, foreground='black')], zorder=7)

    else:
        pass

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA DRY & GUSTY AREAS', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA DRY & GUSTY AREAS')

def plot_relative_humidity_with_metar_obs(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, metar_mask=None, metar_fontsize=10, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    
    data = data
    local_time, utc_time = standard.plot_creation_time()

    if gacc_region != None:
        state = None
    else:
        state = state

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    contourf = np.arange(0, 101, 1)
    labels = contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, 'RH & METAR')            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, 'RH & METAR')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        mask = metar_mask
    
    mask = dims.get_metar_mask(state, gacc_region)
    
    if data == None:
        try:
            data = RTMA_CONUS.RTMA_Relative_Humidity_Synced_With_METAR(utc_time, mask)
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]   
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
        
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif data != None:
        try:
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]            
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            print("Unpacked the data successfully!")

        except Exception as f:
            try:
                print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
                data = RTMA_CONUS.RTMA_Relative_Humidity_Synced_With_METAR(utc_time, mask)
                rtma_data = data[0]
                rtma_time = data[1]
                sfc_data = data[2]
                sfc_data_u_kt = data[3]
                sfc_data_v_kt = data[4]
                sfc_data_rh = data[5]
                sfc_data_decimate = data[6]
                metar_time_revised = data[7]
                plot_proj = data[8] 
                lat = rtma_data['latitude']
                lon = rtma_data['longitude']
                
                print("Unpacked the data successfully!")
            except Exception as g:
                pass            

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    metar_time_revised = metar_time_revised.replace(tzinfo=from_zone)
    metar_time_revised = metar_time_revised.astimezone(to_zone)
    metar_time_revised_utc = metar_time_revised.astimezone(from_zone)
    
    datacrs = ccrs.PlateCarree()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.relative_humidity_colormap()

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=3)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=3)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs = ax.contourf(lon, lat, rtma_data, 
                     transform=datacrs, levels=contourf, cmap=cmap, alpha=alpha)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    # Plots METAR
    stn = mpplots.StationPlot(ax, sfc_data['longitude'][sfc_data_decimate].m, sfc_data['latitude'][sfc_data_decimate].m,
                             transform=ccrs.PlateCarree(), fontsize=metar_fontsize, zorder=10, clip_on=True)
    
    
    stn.plot_parameter('NW', sfc_data['air_temperature'].to('degF')[sfc_data_decimate], color='red',
                      path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_parameter('SW', sfc_data['dew_point_temperature'].to('degF')[sfc_data_decimate], color='blue',
                      path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_symbol('C', sfc_data['cloud_coverage'][sfc_data_decimate], mpplots.sky_cover)
    
    stn.plot_parameter('E', sfc_data_rh.to('percent')[sfc_data_decimate], color='darkgreen',
                        path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_barb(sfc_data['u'][sfc_data_decimate], sfc_data['v'][sfc_data_decimate])

    plt.title("RTMA Relative Humidity (%) & METAR Observations", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')
    
    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: thredds.ucar.edu\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA RH & METAR', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA RH & METAR')

def plot_low_relative_humidity_with_metar_obs(low_rh_threshold=15, western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, metar_mask=None, metar_fontsize=10, aspect=30, tick=9):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    
    data = data
    local_time, utc_time = standard.plot_creation_time()

    if gacc_region != None:
        state = None
    else:
        state = state

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    thresh = low_rh_threshold + 1
    contourf = np.arange(0, thresh, 1)

    if low_rh_threshold <= 15:
        labels = contourf
    elif low_rh_threshold > 15 and low_rh_threshold < 40:
        if (low_rh_threshold % 2) == 0:
            labels = contourf[::2]
        else:
            labels = contourf[::5]
    else:
        labels = contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, 'Low RH & METAR')
            
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, 'Low RH & METAR')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        mask = metar_mask
    
    mask = dims.get_metar_mask(state, gacc_region)
    
    if data == None:
        try:
            data = RTMA_CONUS.RTMA_Relative_Humidity_Synced_With_METAR(utc_time, mask)
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]   
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif data != None:
        try:
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]            
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            print("Unpacked the data successfully!")

        except Exception as f:
            try:
                print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
                data = RTMA_CONUS.RTMA_Relative_Humidity_Synced_With_METAR(utc_time, mask)
                rtma_data = data[0]
                rtma_time = data[1]
                sfc_data = data[2]
                sfc_data_u_kt = data[3]
                sfc_data_v_kt = data[4]
                sfc_data_rh = data[5]
                sfc_data_decimate = data[6]
                metar_time_revised = data[7]
                plot_proj = data[8]            
                
                print("Unpacked the data successfully!")
            except Exception as g:
                pass            

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    metar_time_revised = metar_time_revised.replace(tzinfo=from_zone)
    metar_time_revised = metar_time_revised.astimezone(to_zone)
    metar_time_revised_utc = metar_time_revised.astimezone(from_zone)
    
    datacrs = ccrs.PlateCarree()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.low_relative_humidity_colormap()

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=3)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=3)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    cs = ax.contourf(lon, lat, rtma_data, 
                     transform=datacrs, levels=contourf, cmap=cmap, alpha=alpha)

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Relative Humidity (%)", size=colorbar_fontsize, fontweight='bold')

    # Plots METAR
    stn = mpplots.StationPlot(ax, sfc_data['longitude'][sfc_data_decimate].m, sfc_data['latitude'][sfc_data_decimate].m,
                             transform=ccrs.PlateCarree(), fontsize=metar_fontsize, zorder=10, clip_on=True)
    
    
    stn.plot_parameter('NW', sfc_data['air_temperature'].to('degF')[sfc_data_decimate], color='red',
                      path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_parameter('SW', sfc_data['dew_point_temperature'].to('degF')[sfc_data_decimate], color='blue',
                      path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_symbol('C', sfc_data['cloud_coverage'][sfc_data_decimate], mpplots.sky_cover)
    
    stn.plot_parameter('E', sfc_data_rh.to('percent')[sfc_data_decimate], color='darkgreen',
                        path_effects=[withStroke(linewidth=1, foreground='black')])
    
    stn.plot_barb(sfc_data['u'][sfc_data_decimate], sfc_data['v'][sfc_data_decimate])

    plt.title("RTMA Low Relative Humidity (%) & METAR Observations\n[Relative Humidity (Shaded) <= "+str(low_rh_threshold)+" (%)]", fontsize=title_fontsize, fontweight='bold', loc='left')
    
    plt.title("Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')
    
    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: thredds.ucar.edu\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA LOW RH & METAR', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA LOW RH & METAR')

def plot_wind_speed_with_observed_winds(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, metar_mask=None, metar_fontsize=10, u_component=None, v_component=None, sample_point_type='barbs', aspect=30, tick=9, decimate=None):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    
    data = data
    local_time, utc_time = standard.plot_creation_time()

    if gacc_region != None:
        state = None
    else:
        state = state

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    contourf = np.arange(0, 61, 1)
    labels = contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, 'RTMA Wind Speed & Observed Wind Speed')            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, 'RTMA Wind Speed & Observed Wind Speed')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        mask = metar_mask
    
    mask = dims.get_metar_mask(state, gacc_region, rtma_ws=True)
    
    if data == None:
        try:
            data = RTMA_CONUS.RTMA_Synced_With_METAR('Wind_speed_Analysis_height_above_ground', utc_time, mask)
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]   
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            rtma_data = rtma_data * 2.23694
            u, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'u-component_of_wind_Analysis_height_above_ground')
            v, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'v-component_of_wind_Analysis_height_above_ground')
            u = u * 2.23694
            v = v * 2.23694
            
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif data != None:
        try:
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]            
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            rtma_data = rtma_data * 2.23694
            u = u_component
            v = v_component
            u = u * 2.23694
            v = v * 2.23694
            
            print("Unpacked the data successfully!")

        except Exception as f:
            try:
                print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
                data = RTMA_CONUS.RTMA_Synced_With_METAR('Wind_speed_Analysis_height_above_ground', utc_time, mask)
                rtma_data = data[0] 
                rtma_time = data[1]
                sfc_data = data[2]
                sfc_data_u_kt = data[3]
                sfc_data_v_kt = data[4]
                sfc_data_rh = data[5]
                sfc_data_decimate = data[6]
                metar_time_revised = data[7]
                plot_proj = data[8] 
                lat = rtma_data['latitude']
                lon = rtma_data['longitude']
                rtma_data = rtma_data * 2.23694
                u, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'u-component_of_wind_Analysis_height_above_ground')
                v, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'v-component_of_wind_Analysis_height_above_ground')
                u = u * 2.23694
                v = v * 2.23694
                
                print("Unpacked the data successfully!")
            except Exception as g:
                pass            

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    metar_time_revised = metar_time_revised.replace(tzinfo=from_zone)
    metar_time_revised = metar_time_revised.astimezone(to_zone)
    metar_time_revised_utc = metar_time_revised.astimezone(from_zone)
    
    datacrs = ccrs.PlateCarree()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_colormap()

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=3)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=3)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    if decimate == None:
        decimate = scaling.get_tds_rtma_decimation_by_state_or_gacc_region(state, gacc_region)
    else:
        decimate = decimate

    df_ws = rtma_data.to_dataframe()
    df_u = u.to_dataframe()
    df_v = v.to_dataframe()

    cs = ax.contourf(lon, lat, rtma_data, 
                     transform=datacrs, levels=contourf, cmap=cmap, alpha=alpha, zorder=4, extend='max')

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Speed (MPH)", size=colorbar_fontsize, fontweight='bold')

    # Plots METAR
    stn = mpplots.StationPlot(ax, sfc_data['longitude'][sfc_data_decimate].m, sfc_data['latitude'][sfc_data_decimate].m,
                             transform=ccrs.PlateCarree(), fontsize=metar_fontsize, zorder=10, clip_on=True)
    
    sfc_data['u'] = sfc_data['u'] * 1.15078
    sfc_data['v'] = sfc_data['v'] * 1.15078
    
    stn.plot_barb(sfc_data['u'][sfc_data_decimate], sfc_data['v'][sfc_data_decimate], color='darkorange')

    if sample_point_type == 'points':

        plt.title("RTMA Wind Speed [MPH] & Observed Winds", fontsize=title_fontsize, fontweight='bold', loc='left')

        stn1 = mpplots.StationPlot(ax, df_ws['longitude'][::decimate], df_ws['latitude'][::decimate],
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        stn1.plot_parameter('C', df_ws['Wind_speed_Analysis_height_above_ground'][::decimate], color='crimson', zorder=7)

    if sample_point_type == 'barbs':
        
        plt.title("RTMA Wind Speed (MPH) & Observed Wind [METAR]\nRTMA Wind [Green Barbs]\nObserved Wind [Orange Barbs]", fontsize=title_fontsize, fontweight='bold', loc='left')
        
        stn1 = mpplots.StationPlot(ax, df_u['longitude'][::decimate], df_u['latitude'][::decimate],
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        stn1.plot_barb(df_u['u-component_of_wind_Analysis_height_above_ground'][::decimate], df_v['v-component_of_wind_Analysis_height_above_ground'][::decimate], color='lime', zorder=7)        

    
    
    plt.title("Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')
    
    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: thredds.ucar.edu\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA WIND SPEED & OBS', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA WIND SPEED & OBS')

def plot_wind_gust_with_observed_winds(western_bound=None, eastern_bound=None, southern_bound=None, northern_bound=None, fig_x_length=None, fig_y_length=None, signature_x_position=None, signature_y_position=None, color_table_shrink=1, title_fontsize=12, subplot_title_fontsize=10, signature_fontsize=10, colorbar_fontsize=8, show_rivers=True, reference_system='States & Counties', show_state_borders=False, show_county_borders=False, show_gacc_borders=False, show_psa_borders=False, show_cwa_borders=False, show_nws_firewx_zones=False, show_nws_public_zones=False, state_border_linewidth=2, county_border_linewidth=1, gacc_border_linewidth=2, psa_border_linewidth=1, cwa_border_linewidth=1, nws_firewx_zones_linewidth=0.5, nws_public_zones_linewidth=0.5, state_border_linestyle='-', county_border_linestyle='-', gacc_border_linestyle='-', psa_border_linestyle='-', cwa_border_linestyle='-', nws_firewx_zones_linestyle='-', nws_public_zones_linestyle='-', psa_color='black', gacc_color='black', cwa_color='black', fwz_color='black', pz_color='black', show_sample_points=True, sample_point_fontsize=8, alpha=0.5, data=None, state='us', gacc_region=None, colorbar_pad=0.02, clabel_fontsize=8, metar_mask=None, metar_fontsize=10, sample_point_type='barbs', aspect=30, tick=9, decimate=None):

    r'''
        This function does the following:
                                        1) Downloads the latest availiable temperature and dewpoint data arrays. 
                                        2) Downloads the METAR Data that is synced with the latest availiable 2.5km x 2.5km Real Time Mesoscale Analysis Data. 
                                        3) Uses MetPy to calculate the relative humidity data array from the temperature and dewpoint data arrays. 
                                        4) Plots the relative humidity data overlayed with the METAR reports. 

        

        Inputs:

            1) western_bound (Integer or Float) - Western extent of the plot in decimal degrees.

            2) eastern_bound (Integer or Float) - Eastern extent of the plot in decimal degrees.

            3) southern_bound (Integer or Float) - Southern extent of the plot in decimal degrees.

            4) northern_bound (Integer or Float) - Northern extent of the plot in decimal degrees.

            5) central_longitude (Integer or Float) - The central longitude. Defaults to -96.

            6) central_latitude (Integer or Float) - The central latitude. Defaults to 39.

            7) first_standard_parallel (Integer or Float) - Southern standard parallel. 

            8) second_standard_parallel (Integer or Float) - Northern standard parallel. 
            
            9) fig_x_length (Integer) - The horizontal (x-direction) length of the entire figure. 

            10) fig_y_length (Integer) - The vertical (y-direction) length of the entire figure. 

            11) color_table_shrink (Integer or Float) - The size of the color bar with respect to the size of the figure. Generally this ranges between 0 and 1. Values closer to 0 correspond to shrinking the size of the color bar while larger values correspond to increasing the size of the color bar. 

            12) decimate (Integer) - Distance in meters to decimate METAR stations apart from eachother so stations don't clutter the plot. The higher the value, the less stations are displayed. 

            13) signature_x_position (Integer or Float) - The x-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure. 

            14) signature_y_position (Integer or Float) - The y-position of the signature (The signature is where the credit is given to FireWxPy and the data source on the graphic) with respect to the axis of the subplot of the figure.

            15) title_font_size (Integer) - The fontsize of the title of the figure. 

            16) signature_font_size (Integer) - The fontsize of the signature of the figure. 

            17) colorbar_label_font_size (Integer) - The fontsize of the title of the colorbar of the figure. 

            18) colorbar_pad (Float) - This determines how close the position of the colorbar is to the edge of the subplot of the figure. 
                                       Default setting is 0.05.
                                       Lower numbers mean the colorbar is closer to the edge of the subplot while larger numbers allows for more space between the edge of the subplot and the colorbar.
                                       Example: If colorbar_pad = 0.00, then the colorbar is right up against the edge of the subplot. 

            19) show_rivers (Boolean) - If set to True, rivers will display on the map. If set to False, rivers 
                                        will not display on the map. 


        Returns:
                1) A figure of the plotted 2.5km x 2.5km Real Time Mesoscale Analysis relative humidity overlayed with the latest METAR reports. 
    
    '''
    
    data = data
    local_time, utc_time = standard.plot_creation_time()

    if gacc_region != None:
        state = None
    else:
        state = state

    props = dict(boxstyle='round', facecolor='wheat', alpha=1)

    contourf = np.arange(0, 81, 1)
    labels = contourf[::5]

    if reference_system == 'Custom' or reference_system == 'custom':
        show_state_borders = show_state_borders
        show_county_borders = show_county_borders
        show_gacc_borders = show_gacc_borders
        show_psa_borders = show_psa_borders
        show_cwa_borders = show_cwa_borders
        show_nws_firewx_zones = show_nws_firewx_zones
        show_nws_public_zones = show_nws_public_zones

    if reference_system != 'Custom' and reference_system != 'custom':
        
        show_state_borders = False
        show_county_borders = False
        show_gacc_borders = False
        show_psa_borders = False
        show_cwa_borders = False
        show_nws_firewx_zones = False
        show_nws_public_zones = False

        if reference_system == 'States Only':
            show_state_borders = True
        if reference_system == 'States & Counties':
            show_state_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC Only':
            show_gacc_borders = True
        if reference_system == 'GACC & PSA':
            show_gacc_borders = True
            show_psa_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.25
        if reference_system == 'CWA Only':
            show_cwa_borders = True
        if reference_system == 'NWS CWAs & NWS Public Zones':
            show_cwa_borders = True
            show_nws_public_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_public_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & NWS Fire Weather Zones':
            show_cwa_borders = True
            show_nws_firewx_zones = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                nws_firewx_zones_linewidth=0.25
        if reference_system == 'NWS CWAs & Counties':
            show_cwa_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
        if reference_system == 'GACC & PSA & NWS Fire Weather Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_firewx_zones = True
            nws_firewx_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS Public Zones':
            show_gacc_borders = True
            show_psa_borders = True
            show_nws_public_zones = True
            nws_public_zones_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & NWS CWA':
            show_gacc_borders = True
            show_psa_borders = True
            show_cwa_borders = True
            cwa_border_linewidth=0.25
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                psa_border_linewidth=0.5
        if reference_system == 'GACC & PSA & Counties':
            show_gacc_borders = True
            show_psa_borders = True
            show_county_borders = True
            county_border_linewidth=0.25
        if reference_system == 'GACC & Counties':
            show_gacc_borders = True
            show_county_borders = True
            if state == 'US' or state == 'us' or state == 'USA' or state == 'usa':
                county_border_linewidth=0.25
    
    if state != None and gacc_region == None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_state_data_and_coords(state, 'rtma', False, 'RTMA Wind Speed & Observed Wind Speed')            

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if state == None and gacc_region != None:
        directory_name, western_bound, eastern_bound, southern_bound, northern_bound, fig_x_length, fig_y_length, signature_x_position, signature_y_position, title_fontsize, subplot_title_fontsize, signature_fontsize, sample_point_fontsize, colorbar_fontsize, color_table_shrink, legend_fontsize, mapcrs, datacrs, title_x_position, aspect, tick = settings.get_gacc_region_data_and_coords(gacc_region, 'rtma', False, 'RTMA Wind Speed & Observed Wind Speed')

        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick


    if western_bound != None and eastern_bound != None and southern_bound != None and northern_bound != None and fig_x_length != None and fig_y_length != None and signature_x_position != None and signature_y_position != None and state == None and gacc_region == None:

        fig_x_length = fig_x_length
        fig_y_length = fig_y_length
        signature_x_position = signature_x_position
        signature_y_position = signature_y_position
        western_bound = western_bound
        eastern_bound = eastern_bound
        southern_bound = southern_bound
        northern_bound = northern_bound
        state = 'Custom'
        mpl.rcParams['xtick.labelsize'] = tick
        mpl.rcParams['ytick.labelsize'] = tick
        aspect=aspect
        mask = metar_mask
    
    mask = dims.get_metar_mask(state, gacc_region, rtma_ws=True)
    
    if data == None:
        try:
            data = RTMA_CONUS.RTMA_Synced_With_METAR('Wind_speed_gust_Analysis_height_above_ground', utc_time, mask)
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]   
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            rtma_data = rtma_data * 2.23694
            u, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'u-component_of_wind_Analysis_height_above_ground')
            v, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'v-component_of_wind_Analysis_height_above_ground')
            u = u * 2.23694
            v = v * 2.23694
            
            print("Unpacked the data successfully!")
        except Exception as e:
            pass

    elif data != None:
        try:
            rtma_data = data[0]
            rtma_time = data[1]
            sfc_data = data[2]
            sfc_data_u_kt = data[3]
            sfc_data_v_kt = data[4]
            sfc_data_rh = data[5]
            sfc_data_decimate = data[6]
            metar_time_revised = data[7]
            plot_proj = data[8]            
            lat = rtma_data['latitude']
            lon = rtma_data['longitude']
            rtma_data = rtma_data * 2.23694
            u = u_component
            v = v_component
            u = u * 2.23694
            v = v * 2.23694
            
            print("Unpacked the data successfully!")

        except Exception as f:
            try:
                print("There was a problem with the data passed in by the user.\nNo worries! FireWxPy will now try downloading and unpacking the data for you!")
                data = RTMA_CONUS.RTMA_Synced_With_METAR('Wind_speed_gust_Analysis_height_above_ground', utc_time, mask)
                rtma_data = data[0] 
                rtma_time = data[1]
                sfc_data = data[2]
                sfc_data_u_kt = data[3]
                sfc_data_v_kt = data[4]
                sfc_data_rh = data[5]
                sfc_data_decimate = data[6]
                metar_time_revised = data[7]
                plot_proj = data[8] 
                lat = rtma_data['latitude']
                lon = rtma_data['longitude']
                rtma_data = rtma_data * 2.23694
                u, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'u-component_of_wind_Analysis_height_above_ground')
                v, t = RTMA_CONUS.get_current_rtma_data(utc_time, 'v-component_of_wind_Analysis_height_above_ground')
                u = u * 2.23694
                v = v * 2.23694
                
                print("Unpacked the data successfully!")
            except Exception as g:
                pass            

    else:
        print("Error! Both values either need to have a value of None or have an array of the RTMA Data and RTMA Timestamp.")

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    rtma_time = rtma_time.replace(tzinfo=from_zone)
    rtma_time = rtma_time.astimezone(to_zone)
    rtma_time_utc = rtma_time.astimezone(from_zone)
    metar_time_revised = metar_time_revised.replace(tzinfo=from_zone)
    metar_time_revised = metar_time_revised.astimezone(to_zone)
    metar_time_revised_utc = metar_time_revised.astimezone(from_zone)
    
    datacrs = ccrs.PlateCarree()

    PSAs = geometry.import_shapefiles(f"PSA Shapefiles/National_PSA_Current.shp", psa_color, 'psa')
    
    GACC = geometry.import_shapefiles(f"GACC Boundaries Shapefiles/National_GACC_Current.shp", gacc_color, 'gacc')

    CWAs = geometry.import_shapefiles(f"NWS CWA Boundaries/w_05mr24.shp", cwa_color, 'cwa')

    FWZs = geometry.import_shapefiles(f"NWS Fire Weather Zones/fz05mr24.shp", fwz_color, 'fwz')

    PZs = geometry.import_shapefiles(f"NWS Public Zones/z_05mr24.shp", pz_color, 'pz')

    cmap = colormaps.wind_speed_colormap()

    fig = plt.figure(figsize=(fig_x_length, fig_y_length))
    fig.set_facecolor('aliceblue')

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent((western_bound, eastern_bound, southern_bound, northern_bound), crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'), linewidth=0.75)
    ax.add_feature(cfeature.LAND, color='beige', zorder=1)
    ax.add_feature(cfeature.OCEAN, color='lightcyan', zorder=3)
    ax.add_feature(cfeature.LAKES, color='lightcyan', zorder=3)
    if show_rivers == True:
        ax.add_feature(cfeature.RIVERS, color='lightcyan', zorder=3)
    else:
        pass

    if show_gacc_borders == True:
        ax.add_feature(GACC, linewidth=gacc_border_linewidth, linestyle=gacc_border_linestyle, zorder=6)
    else:
        pass
    if show_psa_borders == True:
        ax.add_feature(PSAs, linewidth=psa_border_linewidth, linestyle=psa_border_linestyle, zorder=5)
    else:
        pass
    if show_county_borders == True:
        ax.add_feature(USCOUNTIES, linewidth=county_border_linewidth, linestyle=county_border_linestyle, zorder=5)
    else:
        pass
    if show_state_borders == True:
        ax.add_feature(cfeature.STATES, linewidth=state_border_linewidth, linestyle=state_border_linestyle, edgecolor='black', zorder=6)
    else:
        pass
    if show_cwa_borders == True:
        ax.add_feature(CWAs, linewidth=cwa_border_linewidth, linestyle=cwa_border_linestyle, zorder=5)
    else:
        pass
    if show_nws_firewx_zones == True:
        ax.add_feature(FWZs, linewidth=nws_firewx_zones_linewidth, linestyle=nws_firewx_zones_linestyle, zorder=5)
    else:
        pass
    if show_nws_public_zones == True:
        ax.add_feature(PZs, linewidth=nws_public_zones_linewidth, linestyle=nws_public_zones_linestyle, zorder=5)
    else:
        pass

    if decimate == None:
        decimate = scaling.get_tds_rtma_decimation_by_state_or_gacc_region(state, gacc_region)
    else:
        decimate = decimate

    df_ws = rtma_data.to_dataframe()
    df_u = u.to_dataframe()
    df_v = v.to_dataframe()

    cs = ax.contourf(lon, lat, rtma_data, 
                     transform=datacrs, levels=contourf, cmap=cmap, alpha=alpha, zorder=4, extend='max')

    cbar = fig.colorbar(cs, shrink=color_table_shrink, pad=colorbar_pad, location='bottom', aspect=aspect, ticks=labels)
    cbar.set_label(label="Wind Gust (MPH)", size=colorbar_fontsize, fontweight='bold')

    # Plots METAR
    stn = mpplots.StationPlot(ax, sfc_data['longitude'][sfc_data_decimate].m, sfc_data['latitude'][sfc_data_decimate].m,
                             transform=ccrs.PlateCarree(), fontsize=metar_fontsize, zorder=10, clip_on=True)

    sfc_data['u'] = sfc_data['u'] * 1.15078
    sfc_data['v'] = sfc_data['v'] * 1.15078
    
    stn.plot_barb(sfc_data['u'][sfc_data_decimate], sfc_data['v'][sfc_data_decimate], color='darkorange')

    if sample_point_type == 'points':

        plt.title("RTMA Wind Gust [MPH] & Observed Gusts [MPH]", fontsize=title_fontsize, fontweight='bold', loc='left')

        stn1 = mpplots.StationPlot(ax, df_ws['longitude'][::decimate], df_ws['latitude'][::decimate],
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        stn1.plot_parameter('C', df_ws['Wind_speed_gust_Analysis_height_above_ground'][::decimate], color='crimson', zorder=7)

    if sample_point_type == 'barbs':
        
        plt.title("RTMA Wind Gust [MPH (Shaded)]\nRTMA Winds [MPH (Green Barbs)]\nObserved Winds [MPH (Orange Barbs)]", fontsize=title_fontsize, fontweight='bold', loc='left')
        
        stn1 = mpplots.StationPlot(ax, df_u['longitude'][::decimate], df_u['latitude'][::decimate],
                                     transform=ccrs.PlateCarree(), fontsize=sample_point_fontsize, zorder=7, clip_on=True)
    
        stn1.plot_barb(df_u['u-component_of_wind_Analysis_height_above_ground'][::decimate], df_v['v-component_of_wind_Analysis_height_above_ground'][::decimate], color='lime', zorder=7)      
    
    plt.title("Analysis & Observations Valid: " + rtma_time.strftime('%m/%d/%Y %H:00 Local') + " (" + rtma_time_utc.strftime('%H:00 UTC')+")", fontsize=subplot_title_fontsize, fontweight='bold', loc='right')
    
    ax.text(signature_x_position, signature_y_position, "Plot Created With FireWxPy (C) Eric J. Drewitz 2024\nReference System: "+reference_system+"\nData Source: thredds.ucar.edu\nImage Created: " + local_time.strftime('%m/%d/%Y %H:%M Local') + " (" + utc_time.strftime('%H:%M UTC') + ")", transform=ax.transAxes, fontsize=signature_fontsize, fontweight='bold', verticalalignment='top', bbox=props, zorder=10)

    path, gif_path = file_functions.check_file_paths(state, gacc_region, 'RTMA WIND GUST & OBS', reference_system)
    file_functions.update_images(fig, path, gif_path, 'RTMA WIND GUST & OBS')

