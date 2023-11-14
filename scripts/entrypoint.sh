#!/bin/bash

echo "==================="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git condig --global --add safe.directory /github/workspace

python3 readme-update.py

git add -A && git commit -m "update the Readme"
git push --set-upstream origin main

echo "==================="
