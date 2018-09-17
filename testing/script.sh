#!/bin/bash

interface=$(iwconfig | grep -i "wlo" | cut -c 1-5)
echo ${interface} >> interfaces.txt
