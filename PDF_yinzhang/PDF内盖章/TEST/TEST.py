#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date:2020-12-03
# Author:Runker54
# -----------------------
# !/usr/bin/env python3

# Ref:
# http://stackoverflow.com/questions/2925484/place-image-over-pdf
# http://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python

# TODO:
# *) [D] Extend transparency of white background
# *) [D] Test with multi-page pdf file
# *) [D] Check if image file and pdf file exist or not
# *) [D] Check if page number is greater than the number of pages of pdf file
# *) [D] Default parameters dictionary including mask
# *) [D] Update helptext
# *) [D] Add xoffset and yoffset
# *) [D] Test for multiple signatures on same page
# *) [D] Fix rotation
# *) [D] Test for multi-page pdf file
# *) [D] Test for multiple signatures on different page
# *) [D] Fix page number variables
# *) [D] Print dictionary in a function
# *) [Won't fix] dpi of template image file has to be 300.
#       Option to change the dpi? higher dpi would take longer time to process.
#       dpi has to be 300, is mentioned in the helptext.
# *) [D] Check dpi and give a warning sign in case dpi is not 300
# *) [D] Sometimes if the correct page is not mentioned, script still inserts
#       signature at wrong place without any error/warning.
# *) [D] Multiple coordinate matches
# *) [D] Option for threshold
# *) [D] Combine sign-pdf.py sign-pdf2.py
# *) [D] Check on windows
# *) Check for extension (should be png) and transparency of signature files

# To make the program compatible with python2
# from __future__ import print_function
from glob import glob
import sys
import re
import time
from os.path import basename, exists, splitext, join, isfile, isdir, dirname
from os import makedirs, remove
from shutil import move
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, grey
from io import BytesIO
from math import floor
import PIL
import random
import wand.image
import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy


# import six  # For print() function compatibility of python 2 and 3

class ImageOptions:

    def __init__(self, info={}):
        """Optionally pass in an initial dictionary of items"""
        if type(info) != type({}):
            raise TypeError("ImageOptions requires a dictionary, but was given %s" % type(info))
        self.info = info
        return

    def add_info(self, info_dict):
        """Add information via a dictionary"""
        if type(info_dict) != type({}):
            raise TypeError("Add_info requires a dictionary, but was given %s"
                            % type(info_dict))

        for key in info_dict.keys():
            self.info[key] = info_dict[key]

    def has_info(self, key):
        """Check whether the required key is present or not"""
        try:
            value = self.info[key]
            return True
        except KeyError:
            return False

    def update_info(self, key, value):
        """ Update the dictionary as long as the key already exits."""
        if self.has_info(key):
            self.info[key] = value
            return True
        else:
            return False

    def print_info(self, key):
        """Return the info corresponding to key"""
        return self.info[key]

    def get_dict(self):
        return self.info


def get_image_size(ifile):
    im = PIL.Image.open(ifile)
    img_wd, img_ht = im.size

    return img_wd, img_ht


def check_files(myfiles, ext=None):
    for ifile in myfiles:
        if not isfile(ifile):
            sys.exit("File '%s' doesn't exist. Aborting." % ifile)
        if ext:
            fileext = splitext(basename(ifile))[1]
            if fileext.lower() != ext.lower():
                print("Warning: The file '%s' doesn't have the extension '%s'."
                      % (ifile, ext))
                print("Might produce unexpected result.")
    return


# https://stackoverflow.com/questions/51417774/how-to-determine-if-a-png-picture-has-a-transparency-layer-in-python?noredirect=1&lq=1
def check_alpha_channel(imgfile):
    fileext = splitext(basename(imgfile))[1]

    # Check whether imgfile is a png file or not
    if fileext.lower() != '.png':
        #         print("Not a png file.")
        return False
    else:

        pic = plt.imread(imgfile)

        if pic.shape[2] == 3:
            #             print("No alpha channel!")
            return False
        elif pic.shape[2] == 4:
            #             print("There's an alpha channel!")
            if np.allclose(pic[:, :, 3], 1):
                #                 print("     Alpha not used because 1 everywhere!")
                return False
            else:
                #                 print("     Alpha channel is used.")
                return True


