<div align="center">
   <img title="a title" alt="Alt text" src="docs/images/github/git-hub-workshops-text.png">
   <br/><br/>
   <h1>Django on Platform.sh workshops</h1>
</div>



## Django on Platform.sh workshops

The following repository can be used to go through a number of different hands-on workshops for working with Django on Platform.sh. 

1. [Platform.sh fundamentals](docs/01-fundamentals.md)
2. Performance: Profiling best practices 
3. [Decoupling monoliths and frontend interchangeability](03-multiapp.md)
4. [Managing a fleet of Django applications](04-fleet.md)


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
