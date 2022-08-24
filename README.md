# python-automate-the-boring-stuff

- [python-automate-the-boring-stuff](#python-automate-the-boring-stuff)
  - [Introduction](#introduction)
  - [Setting up VSCode](#setting-up-vscode)


## Introduction
Programs from the book: Automate the Boring Stuff with Python, 2nd Edition, by 
**Al Sweigart** ![BookCover](/assets/images/book_cover.jpg). 

## Setting up VSCode

- Open up VS Code to a blank editor.
- Save Workspace as "python-automate-the-boring-stuff.code-workspace".
- Create a folder at the same level, with the same name: "python-automate-the-boring-stuff".
- Open up the workspace you just created and add the folder to it.
- Next, go to the "run and Debug" pane (Ctrl+Shift+D) and click on "create a launch.json file".
- Add the following to it
  ```
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "python": "C:\\Users\\vcoelho\\Miniconda3\\python.exe",
                "program": "${file}",
                "console": "integratedTerminal",
                "args": [
                ]
            }
        ]
    }
  ```

- Change the python path accordingly else VSCode default to its own internal version
- Place command line arguments in the arg field
  - if you are using named arguments, provide them as a tuple. For e.g.,
    "--type f" as "args": [("--type", " f")]
