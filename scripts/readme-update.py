from pathlib import Path

import requests


def get_workflow_names(username, repository):
    # GitHub Actions API endpoint for workflow list
    api_url = f'https://api.github.com/repos/{username}/{repository}/actions/workflows'

    # Make a request to the GitHub API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the JSON response
        workflows = response.json()['workflows']
        # print(workflows)
        # return [workflow['name'] for workflow in workflows]
        return workflows
    else:
        print(f"Failed to fetch workflows. Status code: {response.status_code}")
        return None


def get_latest_build_status(workflow):
    # GitHub Actions badge URL
    # badge_url = f'{workflow["badge_url"]}/badge.svg'

    # Fetch the badge image
    response = requests.get(workflow["badge_url"])

    # Check if the badge URL is valid
    if response.status_code == 200:
        return response.text
    else:
        return None


def generate_table_content(username, repository, workflows):
    table_content = "\n| Workflow | Build Status |\n|----------|--------------|\n"
    added_workflows = set()

    for workflow in workflows:
        workflow_name = workflow['name']
        workflow_file = workflow['path'].split('/')[-1]
        if workflow_file not in added_workflows:
            action_url = f'https://github.com/{username}/{repository}/actions/workflows/{workflow_file}'
            # build_status = get_latest_build_status(workflow)

            # if build_status:
            table_content += f"| [{workflow_name}]({workflow['path']}) | [![{workflow_name}]({action_url}/badge.svg)]({action_url}) |\n"
            added_workflows.add(workflow_name)
            # else:
            #     print(f"Failed to fetch the latest build status for {workflow_name}.")

    return table_content


def update_readme(readme_path, table_content):
    # Read the existing content of the README.md file
    existing_content = readme_path.read_text()

    # Find the unique identifiers above and below the table
    start_identifier = "<!-- START_ACTIONS_TABLE -->"
    end_identifier = "<!-- END_ACTIONS_TABLE -->"
    start_pos = existing_content.find(start_identifier)
    end_pos = existing_content.find(end_identifier, start_pos + 1)

    if start_pos != -1 and end_pos != -1:
        # If the identifiers are found, replace the content between them with the new table
        updated_content = (
            existing_content[:start_pos + len(start_identifier)] +
            table_content +
            existing_content[end_pos:]
        )
    else:
        # If the identifiers are not found, create them and insert the table at the end of the README
        updated_content = (
            existing_content +
            f"\n{start_identifier}\n{table_content}{end_identifier}\n"
        )

    # Update the README.md file with the modified content
    readme_path.write_text(updated_content)
    print("README.md updated with the latest build statuses.")

if __name__ == "__main__":
    # GitHub username and repository name
    username = "girish-devops-project"
    repository = "github-action"

    # Path to the README.md file
    readme_path = Path("README.md")

    # Get all workflow names
    workflows = get_workflow_names(username, repository)

    if workflows:
        # Generate README content
        readme_content = generate_table_content(username, repository, workflows)

        # Update the README.md file with the generated content
        update_readme(readme_path, readme_content)
    else:
        print("Failed to fetch workflow names.")
