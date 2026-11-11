# Mission 3 — Understand the Operating System

## 1. Task / objective
I learned what an operating system does and looked at system information, running programs, files, and permissions.

## 2. Work completed

### System information
- Operating system and version: [write what you saw]
- Storage: [write a general result, without private paths]
- Running programs: [name a few ordinary programs; do not include usernames or full paths]

### Processes
A process is a program that is running. It has a number called a PID so the operating system can keep track of it. A browser and a text editor are examples of programs that can run as processes.

### Paths and permissions
An absolute path shows the full location of a file. A relative path shows its location from the folder I am currently in.

- `r` means a file can be read.
- `w` means a file can be changed.
- `x` means a program can be run. For a folder, it allows access to that folder.

### What the operating system does
- Process management: runs programs, such as a browser.
- Memory management: gives programs space to work.
- Device management: helps the computer use devices like a keyboard.
- File management: organizes files and folders.
- User interface: lets me use the desktop or Terminal.
- Security and permissions: controls who can access files.

## 3. Commands / tools used
- `sw_vers` — showed my macOS version.
- `df -h` — showed storage information.
- `ps -ax -o pid,comm | head` — showed some running processes.
- `pwd` — showed my current folder.
- `ls -l` — showed file permissions.

[Keep only the commands you actually ran.]

## 4. My understanding
The operating system helps programs, memory, devices, and files work together. Permissions control who can read or change a file.

## 5. Difficulties faced
I found the process list confusing because it showed many running programs.

## 6. How I resolved them
I looked at the process ID and program name columns and chose a few examples to describe.

## 7. Evidence / files
[List any notes or screenshots you saved. Hide usernames, device names, and private paths.]

## 8. Commit details
Commit message: `Document operating system and file management`
Status: committed and pushed