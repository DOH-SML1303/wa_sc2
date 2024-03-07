# snakemake
rule all:
    input:
        "wa_data/wa-sequences.tar.xz"

rule filter_sequences:
    input:
        fasta="wa_data/full_sequences.fasta.xz"
    output:
        filtered_sequences="wa_data/filtered_sequences.fasta"
    shell:
        """
        bash ./wa_scripts/filter_sequences.sh {input.fasta} {output.filtered_sequences}
        """


rule filter_metadata:
    input:
        filtered_fasta="wa_data/filtered_sequences.fasta",
        metadata="wa_data/full_metadata.tsv.gz",
        headers="wa_data/headers.tsv"
    output:
        temp="wa_data/tmp.tsv",
        filtered_metadata="wa_data/filtered_metadata.tsv"
    shell:
        """
        bash ./wa_scripts/filter_metadata.sh {input.filtered_fasta} {input.metadata} {input.headers} {output.temp} {output.filtered_metadata}
        """


rule add_county_metadata:
    input:
        filtered_metadata="wa_data/filtered_metadata.tsv",
        county_metadata="wa_data/county_metadata.csv"
    output:
        wa_metadata="wa_data/wa-metadata.tsv"
    shell:
        """
        python3 ./wa_scripts/wa-nextstrain-update-location-genbank.py {input.filtered_metadata} {input.county_metadata} {output.wa_metadata}
        """
rule compress_files:
    input:
        filtered_fasta="wa_data/filtered_sequences.fasta",
        wa_metadata="wa_data/wa-metadata.tsv"
    output:
        compressed_output="wa_data/wa-sequences.tar.xz"
    shell:
        """
        tar -cJf {output.compressed_output} {input.filtered_fasta} {input.wa_metadata}
        """
