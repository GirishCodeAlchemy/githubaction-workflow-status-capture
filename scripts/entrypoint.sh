#!/bin/bash

echo "==================="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git config --global --add safe.directory /github/workspace

python3 /app/readme-update.py

git add -A && git commit -m "update the Readme"
git pull origin main
git push --set-upstream origin main

echo "==================="