def check_parameters(string, char, n1, n2):
    nparams = string.count(char) + 1

    if nparams == n1:
        return True
    elif nparams == n2:
        return False
    else:
        print("Number of parameters should either be %s or %s. Aborting."
              % (n1, n2))
        sys.exit(1)


def split_parameters(iopts, dflt_params, othr_params):
    # Copy the dictionary
    data = copy.deepcopy(dflt_params)

    strsep = othr_params['fldsep']
    p6 = othr_params['p6']
    p7 = othr_params['p7']

    data['viacoord'] = check_parameters(iopts, strsep, p6, p7)

    if data['viacoord']:

        # Via coordinates
        ifile, xcrd, ycrd, sclng, pgn, rot = None, None, None, None, None, None
        ifile, xcrd, ycrd, sclng, pgn, rot = iopts.split(',')
        data['xcord'] = float(xcrd)
        data['ycord'] = float(ycrd)

    else:

        # Via templates
        ifile, itmplt, xofst, yofst, sclng, pgn, rot = (None, None, None, None,
                                                        None, None, None)
        ifile, itmplt, xofst, yofst, sclng, pgn, rot = iopts.split(',')

        # Check the existence of the template image file
        check_files([itmplt])
        data['template'] = itmplt

        if xofst.upper() != 'D':
            data['xoffset'] = float(xofst)

        if yofst.upper() != 'D':
            data['yoffset'] = float(yofst)

    # Check the existence of the signature image file
    # Also check if the signature file is a png file or not
    check_files([ifile], '.png')
    using_alpha = check_alpha_channel(ifile)
    if using_alpha:
        print("Warning: Signature file '%s' has transparent background."
              % (ifile))
        print("Might produce unexpected result.")

    if sclng.upper() != 'D':
        data['scaling'] = sclng
    data['scaling'] = float(re.sub('%', '', data['scaling']).strip())

    if pgn.upper() != 'D':
        data['pagenum'] = int(pgn)

    if rot.upper() != 'D':
        data['angle'] = float(rot)

    # Rotate image file (if necessary)
    rfile, rotstat = rotate_image(ifile, data['angle'])
    data['image'] = rfile
    data['rotstat'] = rotstat
    data['oldimage'] = ifile

    img_wd, img_ht = get_image_size(data['image'])

    xsz, ysz = get_scaled_size(data['scaling'], img_wd, img_ht)
    data['xsize'] = xsz
    data['ysize'] = ysz

    return data


def collect_all_imgs(cli_iopts, aimgs, dflt_params, othr_params):
    data = split_parameters(cli_iopts, dflt_params, othr_params)
    imgopts = ImageOptions(data)
    aimgs.append(imgopts)

    return aimgs


def get_mask(msk_comma):
    msk_list = ([int(x) for x in msk_comma.split(',')
                 if x.strip().isdigit()])

    return msk_list


# https://stackoverflow.com/questions/5252170/specify-image-filling-color-when-rotating-in-python-with-pil-and-setting-expand/5253554
def rotate_image(image, angle):
    rotated_img = str(random.randint(10000, 100001)) + '.png'
    rotstat = None
    #     angle = float(angle)

    if angle != 0:
        #         print('Rotating image')
        # original image
        img = PIL.Image.open(image)
        # converted to have an alpha layer
        im2 = img.convert('RGBA')
        # rotated image
        rot = im2.rotate(angle, expand=1)
        # a white image same size as rotated image
        white_img = PIL.Image.new('RGBA', rot.size, (255,) * 4)
        # create a composite image using the alpha layer of rot as a mask
        out = PIL.Image.composite(rot, white_img, rot)
        # save your work (converting back to mode='1' or whatever..)
        out.convert(img.mode).save(rotated_img)
        rotstat = True
    else:
        #         print('No rotation')
        rotated_img = image
        rotstat = False

    return (rotated_img, rotstat)


