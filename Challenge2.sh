#!/bin/bash

# Script Name:                  Ops Challenge 2 
# Author:                       Rodolfo Gonzalez
# Date of latest revision:      11/29/2023
# Purpose:                      Append Date and Time 

# Set the source and destination file paths
source_file="/var/log/syslog"                     # Path to the source syslog file
destination_dir="syslog_backups"                  # Name of the destination directory for log files

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"                         # Create the destination directory if it doesn't exist
                                                    # '-p' flag ensures that parent directories are created as needed

# Get the current date and time for timestamping
current_date=$(date +"%Y-%m-%d")                    # Get the current date in YYYY-MM-DD format
current_time=$(date +"%H:%M:%S")                    # Get the current time in HH:MM:SS format

# Construct the destination filename with timestamp
destination_file="${destination_dir}/syslog_${current_date}_${current_time}.log"   # Combine the date, time, and base filename

# Copy the syslog file to the destination directory
cp "$source_file" "$destination_file"              # Copy the syslog file to the destination file path

echo "Log file copied to: $destination_file"       # Display a message indicating the file was copied successfully
