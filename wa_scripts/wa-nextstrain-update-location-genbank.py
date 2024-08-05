import argparse
import sys
import pandas as pd

parser = argparse.ArgumentParser(description='This script is part of the snakemake workflow that uses the \
    filtered metadata file from the Genbank ingest, the WA DOH metadata file, and updates the filtered \
    metadata file with the location information, specifically the Washington state counties for the \
    sequences in the file that will be used for Nextstrain. As a result, the build will display the \
    county location on the map. Example link to the build here: https://nextstrain.org/groups/waphl/ncov/wa/6m \n \
    Since this script is compatible with the wa_sc2 workflow to ingest the sequencing and metadata for the \
    WA-focused SARS-CoV-2 build, the file names should match in order for the entire workflow to run.')
parser.add_argument(help="File path to the input and output metadata files",
    type=str, dest="wa_data/filtered_metadata.tsv, wa_data/county_metadata.csv, wa_data/wa-metadata.tsv")

args = parser.parse_args()
print(args.help)

# read in the metadata files to be used for updating
def read_files(input_file_1, input_file_2):
    genbank_metadata = pd.read_csv(input_file_1, sep='\t', index_col=['strain'], low_memory=False)
    doh_metadata = pd.read_csv(input_file_2)
    return genbank_metadata, doh_metadata

# rename the columns in the WA metadata file to be
# consistent with nextstrain metadata file
def rename_columns(doh_metadata):
    doh_metadata = doh_metadata.rename(columns={
    'COUNTY_NAME': 'County',
    'SEQUENCE_GISAID_STRAIN': 'strain'})
    return doh_metadata

# set index for doh metadata
def set_index(doh_metadata):
    doh_metadata = doh_metadata.set_index('strain')
    return doh_metadata

# drop duplicates in index
def drop_index_dup(doh_metadata):
    doh_metadata = doh_metadata[~doh_metadata.index.duplicated(keep='first')]
    return doh_metadata

# create a new column called "location with the desired format
# e.g. North America / USA / Washington / King County
# update as of 240307 this formatting is no longer needed

# update location
def update_location(doh_metadata, genbank_metadata):
    doh_metadata['location'] = doh_metadata['County'] + ' County'
    # merge the dataframes on a common column
    merged_df = pd.merge(genbank_metadata, doh_metadata, on='strain')
    # update the location column in the genbank dataframe
    merged_df['location_x'] = merged_df['location_y']
    # drop the extra column (Location_y)
    merged_df.drop(['location_y'], axis=1, inplace=True)
    # rename the original Location column (Location_x)
    merged_df.rename(columns={'location_x': 'location'}, inplace=True)
    return merged_df

# processing the metadata files
def main(input_file_1, input_file_2, output_file):
    genbank_metadata, doh_metadata = read_files(input_file_1, input_file_2)
    doh_metadata = rename_columns(doh_metadata)
    doh_metadata = set_index(doh_metadata)
    doh_metadata = drop_index_dup(doh_metadata)
    merged_df = update_location(doh_metadata, genbank_metadata)
    merged_df.to_csv(output_file, sep='\t')
    print('Success! Exit Code 0')
    print("County level metadata has been added to the metadata file")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 ./wa_scripts/wa-nextstrain-update-location-genbank.py wa_data/filtered_metadata.tsv wa_data/county_metadata.csv wa_data/wa-metadata.tsv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
