###
# week3sol.py
# Version: 1.2
# <*Python verion: 3.4>
# 
# Parse 3 files required to check parentage of individuals.
# 1. Script asks for the location of the SNP map file, parses it, then prints some information.
# 2. Script asks for the location of the informative SNPs file, parses it, then prints some information.
# 3. Script asks for the location of the genotype data.
# 4. Script extracts informative SNP positions from the SNP map.
# 5. Script parses the genotypes, filtering out all non-informative SNPs and exports the resulting data to a *.txt file
# then it extracts the files to it.
# 
# Usage:
# command line
# > python week3sol.py
# 
# <specify SNPmap location when promted>
# e.g., https://raw.githubusercontent.com/SRUCProgrammers/Challenge-Week-3/master/Illumina50kV2map.txt
# 
# <specify InformativeSNPs location when promted>
# e.g., https://raw.githubusercontent.com/SRUCProgrammers/Challenge-Week-3/master/parentageSNPs.txt
# 
# <specify SimulatedData location when promted>
# e.g., C:\Users\Scott\My Dropbox\WorkBox\Programming\SRUCProgrammers\week3challenge\mMatrixFileSimulated_54609_1000_1.dat
#
# By Scott J. Denholm
###
##############################
# import required libraries  #
##############################

import numpy as np 
import pandas as pd 

##############################
#   read in required data    #
##############################

SNPchip=input('Please specify SNP map file:   ')
print('Reading in SNP map data . . .')
SNPmap=pd.read_csv(SNPchip)
print('Read complete, printing number of rows and columns followed by data types and top 5 rows . . .')
print(SNPmap.shape)
print(SNPmap.dtypes)
print(SNPmap.head())

parentSNPs=input('Please specify informative SNPs file:  ')
print('Reading in informative SNPs . . .')
pSNPs=pd.read_csv(parentSNPs)
print('Read complete, printing number of rows and columns followed by data types and top 5 rows . . .')
print(pSNPs.shape)
print(pSNPs.dtypes)
print(pSNPs.head())

GMdata=input('Please specify genotype file:  ')

##########################################################################
# Join SNP position on genome from Illumina50kV2map.txt,i.e., SNPmap,    #
# to 108 informative SNPs from parentageSNPs.txt,i.e., pSNPs. Use pandas #
# left join feature and print top 5 rows of resulting output             #
##########################################################################

print('Obtaining SNP postions of informative SNPs from SNP map file . . .')
pSNPs_positions=pd.merge(pSNPs, SNPmap, on='snpName', how='left')
print('Process complete, printing number of rows and columns followed by data types and first 5 rows of data . . .')
print(pSNPs_positions.shape)
print(pSNPs_positions.dtypes)
print(pSNPs_positions.head())
print('Printing number of items in newly joined column . . .')
print(len(pSNPs_positions['position']))


print('Extracting informative SNP positions into a list . . .')

#############################################
# put informative SNP positions into a list #
#############################################

SNPpositions=list(pSNPs_positions['position'])
print('List of informative postions saved . . .')

################################################################
# create a new list with "position value - 1"                  #
# -> This is to conform to Python indexing from 0 instead of 1 #
################################################################

print('Re-indexing position list to conform with Python indexing format . . .')
SNPpositionsIndex=[x-1 for x in SNPpositions]
print('Printing number of items in list . . .')
print(len(SNPpositionsIndex))
print('Printing first and last 5 items in list')
print(SNPpositionsIndex[0:4]) ## print first 5 items in list ##
print("...")
print(SNPpositionsIndex[-5:]) ## print last 5 items in list ##

#############################
#   parse genotype matrix   #
#############################

#genotypes=pd.read_csv(GMdata, header=None, delim_whitespace=True)
#didn't work. No delimiters in data so file being read in as a 1000x1 vector. Need to define delimiter width.

####################################################################
# Create a list of 54,609 1s, i.e., the widths of each column      #
# since each character of the genome string is 1 column.           #
# Pass to the read file command to create 54609 columns of width 1 #
####################################################################

SNPwidth=[]

for i in range(0,len(SNPmap)):

    SNPwidth.append(int(1))

###########################################
# check 1st and last positions and length #
###########################################

#print(SNPwidth[0], SNPwidth[-1]) ##uncomment if required. print 1st and last elements of SNPwidth (both should be equal to 1)
#print(len(SNPwidth))             ##uncomment if required. Print length os SNPwidth (should be equal to number of rows in SNPmap)

print('Reading in genotypes. Filtering out all non-informative SNP positions . . .')
genotypes = pd.read_fwf(GMdata,header=None, widths=SNPwidth, usecols=SNPpositionsIndex)
print('Read complete, printing number of rows and columns followed by data types and top 5 rows . . .')
print(genotypes.shape)
print(genotypes.dtypes)
print(genotypes.head())
print(' ')
print('PARSING PROCESS COMPLETE')

######################################
# Save filtered data to a *.txt file #
######################################

print('EXPORTING FILTERED GENOTYPES TO *.txt file')
genotypes.to_csv('InformativeSNPsOnly.txt',index=False,header=True)
print(' ')
print('COMPLETE . . . data exported to InformativeSNPsOnly.txt')
