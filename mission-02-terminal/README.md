# Mission 2 - Terminal and File Management

## 1. Task / objective
I practised using Terminal to create, copy, rename, and read files.

## 2. Work completed
I created a practice folder and a text file. I added two lines to the file, copied it, and renamed the copy as a backup. I also used a pipe to count the lines.

## 3. Commands / tools used
- `mkdir` - created the practice folder.
- `cd` - moved into the practice folder.
- `touch` - created an empty text file.
- `printf` - added text to the file.
- `cp` - copied the file.
- `mv` - renamed the copy as a backup.
- `cat` - displayed the file contents.
- `ls` - listed the files in the folder.
- `cat notes.txt | wc -l` - used a pipe to count the lines in the file.

## 4. My understanding
Terminal lets me manage files by typing commands. `cp` makes a copy, while `mv` moves or renames a file. A pipe (`|`) sends the output of one command to another command.

## 5. Difficulties faced
At first, I was not sure what a pipe did or how it could be useful.

## 6. How I resolved them
I used `cat notes.txt | wc -l`. The first command showed the text, and the pipe sent its output to `wc -l`, which counted two lines.

## 7. Evidence / files
- `practice-files/notes.txt` - the original text file.
- `practice-files/notes-backup.txt` - the renamed copy.
- [`../evidence/mission-02-terminal.txt`](../evidence/mission-02-terminal.txt) - a short record of the commands and results.
- [`../evidence/mission-02-terminal.png`](../evidence/mission-02-terminal.png) - screenshot with the username and computer name covered.

## 8. Commit details
Commit message: `Add redacted Mission 2 terminal screenshot`
Status: Committed and pushed.