# Delete file if required
def delete_file(del_file, delstat):
    if delstat:
        remove(del_file)

    return


def drawGrid(pfrpg):
    # Step size of grid
    h = 25

    [llx, lly, urx, ury] = pfrpg.mediaBox

    packet = BytesIO()
    can = canvas.Canvas(packet)
    can.setPageSize([urx, ury])

    nx = int(floor((urx - llx) / h)) + 1
    ny = int(floor((ury - lly) / h)) + 1

    xlist = []
    for i in range(nx + 1):
        xlist.append(llx + i * h)

    ylist = []
    for j in range(ny + 1):
        ylist.append(lly + j * h)

    can.setStrokeColor(pink)
    can.grid(xlist, ylist)

    can.setStrokeColor(grey)
    can.setFont("Times-Roman", 8)

    for i in range(0, nx, 2):
        can.drawString(xlist[i], 0, str(xlist[i]))

    for j in range(0, ny, 2):
        can.drawString(0, ylist[j], str(ylist[j]))

    can.save()

    packet.seek(0)
    grid_page = PdfFileReader(packet).getPage(0)

    pfrpg.mergePage(grid_page)
    return pfrpg


def scaling(len1, len2, slen1):
    slen2 = int(slen1 * len2 / len1)
    return slen2


def get_scaled_size(scl, img_wd, img_ht):
    xsz, ysz = None, None
    xsz = scaling(100, scl, img_wd)
    ysz = scaling(100, scl, img_ht)

    return xsz, ysz


def insertImage(pfrpg, cimg):
    ifile = cimg.info['image']
    xcrd = cimg.info['xcord']
    ycrd = cimg.info['ycord']
    xsz = cimg.info['xsize']
    ysz = cimg.info['ysize']
    msk = cimg.info['mask']

    iTemp = BytesIO()
    imgDoc = canvas.Canvas(iTemp)

    # Draw image on Canvas and save PDF in buffer
    imgDoc.drawImage(ifile, xcrd, ycrd, width=xsz, height=ysz,
                     mask=msk)  # masking colors, usually background
    imgDoc.save()

    # Use PyPDF to merge the image-PDF into the template
    overlay = PdfFileReader(BytesIO(iTemp.getvalue())).getPage(0)
    pfrpg.mergePage(overlay)


def print_dict(dicti, datatype=False):
    for key in sorted(dicti):
        #         six.print_("     %s\t= %s" % (key, dicti[key]),end='')
        print("     %s\t= %s" % (key, dicti[key]), end='')
        if datatype:
            print("%s" % type(dicti[key]))
        else:
            print("")

    return


# https://stackoverflow.com/questions/27826854/python-wand-convert-pdf-to-png-disable-transparent-alpha-channel/36279291#36279291
def convert_pdf(filename, pypgn, img_format='jpg', resolution=300):
    """ Convert a PDF into images.
        All the pages will give a single png file with format:
        {pdf_filename}-{page_number}.png
        The function removes the alpha channel from the image and
        replace it with a white background.
    """

    all_pages = wand.image.Image(filename=filename, resolution=resolution)
    # Python numbers start from zero
    single_image = all_pages.sequence[pypgn]
    with wand.image.Image(single_image) as img:
        # Set white background.
        img.background_color = wand.image.Color('white')
        # Remove transparency and replace with bg.
        img.alpha_channel = 'remove'

        image_filename = str(random.randint(10000, 100001)) + '.' + img_format
        img.save(filename=image_filename)
        return image_filename


# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
def get_coordinates(imgfile, templatefile, imgdpi, thrshld):
    meth = 'cv2.TM_CCOEFF_NORMED'
    method = eval(meth)
    inch_to_pt = 72

    # Read the main image file
    img_rgb = cv2.imread(imgfile)
    #       width, height = img_rgb.shape[::-1]
    height, width = img_rgb.shape[:2]
    #     print width, height

    # Convert it to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Read the template file
    tmplt_rgb = cv2.imread(templatefile, 0)
    # Store width and heigth of template in w and h
    h, w = tmplt_rgb.shape[:2]
    #     w, h = tmplt_rgb.shape[::-1]

    # Perform match operations.
    res = cv2.matchTemplate(img_gray, tmplt_rgb, method)

    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= thrshld)

    # Create an array for multiple matches
    coord = []

    # Get the coordinates in case of multiple match
    for pt in zip(*loc[::-1]):
        ulx, uly, lrx, lry = pt[0], pt[1], pt[0] + w, pt[1] + h

        # Draw a rectangle around the matched region
        #         cv2.rectangle(img_rgb, (ulx, uly), (lrx, lry), (0,0,255), 2)
        #         print ulx, uly

        # x_pt = x_inch * DPI
        # y_pt = y_inch * DPI
        # 1 inch = 72 pt
        # Change origin from top left corner to bottom left corner
        # Convert to pt and round to nearest integer
        ulx_pt = int(ulx * inch_to_pt / float(imgdpi) + 0.5)
        uly_pt = int((height - uly) * inch_to_pt / float(imgdpi) + 0.5)

        coord.append([ulx_pt, uly_pt])

    if not coord:
        return False
    else:
        return coord


# Check dpi of template imagefile. It should match with the std dpi
def check_dpi(imgfile, stddpi):
    xdpi, ydpi = None, None

    im = PIL.Image.open(imgfile)
    xdpi, ydpi = im.info['dpi']

    if xdpi and ydpi:
        if xdpi != stddpi and ydpi != stddpi:
            print("Warning: Template file '%s' doesn't have dpi of %d"
                  % (imgfile, stddpi))
            print("Might produce unexpected result.")
            return
        else:
            # dpi matches with stddpi. Don't do anything.
            #             print("xdpi = %s, ydpi = %s" %(xdpi, ydpi))
            pass
    else:
        print("Couldn't detect dpi of template file '%s'" % (imgfile))
        print("Might have unexpected result.")


def helptext(scrptnm, athr, vrsn, dflt_params, shw_grd, multpl_mtchs):
    print("Script to insert an image file in a pdf file")
    print("Usage: %s [options] pdffile" % scrptnm)
    print("Author: %s" % athr)
    print("Version: %s" % vrsn)
    print("Options:")
    print("-h|--help        Show this help and exit.")
    print("")
    print("-i signfile,xcord,ycord,scale,pagenum,rotation")
    print("  Insert image 'signfile' at coordinates  'xcord', 'ycord' at a")
    print("  scale of 'scale' of the original image on page 'pagenum'")
    print("  with rotation of 'rotation' angle.")
    print("")
    print("-i signfile,templatefile,xoffset,yoffset,scale,pagenum,rotation")
    print("  Searching the page for 'templatefile' and insert the signature")
    print("  'signfile' file on top of this. Use 'xoffset' and 'yoffset' to")
    print("  to offset the insertion of the signature.")
    print("  The signature file will be scaled by 'scale',")
    print("  inserted on the page 'pagenum', and ")
    print("  rotated by the angle 'rotation'.")
    print("")
    print("-g|--grid        Show grid. Default: %s." % shw_grd)
    print("--no-grid        Do not show grid.")
    print("")
    print("--multiple       Consider multiple matches for same template."
          + " Default: %s." % multpl_mtchs)
    print("--no-multiple    Do not consider multiple matches for same"
          + " template.")
    print("")
    print("-t|--threshold threshold_value")
    print("  Only applies to insertion of signfile via template.")
    print("  Value must be 0-1. Signifies the match of template file")
    print("  in the pdf file.")
    print("")
    print("-m Ri,Rf,Gi,Gf,Bi,Bf")
    print("  Make the RGB colors in the range 0-255 transparent.")
    print("  For example with '0,4,30,40,125,139' it will mask out any pixels")
    print("  with a Red value from 0 to 3, Green from 30 t0 39 and Blue from")
    print("  125 to 138 (on a scale of 0-255).")
    print("  Default value: %s." % dflt_params['mask'])
    print("  The masking and threshold value is common for all images.")
    print("")
    print("  Default parameters are:")
    print_dict(dflt_params)
    print("  The xoffset, yoffset, dpi and threshold are meant only for")
    print("  insertion of signfile via template file.")
    print("")
    print("Note: The dpi of the template image file should be %s."
          % dflt_params['dpi'])
    print("")
    print("Ex1: %s" % scrptnm),
    print("-i sign1.jpg,template1.jpg,10,20,15%,2,45 *.pdf"),
    print("-i sign2.png,template2.jpg,d,d,d,d,d"),
    print("-i sign3.jpg,400,235,d,d,d")
    print("")
    print("The above command inserts the following images:")
    print(" 'sign1.jpg' on top of 'template1.jpg' with xoffset and yoffset of")
    print("     10 and 20 respectively, at 15% scale of original size on")
    print("     page 2, with a rotation of 45 degree angle.")
    print(" 'sign2.png' on top of 'template2.jpg' with default parameters.")
    print(" 'sign3.png' at (400, 235) with default parameters.")

    return


