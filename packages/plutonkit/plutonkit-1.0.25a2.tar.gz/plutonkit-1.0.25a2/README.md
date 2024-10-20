# pluton-kit
Create your project from the current selection we had on the lobby, But in the future we are working to share your ideas with other developer.

[![PIP version][pip-image]][pip-url] 
[![Build Status](https://github.com/fonipts/pluton-kit/actions/workflows/cicd.yaml/badge.svg?branch=main)](https://github.com/fonipts/pluton-kit/actions)

[Site](https://plutonkit.codehyouka.xyz/) |
[Docs](https://plutonkit.codehyouka.xyz/api) |
[Architecture lobby](https://github.com/fonipts/pluton-lobby) |
[Readthedocs sources](https://pluton-kit.readthedocs.io/en/latest/) |

## Introduction
Building from scratch is quite a daunting task. Constructing your thought, looking for feature and research it will take alot of your time in figuring what will you do next. Therefore I decided to create application where you can choose in different framework, either zero or hero it will help you alot to visualize what framework will you choose.

## Installation
In your local machine
```
pip install -e .
```
In using Pip install
```
pip install plutonkit
```

## Why we need another project template
There are several template generator that is available public repository, but they lack of user control in favored of there likes.
- to have condition, for feature that you want and available in architecture.
- Custom template that makes this project unique.


## Roadmap
Currently we are in alpha phase had not reach 100% test coverage and some linter(due to feature I am currently in focused) but still committed to deliver the improvement if the tool.

## Available command you can use at your terminal
The commands must in this format  `plutonkit <Command type>` 
|Command type | Description| Example |
|------------- | ------------- | ------------- |
|clone_project | Clone your project from project.yaml file  | `plutonkit clone_project source=<directory name>`|
|create_achitecture | Start creating your own architecture from scratch  | `plutonkit create_achitecture`|
|create_project | Start creating your project in our listed framework  | `plutonkit create_project`|
|validate_blueprint | Validated your blueprint before shipping to production  | `plutonkit validate_blueprint <directory name>`|
|cmd | Executing command using plutonkit. the details of your command can be found at `command.yaml` | `plutonkit cmd start` or `plkcmd start`|
|help | See available command for plutonkit | `plutonkit help` |

![Alt text](https://github.com/fonipts/pluton-kit/blob/pre/document-1.0.2a0/resources/pluton-kit-terminal-design.gif?raw=true "terminal")


## How to use the command
Structure of your command, should follow this format

in `command.yaml` 
```
env: {} 
script: 
  {command_name}:
    command:
    - {executed command}
   

```
For quick command execution, we had a new abbrevation that called
`plkcmd` instead of `plutonkit cmd`. 

[pip-url]: https://pypi.org/project/plutonkit/
[pip-image]: https://img.shields.io/badge/plutonkit-1.0.25alpha2-brightgreen
