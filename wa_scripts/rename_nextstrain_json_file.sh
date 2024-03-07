#!/bin/bash

# may need to update auspice location as needed
cd /data/ncov/auspice

for file in *; do
  if [[ "$file" == *two_mon* ]]; then
    new_file="${file//two_mon/2m}"
    mv "$file" "$new_file"
    echo "Renamed $file to $new_file"
  elif [[ "$file" == *four_mon* ]]; then
    new_file="${file//four_mon/4m}"
    mv "$file" "$new_file"
    echo "Renamed $file to $new_file"
  elif [[ "$file" == *six_mon* ]]; then
    new_file="${file/six_mon/6m}"
    mv "$file" "$new_file"
    echo "Renamed $file to $new_file"
  fi
done

echo "File names have been updated."
