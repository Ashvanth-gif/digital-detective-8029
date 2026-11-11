# Mission 3 - Understand the Operating System

## 1. Task / objective
I explored the operating system, running processes, storage, paths, permissions, and the jobs an operating system does.

## 2. Work completed

### System information

| Information | What it tells me | My observation |
|---|---|---|
| Operating system | The system software managing the computer | macOS 27.3 |
| Current account | Which account is active | Checked; account name is `[redacted]`. |
| Storage | How much space is used and available | About 298 GiB used and 136 GiB available on a 460 GiB volume. |
| System activity | Which apps and background tasks are running | Activity Monitor showed running apps and background processes. I saw Safari and Google Chrome in the list. |

### Processes
A process is a program that is running. The PID column shows each process's identification number. The number helps the operating system keep track of each running program. Examples I saw were Safari and Google Chrome.

### Paths and permissions
I checked the current location in the repository and then moved into the Mission 3 folder. The displayed location changed when I changed folders.

- An **absolute path** starts at the root of the computer and gives the full location. Privacy-safe example: `/Users/[redacted]/Desktop/digital-detective-8029/mission-03-operating-system/README.md`.
- A **relative path** starts from the folder I am already in. Example from the repository root: `mission-03-operating-system/README.md`.

The README file's permission listing was `-rw-r--r--@`. The owner's letters are `rw-`, so the owner can read and change the file but cannot run it as a program. The other permission letters show read access. The `@` is macOS's marker for extended file attributes.

### Operating-system responsibilities

| Responsibility | My explanation | Example |
|---|---|---|
| Process management | Keeps track of programs that are running and shares processor time between them. | A browser and a text editor can both run at once. |
| Memory management | Gives programs memory while they work and reuses it when they close. | A browser uses memory to keep a page open. |
| Device management | Helps programs communicate with connected hardware. | The OS sends a document to a printer. |
| File management | Organizes files and folders and controls how they are opened or changed. | I open and save a README file. |
| User interface / shell | Lets me control the computer with windows and menus or by typing commands. | The desktop is a graphical interface; Terminal is a shell. |
| Security and permissions | Controls which accounts can read, change, or run files. | The file's permission letters show what its owner can do. |

## 3. Commands / tools used
- `sw_vers` - checked the macOS version.
- `whoami` - checked the active account; I redacted the account name in this report.
- `df -h "$HOME"` - checked used and available storage.
- Activity Monitor - viewed running processes and the PID column.
- `pwd` - displayed the current location.
- `cd mission-03-operating-system` - moved into the mission folder.
- `ls -l README.md` with `awk` - checked the permission letters and left the account name out of the recorded result.

I also tried `ps -ax -o pid,comm`, but the shell blocked it in this environment. I used Activity Monitor to view the process list instead.

## 4. My understanding
The operating system manages programs, memory, files, and connected devices. It also gives me ways to use the computer and controls access to files. A process is a running program, and its PID helps the system identify it. Absolute paths give the full location; relative paths are written from the current folder.

## 5. Difficulties faced
The process-list command was blocked, and I had to be careful not to share the account name or a private path.

## 6. How I resolved them
I used Activity Monitor to view running processes and their PID values. In the report, I replaced the account name with `[redacted]` and used a redacted example for the absolute path.

## 7. Evidence / files
- [`../evidence/mission-03-system.txt`](../evidence/mission-03-system.txt) - privacy-safe notes about the observations and permissions.

## 8. Commit details
Commit message: `Document operating system and file management`
Status: Committed and pushed.
