<div align="center">
   <img title="a title" alt="Alt text" src="images/github/git-hub-demos.png">
   <br/><br/>
   <h1>Platform.sh fundamentals for Django</h1>
</div>

## About

DevOps engineers are often the sole key-holders of both environments and the understanding of how infrastructure dependencies are satisfied and updated. But what happens if they leave? And how easy are development environments to provision once you have hundreds of sites?

You’ll find those answers in this workshop, where you’ll approach DevOps differently for Django with Platform.sh. Each developer will configure infrastructure themselves with simple abstractions, and leverage tools they’re already using to provision environments on-demand.

### Outline

1. Getting started and introduction
1. Running locally
1. Setting up Platform.sh with an integration
1. Adding Platform.sh configuration
1. Data and environments on Platform.sh
1. Writing and merging new features
1. Rolling back changes: Reverts and rollbacks
1. Next steps

## Before the workshop

Before starting the workshop, there are a few requirements you will need to install and setup in order to follow the lesson.
Take a look at those requirements, then follow the steps listed below.

### Requirements

- A GitHub account
- Docker installed
- pipenv installed
- A Platform.sh account
- The Platform.sh CLI installed locally

### Steps

1. Create a Platform.sh account.

    Platform.sh provides a free one month trial, which will provide all of the resources you will need to go through these Getting Started guides.

    Before starting, be sure to [register for a trial Platform.sh account](https://auth.api.platform.sh/register) if you have not done so already. You can use your email address to register, or you can sign up using an existing GitHub, Bitbucket, or Google account. If you choose this option, you will be able to set a password for your Platform.sh account later.

    You will be given an option to create a project at this point (two options: Use a template and Create from scratch). Click the Cancel button in the right-hand corner of the screen for now - you will create a project later in the workshop.

1. Install the Platform.sh CLI:

    In addition to a Platform.sh account, this workshop uses the Platform.sh CLI. The CLI is the primary, and the most useful, tool for deploying applications and interacting with your projects.

    ```bash
    > curl -fsS https://platform.sh/cli/installer | php                 # Linux/MacOS
    > curl -f https://platform.sh/cli/installer -o cli-installer.php    # Windows
    > php cli-installer.php
    ```

1. Authenticate the CLI with your Platform.sh account:

    ```bash
    platform login
    ```

1. Generate template repo

    [Use this link to generate a copy of the workshop repository in your own namespace](https://github.com/platformsh-workshops/django/generate).

1. Clone a copy locally

    Use the **<> Code** dropdown on your repository to retrieve the clone command

    ```bash
    git clone git@github.com:<YOUR_NAMESPACE>/django.git
    ```

## Getting started and introduction

## Running locally
 
1. Install requirements using `pipenv`:

   ```bash
   cd django
   pipenv install
   ```

1. Install PostgreSQL requirements (`pyscopg2`) if needed (You will see a `pg_config_executable not found` error during installation if needed):

   ```bash
   > brew install postgresql           # MacOS
   > sudo apt-get install postgresql   # Ubuntu
   ```

1. Start the PostgreSQL container:

    ```bash
    docker-composer up -d
    ```

1. Create the database:

    This repository's `settings.py` configures the database credentials by default as follows:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bigfoot',
            'USER': 'bigfoot',
            'PASSWORD': 'bigfoot',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Create the `bigfoot` database and user in the PostgreSQL container:

    ```bash
    > sudo -u postgres psql
    postgres> createdb bigfoot && createuser -s bigfoot
    ```

1. Perform migrations:

    ```bash
    pipenv run python manage.py migrate
    ```

1. Generate starter data in the database:

    ```bash
    pipenv run python manage.py generate_fake_data
    ```

1. Run the server

    ```bash
    pipenv run python manage.py runserver
    ```

<div align="center">
<img title="a title" alt="Alt text" src="images/app-preview.png">
</div>


## Setting up on Platform.sh

1. Create your first empty project:

    ```bash
    platform create
    ```

    Follow the prompts to name the project, 

1. Get a GitHub token

1. Set up the integration

## Add Platform.sh configuration

1. Create a new branch to work from:

    ```bash
    git checkout -b platformify
    ```

1. Configure services:

1. Configure routes:

1. Configure application:

1. Commit and push to Platform.sh:

1. Test the data:

1. Merge into production:

1. Reseed production data: