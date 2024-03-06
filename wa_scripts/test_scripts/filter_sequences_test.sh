#!/bin/bash

input_file="$1"
output_file="$2"
pattern="USA/WA"

xzcat "$input_file" | awk -v pattern="$pattern" 'BEGIN { RS=">"; ORS="" } $0 ~ pattern { print ">"$0 }' > "$output_file"

echo "WA seqs have been filtered and written to $output_file."
