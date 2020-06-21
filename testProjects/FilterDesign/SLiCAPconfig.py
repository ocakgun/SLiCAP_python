#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:10:18 2020

@author: anton
"""

LOGFILE         = True
LANGUAGE        = 'english' # Language for error and warnings:
                            # not yet implemented
DISP            = 4         # Numner of digits for floats in output
MATHML          = False     # If True: MathML, else MathJaX cloud for rendering
                            # math
STEPFUNCTION    = True      # Method for parameter stepping:
                            # True:  substitution of step variable(s) after 
                            #        calculation of numerator/denominator
                            #        Laplace functions
                            # False: substitution of step values in the matrix
DISPMAXRESULT   = False     # Displays result from Maxima CAS before it is
                            # converted to a sympy expression.
LAPLACE         = 's'       # Laplace veriable
FREQUENCY       = 'f'       # Frequency in Hz
OMEGA           = 'omega'   # Frequency in rad/s
MAXRECSUBST     = 10        # Maximum number of recursic=ve substitutions
HZ              = True      # If true: frequency in Hz, else rad/s
MAXSOLVE        = True      # If true: Maxima CAS is used as default solver, 
                            # else: Sympy

# PATHS: relative to the project path
HTMLPATH        = 'html/'   # path for html output
CIRCUITPATH     = 'cir/'    # path for .asc, .net, .cir, .sch files
LIBRARYPATH     = 'lib/'    # path for include and library files
TXTPATH         = 'txt/'    # path for text files (text2html)
CSVPATH         = 'csv/'    # path for CSV files (csv2html)
LATEXPATH       = 'tex/'    # path for LaTeX output saveTeX()
MATHMLPATH      = 'mathml/' # path for mathML output saveMathML()
IMGPATH         = 'img/'    # path for image files

# Default plot settings
figureAxisHeight= 5
figureAxisWidth = 7
plotFontSize    = 10
defaultColors   = ('r','b','g','c','m','y','k')
gainColors      = {'gain': 'b', 'asymptotic': 'r', 'loopgain': 'k',
                   'direct': 'g', 'servo': 'm', 'vi': 'c'}
defaultMarkers  = ['']
tableFileType   = 'csv'
figureFileType  = 'svg'
axisXscale      = 'linear'    # Scale for the x-axis can be 'linear' or 'log'
axisYscale      = 'linear'    # Scale for the y-axis can be 'linear' or 'log'
legendLoc       = 'best'

# Project information
PROJECT    = '4-th order Linkwitz-Riley Filter'
AUTHOR     = 'anton'
CREATED    = '2020-06-21 15:06:23.192395'
LASTUPDATE = '2020-06-21 18:56:37.689326'