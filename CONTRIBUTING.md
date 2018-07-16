# Contributing to Titan Embeds - Ansible Playbooks

There are many ways to contribute to Titan. There is no one right method to contribute. As long as your Pull Request is valid and is beneficial to the project, we'll take it. Whether you are a designated developer of this project, or just a seasonal hacker who want to fix a mistake that we probably made, you're welcomed to help as long as you abide by these guidelines. This document outlines of the practices and mistakes involving with contributing to the project.

## Development Environment
For those who would like to run the codebase yourself, you may follow the instructions to the webapp and discordbot to setup the components on your own server. You could however also develop the code on Cloud9. It is free* and very simple to get it off running under ten minutes or less. Either way, if you would like to contribute to the project, I strongly advise you to run Titan on a development server. Making changes on a dev server has many benefits. Especially if you are making changes other than wording issues, the GitHub editor is not the way to go. You may follow these steps to run Titan with Cloud9.

## Pull Requesting
If you do not have write access to the codebase, please make a fork of the project. Edit your changes on your fork and push it out onto GitHub. Afterwards, you may submit a pull request for your changes to be merged to the master branch (production). If you do however have write access to the repository, please create a branch and propose pull requests for me to merge into the production.

I have recently decided to restrict pushing into the master branch so that all commits to the codebase is complete and meaningful. The production environment is not used for testing and every new errors in the error log makes me feel a little bit sadder. Using branches and pull requests also means that I may squash and edit the commit messages before pulling into the master so they may look more nicer.
To create a new branch, run this command `git checkout -b <new branch name>`. Then use `git checkout <branch name>` to switch between branches.

Make sure that you thoughly test your changes so that it works and doesn't introduce new bugs. *I won't merge any pull requests until your changes are complete.* I do not like to accept features that are "half done" as these may be left abandoned at any time and may look odd. Please keep in mind to create one branch/pull request for every new feature.
