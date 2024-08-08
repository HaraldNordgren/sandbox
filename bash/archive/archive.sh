#!/bin/bash

# Array of file extensions to move
extensions=(
    avif
    csv
    docx
    eml
    gif
    graphql
    html
    heic
    ics
    jpeg
    jpg
    json
    mov
    mp4
    pdf
    png
    pptx
    sql
    txt
    webp
    xls
    xlsx
    zip
)

# Function to move files with a specific extension to a target directory
move () (
	shopt -s nocaseglob
	if compgen -G "*.$1" > /dev/null; then
		echo "    Found $1 files, will move them"
		if ! mv -- *."$1" "$2"; then
            echo "    Error moving $1 files"
        fi
	fi
	shopt -u nocaseglob
)

# Function to organize files in a specified directory
organize () (
	echo Archiving in "$1"
	cd "$1" || { echo "Failed to change directory to $1"; return; }

	folder="misc/$(date +'%Y-%m-%d')"
	mkdir -p "$folder"

	# Loop through each extension and move files
	for ext in "${extensions[@]}"; do
		move "$ext" "$folder"
	done

	rmdir "$folder" 2>/dev/null

	echo "    Done"
	echo
)

organize ~/Desktop
organize ~/Downloads
organize ~/Documents
