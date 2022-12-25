# Configuring WSL to use the Pants Build System

**WSL**: Windows Subsystem for Linux (Version 2)

Learn about Pants [here](https://www.pantsbuild.org/docs).

The Pants 2 build system runs under Linux. If you are running on either MacOS or
Linux, you're ready to use Pants if you can use the terminal on those systems
(although you might still need to install additional Python interpreters, as
shown later). On Windows, Pants only runs under WSL (_They are working on
supporting Windows directly_). If you have not installed WSL on your machine,
the following instructions will guide you.

## Installing WSL on Windows 10/11 from the Microsoft Store

NOTE: These instructions assume there is no prior WSL on your system. Some steps
might have changed after this was written. You might not see some of the error
messages described here. Some messages changed and even went away during the
development of this information.

- Inside the Microsoft Store, find Ubuntu 22.04.1 LTS. Click the "get" button.
- Upon clicking the "Open" button after installing from the MS Store, you will
  see: `Error: 0x800701bc WSL 2 requires an update to its kernel component. For
  information please visit
  [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)`
- Follow the instructions at the above link to install the update.
- Opening Ubuntu now produces a "virtual disk system limitation" error.
- To fix this, open the Windows File Explorer and navigate to: \
  **`C:\Users\YOUR_USER\AppData\Local\Packages\CanonicalGroupLimited...`**
- Right click on **LocalState**, then **Properties**, then **Advanced**.
- Ensure "Compress contents to save disk space" and "Encrypt contents to secure data" are both ***de***selected.
- Click "OK," then "Apply," then "Apply changes to this folder only."
- Now when you start Ubuntu it should be successful, and will ask for a username and password.
- As per the suggestion, run **`wsl.exe --update`**
- Double check your OS version by running **`lsb_release -a`**

## Starting WSL

- If you're in the Windows command prompt or PowerShell, you can start WSL with
  either `wsl` or `bash`.
- I recommend installing the
  [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install)
  to produce a better experience. This can start up any kind of shell and
  uses multiple tabs.

## Windows Directories vs. Linux Directories

- WSL (Linux) uses its own directory system. It's possible to access the Windows
  directory system from within WSL, but there are problems that show up when
  using Pants.
- It is important that you use the Linux directory system and not the Windows
  directory system when creating Pants projects in WSL.
- If you have cloned this repository into a Windows directory, re-clone it into
  a Linux directory before going through the subsequent sections.
- To discover whether you're in a Windows directory, at your WSL command prompt
  inside your cloned repository, run `pwd`. If the resulting path starts with
  `/mnt/` (typically `/mnt/c/`), then you are in the Windows file system and
  you will [have problems](https://github.com/pantsbuild/pants/issues/16534).
- To fix this, start up a new Linux shell and run `cd ~` to move to your home
  directory on Linux.
- When you run `pwd` you should now see something like `/home/bruce`. Notice
  there's no `/mnt/` at the beginning of the path.
- Navigate to the directory where you want to clone this repository (or create a
  new directory and navigate there) and clone using the `git` command. For
  example: \
  `mkdir tmp` \
  `cd tmp` \
  `git clone https://github.com/BruceEckel/ConfiguringWSLForPants`

### Using Github Desktop

- If you prefer using [Github Desktop](https://desktop.github.com/) rather than
  the command line...
- Start a Linux shell and navigate to the Linux directory where you want
  to clone the repository, as described above.
- Find the path of that directory, to tell Github Desktop where to put the
  repository: run `explorer.exe .` which will open the Windows Explorer
  in that directory.
- Click to the right (away from the path information) inside the address
  bar, and the path information will convert into a URL. For example:
  `\\wsl.localhost\Ubuntu-22.04\home\bruce\tmp`. Copy this to the clipboard.
- Go to <https://github.com/BruceEckel/ConfiguringWSLForPants>.
- Click on the green `<> Code` button.
- Select "Open with Github Desktop."
- Github Desktop should start, and give you a popup window. One of the fields
  in that window is labeled "Local Path".
- Paste the clipboard information as that local path and press the "Clone"
  button.

## Python Version

- Go through steps 0-4 in this repository. Each step contains its own README
  containing the instructions for that step. You'll start with an ordinary
  Python repository (0_sample_without_pants), and add Pants support one step
  at a time.
- You will encounter the following problem:
- The default interpreter for Ubuntu 22.04.1 is Python 3.10.6, so trying to run
  Pants produces: \
`No valid Python interpreter found. For pants_version = "2.16.0.dev0", Pants requires Python 3.7, 3.8, or 3.9 to run. Please check that a valid interpreter is installed and on your $PATH.`
- We need to install a Python interpreter that Pants can work with.

## Installing Additional Python Interpreters

- Ubuntu depends on its default Python installation so you can't remove or
  replace it.
- Note: If you have problems connecting to repos, make sure your VPN is turned
  off.
- The `deadsnakes` repository was the one used in all the posts I found.
- **`sudo add-apt-repository ppa:deadsnakes/ppa`**
- **`sudo apt update`**
- We'll look for Python 3.9: \
  **`apt list | grep python3.9`**
- Install it: \
  **`sudo apt install python3.9`**
- We only need to add it to `$PATH`. No need to use `update-alternatives`.
- If you run **`which python3.9`**, you should see `/usr/bin/python3.9`
- Add the path for python3.9 to the `$PATH` variable. Open the file with
  **`code ~/.bashrc`** and add this to the end: \
  `export PATH="$PATH:/usr/bin/python3.9"`
- Either **`source ~/.bashrc`** or start a new bash shell.
- **`echo $PATH`** to verify that `:/usr/bin/python3.9` is at the end of the path.
- Now when you run Pants you may get a new error: \
`ModuleNotFoundError: No module named 'distutils.util'`
- Fix with: **`sudo apt install python3.9-distutils`**
- Full details of this process can be found [here](https://hackersandslackers.com/multiple-python-versions-ubuntu-20-04/).

## Configuring for PyCharm or VSCode

- [Instructions for configuring an IDE](https://www.pantsbuild.org/docs/setting-up-an-ide).
