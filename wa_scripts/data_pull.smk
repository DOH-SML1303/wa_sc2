rule pull_global_data:
    output:
        global_metadata="wa_data/global_metadata.tsv.xz",
        global_aligned_sequences="wa_data/global_aligned_sequences.fasta.xz"
    params:
        global_metadata_url="https://data.nextstrain.org/files/ncov/open/global/metadata.tsv.xz",
        global_aligned_sequences_url="https://data.nextstrain.org/files/ncov/open/global/aligned.fasta.xz"
    shell:
        """
        bash ./wa_scripts/pull_global_data.sh {params.global_metadata_url} {params.global_aligned_sequences_url} {output.global_metadata} {output.global_aligned_sequences}
        """

rule pull_full_data:
    output:
        full_metadata="wa_data/full_metadata.tsv.xz",
        full_sequences="wa_data/full_sequences.fasta.xz"
    params:
        full_metadata_url="https://data.nextstrain.org/files/ncov/open/metadata.tsv.gz",
        full_aligned_sequences_url="https://data.nextstrain.org/files/ncov/open/sequences.fasta.xz"
    shell:
        """
        bash ./wa_scripts/pull_full_data.sh {params.full_metadata_url} {params.full_sequences_url} {output.full_metadata} {output.full_sequences}
        """
