# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:13:41 2023

@author: au156185
"""
import argparse

from edcrop import edcrop

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description =
                                     'Runs script to compute ET and drainage')
    parser.add_argument('--yaml', default='edcrop.yaml', 
                        help='YAML is name of yaml file')
    parser.add_argument('--log', default='edcrop.log', 
                        help='LOG is name of log file')
    
    args = vars(parser.parse_args())
    
    edcrop.run_model(args['yaml'], args['log'])
pass