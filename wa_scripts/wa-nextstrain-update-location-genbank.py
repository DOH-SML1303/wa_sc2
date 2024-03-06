import sys
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 ./wa_scripts/wa-nextstrain-update-location-genbank_smk.py wa_data/test_filtered_metadata.tsv wa_data/county_metadata.csv wa_data/test_wa-metadata.tsv")
        sys.exit(1)

input_file_1 = sys.argv[1]
input_file_2 = sys.argv[2]
output_file = sys.argv[3]

# read in files
genbank_metadata = pd.read_csv(input_file_1, sep='\t', index_col=['strain'], low_memory=False)
doh_metadata = pd.read_csv(input_file_2)

# rename county column
doh_metadata = doh_metadata.rename(columns={'COUNTY_NAME': 'County',
                                            'SEQUENCE_GISAID_STRAIN': 'strain'})

# set index for doh metadata
doh_metadata = doh_metadata.set_index('strain')

# drop duplicates in index
doh_metadata = doh_metadata[~doh_metadata.index.duplicated(keep='first')]

# create a new column called "location with the desired format
# e.g. North America / USA / Washington / King County
doh_metadata['location'] = 'North America / USA / Washington / ' + doh_metadata['County'] + ' County'

# merge the dataframes on a common column
merged_df = pd.merge(genbank_metadata, doh_metadata, on='strain')

# update the location column in the genbank dataframe
merged_df['location_x'] = merged_df['location_y']

# drop the extra column (Location_y)
merged_df.drop(['location_y'], axis=1, inplace=True)

# rename the original Location column (Location_x)
merged_df.rename(columns={'location_x': 'location'}, inplace=True)

# fill nas in the location column
merged_df['location'] = merged_df['location'].fillna('North America / USA / Washington')

# write out to tsv file
merged_df.to_csv(output_file, sep='\t')

print("County level metadata has been added to the metadata file")
