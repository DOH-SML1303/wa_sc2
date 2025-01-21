# wa_sc2
WA-focused ncov Nexstrain builds for genomic surveillance of SARS-CoV-2 in Washington state.
Builds located here:
- [Washington-focused SARS-CoV-2 genomic analysis: Past two months](https://nextstrain.org/groups/waphl/ncov/wa/2m)
- [Washington-focused SARS-CoV-2 genomic analysis: Past four months](https://nextstrain.org/groups/waphl/ncov/wa/4m)
- [Washington-focused SARS-CoV-2 genomic analysis: Past six months](https://nextstrain.org/groups/waphl/ncov/wa/6m)

# Setup
First, install the [ncov nextstrain pipeline](https://github.com/nextstrain/ncov) and clone the ncov repository using `git clone https://github.com/nextstrain/ncov` or `gh repo clone nextstrain/ncov`.

Next, clone this repository in the `ncov` folder. You can do this in the command-line terminal by navigating to the `ncov` repository using `cd ncov` and then cloning the repository using `git clone https://github.com/DOH-SML1303/wa_sc2.git` or `gh repo clone DOH-SML1303/wa_sc2`.

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
