import matplotlib
matplotlib.use('Agg')
import os
import argparse
import ehtim as eh

#-------------------------------------------------------------------------------
# Load command-line arguments
#-------------------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Script to convert EHT_Difmap fits files to pdf images")
parser.add_argument('-i', '--infile' , default=""   , help="input FITS file")
parser.add_argument('-o', '--outfile', default=""   , help="output PDF file")
parser.add_argument('-r', '--regrid' , default=False, help="regrid image object"              , action='store_true')
parser.add_argument('-c', '--center' , default=False, help="center image object"              , action='store_true')
parser.add_argument('-s', '--scale'  , default=False, help="display scale in output"          , action='store_true')
parser.add_argument('-b', '--beam'   , default=False, help="display beam size in output"      , action='store_true')
parser.add_argument('-a', '--all'    , default=False, help="perform all post-processing steps", action='store_true')
args = parser.parse_args()

# Default location if not specified -- should be the location where DIFMAP is outputting files, i.e., the directory it was called in
if(args.outfile == ""):
    args.outfile = '../data/difmap-pdfs/'+args.infile[:-4]+'pdf'

print("Exporting PDF to", args.outfile)

if(args.scale or args.all): scale = 'scale'
else: scale = 'none'

# Load fits file into image object
im_obj = eh.image.load_fits(args.infile)
if(args.center or args.all): im_obj = im_obj.shift([8, 0]) # Not an exact value, but a close estimate
if(args.regrid or args.all): im_obj = im_obj.regrid_image(128*eh.RADPERUAS, 64)
params = [9.696e-11, 9.696e-11, 0] # This is for DIFMAP (20 uas) -- do NOT blur, as it is already applied. This is used only for display()’s beamparams

if(args.beam or args.all): im_obj.display(cbar_unit=['Tb'], label_type=scale, beamparams=params, export_pdf=args.outfile)
else: im_obj.display(cbar_unit=['Tb'], label_type=scale, export_pdf=args.outfile)