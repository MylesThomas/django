#! /bin/sh

#git config --global user.email "mylescgthomas@gmail.com"
#git config --global user.name "mylesthomas"

echo "# django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/django.git
git push -u origin main