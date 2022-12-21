# Configuring Your Computer to use the Pants Build System

Learn about Pants [here](https://www.pantsbuild.org/docs).

The Pants 2 build system runs under Linux. If you are running on either MacOS or
Linux, you're ready to use Pants if you know how to use the terminal on those
systems (although you might still need to install additional Python
interpreters). On Windows, Pants only runs under Windows Subsystem for Linux
(WSL). (_They are working on supporting Windows directly_). If you have not
installed WSL on your machine, the following instructions will guide you.

## Installing WSL on Windows 10/11 from the MS Store

NOTE: These instructions assume there is no prior WSL on your system. Some steps
might have changed after this was written. You might not see some of the error
messages described here. Some messages changed and even went away during the
development of this information.

- Inside the MS Store, find Ubuntu 22.04.1 LTS, click the "get" button.
- Upon clicking the "Open" button after installing from the MS Store, you will
  see: `Error: 0x800701bc WSL 2 requires an update to its kernel component. For
  information please visit
  [https://aka.ms/wsl2kernel](https://aka.ms/wsl2kernel)`
- Follow the instructions at the link to install the update.
- Opening Ubuntu now produces a "virtual disk system limitation" error.
- To fix this, open the Windows File Explorer and navigate to:
- **`C:\Users\YOUR_USER\AppData\Local\Packages\CanonicalGroupLimited...`**
- Right click on "LocalState", then "Properties," then "Advanced."
- Ensure "Compress contents to save disk space" and "Encrypt contents to secure data" are both **de**selected.
- Click "OK," then "Apply," then "Apply changes to this folder only."
- Now when you start Ubuntu it should be successful, and will ask for a username and password.
- As per the suggestion, run **`wsl.exe --update`**
- Double check your OS version by running **`lsb_release -a`**

## Python Version

- [**Need a better tutorial**] Try this [getting-started tutorial for
  Pants](https://semaphoreci.com/blog/building-python-projects-with-pants). This
  was written for Pants V1, so there are some commands in the tutorial that have
  small mistakes but Pants V2 will help you correct the issues). You will encounter the following problem:
- The default interpreter for Ubuntu 22.04.1 is Python 3.10.6, so trying to run
  Pants produces: \
`No valid Python interpreter found. For pants_version = "2.16.0.dev0", Pants requires Python 3.7, 3.8, or 3.9 to run. Please check that a valid interpreter is installed and on your $PATH.`
- We need to install a Python interpreter that Pants can work with.

## Installing Additional Python Interpreters

- See [here](https://hackersandslackers.com/multiple-python-versions-ubuntu-20-04/) for details.
- Ubuntu depends on its default Python installation so you can't remove or
  replace it.
- Note: If you have problems connecting to repos, make sure your VPN is turned
  off.
- The "deadsnakes" repository was the one used in all the posts I found.
- **`sudo add-apt-repository ppa:deadsnakes/ppa`**
- **`sudo apt update`**
- We'll look for Python 3.9:
- **`apt list | grep python3.9`**
- Install it:
- **`sudo apt install python3.9`**
- We only need to add it to `$PATH`. No need to use `update-alternatives`.
- If you run **`which python3.9`**, you should see `/usr/bin/python3.9`
- Add the path for python3.9 to the `$PATH` variable. Open the file with
  **`code ~/.bashrc`** and add this to the end:
- `export PATH="$PATH:/usr/bin/python3.9"`
- Either **`source ~/.bashrc`** or start a new bash shell.
- **`echo $PATH`** to verify it's at the end.
- Now when you run Pants you may get a new error: \
`ModuleNotFoundError: No module named 'distutils.util'`
- Fix with: **`sudo apt install python3.9-distutils`**
