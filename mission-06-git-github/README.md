# Mission 6 - Git and GitHub

## 1. Task / objective
I learned how Git records changes and how GitHub supports teamwork through branches and Pull Requests.

## 2. Work completed

### Basic Git workflow

| Git operation | What it does |
|---|---|
| Check repository status | `git status` shows which files have changes and whether they are staged. |
| Stage selected changes | `git add README.md` selects the changes to include in the next commit. |
| Create a commit | `git commit` saves the staged changes in the local Git history. |
| View commit history | `git log --oneline` shows recent commits. |

Staging and committing are separate steps. Staging chooses the changes for the next saved version; committing records those chosen changes in the repository history.

### Branch and Pull Request
I used the `update-about` branch to add a “My Learning” section to the root README. Pull Request #1 asked to add that change to `main`; it was reviewed and merged.

- Pull Request: [#1 - Add project overview and mission links](https://github.com/Ashvanth-gif/digital-detective-8029/pull/1)
- Status: Merged

A branch gives me a separate place to work on changes. A Pull Request lets me show those changes and ask for review before they are merged into the main branch.

### Git command glossary

| Operation | Command | What it means |
|---|---|---|
| Initialize a repository | `git init` | Start tracking a project with Git. |
| Check status | `git status` | See changed, staged, and untracked files. |
| Stage changes | `git add README.md` | Choose a file's changes for the next commit. |
| Commit changes | `git commit -m "message"` | Save staged changes in the local history with a short description. |
| View history | `git log --oneline` | See earlier commits. |
| Create or list branches | `git branch name` / `git branch` | Create a branch or list the branches. |
| Switch branches | `git switch name` | Move to another branch. |
| Publish changes | `git push -u origin name` | Send a branch and its commits to GitHub. |
| Retrieve remote changes | `git pull origin main` | Get changes from the remote `main` branch and bring them into the current branch. |

## 3. Commands / tools used
- `git status` - checked which files had changes.
- `git add` - staged selected changes.
- `git commit` - recorded changes in history.
- `git log --oneline` - viewed the commit history.
- `git branch -a` - viewed local and remote branches.
- `git push` - published commits to GitHub.
- GitHub Pull Requests - reviewed and merged Pull Request #1.

## 4. My understanding
Git keeps a history of my project. I stage the changes I want, then commit them to save a version. A branch keeps work separate, and a Pull Request lets people review it before it is merged. GitHub stores the remote copy so I can share changes with others.

## 5. Difficulties faced
At first, I mixed up staging, committing, branches, and Pull Requests.

## 6. How I resolved them
I followed the steps in order: check the status, stage the selected file, commit it, and push the branch. I used Pull Request #1 to review the README change before it was merged.

## 7. Evidence / files
- Root [`README.md`](../README.md) - contains the “My Learning” section.
- [Pull Request #1](https://github.com/Ashvanth-gif/digital-detective-8029/pull/1) - merged branch and review record.

## 8. Commit details
Commit message: `Complete Git command glossary`
Status: Committed and pushed.
