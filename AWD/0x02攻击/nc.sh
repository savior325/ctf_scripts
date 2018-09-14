#!/bin/sh
ip =(
192.168.31.143
)
for i in $ip; do
	nc i 1524
