# Imports.

import os
import glob
import re
import numpy as np
import pandas as pd

from .. import Global_Utilities as gu

# Function definitions.

def read_raw_data_file_1( filename, f, resin_data, file_data, data ):

    pattern = re.compile( r"^Resin(\d+)" )

    resin = int( pattern.search( f ).groups()[0] )

    dict_specimen_removed = {4:[0], 10:[2], 18:[2], 2:[5, 6], 8:[5, 6], 13:[5, 6], 22:[5, 6], 23:[5, 6]} #Why: Strain all zeros. Or not present.

    sheets = ["Sheet1", "Sheet2", "Sheet3", "Sheet4", "Sheet5", "Sheet6", "Sheet7"]

    for specimen, s in enumerate( sheets ):

        if resin in dict_specimen_removed.keys():

            if specimen in dict_specimen_removed[resin]:

                continue

        df = pd.read_excel( filename, s )

        crop = 0

        strain = df.iloc[:, 5].tolist()

        for i, j in enumerate( strain ):

            if j > 0.5:

                crop = i
                break

        for i in range( len( df.columns ) ):

            data[i].append( df.iloc[:, i].to_numpy( dtype = np.float64 )[crop:] )

        file_data.append( [resin, specimen, resin_data.loc[resin]["Label"] + ".{}".format( specimen ), ""] )

def extract_raw_data( directory, data_directory ):
    '''Extract the raw data from the files.'''

    resin_data = gu.get_list_of_resins_data( directory ) # Obtain the spreadsheet of data for the resins.

    resins = sorted( [os.path.basename( path ) for path in glob.glob( data_directory + "*" )], key = gu.sort_raw_files_1 )

    file_data, data = [], [[], [], [], [], [], [], []]

    pattern = re.compile( r"^Resin(\d+)" )

    for r in resins:

        filenames = sorted( [os.path.basename( path ) for path in glob.glob( data_directory + r + "/*" )], key = gu.sort_raw_files_1 )

        resin = int( pattern.search( r ).groups()[0] )

        for f in filenames:

            read_raw_data_file_1( data_directory + r + "/" + f, f, resin_data, file_data, data )

    return file_data, data

def standardise_data( data ):
    '''Standardise data.'''

    pass

def add_description_to_file_data( file_data ):
    '''Add descriptions in the form of letters to each specimen.'''

    pass

def read_files_and_preprocess( directory, data_directory, merge_groups ):
    '''Read files and preprocess data.'''

    file_data, data = extract_raw_data( directory, data_directory )

    standardise_data( data )

    add_description_to_file_data( file_data )

    if merge_groups:

        gu.merge( file_data )

    return file_data, data

def write_csv( output_directory, file_data, data ):
    '''Write read and preprocessed data to a .csv file.'''

    for i, f in enumerate( file_data ):

        array = np.array( data[0][i] )[:, np.newaxis]

        for j in range( 1, 7 ):

            array = np.hstack( (array, np.array( data[j][i] )[:, np.newaxis]) )

        np.savetxt( output_directory + "TT/Condensed_Data/Resin{}_{}_.csv".format( f[0], f[1] ), array, delimiter = ",", fmt = "%.4f" )

    array = np.array( file_data )

    np.savetxt( output_directory + "TT/File_Data/file_data.csv", array, delimiter = ",", fmt = "%s" )

def read_csv( directory, output_directory, merge_groups ):
    '''Read the preprocessed .csv files.'''

    resin_data = gu.get_list_of_resins_data( directory ) # Obtain the spreadsheet of data for the resins.

    file_data = []

    df = pd.read_csv( output_directory + "TT/File_Data/file_data.csv", sep = ",", header = None )

    for i in range( len( df.index ) ):

        resin = df.iloc[i, 0]
        specimen = df.iloc[i, 1]

        file_data.append( [resin, specimen, resin_data.loc[resin]["Label"] + ".{}".format( specimen ), ""] )

    data = [[], [], [], [], [], [], []]

    filenames = sorted( [os.path.basename( path ) for path in glob.glob( output_directory + "TT/Condensed_Data/*" )], key = gu.sort_raw_files_3 )

    for f in filenames:

        df = pd.read_csv( output_directory + "TT/Condensed_Data/" + f, sep = ",", header = None )

        for i in range( len( df.columns ) ):

            data[i].append( df.iloc[:, i].to_numpy( dtype = np.float64 ) )

    add_description_to_file_data( file_data )

    if merge_groups:

        gu.merge( file_data )

    return file_data, data

def remove_files( file_data, data ):
    '''Remove files not needed/wanted for analysis by searching for letters in file descriptions.'''

    files_to_remove = []

    files_to_remove.reverse()

    for r in files_to_remove:

        file_data.pop( r )

        for i in range( len( data ) ):

            data[i].pop( r )

def compute_mean( output_directory, file_data, data):
    '''Compute the mean data for each resin.'''

    pass

def read_mean( output_directory, data ):
    '''Read the computed means for each resin from a file.'''

    pass
