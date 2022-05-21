<h1 align="center"><b>Vehicle Shifter Backend</b></h1>

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://github.com/maxwellwachira/vehicle-shifter-backend.git)

# Description

Public Service Vehicle commonly known as Matatus usually queue to wait for their turn to carry passengers. The Queuing Process is not done in an ordely way. If the drivers are not keen, they might be skipped by other drivers.<br>
The vehicle shifter app is meant to automate the queuing process. In addition, it can generate reports. The app is made using React JS and FastAPI

# Demo

I have a deployed the application on [Heroku](https://www.heroku.com/)<br>
click the following link to check the API endpoints[https://vehicle-shifter-api.herokuapp.com/docs](https://vehicle-shifter-api.herokuapp.com/docs)

# Table of contents

- [Prerequisites](#Prerequisites)
- [Directory Structure](#Directory-Structure)
- [Running Locally](#Setting-up-Local-Environment)
- [Acknowledgement](#Acknowledgement)
- [License](#License)

# Prerequisites

- [Python - version 3.7 and above ](https://www.python.org/)

# Directory-Structure

vehicle-shifter-backend  
├── auth/  
├── config/  
├── crud/  
├── models/  
├── routes/  
├── schemas/  
├── templates/  
├── **init**.py  
├── .env  
├── main.py # Application entry point  
├── requirements.txt  
└── README.md

# Setting-up-Local-Environment

### clone the repository and navigate to the project directory

```bash
git clone https://github.com/maxwellwachira/vehicle-shifter-backend.git
cd vehicle-shifter-backend/
```

### Create a python virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Project dependencies

```bash
pip install -r requirements.txt
```

create a file and name it as .env. Copy contents of .env.example to .env

# Acknowledgement

Special thanks to [@skndung'u](https://github.com/skndungu) for the idea to make the app.<br>
Special thanks to [Sebastián Ramírez aka @tiangolo](https://github.com/tiangolo) the creator of FastAPI

## <b>License</b>

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=for-the-badge)](LICENSE)
