#!/usr/bin/python3

# Run script for instrictions on how to make a new release

import re
import sys


def wait_for_enter():
    input("Press Enter to continue: ")
    print()


class Prepare:
    def run(self, context):
        print(
            (
                "> Place yourself in the root folder of your gordias fork"
                " clone, checkout the 'main' branch and do 'git fetch --all'."
            )
        )
        wait_for_enter()
        print(
            (
                "> Make sure your 'main' branch is up to date with the"
                " upstream 'main' and that there are no local changes."
            )
        )
        wait_for_enter()
        print(
            (
                "> Make sure the dependency list in 'pyproject.toml' is up"
                " to date with the non-developer dependencies in the"
                " 'environment.yml' file. Also make sure the other sections"
                " of 'project.toml' file is up to date."
            )
        )
        wait_for_enter()


class UpdateChangeLog:
    def run(self, context):
        print(
            f"> Run the command 'utils/update-changelog.sh"
            f" {context['new_version'][1:]}'."
        )
        wait_for_enter()
        print(
            (
                "> Copy the output from the command and paste it into"
                " 'CHANGELOG.md' (the structure of the document will show"
                " where to put the generated text)."
            )
        )
        wait_for_enter()
        print(
            (
                "> In the pasted text in 'CHANGELOG.md', move each commit to a"
                " proper commit category section"
            )
        )
        wait_for_enter()
        print(
            (
                "> In the pasted text in 'CHANGELOG.md', remove commit"
                " category headers with no commits."
            )
        )
        wait_for_enter()
        print(
            (
                "> At the end of 'CHANGELOG.md', replace the top line of the"
                " link list (the line starting with [unreleased]) with the"
                " following two lines:"
            )
        )
        print(
            f"[unreleased]: https://git.smhi.se/climix/gordias/compare/"
            f"{context['new_version']}...HEAD"
        )
        print(
            f"[{context['new_version'][1:]}]:"
            f" https://git.smhi.se/climix/gordias/compare/"
            f"{context['old_version']}...{context['new_version']}"
        )
        wait_for_enter()


class CreateNewBranchAndCommit:
    def run(self, context):
        print(
            f"> Create a new branch called"
            f" 'changelog-{context['new_version']}' and checkout the new"
            f" branch."
        )
        wait_for_enter()
        print(
            f"> Add the 'CHANGELOG.md' file and make a new commit with"
            f" message: 'Update changelog for release"
            f" {context['new_version']}'."
        )
        wait_for_enter()
        print("> Push the new branch to your gordias fork.")
        wait_for_enter()


class CreateMergeRequestAndMerge:
    def run(self, context):
        print(
            (
                "> Go to https://git.smhi.se/climix/gordias and create a new"
                " merge request for the new branch from your fork into the"
                " main branch of the gordias upstream repo."
            )
        )
        wait_for_enter()
        print(("> Have a colleague sanity check the merge request."))
        wait_for_enter()
        print(("> Merge."))
        wait_for_enter()


class TagVersion:
    def run(self, context):
        print(
            (
                "> Checkout the 'main' branch of your fork, and update it to"
                " be in sync with the upstream repo."
            )
        )
        wait_for_enter()
        print(
            f"> Run the command 'git tag -a {context['new_version']}',"
            f" and use the tag message 'Release {context['new_version']}'."
        )
        wait_for_enter()
        print(
            f"> Push the new tag by running the command"
            f" 'git push upstream {context['new_version']}'."
        )
        wait_for_enter()


class BuildForPYPI:
    def run(self, context):
        print(
            (
                "> This section requires an account on https://pypi.org/, and"
                " access to the pypi gordias project. If you don't have this,"
                " please talk to a colleague."
            )
        )
        wait_for_enter()
        print(
            (
                "> If you have a 'dist' folder in the root of your clone, run"
                " the command 'rm dist/*' to clear out old builds."
            )
        )
        wait_for_enter()
        print(
            (
                "> Make sure to activate a mamba environment with updated"
                " versions of 'pip', 'build' and 'twine' installed."
            )
        )
        wait_for_enter()
        print(
            (
                "> Run the command 'python -m build', and check that you have"
                " a new build in the 'dist' folder."
            )
        )
        wait_for_enter()
        print(
            (
                "> Make sure you have an api token from pypi. This is needed"
                " to upload the new build."
            )
        )
        wait_for_enter()
        print(
            (
                "> From your clone root folder, run the command 'twine upload"
                " dist/*'. You may get a warning about an error regarding"
                " getting password from keyring. Disregard this warning and"
                " use your API token when requested."
            )
        )
        wait_for_enter()
        print("> Make sure the new build is available at https://pypi.org/.")
        wait_for_enter()


class UpdateOnConda:
    def run(self, context):
        print(
            (
                "> This section requires an account on github, and access to"
                " the gordias conda-forge feedstock repo. If you don't have"
                " this, please talk to a colleague."
            )
        )
        wait_for_enter()
        print("> Go to https://github.com/conda-forge/gordias-feedstock.")
        wait_for_enter()
        print(
            (
                "> In the file 'recipe/meta.yaml', make sure the"
                " 'requirements' list is up to date with the 'dependencies'"
                " list in the gordias repo 'environment.yml' file. You can"
                " edit and commit changes to 'recipe/meta.yaml' in the browser"
                " if necessary."
            )
        )
        wait_for_enter()
        print(
            (
                "> Create a new issue, then choose the 'Bot commands'"
                " category. Set the issue title to"
                " '@conda-forge-admin, please update version'."
            )
        )
        wait_for_enter()
        print(
            (
                "> conda-forge-webservices will create a pull request and"
                " run tests. Wait for it to finish."
            )
        )
        wait_for_enter()
        print(
            (
                "> After all tests have finished successfully, merge the"
                " merge request."
            )
        )
        wait_for_enter()
        print(
            (
                "> Make sure the new version appears on "
                " https://anaconda.org/conda-forge/gordias. It may take a"
                " short while after the merge."
            )
        )
        wait_for_enter()


def _checkargs():
    if len(sys.argv) < 3:
        print(
            (
                "Please provide the previous and current release version"
                " numbers, in format 'vMajor.Minor.Patch',"
            )
        )
        print(("e.g.: 'python3 gordias-release.py v0.20.0 v0.21.0'"))
        return False

    version_re = r"^v[0-9]+.[0-9]+.[0-9]+"
    old_version_ok = re.fullmatch(version_re, sys.argv[1])
    new_version_ok = re.fullmatch(version_re, sys.argv[2])

    if not old_version_ok or not new_version_ok:
        print(
            (
                "Format number in wrong format. Format should be"
                " 'vMajor.Minor.Patch', e.g. 'v0.20.0'."
            )
        )
        return False

    return True


if __name__ == "__main__":
    if _checkargs():
        context = {
            "old_version": sys.argv[1],
            "new_version": sys.argv[2],
        }

        procedure = [
            Prepare(),
            UpdateChangeLog(),
            CreateNewBranchAndCommit(),
            CreateMergeRequestAndMerge(),
            TagVersion(),
            BuildForPYPI(),
            UpdateOnConda(),
        ]
        for step in procedure:
            print("----------------------------------------")
            print(step.__class__.__name__)
            print("----------------------------------------")
            step.run(context)
        print("Done.")
