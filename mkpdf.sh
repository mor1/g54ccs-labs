#! /usr/bin/env bash
set -ex

grep -v '^```' README.md | markdown2pdf -o README.pdf

for d in * ; do 
  [ -d "$d" -a -f "$d/README.md" ] && (
    cd $d && grep -v '^```' README.md | markdown2pdf -o ../$d.pdf
  )
done
