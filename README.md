SIEMEz
=====

SIEMEz is a truly free security solution that allows anyone the ability to deploy their own Security Incident and Event Management System.
SIEMEz allows for the ingestion of Syslog content which can then be searched and analysed. The aim of the project is to allow for easy integration of DevOps, Machine Learning and Advanced Automation.

# Motivation
While there are several SIEM solutions available, many require enterprise licensing to utilise effectively.
The annoyance of enterprise licensing for user management, or even dashboarding and the lack of further integration of other areas of computing has led
to the creation of this project. Security for hobbyists, small- medium, and large businesses should not be held ransom to enterprise licensing.

# Build Status
Build status from TravisCI
[![Build Status](https://img.shields.io/travis/TheAlgorithms/Python.svg?label=Travis%20CI&logo=travis&style=flat-square)](https://travis-ci.com/github/jwhitt3r/SIEMEz)

# Documentation
For all documentation regarding SIEMEz, please navigate to the [Wiki](https://github.com/jwhitt3r/SIEMEz/wiki).

# Code Style
This project follows the standard styling of [PEP8](https://www.python.org/dev/peps/pep-0008/)

# Framework
The core of SIEMEz is the Django framework, with its maturity in the web development world, coupled with the flexibility of Python, allows anyone to extend SIEMEz.
In addition, the pipenv virtual environment is used along with Docker for the ability to deploy quickly, seamlessly and efficiently.

Overall the project utilises five main components:
* Django Web and Rest Framework
* Pipenv
* Docker
* Python
* RSyslog

The TravisCI also allows for extensions to allow for DevSecOps extensions, see .travis.yml

# Features
SIEMEz allows for the quick deployment and integration of log files to allow for quick security analysis but also extending to the easy integration of machine learning models.

# License
This project is ment to be flexible and easy to integrate but allowing others to use and adapt to their needs. While this is the case, any changes to the project should be open and discussed to better the security community.

# Contribution
To help out with SIEMEz contact me at: contribute_siemez@exit.wtf
Follow me on [Twitter](https://twitter.com/Jack_WJ)

# Screenshots
![Event Dashboard](https://github.com/jwhitt3r/SIEMEz/blob/master/docs/screenshots/images/event_dashboard.png)
![Incident Case](https://github.com/jwhitt3r/SIEMEz/blob/master/docs/screenshots/images/incident_case.png)
![Search Event](https://github.com/jwhitt3r/SIEMEz/blob/master/docs/screenshots/images/search_event.png)
