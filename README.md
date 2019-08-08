# Simple Notifications

A small package to make sending notifications easy on macOS.

## Installation

```sh
pip install simple-notifications
```

For installation from source, see below.

# System Requirement

Supports OS X 10.10 (Yosemite) to macOS 10.14 (Mojave).

Supports python 2.7, 3.5, 3.6, 3.7.

# Why another package?

The current popular package for sending notifications, `pync`, depends on a ruby program and uses `subprocess` to communicate with that program. Also, to use it, you have to go to install its dependencies separately. 
`simple-notifications`, on the other hand, does not have any non-Python dependency and is super lightweight. 

# Usage

```py
from simple_notifications import notify
notify("Your task is done!")
notify("Your task is done!", sound=True) # This will invoke the default notification sound
notify("Your task is done!", subtitle="Status: Success")
notify("Your task is done!", informative_text="Task took 128ms")
notify("Your task is done!", sound='Glass')

... # Any combination of the above settings

```

# The Hack

Apple requires all programs that sends a notification to have a valid bundle identifier. For a simple Python script, this may not be trivial. So a hack is involved: injecting a bundle identifier into the Objective-C runtime. 

By default, the injected bundle identifier is `org.python.PythonLauncher`. If you have never installed a distribution from the python.org installer, you may not have the `Python.app` software. This may result in your notification not showing up. To solve this, you can change bundle identifier to a package which you know for sure is installed. For example,

```py
from simple_notifications import notify, inject_bundle_identifier
inject_bundle_identifier("com.apple.Terminal")
notify("Your task is done!")
```

Note that this also changes the notification icon. WARNING: You have to do this BEFORE sending out a notification!

# Installation From Source

```sh
git clone https://github.com/pkqxdd/simple-notifications/
cd simple-notifications/simple_notifications
cmake .
make
cd ..
python setup.py install
```
