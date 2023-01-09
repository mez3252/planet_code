#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 10:55:19 2023

@author: michaelzelinski

Code for loading a geoTif image, calculating NDVI from that image, thresholding 
that image, and then saving a thresholded output geoTiff (EPSG: 4326) mask 
where values below the threshold are 0 (non-vegatation) and above the 
threshold are 255 (vegatation).
"""

from osgeo import gdal
import numpy as np
import argparse

def calculate_ndvi_epsg_4326( fn_in, fn_out, thresh=.5 ):
    '''
    Inputs
    fn_in: input filename [string]
    fn_out: output filename [string]
    thresh: detection threshold, default value .5 [float]
    
    Output
    saved geoTiff with EPSG:4326 coordinate reference system 
    '''
    
    # load dataset and obtain red and infra-red spectral bands
    ds = gdal.Open(fn_in)
    r  = ds.GetRasterBand(6).ReadAsArray().astype('float')
    ir = ds.GetRasterBand(8).ReadAsArray().astype('float')    
    rows, cols = r.shape

    # compute ndvi, and be careful not to divide by zero. 
    a = ir - r
    b = ir + r    
    ndvi = np.divide( a, b, out=np.zeros_like(a), where=b!=0, dtype=float )
    
    # create a new dataset for output  
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(fn_out, cols, rows, 1, gdal.GDT_UInt16)
    outdata.SetGeoTransform(ds.GetGeoTransform())
    outdata.SetProjection(ds.GetProjection())
    outdata.GetRasterBand(1).WriteArray( 255*(ndvi > thresh).astype('uint16') )
    
    # use gdal warp to convert the dataset to epsg:4326
    gdal.Warp(fn_out, outdata, dstSRS='EPSG:4326')
    outdata=None



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--fn_in",
        type=str,
        default=r"./data/20210827_162545_60_2262_3B_AnalyticMS_8b.tif",
        help="input filename",
    )
    
    parser.add_argument(
        "--fn_out",
        type=str,
        default=r"./data/20210827_162545_60_2262_3B_AnalyticMS_8b_NDVI_epsg_4326.tif",
        help="output filename",
    )    

    parser.add_argument(
        "-t", "--thresh",
        type=float,
        default=.5,
        help="ndvi threshold",
    )

    
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    
    args = parser.parse_args()

    if args.verbose:
        print( 'Input filename: {}'.format(args.fn_in) )
        print( 'Output filename: {}'.format(args.fn_out) )
        print( 'NDVI threshold: {}'.format(args.thresh) )
    
    calculate_ndvi_epsg_4326( args.fn_in, args.fn_out, args.thresh )
    
    
    