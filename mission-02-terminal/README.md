# Mission 2 - Become Comfortable with the Terminal

## 1. Task / objective
I practised using Terminal to find folders, manage files, use command options and pipes, and check a package manager.

## 2. Work completed
I checked my current location and directory contents, created practice files, added a second line without replacing the first, copied and renamed a backup, and displayed the file. I compared normal and detailed listings, included hidden files, and sent a listing through a pipe. I also checked Homebrew and viewed its package lists without installing or removing anything.

## 3. Commands / tools used
- `pwd` - displayed the current folder.
- `ls` - listed visible files and folders.
- `ls -lah` - showed a detailed listing, including hidden files and readable file sizes. `-l`, `-a`, and `-h` are options (flags).
- `cd ..` - moved to the parent folder.
- `mkdir` - created a practice folder.
- `touch` - created an empty file.
- `printf` with `>` and `>>` - wrote the first line and then added another line.
- `cp` - made a copy of a file.
- `mv` - renamed the copied file as a backup.
- `cat` - displayed the file contents.
- `ls -lah | head -n 5` - sent the listing through a pipe and displayed its first five lines.
- `brew --version`, `brew list --formula`, and `brew list --cask` - checked Homebrew and viewed its package lists.

The Homebrew check showed version 7.0.6, 131 formula packages, and no cask packages. I did not install or remove software.

## 4. My understanding
`pwd` tells me where I am, and `ls` helps me see what is in that folder. Using `>` replaces a file's contents, while `>>` adds text at the end. `cp` makes another copy; `mv` moves or renames a file. The `-l` option adds details, `-a` includes hidden files, and `-h` makes sizes easier to read. A pipe (`|`) sends the left command's output to the command on the right. A package manager helps install, update, and remove software in an organized way.

### Task 2.2 reflection questions

- **What is the difference between replacing a file's contents and adding text to the end?** Replacing removes the old contents and writes new text. Adding text keeps the old contents and puts the new text after them.
- **What is the difference between copying and moving a file?** Copying makes another file and keeps the original. Moving changes the file's location or name.
- **What information does the current-directory display provide?** It shows the full path of the folder I am currently working in.
- **Why is a directory listing useful?** It shows the files and folders in a location so I can find and manage them.

## 5. Difficulties faced
At first, I was unsure how command options changed a listing and how the pipe passed information between commands.

## 6. How I resolved them
I compared `ls` with `ls -lah` to see the extra details and hidden file. Then I used `ls -lah | head -n 5` to see how the pipe sends the listing to `head`. I checked the Homebrew version and package lists without changing the installed software.

## 7. Evidence / files
- `practice-files/notes.txt` and `practice-files/notes-backup.txt` - the first file practice.
- `terminal-practice/notes.txt` and `terminal-practice/notes-backup.txt` - the two-line file and its backup.
- [`../evidence/mission-02-terminal.txt`](../evidence/mission-02-terminal.txt) - privacy-safe notes about the command results.
- [`../evidence/mission-02-terminal.png`](../evidence/mission-02-terminal.png) - screenshot with the username and computer name covered.

## 8. Commit details
Commit message: `Complete Mission 2 flags and package manager tasks`
Status: Committed and pushed.
