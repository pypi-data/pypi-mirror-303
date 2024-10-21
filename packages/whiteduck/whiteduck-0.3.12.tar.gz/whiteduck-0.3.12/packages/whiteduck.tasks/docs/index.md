
# white duck templater

Welcome to the Python Project Starter! This tool allows you to quickly generate and configure Python project templates tailored to different types of development workflows, from general-purpose projects to specialized setups like data science or web applications. With built-in wizards, dependency management, and ready-to-use configurations, you can start coding right away with minimal setup hassle.

!!! note

    You probably know the drill. Scaffolding a project is not hard, but it is cumbersome. Generating this mkdocs documentation took like 3 plugings and a couple of line of codes, which would mean me spending 2 hours of googling the next time I need it.

    This app's main job is it to help in exactly those situation, to ramp yourself up into your next project, without wasting thoughts and time with the boring stuff

## Features

- **Automated Project Setup**: Create fully-configured Python projects in minutes with essential dependencies and tools pre-installed.
- **Modular and Flexible**: Choose from a variety of templates, each designed to support specific development needs such as libraries, web apps, CLI tools, or data science projects.
- **Configuration Wizard**: A step-by-step guide to configure your project type, name, and directory, with options to customize dependencies and modules.
- **Pre-configured Development Tools**: Includes options for setting up linting, testing, profiling, logging, and more, with popular tools like `pytest`, `mypy`, `Black`, and `Loguru`.
- **Documentation Generation**: Templates include support for `MkDocs` and `MkDocs Material` to make it easy to document your project.

## Templates Available

The app comes with pre-built templates to support various types of projects:

- **White Duck Python Stack**: A versatile template with essential development tools for general Python projects.
- **Python Data Science Project Stack**: A data science-focused template, pre-configured with libraries for data manipulation, visualization, and machine learning.

You can also extend and customize these templates to include additional dependencies or features specific to your project needs.

## Getting Started

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/python-project-starter.git
   cd python-project-starter
   ```

2. **Select a Template**: 
   Open the app and select the template that best suits your project type. Each template includes a setup wizard that will guide you through the configuration.

3. **Configure Your Project**:
   - **Project Type**: Choose the project type based on your workflow (e.g., library, web app, CLI tool, data science).
   - **Project Name and Directory**: Specify the name and directory where you want the project to be created.
   - **Modules and Dependencies**: Select additional modules and dependencies you want to include, such as `pre-commit`, `pytest`, `Black`, and others.
  
4. **Run the Setup Wizard**:
   Follow the prompts to configure the project. The wizard will install dependencies, set up project structure, and configure any selected tools.

5. **Initialize the Project**:
   Once configured, the app will initialize the project with the specified tools and settings. You’re now ready to start coding!

## Modules and Dependencies

Each template includes a set of default tools that can be extended or customized. Below is an overview of the main dependencies included:

- **Development Tools**: `pre-commit`, `pytest`, `Black`, `Flake8`, `Mypy`, `Loguru`
- **Data Science Libraries** (Data Science Stack): `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `Jupyter Notebook`
- **Documentation**: `MkDocs`, `MkDocs Material`

These tools help ensure code quality, facilitate testing, and support interactive data exploration and visualization.

## Adding Custom Templates

You can extend the app by creating custom templates. Simply create a new YAML file in the `templates` directory with your desired configuration. Ensure the structure follows the same format as the existing templates, and the app will recognize your custom template during setup.



