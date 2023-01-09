#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:26:18 2023

@author: michaelzelinski

This is an example script demonstrating how to call the 
'calculate_ndvi_epsg_4326' method from a python script. 

"""

from planet_code import calculate_ndvi_epsg_4326 as c_4326

fn_in = r"./data/20210827_162545_60_2262_3B_AnalyticMS_8b.tif"
fn_out = r"./data/20210827_162545_60_2262_3B_AnalyticMS_8b_NDVI_epsg_4326.tif"

c_4326(fn_in, fn_out, thresh=.5)
