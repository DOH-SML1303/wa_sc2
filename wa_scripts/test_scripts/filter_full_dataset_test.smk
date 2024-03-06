# snakemake

rule filter_sequences:
    input:
        fasta="wa_data/global_sequences.fasta.xz"
    output:
        filtered_sequences="wa_data/test_filtered_sequences.fasta"
    shell:
        """
        bash ./wa_scripts/filter_sequences_test.sh {input.fasta} {output.filtered_sequences}
        """


rule filter_metadata:
    input:
        filtered_fasta="wa_data/test_filtered_sequences.fasta",
        metadata="wa_data/global_metadata.tsv.xz",
        headers="wa_data/headers.tsv"
    output:
        temp="wa_data/tmp.tsv",
        filtered_metadata="wa_data/test_filtered_metadata.tsv"
    shell:
        """
        bash ./wa_scripts/filter_metadata_test.sh {input.filtered_fasta} {input.metadata} {input.headers} {output.temp} {output.filtered_metadata}
        """


rule add_county_metadata:
    input:
        filtered_metadata="wa_data/test_filtered_metadata.tsv",
        county_metadata="wa_data/metadata_2024-02-20.csv"
    output:
        wa_metadata="wa_data/test_wa-metadata.tsv"
    shell:
        """
        python3 ./wa_scripts/wa-nextstrain-update-location-genbank_smk.py {input.filtered_metadata} {input.county_metadata} {output.wa_metadata}
        """


rule all:
    input:
        "test_filtered_sequences.fasta",
        "test_filtered_metadata.tsv",
        "test_wa-metadata.tsv"
