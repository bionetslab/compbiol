# README for ht-seq course
## Setup

This repository contains the repositories for the ht-seq course. Each folder contains a README 
detailing how to setup the repo and get started.

This part of the course has 9 parts, but not all have an associated repository.


###
Prerequisites: 
Please install ![pixi](https://pixi.prefix.dev/latest/). 
```
curl -fsSL https://pixi.sh/install.sh | sh
```

### Windows
While it is possible to stay on Windows for most of the course, some elements require a Linux distribution. This can be obtained here ![Windows Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

## Basic commandline navigation
| Action | Unix (Linux/macOS) | Windows (CMD) |
| :--- | :--- | :--- |
| Print Working Directory | `pwd` | `cd` |
| List Contents | `ls` | `dir` |
| Change Directory | `cd [path]` | `cd [path]` |
| Move Up One Level | `cd ..` | `cd ..` |
| Make Directory | `mkdir [name]` | `mkdir [name]` |
| Clear Screen | `clear` | `cls` |

## Basic Git commands.
Git is a version control system used to track changes in source code during software development. The following commands represent the standard workflow for managing a local repository and interacting with a remote server:
- git clone [url]: Creates a local copy of a remote repository.
- git status: Displays the state of the working directory and the staging area, showing which changes have been staged and which have not.
- git pull: Fetches updates from the remote repository and immediately integrates them into the local branch.
- git add [file]: Adds file changes in the working directory to the staging area.
- git commit -m "[message]": Records the staged snapshots to the project history with a descriptive message.
- git push: Uploads local repository content to a remote repository.

Merging Files
Merging is the process of integrating changes from one branch into another. This typically occurs when a developer has completed work on a feature branch and wishes to incorporate those updates into the main codebase. On pull, Git attempts to automatically combine the code. If the changes occur in different parts of a file, Git joins them seamlessly. However, if the same lines were modified differently in both branches (eg. remote and locallt), a merge conflict occurs. In this instance, Git pauses the process and requires the user to manually select which changes to keep before finalizing the commit. Jupyter notebooks, as used in this course, are difficult to merge, there are special tools for this. If you want to avoid merge conflicts, create a copy of the notebook you are working on.
