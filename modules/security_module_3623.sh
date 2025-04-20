#!/bin/bash
echo 'Scanning network...'
nmap -sS -P0 192.168.1.0/24