if __name__ == '__main__':

    allpdf = []
    allimgs = []
    outdir = 'output'
    show_grid = False
    multiple_matches = False
    mask_cli = None
    threshold_cli = None
    default_parameters = {'scaling': '15%', 'pagenum': 1, 'angle': 0,
                          'mask': '254,255,254,255,254,255',
                          'viacoord': None,
                          # Only for viatemplate
                          'xoffset': 0.0, 'yoffset': 0.0,
                          'dpi': 300, 'threshold': 0.9}

    other_parameters = {'fldsep': ',', 'p6': 6, 'p7': 7}

    common_image_info = {}

    scriptname = basename(sys.argv[0])
    author = 'Anjishnu Sarkar'
    version = '0.11'

    # Number of arguments supplied via cli
    numargv = len(sys.argv) - 1
    # Argument count
    iargv = 1

    # Parse cli options
    while iargv <= numargv:

        if sys.argv[iargv] == "-h" or sys.argv[iargv] == "--help":
            helptext(scriptname, author, version, default_parameters,
                     show_grid, multiple_matches)
            sys.exit()

        elif re.search(".pdf$", sys.argv[iargv]):
            allpdf.extend(glob(sys.argv[iargv]))

        elif sys.argv[iargv] == '-g' or sys.argv[iargv] == '--grid':
            show_grid = True

        elif sys.argv[iargv] == '--no-grid':
            show_grid = False

        elif sys.argv[iargv] == "-i":
            cli_ioptions = sys.argv[iargv + 1]
            allimgs = collect_all_imgs(cli_ioptions, allimgs,
                                       default_parameters, other_parameters)
            iargv += 1

        elif sys.argv[iargv] == "-m" or sys.argv[iargv] == '--mask':
            mask_cli = sys.argv[iargv + 1]
            iargv += 1

        elif sys.argv[iargv] == "-t" or sys.argv[iargv] == '--threshold':
            threshold_cli = sys.argv[iargv + 1]
            iargv += 1

        elif sys.argv[iargv] == '--multiple':
            multiple_matches = True

        elif sys.argv[iargv] == '--no-multiple':
            multiple_matches = False

        else:
            print("%s: Unspecified option: '%s'. Aborting."
                  % (scriptname, sys.argv[iargv]))
            sys.exit(1)

        iargv += 1

    # Sort list of images in place
    kmax = len(allimgs)  # Maximum images to be inserted

    if mask_cli:
        mask = get_mask(mask_cli)
    else:
        mask = get_mask(default_parameters['mask'])
    common_image_info.update({'mask': mask})

    #### Only for viatemplate #########
    if threshold_cli:
        threshold = float(threshold_cli)
    else:
        threshold = default_parameters['threshold']
    common_image_info.update({'threshold': threshold})
    #############

    # Add common image information to all images
    for k in range(kmax):
        allimgs[k].add_info(common_image_info)

    # Check if allpdf list is empty or not
    if not allpdf:
        print("List of pdf is empty or supplied pdf file not found in the")
        print("current working directory.")
        sys.exit(1)

    # Total number of pdf files
    npdf = len(allpdf)
    i = 0

    for inpdf in allpdf:

        check_files([inpdf])

        filepath = dirname(inpdf)
        filebase = basename(inpdf)
        filename = splitext(filebase)[0]

        # Create the output directory
        outdirpath = join(filepath, outdir)
        if not isdir(outdirpath):
            makedirs(outdirpath)

        outpdf = filename + '_signed.pdf'
        output = PdfFileWriter()

        pdf = PdfFileReader(open(inpdf, 'rb'))
        totpgs = pdf.getNumPages()

        # For each page of the pdf file
        for pypgn in range(totpgs):

            pfrpage = PdfFileReader(open(inpdf, 'rb')).getPage(pypgn)

            for k in range(kmax):

                img_pgn_opt = allimgs[k].info['pagenum']
                # Python pagenumber starts from zero
                img_pypgn_opt = img_pgn_opt - 1

                # If page number supplied is greater than number of pages
                # of the pdf file.
                if img_pgn_opt > totpgs:
                    print("Page number option supplied with '%s' image file"
                          % allimgs[k].info['image']
                          + " exceeds the total number of pages of '%s' pdf"
                          % inpdf
                          + " file. Aborting.")
                    sys.exit(1)

                if pypgn == img_pypgn_opt:

                    if allimgs[k].info['viacoord']:

                        # If insert image viacoord
                        # Insert image in the pdf file
                        insertImage(pfrpage, allimgs[k])

                    else:
                        # If insert image viatemplate
                        tmpimgfile = convert_pdf(inpdf, pypgn, 'jpg',
                                                 allimgs[k].info['dpi'])

                        # Check dpi of template imagefile.
                        check_dpi(allimgs[k].info['template'],
                                  allimgs[k].info['dpi'])

                        coordinate_list = get_coordinates(tmpimgfile,
                                                          allimgs[k].info['template'],
                                                          allimgs[k].info['dpi'],
                                                          allimgs[k].info['threshold'])

                        # Delete temporary image of pdf file
                        delete_file(tmpimgfile, True)

                        # If coordinate list is empty (no match found), continue
                        # to next signature
                        if not coordinate_list:
                            print("Couldn't find match of template file"
                                  + " '%s' in page %s of '%s'."
                                  % (allimgs[k].info['template'], pypgn + 1,
                                     inpdf))
                            print("Not inserting the '%s' in page %s."
                                  % (allimgs[k].info['image'], pypgn + 1))
                            continue

                        # Based on threshold the number of matches
                        # we have had
                        num_matches = len(coordinate_list)

                        # If multiple matches is not allowed then
                        # consider only the first match.
                        if not multiple_matches:
                            num_matches = 1

                        # For multiple matches insert multiple signs
                        for j in range(num_matches):
                            xcrd, ycrd = coordinate_list[j]

                            # Offset the insertion of the signature file
                            xcrd = xcrd + allimgs[k].info['xoffset']
                            ycrd = ycrd + allimgs[k].info['yoffset']

                            coordinates = {'xcord': xcrd, 'ycord': ycrd}

                            allimgs[k].add_info(coordinates)

                            # Insert image in the pdf file
                            insertImage(pfrpage, allimgs[k])

            if show_grid:
                pfrpage = drawGrid(pfrpage)

            # Add the page to the output file
            output.addPage(pfrpage)

        # Save the result
        output.write(open(outpdf, "wb"))

        # Move the output to the output directory
        dest = join(outdirpath, filebase)
        move(outpdf, dest)

        i = i + 1
        print("%s/%s: Created '%s'" % (i, npdf, dest))

        time.sleep(1)

    # Delete any temporary rotated image file
    for k in range(kmax):
        delete_file(allimgs[k].info['image'], allimgs[k].info['rotstat'])