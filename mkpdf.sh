#! /usr/bin/env bash
set -ex

[ ! -r README.pdf ] &&
  grep -v '^```' README.md | markdown2pdf -o README.pdf

[ ! -r 05-guestbook.pdf ] &&
  grep -v '^```' 05-guestbook.md | markdown2pdf -o 05-guestbook.pdf

for d in * ; do 
  [ -d "$d" -a -f "$d/README.md" -a ! -r "$d.pdf" ] && (
    cd $d && grep -v '^```' README.md | markdown2pdf -o ../$d.pdf
  )
done
