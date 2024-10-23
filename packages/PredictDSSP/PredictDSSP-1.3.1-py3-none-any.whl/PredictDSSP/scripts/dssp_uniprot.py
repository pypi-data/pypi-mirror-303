#!/usr/bin/env python

# executing script for IDR predictor in command line.

# import stuff for making CLI
import os
import sys
import argparse


import csv
import protfasta
from getSequence import getseq

from PredictDSSP.dssp_exceptions import DsspError
import PredictDSSP as dssp

def main():

    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='Predict dssp scores from a UniProt accession number.')

    parser.add_argument('uniprot', nargs='+', help='Name of the protein or unipot id.')

    parser.add_argument('-D', '--dpi', default=150, type=int, metavar='DPI',
                        help='Optional. Set DPI to change resolution of output graphs. Default is 150.')

    parser.add_argument('-c', '--cutoff', default=0.3, type=float,
                        help='Optional. Set disorder cutoff value.')

    parser.add_argument('-e', '--exclude_disorder', action='store_true', help='Optional. Use this flag to exclude disordered regions.')                        

    parser.add_argument('-o', '--output-file', const='USE_DEFAULT', help='Filename for where to save the returned graph. \
    The can included file extension, which in turn defines the filetype (pdf, png, jpg etc.) Note if no filename is included then \
    the -o acts as a flag and the file will be saved as the Uniprot ID', nargs='?')
    
    parser.add_argument('-t', '--title', help='Title to put on graph')

    parser.add_argument('-r', '--raw_vals', action='store_true', help='Optional. Use this flag to graph raw probabilities for each secondary structure.')                        

    args = parser.parse_args()

    # get protein name 
    if len(args.uniprot) == 1:
        final_name = args.uniprot[0]
        just_protein_name = True

    else:
        final_name = ''
        for i in args.uniprot:
            final_name += i
            final_name += ' '
        final_name = final_name[:len(final_name)-1]
        just_protein_name = False


    if args.exclude_disorder == True:
        exclude_disorder=True
    else:
        exclude_disorder=False

    if args.raw_vals == True:
        raw_vals = True
    else:
        raw_vals = False


    # set title
    if args.title:
        graph_title = args.title
    else:
        graph_title = 'DSSP scores for %s'%(final_name)

    # if we don't want to save...
    if args.output_file is None:
        try:
            dssp.graph_dssp_uniprot(final_name, title=graph_title, raw_vals=raw_vals, dis_threshhold = args.cutoff, exclude_disorder=exclude_disorder, DPI=args.dpi)
        except DsspError as e:
            print(e)
            exit(1)

    # if we do wan tto save
    else:

        if args.output_file == 'USE_DEFAULT':
            outname = '%s.png'%(args.uniprot)
        else:
            outname = args.output_file

        dssp.graph_dssp_uniprot(final_name, title=graph_title, raw_vals=raw_vals, dis_threshhold = args.cutoff, exclude_disorder=exclude_disorder, DPI=args.dpi, output_file=outname)




