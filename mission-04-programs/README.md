# Mission 4 - How Programs Run

## 1. Task / objective
I wrote and ran a small Python program and compared compilers with interpreters.

## 2. Work completed
I created `hello.py` with one line of Python code:

```python
print("Hello from Python")
```

When I ran it, the output was:

```text
Hello from Python
```

| Point | Compiler | Interpreter |
|---|---|---|
| When it works | Usually translates the source before the program runs. | Usually reads and carries out instructions while the program runs. |
| Typical result | Often creates a separate executable or translated file. | Produces the program's results as it runs. |
| Example | GCC can compile C code. | Python can run a `.py` program. |
| One advantage | The translated program can run quickly. | It is quick to try and change code while learning. |

A compiler translates source code before the program runs. An interpreter reads instructions and carries them out while the program runs. Python is commonly used as an interpreted language, though its implementation can also translate code into bytecode first. Both approaches help the computer carry out the program's instructions.

## 3. Commands / tools used
- `python3 --version` - checked the Python version (Python 3.14.5).
- `python3 hello.py` - ran the program and displayed `Hello from Python`.

## 4. My understanding
The computer needs software to translate or carry out the instructions in a program. A compiler usually translates code before it runs, while an interpreter works through the instructions as the program runs.

## 5. Difficulties faced
At first, I was unsure how to run the Python file from Terminal.

## 6. How I resolved them
I ran `python3 hello.py` from the Mission 4 folder and checked that the message appeared.

## 7. Evidence / files
- [`hello.py`](hello.py) - the program I ran.

## 8. Commit details
Commit message: `Add and run Mission 4 Python program`
Status: Committed and pushed.
