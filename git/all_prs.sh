#!/bin/bash

for i in *; do
(
  set -e
  cd $i
  if git status | grep -q 'modified:'; then
    echo $i
    (
      ticket=DEV-123
      git add .
      git commit -m "[$ticket] Update something"
      git push origin $(git rev-parse --abbrev-ref HEAD)
      hub pull-request --push -f -a HaraldNordgren --no-edit
    )
  fi
); done

