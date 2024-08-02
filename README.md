# python-file-handling
 python file handling project created with virtual environment

 #STEPS FOR CREATING VIRTUAL ENVIRONMENT
         Creating Virtual Environment
Setting up a virtual environment for each Python project on both Windows and macOS ensures that dependencies are isolated and managed effectively. Below is a step-by-step guide for setting up a virtual environment using Python's built-in `venv` module on both operating systems.

### Setting Up a Virtual Environment on macOS

#### Step 1: Install Python
Ensure Python is installed. You can download it from the [official Python website](https://www.python.org/downloads/).

#### Step 2: Create a Project Directory
Create a directory for your project and navigate into it:
```sh

mkdir myproject
cd myproject
```

#### Step 3: Create a Virtual Environment
Use the `venv` module to create a virtual environment:
```sh
python3 -m venv env
```

#### Step 4: Activate the Virtual Environment
Activate the virtual environment:
```sh
source env/bin/activate
```

You should see `(env)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

#### Step 5: Install Packages
Install any packages you need using `pip`:
```sh
pip install Flask
```

#### Step 6: Verify Installation
Check the installed packages:
```sh
pip list
```

#### Step 7: Deactivate the Virtual Environment
When you're done, deactivate the virtual environment:
```sh
deactivate
```

### Setting Up a Virtual Environment on Windows

#### Step 1: Install Python
Ensure Python is installed. You can download it from the [official Python website](https://www.python.org/downloads/).

#### Step 2: Create a Project Directory
Create a directory for your project and navigate into it:
```sh
mkdir myproject
cd myproject
```

#### Step 3: Create a Virtual Environment
Use the `venv` module to create a virtual environment:
```sh
python -m venv env
```

#### Step 4: Activate the Virtual Environment
Activate the virtual environment:
- **Command Prompt**:
  ```sh
  env\Scripts\activate.bat
  ```
- **PowerShell**:
  ```sh
  env\Scripts\Activate.ps1
  ```

You should see `(env)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

#### Step 5: Install Packages
Install any packages you need using `pip`:
```sh
pip install Flask
```

#### Step 6: Verify Installation
Check the installed packages:
```sh
pip list
```

#### Step 7: Deactivate the Virtual Environment
When you're done, deactivate the virtual environment:
```sh
deactivate
```

### Summary of Commands

#### macOS
1. **Create project directory**:
   ```sh
   mkdir myproject
   cd myproject
   ```
2. **Create virtual environment**:
   ```sh
   python3 -m venv env
   ```
3. **Activate virtual environment**:
   ```sh
   source env/bin/activate
   ```
4. **Install packages**:
   ```sh
   pip install Flask
   ```
5. **Verify installation**:
   ```sh
   pip list
   ```
6. **Deactivate virtual environment**:
   ```sh
   deactivate
   ```

#### Windows
1. **Create project directory**:
   ```sh
   mkdir myproject
   cd myproject
   ```
2. **Create virtual environment**:
   ```sh
   python -m venv env
   ```
3. **Activate virtual environment**:
   - Command Prompt:
     ```sh
     env\Scripts\activate.bat
     ```
   - PowerShell:
     ```sh
     env\Scripts\Activate.ps1
     ```
4. **Install packages**:
   ```sh
   pip install Flask
   ```
5. **Verify installation**:
   ```sh
   pip list
   ```
6. **Deactivate virtual environment**:
   ```sh
   deactivate
   ```

By following these steps, you can set up isolated virtual environments for each of your Python projects on both Windows and macOS, ensuring that dependencies are managed effectively and do not interfere with each other.



