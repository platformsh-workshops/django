<div align="center">
   <img title="a title" alt="Alt text" src="docs/images/github/git-hub-workshops-text.png">
   <br/><br/>
   <h1>Django on Platform.sh</h1>
</div>

<p align="center">
<strong>Contribute, request a feature, or check out our resources</strong>
<br />
<br />
<a href="https://community.platform.sh"><strong>Join our community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://docs.platform.sh"><strong>Documentation</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://platform.sh/blog"><strong>Blog</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/issues/new?assignees=&labels=bug&template=bug_report.yml"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/issues/new?assignees=&labels=feature+request&template=improvements.yml"><strong>Request a feature</strong></a>
<br /><br />
</p>

<p align="center">
<a href="https://github.com/platformsh-workshops/django/issues">
<img src="https://img.shields.io/github/issues/platformsh-workshops/django.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Issues" alt="Open issues" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/pulls">
<img src="https://img.shields.io/github/issues-pr/platformsh-workshops/django.svg?style=for-the-badge&labelColor=f4f2f3&color=ffd9d9&label=Pull%20requests" alt="Open PRs" />
</a>&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/blob/master/LICENSE">
<img src="https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&labelColor=f4f2f3&color=ffd9d9" alt="License" />
</a>&nbsp&nbsp
<br /><br />
</p>
</p>

<hr>

<p align="center">
<strong>Contents</strong>
<br /><br />
<a href="#about"><strong>About</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#workshops"><strong>Workshops</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contact"><strong>Contact</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="#contribute"><strong>Contribute</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<hr>

## About

Platform.sh is a unified, secure, enterprise-grade platform for building, running, and scaling fleets of websites and applications.
There are many resources available to help you get started running applications on the Platform, and this repository is meant to provide a number of half-day workshops to complement those materials. 

## Workshops

Depending on what you would like to learn, choose one of the available workshops below to start working with Platform.sh. 
The order of the workshops is presented as a kind of learning path - that is, you can start at the top of the list and work your way through each workshop for a full training.

1. [Platform.sh fundamentals for Django](docs/fundamentals/README.md)
2. Performance: Profiling best practices 
3. Decoupling monoliths and frontend interchangeability
4. [Managing a fleet of Django applications](docs/fleet/README.md)

## Contact

This repository is maintained by the Platform.sh Developer Relations team, and they will be notified of all issues and pull requests you open here.

- **Community:** Share your question with the community, or see if it's already been asked on our [Community site](https://community.platform.sh).
- **Slack:** If you haven't done so already, you can join Platform.sh's [public Slack](https://chat.platform.sh/) channels and ping the `@devrel_team` with any questions.

## Contribute

<h3 align="center">Help us keep top-notch templates!</h3>

Every one of our templates is open source, and they're important resources for users trying to deploy to Platform.sh for the first time or better understand the platform. They act as getting started guides, but also contain a number of helpful tips and best practices when working with certain languages and frameworks. 

See something that's wrong with this template that needs to be fixed? Something in the documentation unclear or missing? Let us know!

<p align="center">
<strong>How to contribute</strong>
<br /><br />
<a href="https://github.com/platformsh-workshops/django/issues/new?assignees=&labels=bug&template=bug_report.yml"><strong>Report a bug</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/issues/new?assignees=&labels=feature+request&template=improvements.yml"><strong>Submit a feature request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://github.com/platformsh-workshops/django/pulls"><strong>Open a pull request</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<p align="center">
<strong>Need help?</strong>
<br /><br />
<a href="https://community.platform.sh"><strong>Ask the Platform.sh Community</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<a href="https://chat.platform.sh"><strong>Join us on Slack</strong></a>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
<br />
</p>
<br />
<h3 align="center"><strong>Thanks to all of our amazing contributors!</strong></h3>
<br/>
<p align="center">
<a href="https://github.com/platformsh-workshops/django/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=platformsh-workshops/django" />
</a>
</p>

<br/>

<hr>


# BigFoot Django project

## Outline

1. [Platform.sh fundamentals](docs/01-fundamentals.md)
    - Introduction
    - Configuration & deploys
    - Data & services
    - Rolling back changes
    - Next steps
2. Profiling best practices 
3. [Decoupling monoliths and frontend interchangeability](03-multiapp.md)
    - Introduction
    - Deploying the backend
    - Deploying the frontend
    - Inheritance and editorial workflows
    - Next steps
4. [Managing a fleet of WordPress applications](04-fleet.md)
    - Introduction
    - Organizations
    - Managing multiple projects
    - Growing the fleet
    - Managing the fleet
    - Next steps


- [Debugging Performance in Python and Django applications](https://www.youtube.com/watch?v=khcuqNJR07U)

## Installation

Tested only with Python 3.9.

1. Install requirements using `pipenv`:

   ```bash
   pipenv install
   ```

1. Start the PostGreSQL container:

   ```bash
   docker-compose up -d
   ```

2. `pyscopg2` library requires PostgreSQL to be installed on the system.
   (E.x: you might get `pg_config executable not found` errors during installation)

   Make sure PostgreSQL is installed on the host:

   ```
   > brew install postgresql           # MacOS
   > sudo apt-get install postgresql   # Ubuntu
   ```

3. The database user/name are set to `bigfoot` by default. So, you might
   need to run:
   
   ```
   > sudo -u postgres psql
   postgres> createdb bigfoot && createuser -s bigfoot
   ```


4. Generate fake data:
   
   ```bash
   pipenv run python manage.py migrate
   pipenv run python manage.py generate_fake_data
   ```

5. Run server with `blackfire-python`:

   ```bash
   blackfire-python manage.py runserver
   ```
