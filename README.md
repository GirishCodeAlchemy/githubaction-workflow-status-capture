# Githubaction-Workflow-Status-Capture

<p align="center">
  <img src="./cover.gif" width="300" alt="githubaction workflow status generator">
</p>

Update all the Githubaction workflow status automatically to the readme

Usage example:

```yaml
name: Use githubaction status generator to update workflow status in README
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3
      - name: Run Githubaction Generator
        uses: GirishCodeAlchemy/githubaction-workflow-status-capture@v2
```

# output

<!-- START_ACTIONS_TABLE -->

| Workflow                                                                                                                     | Build Status                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Update Readme Workflows 1](.github/workflows/readme-script.yaml)                                                            | [![Githubaction Status](https://github.com/girish-devops-project/github-action/actions/workflows/readme-script.yaml/badge.svg)](https://github.com/girish-devops-project/github-action/actions/workflows/readme-script.yaml)                                                                                                             |
| [Use githubaction status generator to update workflow status in README](.github/workflows/update-readme-worflow-status.yaml) | [![Use githubaction status generator to update workflow status in README](https://github.com/GirishCodeAlchemy/alchemy-githubaction-playground/actions/workflows/update-readme-worflow-status.yaml/badge.svg)](https://github.com/GirishCodeAlchemy/alchemy-githubaction-playground/actions/workflows/update-readme-worflow-status.yaml) |

<!-- END_ACTIONS_TABLE -->
