#!/usr/bin/env bash

filename=/home/qiankun/termConfig.txt
gnome-terminal --save-config=$filename

LINES=($(grep -n '\[Terminal' $filename | cut -d: -f1))
for ((i=0; i<$(grep '\[Terminal' $filename | wc -l); i++))
do
    TITLE=$(xprop -id $WINDOWID WM_NAME | sed -e 's/WM_NAME(STRING) = "//' -e 's/"$//';xdotool key ctrl+Page_Down;)
    sed -ri "$((${LINES[$i]}+$i))s/.*/&\nTitle=$TITLE/" $filename 
done
