
# YAML Template Structure and Logic Guide

This document explains the structure and logic of the YAML files used in the Python Project Starter. Each YAML file defines the configuration for creating a specific type of Python project template, with options for customizing tools, dependencies, and project settings.

## General Structure of the YAML Files

The YAML files are organized into key sections:

- **version**: Specifies the template version.

- **template**: The name of the project template.

- **short_description**: A brief overview of the template’s purpose.

- **description**: A detailed description of what the template includes and its main features.

- **docs**: Points to a documentation file within the template structure.

- **components**: Specifies additional modules or components included in the template.

- **variables**: Defines default variables for the project configuration.

- **modules**: Lists the specific modules to be installed and configured as part of the project setup.

- **prompts**: Configures the interactive prompts that guide users through the template setup.

- **steps**: Details the sequence of operations that will be executed during the template setup process.


### Example Overview
```yaml
version: 1.0
template: "Python Data Science Project Stack"
short_description: "A template to create a Python data science project."
description: |
  This template sets up a Python project optimized for data science workflows.
docs: "templates/docs/data_science_guide.md"
components: "templates/modules"
```

## Key Sections Explained

### Variables
The `variables` section holds default values for various project settings. These values can be used to prepopulate fields during project setup.
```yaml
variables:
  - projectname:
      value: "ds_project_[[wd.GUID]]"
  - projectdir:
      value: "C:/DataScienceProjects"
```

### Modules
The `modules` section lists all modules that will be installed and configured. Each module has an `id`, `type`, and `displayName`. Modules can have arguments that specify paths or settings.
```yaml
modules:
  - id: "pandas"
    type: dependency
    displayName: "Installing Pandas..."
  - id: "init_project"
    type: init
    arguments:
      - path: "[[projectdir]]"
      - projectname: "[[projectname]]"
```

### Prompts
The `prompts` section defines interactive questions that gather user input. Each prompt has an `id`, a `prompt` question, a `value_set` for choices, and a `default` value. Some prompts include `description` for additional context.
```yaml
prompts:
  - id: "kind_of_project"
    prompt: "What type of data science project are you creating?"
    value_set: ["data_analysis", "machine_learning", "data_visualization"]
    default: "[[kind_of_project]]"
```

### Steps
The `steps` section outlines the execution order. Each step can refer to a module, prompt, or other action. Conditional logic is also available to skip certain steps based on previous inputs.
```yaml
steps:
  - id: "wizard"
    type: wizard
    title: "Configure Your Data Science Project"
    value:
      - prompt: "kind_of_project"
      - prompt: "projectname"
  - id: "exec_init_project"
    title: "Setting Up Project"
    type: module
    value: init_project
```

## Conditional Logic in Steps
The steps can include conditions to control the flow based on user responses. Conditions use variables to determine if certain steps should be executed.
```yaml
steps:
  - id: "exec_do_pre_commit"
    title: "Configuring Pre-commit"
    type: module
    value: pre-commit
    condition:
      - var: "do_pre_commit"
        value: True
```

By following this structure, each template is highly customizable and can be adapted to different types of projects while maintaining a consistent setup process.
