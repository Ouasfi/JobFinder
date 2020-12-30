# Job Finder

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
## About <a name = "about"></a>

A simple utility to automate job offers search and filtring usings keywords searchs. Next releases should include filtring features bases on natural language processing models.  
## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.



### Prerequisites
 - Python 

### Installing

First clone this repo:
```
git clone https://github.com/Ouasfi/JobFinder.git
```

Use a virtual env and install requirements

```
python3 -m venv ./.venv
source .venv/bin/activate
```
Install deps
```
pip install -r requirements.txt
```
## Usage<a name = "usage"></a>

Run a job search:
```
python main.py -j data -t internship
```

