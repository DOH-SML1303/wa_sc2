import sys
import pandas as pd

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
#doh_metadata['location'] = 'North America / USA / Washington / ' + doh_metadata['County'] + ' County'
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
