#!/bin/bash

echo "==================="

git config --global user.name "${INPUT_NAME}"
git config --global user.email "${INPUT_EMAIL}"
git config --global pull.ff only
git config --global --add safe.directory /github/workspace

python3 /app/readme-update.py

echo "Committer's Email: ${INPUT_EMAIL}"
echo "Committer's Name: ${INPUT_NAME}"

git add -A && git commit -m "update the Readme"

# Get the current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
echo "Current branch: $current_branch"

# Attempt a non-interactive rebase
git pull --rebase --no-edit origin "$current_branch"

# Check if the rebase failed
if [ $? -ne 0 ]; then
    echo "Rebase failed. Falling back to merge."
    # Abort the rebase
    git rebase --abort
    # Perform a non-interactive merge
    git pull --no-edit origin "$current_branch"
fi

git push --set-upstream origin "$current_branch"


echo "==================="