#!/bin/bash

# Script Name:                  Ops Challenge 2 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      12/01/2023
# Purpose:                      
# # This script automates the process of backing up log files.
# It compresses, timestamps, and stores backup files for better management.


#!/bin/bash

# Backup directory
backup_dir="/var/log/backups"

# List of log files
log_files=(
  "/var/log/syslog"
  "/var/log/wtmp"
)

# Timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Print original file sizes
echo "Original File Sizes:"

# Iterate over each log file and print its size
for log_file in "${log_files[@]}"; do
  # Use du to get disk usage, and cut to extract only the size
  original_size=$(du -h "$log_file" | cut -f1)
  echo "  $log_file: $original_size"
done

# Compress log files with timestamped filenames
echo "Compressing log files..."

# Iterate over each log file, compress it, and save with a timestamped filename
for log_file in "${log_files[@]}"; do
  # Extract filename without path using ${log_file##*/}
  gzip -c "$log_file" > "$backup_dir/${log_file##*/}-$timestamp.zip"
done

# Clear original log files
echo "Clearing original logs..."

# Iterate over each log file and clear its content
for log_file in "${log_files[@]}"; do
  # Clear log file content by overwriting it with an empty string
  echo "" > "$log_file"
done

# Print compressed file sizes
echo "Compressed File Sizes:"

# Iterate over each log file and print the size of its compressed version
for log_file in "${log_files[@]}"; do
  # Extract filename without path using ${log_file##*/}
  compressed_size=$(du -h "$backup_dir/${log_file##*/}-$timestamp.zip" | cut -f1)
  echo "  ${log_file##*/}-$timestamp.zip: $compressed_size"
done

# Compare original and compressed file sizes
echo "File Size Comparison:"

# Iterate over each log file and compare the original and compressed sizes
for log_file in "${log_files[@]}"; do
  # Get original file size
  original_size=$(du -h "$log_file" | cut -f1)
  # Get compressed file size
  compressed_size=$(du -h "$backup_dir/${log_file##*/}-$timestamp.zip" | cut -f1)
  
  # Calculate percentage reduction using bc -l for floating-point arithmetic
  percentage_reduction=$(echo "scale=2; (($original_size - $compressed_size) / $original_size) * 100" | bc -l)
  
  # Print comparison results
  echo "  $log_file: Original: $original_size, Compressed: $compressed_size, Reduction: $percentage_reduction%"
done
