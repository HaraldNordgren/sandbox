#!/bin/bash

move () (
	if compgen -G "*.$1" > /dev/null; then
		echo "    Found $1 files, will move them"
		mv *.$1 $2
	fi
)

organize () (
	echo Archiving in $1
	cd $1

	folder="misc/$(date +'%Y-%m-%d')"

	mkdir -p $folder

	move avif $folder
	move csv $folder
	move docx $folder
	move eml $folder
	move gif $folder
	move graphql $folder
	move html $folder
	move HEIC $folder
	move ics $folder
	move jpeg $folder
	move jpg $folder
	move json $folder
	move mov $folder
	move mp4 $folder
	move pdf $folder
	move png $folder
	move pptx $folder
	move sql $folder
	move txt $folder
	move webp $folder
	move xls $folder
	move xlsx $folder
	move zip $folder

	rmdir $folder 2>/dev/null

	echo "    Done"
	echo
)

organize ~/Desktop
organize ~/Downloads
organize ~/Documents

