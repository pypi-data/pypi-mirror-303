# Imports

import pandas as pd
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import rpy2.robjects as robjects

from . import Utilities as util

from .. import Global_Utilities as gu

# Function definitions.

def source_R_functions( directory ):

    r = robjects.r
    r['source']( directory + 'rHDPE_R_Functions.R' )

def authorise_googledrive( directory ):

    robjects.globalenv['authorise_googledrive']( directory )

def read_googlesheet_via_R( filename ):

    read_googlesheet = robjects.globalenv['read_googlesheet']

    rdf = read_googlesheet( filename )

    with localconverter( robjects.default_converter + pandas2ri.converter ):

        pydf = robjects.conversion.rpy2py( rdf )

    return pydf

def read_files_and_preprocess( directory, output_directory, shiny, datasets_to_read, sample_mask ):

    if shiny:

        source_R_functions( directory )

        authorise_googledrive( directory )

    resin_data = gu.get_list_of_resins_data( directory )

    dataset_names = ["FTIR", "DSC", "TGA", "Rheology", "TT", "Colour", "SHM", "TLS", "ESCR", "FTIR2", "FTIR3", "TGA_SB"]

    dataset_names = [dataset_names[i - 1] for i in datasets_to_read]

    dataset = []

    for n in dataset_names:

        if n == "FTIR2":

            df = pd.read_csv( output_directory + "FTIR/Integral_Analysis/Mean_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        elif n == "FTIR3":

            df = pd.read_csv( output_directory + "FTIR/Component_Analysis/Features/Mean_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        elif n == "TGA_SB":

            df = pd.read_csv( output_directory + "TGA/Sandbox/Mean_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        else:

            if shiny:

                try:

                    df = pd.read_csv( output_directory + n + "/Features/Mean_Features.csv" )

                    df.drop( columns = [df.columns[0]], inplace = True )

                except FileNotFoundError:

                    print( "File not found on server, getting it from Google Drive." )

                    df = read_googlesheet_via_R( "~/Input/Sheets/" + n + "/Mean_Features" )

            else:

                df = pd.read_csv( output_directory + n + "/Features/Mean_Features.csv" )

                df.drop( columns = [df.columns[0]], inplace = True )

        dataset.append( df )

    for i in range( len( dataset ) ):

        samples_present = dataset[i].iloc[:, 0].tolist()

        sample_mask = gu.remove_redundant_samples( sample_mask, samples_present )

    #===============

    # Extracting the whole dataset as a .csv.

    # features_2, feature_names_2, total_samples_present = util.compile_full_dataset_of_features( dataset )
    #
    # features_2_df = gu.array_with_column_titles_and_label_titles_to_df( features_2, feature_names_2, total_samples_present )
    #
    # features_2_df.drop( columns = ["TT_SHM"], inplace = True )
    # features_2_df.drop( index = [24, 401, 402, 403, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416], inplace = True )
    #
    # features_2_df = features_2_df.set_axis( [resin_data.loc[i]["Label"] for i in features_2_df.index], axis = "index" )
    #
    # features_2_df.to_csv( directory + "Global/Output/Dataset/Full_Dataset.csv" )

    #===============

    features, feature_names = util.produce_full_dataset_of_features( dataset, sample_mask )

    rank_features = util.rank_features( features )

    features_df = gu.array_with_column_titles_and_label_titles_to_df( features, feature_names, sample_mask )

    rank_features_df = gu.array_with_column_titles_and_label_titles_to_df( rank_features, feature_names, sample_mask )

    dataset = []

    for n in dataset_names:

        if n == "FTIR2":

            df = pd.read_csv( output_directory + "FTIR/Integral_Analysis/Std_of_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        elif n == "FTIR3":

            df = pd.read_csv( output_directory + "FTIR/Component_Analysis/Features/Std_of_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        elif n == "TGA_SB":

            df = pd.read_csv( output_directory + "TGA/Sandbox/Std_of_Features.csv" )

            df.drop( columns = [df.columns[0]], inplace = True )

        else:

            if shiny:

                try:

                    df = pd.read_csv( output_directory + n + "/Features/Std_of_Features.csv" )

                    df.drop( columns = [df.columns[0]], inplace = True )

                except FileNotFoundError:

                    print( "File not found on server, getting it from Google Drive." )

                    df = read_googlesheet_via_R( "~/Input/Sheets/" + n + "/Std_of_Features" )

            else:

                df = pd.read_csv( output_directory + n + "/Features/Std_of_Features.csv" )

                df.drop( columns = [df.columns[0]], inplace = True )

        dataset.append( df )

    std_of_features, _ = util.produce_full_dataset_of_features( dataset, sample_mask )

    std_of_features_df = gu.array_with_column_titles_and_label_titles_to_df( std_of_features, feature_names, sample_mask )

    return features_df, std_of_features_df, rank_features_df

def read_unnormalised_data( output_directory, feature_1, feature_2, sample_mask ):

    dataset_names = ["FTIR", "DSC", "TGA", "Rheology", "TT", "Colour", "SHM", "TLS", "ESCR"]

    dataset, std_dataset = [], []

    for n in dataset_names:

        df = pd.read_csv( output_directory + n + "/Features/Mean_Features_Unnormalised.csv" )

        if feature_1[0] not in df.columns.tolist():

            if feature_2[0] not in df.columns.tolist():

                continue

        df.drop( columns = [df.columns[0]], inplace = True )

        dataset.append( df )

        df = pd.read_csv( output_directory + n + "/Features/Std_of_Features_Unnormalised.csv" )

        df.drop( columns = [df.columns[0]], inplace = True )

        std_dataset.append( df )

    for i in range( len( dataset ) ):

        samples_present = dataset[i].iloc[:, 0].tolist()

        sample_mask = gu.remove_redundant_samples( sample_mask, samples_present )

    features, feature_names = util.produce_full_dataset_of_features( dataset, sample_mask )

    features_df = gu.array_with_column_titles_and_label_titles_to_df( features, feature_names, sample_mask )

    std_of_features, _ = util.produce_full_dataset_of_features( std_dataset, sample_mask )

    std_of_features_df = gu.array_with_column_titles_and_label_titles_to_df( std_of_features, feature_names, sample_mask )

    return features_df, std_of_features_df
