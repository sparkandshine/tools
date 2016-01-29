#!/usr/bin/env bash

if [ -z $1 ]; 
then
    echo "Usage: $0 path/filename.tex" 
    exit
fi

tex_file_origin=$1
tex_file_old="${tex_file_origin}.old" # backup the original tex file

# create a tmp file and delete while exiting
tmp_file="/tmp/tmp_file.$$"
trap "rm -f $tmp_file" EXIT


# indent a tex document
perl latexindent.pl -s -o $tex_file_origin $tmp_file


mv $tex_file_origin $tex_file_old
cp $tmp_file $tex_file_origin
