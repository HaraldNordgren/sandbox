#!/bin/bash

for i in $WORK/*/; do (
  set -e
  cd $i
  git stash
  git checkout master
  git clean -fxd
  git checkout .
  git pull
)&; done

