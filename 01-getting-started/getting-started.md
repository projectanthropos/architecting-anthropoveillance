## Getting started

* Installing Python + Editors
* Basic shell commands
* Pip and virtual environments
* Basic git

&nbsp;
&nbsp;
&nbsp;

### Installing Python

To install you visit https://www.python.org go to downloads and get the latest version for your particular system.

Python comes with its own default shell with a stand alone GUI which you can check out after installation. If you search for "idle" in your start menu or Mac search box and open the first result, you'll see what it looks like. In this environment you work line by line; you type your command, e.g. `2+2` hit enter, and it returns the result. 

Usually, however, you'd want to work in an editor. If you go "File > New File" from the shell you'll open the python's default editor. As you type in your code, e.g. `print("Hello World!")` it colors different python objects, commands, etc., making it easier for you to read your code. It doesn't autocomplete for you. To run your code you go to  "Run > Run Module."

You may choose to work in the default shell + editor combination. However, there are other editors you can choose from. Atom is one of them for example. To install you visit https://atom.io and download the version for your particular system. It's a free lightweight editor, it autocompletes your code for you, and has many other advantages. When you open Atom, save your file with a .py extension, e.g. "filename.py" and you're ready to code in python.

&nbsp;

### Basic shell commands

Shell, as you've probably guessed by now, is an environment where you do things by typing in commands for your machine to run. Shell is your Command Prompt cmd.exe or its newer version PowerShell in Windows or Terminal in Mac, and Linux. When coding, It's quite useful to know some of its basics.

In MacOSX / Linux Search for `terminal` and open it. In Windows hit `windows key + R` type `PowerShell` hit enter. You can change that annoying blue color in windows powershell by right clicking on the frame and navigating to the color tab. Try typing in some of these.

&nbsp;

**Run a python code** (same as running a code from the python's stand alone shell and editor)

```
python filename.py
```

**Print working directory; show its path** (directory is another name for folders)

```
pwd
```

**List the content of the current directory**

```
ls
```

**Make a new directory**

```
mkdir NAME_OF_YOUR_DIRECTORY
```

**Change directory**

```
cd NAME_OF_YOUR_DIRECTORY
```

**Go up one directory**
```
cd ..
```

**Open a file (mac only)**

```
open FILENAME
```

**Open the current directory in the Finder (mac only)**

```
open .
```

**Print the contents of a file to the screen**

```
cat FILENAME
```

**Print the contents of a file to the screen, with pagination**

```
more FILENAME
```

**Clear the screen**

```
clear
```

**Search for something in a text file, e.g. .txt or .md**

```
grep 'SearchTerm' FileName
```

**Output your search results into a separate text file**

```
grep 'SearchTerm' File.txt > NewFile.txt
```

**Sort a text file alphabetically**
```
sort FILENAME
```

**Get help/print the manual of a given command**
```
man COMMAND
```

&nbsp;
&nbsp;

### Pip and Virtual Environments

While working on your python project you're likely to install additional functionality for python i.e. a library/package. You do so by typing in `pip install packagename` in your system's shell. This, however, will download and install the package in your python's systems folder, making it available globally. This might be a problem e.g. when you're using two different versions of python or working with two different versions of the same package for separate projects, which with the time will most certainly be the case. To avoid cluttering your system, you'd want to create a separate folder and place all the files necessary to run your script in that location, including a particular version of the python interpreter. This separate environment where your project lives is referred to as Virtual Environment. Note, your python script file itself doesn't have to be in that folder.

To create a virtual environment first start your shell (terminal in Mac, powershell in Windows). It'll start in your user's folder which is one folder up from the desktop. Type `pwd` to make sure. You can make a folder right there to store all your virtual environments e.g. by typing `mkdir packages` this will create a folder named packages inside your user's folder. Change into that directory by typing in `cd packages`. Now make another directory for your project's virtual env `mkdir my-project-name` then again change into the new directory `cd my-project-name`. 

&nbsp;

**To create the virtual environment type this** 
```
python -m venv ./venv
``` 

This will create a virtual environment inside that folder, in a subdirectory `./` named `venv` which can also be named otherwise. If you're in a Windows powershell type `tree`, if you're in a Mac Terminal type `ls * -r`, these will show all the files and folders that just got created inside that folder. If you type in `pip --version` however, you'll see that your package installer is still running from the global directory. 

&nbsp;

**To activate the virtual environment you need to load a script from inside the venv folder.** 

In MacOSX type
```
source ./venv/bin/activate
```

in Windows
```
.\\venv\scripts\activate
```

now you should see a `(venv)` in the begining of the line, which indicates you're in that particular virtual environment, and can now work from it. 

If you ran into an 'execution policy' error in windows, run your shell as an administrator (by searching for it then right clicking and running as an admin), then, type in the following `Set-ExecutionPolicy Unrestricted -Force`, and exit the shell. 
Now when you run the powershell just like you did the first time and navigate to your project's virtual env folder e.g. in Windows `cd packages\my-project-name` in Mac `cd packages/my-project-name` you should be able to activate the virtual env, as shown above.

While your virtual env is active you can type in `pip list` to see the default packages installed. For a test type in `pip install beautifulsoup4`to install the beautifulsoup package. Now type in `pip list` again, and you can notice the added package. Type in this `pip freeze > requirements.txt`, it'll create a text file containing info about the packages installed in that virtual environment.

&nbsp;

**To deactivate the virtual environment type** 
```
deactivate
```

&nbsp;
&nbsp;

### Basic git

Git is a form of version control. 
It tracks the changes made to a file, usually a code file, giving you an ability to retrieve an older version of the same file in case your most recent changes broke your code. 

Git is used for collaborations.
When several people work on the same file and commit and push those changes (basically save and upload them to GitHup), git will automatically merge all the changes so you won't have to go line by line to see how your separate versions of code are different.

To use git with a user interface (GUI) go to https://desktop.github.com/ and install GitHub Desktop, then log in. The interface is self-explanatory. You first start a new project or a repository, then enter the project name. Git initializes with certain files that tell it which files to track. You then publish the commit before you make any changes by clicking publish, so your project will be tracked from that point on (a commit is when you submit your changes to GitHub, everytime you progress with a workable version of your code you make a commit).

Note from your virtual env you only need one file to be added to your git repository (another name for project folder), and that's the `requirements.txt`, which is just a list of names of packages and their particular versions.

To use git from the shell, you first need to install it. For Windows visit https://gitforwindows.org/ download and install it.

For Mac you first install homebrew by typing the following (src https://brew.sh/)
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Then, once the install is completed, by typing in the this
```
brew install git
```
Once you've installed the git, you can follow the few simple steps described [here](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) to initialize a git repo on your machine, committing and pushing it to your GitHub account, basically uploading it and keeping in sync. Note, don't upload the virtual env folder you've created, make another directory someplace else and make that your project folder for your python scripts.
