#!/bin/bash
# Script to show information about the battery

# Collect the information from the system
INFO=$(grep -e "STATUS\|HEALTH\|CAPACITY" /sys/class/power_supply/battery/uevent | tr "=" " " | awk '{print $2}')

# Split the information into different variables
STATUS=$(echo $INFO | awk '{print $1}')
HEALTH=$(echo $INFO | awk '{print $2}')
CAPACITY=$(echo $INFO | awk '{print $3}')

# Show the information
echo "Status: $STATUS"
echo "Health: $HEALTH"
echo "Capacity: $CAPACITY"
  
