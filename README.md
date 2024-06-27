# Python: 100 Days of Coding <!-- omit in toc -->

# Table of Contents <!-- omit in toc -->
- [Introduction](#introduction)
- [General Setup](#general-setup)
  - [Using GitHub Codespaces](#using-github-codespaces)
  - [Using Local VS Code](#using-local-vs-code)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Creating a venv Environment](#creating-a-venv-environment)
    - [Creating a Conda Environment within your Workspace](#creating-a-conda-environment-within-your-workspace)
    - [Setting up PyLint](#setting-up-pylint)
- [Course Notes](#course-notes)

# Introduction

This repository contains all the coding assignments from the Udemy course, _100 Days of Code: The Complete Python Pro Bootcamp_.

# General Setup
:memo: I use Visual Studio Code as my primary development IDE
:memo: I use virtualenv to create a contained environment for all my Python packages, which i manage with pip.
:memo: I also use GitHub Codespaces to create a remote online instance of Visual Studio Code to run my programs

:warning: *GitHub Codespaces is free to use--for education--at the time of writing*

## Using GitHub Codespaces

1. Create a repsitory using this one as a template
2. Create a GitHub codespace
![create_github_codespace](https://user-images.githubusercontent.com/4308316/208309296-505748f4-0a4a-45d3-913f-2cc3b41c5978.png)
3. Open a teminal in the VSC instance and verify the virtualenv was sourced

## Using Local VS Code
- Open up VS Code to a blank editor.
- Save Workspace as _python_100_days_of_coding.code-workspace_.
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
                    "PYTHONPATH": "${workspaceFolder}\\python_100_days_of_coding",
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

## Creating a Virtual Environment
 You have the option to create an environment using either _venv_ or _conda_.

### Creating a venv Environment
- _venv_ is part of Python's standard library
- Create a virtual environment folder at the root of your repository
    ```bash
    python -m venv venv
    ```
- activate the virtual environment
    ```bash
    source venv/Scripts/activate
    ```
  You will see the activated environment over your terminal prompt
  ![activated_python_venv](/docs/images/activated_python_venv.png)
- Install the python dependencies
    ```
    python -m pip install -r requirements.txt
    ```
- If you do add more pacakges to your environment, be sure to update the requirements.txt file
    ```
    python -m pip freeze > requirements.txt
    ```
- To deactivate the virtual environment simply,
    ```bash
    deactivate
    ```

### Creating a Conda Environment within your Workspace
- Create a .bash_profile (if one wasnt already created) with the following:
    ```bash
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    eval "$('/c/Users/<username>/Miniconda3/Scripts/conda.exe' 'shell.bash' 'hook')"
    # <<< conda initialize <<<
    if [ -f ~/.bashrc ]; then
        source ~/.bashrc
    fi
    ```
- Hit Ctrl+~ to open up the terminal and create a new Conda environment:
    ```conda create -n python_100_days_of_coding python=3.11```
- If its unable to find python 3.11, add conda-forge to the list of channels
    ```conda config --append channels conda-forge```
- Activate your environment
    ```conda activate python_100_days_of_coding```
- Confirm the version of python installed is 3.11
    ```python --version```
- Add additional tools for linting and type-hinting
    ```python -m pip install autopep8 pylint mypy```
- Tie this new environment in to your launch configuration; Add it to settings.json
    ```
    "python.pythonPath": "C:\\Users\\<username>\\Miniconda3\\envs\\python_100_days_of_coding"
    ```
    > Note: You can find the environment folder by running
    > ```conda env list```
    >```python_100_days_of_coding        *  C:\Users\<username>\Miniconda3\envs\python_100_days_of_coding```

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

  For example,

  ```
  init-hook=init-hook='import sys; sys.path.append("C:\\Users\\<username>\\repositories\\python_100_days_of_coding\\src")
  ```

# Course Notes
