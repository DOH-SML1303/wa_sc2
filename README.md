# wa_sc2
WA-focused build for ncov Nextstrain

# Setup
First, install the [ncov nextstrain pipeline](https://github.com/nextstrain/ncov) and clone the ncov repository using `git clone https://github.com/nextstrain/ncov` or `gh repo clone nextstrain/ncov`.

Next, clone this repository in the `ncov` folder. You can do this in the command-line terminal by navigating to the `ncov` repository using `cd ncov` and then cloning the repository using `git clone https://github.com/DOH-SML1303/wa_sc2.git` or `gh repo clone DOH-SML1303/wa_sc2`.

# County-level metadata file
The WA-Focused build includes county level metadata for the sequences that may not be present in Genbank. For Molecular Epi folks, this data can be retrieved from the Y-drive. When you retrieve this file, change the file name to `county_metadata.csv` and move it into the `wa_data/` folder prior to running the `fetch_n_process.smk` workflow.

# Retrieving sequencing and metadata files for the WA-focused ncov nextstrain
The SARS-CoV-2 datasets are maintained by the Nextstrain team. You can view the [list of remote datasets here](https://docs.nextstrain.org/projects/ncov/en/latest/reference/remote_inputs.html#remote-inputs-open-files).

A workflow has been configured for you to pull the inputs that you will need for the WA-focused build. To run this workflow, first `cd wa_sc2` to navigate to the `wa_sc2 repository`. Next, to run the workflow, run `snakemake -s wa_scripts/fetch_n_process.smk --cores 6`. You can specify different number of cores to use for the workflow based on your computing capacity.

# Configuring the WA-focused build
Prior to running the WA-focused build, you will need to update your input locations in the `wa_sc2/wa_profiles/wa-subsampled-background-genbank/subsampled-background-builds.yaml` on lines 13 to 20. The `subsampled-background-builds.yaml` is set up for you to move your data into an S3 Bucket, but you can keep the files locally. If you decide to move the data to an S3 bucket the recommended path would be `s3://bucket-name/ncov/data/wa-sequences.tar.xz"` for both the metadata and sequencing data inputs.

If you decide to keep things locally then the file path might look something like this:
`wa_sc2/wa_data/wa-sequences.tar.xz`

# Running the builds
This ncov Nexstrain build sources data from Genbank and inclues a 2m, 4m, and 6m build. Once you have your inputs and have updated the `subsampled-background-builds.yaml` with the input location, you can run the pipeline. If you're running Nextstrain in a conda environment then you want to make sure you pull the latest ncov github repository updates first by running `git pull` in the `ncov` directory, activating the conda environment using `conda activate nextstrain` followed by `nextstrain update` to update Nextstrain. It's recommended to pull updates prior to running the pipeline. The same could also be said for this repo as well! :)

## To run the builds using inputs stored on an AWS Bucket:
You can configure your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in your AWS credentials file which can be accessed in terminal using `nano ~/.aws/credentials`, or you can simply export the environmental variables upon opening a terminal window using:
`export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=`

If you're running Batch then you need to make sure all of the information is included in your `~/.nextstrain/config`. File. See [this documentation](https://docs.nextstrain.org/projects/cli/en/stable/aws-batch/) for more information.

To run the builds with your data stored in an AWS Bucket, navigate to the `ncov` directory and run:
`nextstrain build --aws-batch-s3-bucket bucket-name --cpus=6 . --profile wa_sc2/wa_profiles/wa-subsampled-background-genbank `

## Run the builds locally
`nextstrain build --cpus=6 . --profile wa_sc2/wa_profiles/wa-subsampled-background-genbank `

# Visualizing the results
You can check your results once the pipeline is done running using `nextstrain view auspice`
