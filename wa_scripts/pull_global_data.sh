#!/bin/bash

global_metadata_url="$1"
global_aligned_sequences_url="$2"
global_metadata="$3"
global_aligned_sequences="$4"

wget -O "$global_metadata" "$global_metadata_url"
chmod +x "$global_metadata"

wget -O "$global_aligned_sequences" "$global_aligned_sequences_url"
chmod +x "$global_aligned_sequences"

echo "Global data pull complete"
