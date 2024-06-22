#Table of Contents
- [Template for all Python Projects](#template-for-all-python-projects)
  - [Using GitHub Codespaces](#using-github-codespaces)
  - [Using Local VS Code](#using-local-vs-code)
    - [Creating a Conda Environment within your Workspace](#creating-a-conda-environment-within-your-workspace)
    - [Setting up PyLint](#setting-up-pylint)
- [Notes](#notes)
  - [Notes on Command Line Tools](#notes-on-command-line-tools)
  - [Notes on FastAPI](#notes-on-fastapi)

# Template for all Python Projects

This is a template repository for all of my Python projects. I use virtualenv to create a contained environment for all my Python packages, which i manage with pip. I use GitHub Codespaces to create a remote online instance of Visual Studio Code to run my programs

*GitHub Codespaces is free to use--for education--at the time of writing*

## Using GitHub Codespaces

1. Create a repsitory using this one as a template
2. Create a GitHub codespace
![create_github_codespace](https://user-images.githubusercontent.com/4308316/208309296-505748f4-0a4a-45d3-913f-2cc3b41c5978.png)
3. Open a teminal in the VSC instance and verify the virtualenv was sourced

## Using Local VS Code
- Open up VS Code to a blank editor.
- Save Workspace as "python-sandbox.code-workspace".
- Open up the workspace you just created and add the repository folder to it.
  - It should already contain a .vscode folder with settings configurations
- If you wish to create your own launch.json, go to the "run and Debug" pane (Ctrl+Shift+D) and click on "create a launch.json file".
- As an exmaple, lets create a launch configuration for a python training folder:
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
                "env": {
                    "PYTHONPATH": "${workspaceFolder}\\python_training_nov_2022",
                },
                "args": [
                ]
            }
        ]
    }
  ```

- Change the python path to wherever you have installed python else VSCode default to its own internal version
- Place command line arguments in the arg field
  - if you are using named arguments, provide them as a tuple. For e.g.,
    "--type f" as "args": [("--type", " f")]

### Creating a Conda Environment within your Workspace
- Create a .bash_profile (if one wasnt already created) with the following:
    ```bash
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    eval "$('/c/Users/vcoelho/Miniconda3/Scripts/conda.exe' 'shell.bash' 'hook')"
    # <<< conda initialize <<<
    if [ -f ~/.bashrc ]; then
        source ~/.bashrc
    fi
    ```
- Hit Ctrl+~ to open up the terminal and create a new Conda environment:
    ```conda create -n python_sandbox python=3.11```
- If its unable to find python 3.11, add conda-forge to the list of channels
    ```conda config --append channels conda-forge```
- Activate your environment
    ```conda activate python_sandbox```
- Confirm the version of python installed is 3.11
    ```python --version```
- Add additional tools for linting and type-hinting
    ```python -m pip install autopep8 pylint mypy```
- Tie this new environment in to your launch configuration; Add it to settings.json
    ```
    "python.pythonPath": "C:\\Users\\vcoelho\\Miniconda3\\envs\\python_sandbox"
    ```
    > Note: You can find the environment folder by running
    > ```conda env list```
    >```python_sandbox        *  C:\Users\vcoelho\Miniconda3\envs\python_sandbox```

- Install the python dependencies
    ```
    python -m pip install -r requirements.txt
    ```
- If you do add more pacakges to your environment, be sure to update the requirements.txt file
    ```
    python -m pip freeze > requirements.txt
    ```
- Alternatively, if you have your requirements.txt arranged a certain way, you can add the package name to the file (without a version number), run pip install and figure out which version was installed. For example, we want to install the 'fire'package, we would
  - add fire to requirements.txt
  - run ```python -m pip install -r requirements.txt```
  - run ```python -m pip freeze | grep fire``` to see the version of the package installed,
        ```fire==0.5.0```
  - copy the line over to requirements.txt and pin the fire module to a specific version.

### Setting up PyLint


- Pylint doesn't know where the imports are located. Once the environment is active, we will have pylint create a configuration file for us
    ```pylint --generate-rcfile > .pylintrc```
- Open the file, search for init-hook; the line is usually commented, uncomment it
- Amend the line as follows:
  ```init-hook='import sys; sys.path.append("<path/to/importable/modules>")```

# Notes
## Notes on Command Line Tools

For either the Click or Fire based CLI tools, be sure to make them executables.
```
chmod +x funclog/cli_fire_math_code.py
chmod +x funclog/cli_math_code.py
```
Be sure to add the shebang at the top of the cli python file so it knows where to find the interpreter.
```
#!.env/Scripts/python.exe
```
You can then invoke each script directly at the command line:

```
./funclog/cli_math_code.py --help
```
or,
```
./funclog/cli_fire_math_code.py --help
```

## Notes on FastAPI
*funclog/web_math_code.py* adds a web-accessible API to each of the math functions; you will be able to start a server at http://localhost:8080/docs and play around with each of the functions in real time.