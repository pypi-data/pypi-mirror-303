# Earthscale

This is a monorepo for Earthscale. It includes the following packages:
- `earthscale-core`: Core functionality for connecting to the Earthscale backend
- `tiler`: A package for a tile server that serves raster data to the frontend.
- `frontend`: A frontend for visualizing geospatial data.
- `earthscale`: an SDK and CLI for interacting with Earthscale.

Read the [documentation](https://docs.earthscale.ai) for more information.

## Installation

The project requires Python 3.10 and `poetry>=1.8` to be installed. Please checkout [poetry's installation guide](https://python-poetry.org/docs/#installation) for more information. We recommend creating a conda environment for the project:

```shell
conda create -n earthscale python=3.10
conda activate earthscale
```

First, clone the repository via
```shell
git clone https://github.com/earthscale/earthscale.git
```

Then, navigate to the project directory:
```shell
cd earthscale
```

To initialize the project, run:

```shell
make setup
```

## Remote usage

To use the Earthscale SDK, first authenticate with the Earthscale backend in your terminal by running:

```shell
earthscale authenticate
```

Follow the Google OAuth flow to authenticate with the Earthscale backend.

You can access the frontend at [https://app.earthscale.ai](https://app.earthscale.ai). You may need to log in with the same Google account you used to authenticate with the Earthscale backend.

## Local development

### Database setup

First, log into the Earthscale [supabase project](https://supabase.com/dashboard/project/mvkmibwhbplfmurjawlk) via the supabase CLI

```shell
supabase login
supabase link --project-ref mvkmibwhbplfmurjawlk
```

It may initially ask for the database password, which can be found in our secret manager [here](https://console.cloud.google.com/security/secret-manager/secret/supabase_db_password/versions?project=arcane-rigging-422722-h8).

Then, start a local supabase instance and seed it with the necessary data:

```shell
supabase start
make recreate-local-database
```

### Set the development environment variables

With the supabase instance running, you can set the necessary environment variables for local development:

```shell
make dev-env
```

This creates a local `.env` file with the necessary environment variables.

### Running the frontend

To run the frontend, in one shell, run

```shell
make start-frontend
```

This will launch the frontend at `http://localhost:5173`. By default, you can log in with a seeded fake user with the following credentials:
- email: `user1@example.com`
- password: `password123`

### Running the tiler with a local database

To run the tiler with the local database, first edit the credentials file `~/.earthscale/credentials.json` to :

```json
{
    "email": "user1@example.com",
    "password": "password123",
    "supabase_url": "http://localhost:54321",
    "supabase_anon_key": <anon_key_here>
}
```

The anon key can be found in `.env` as `EARTHSCALE_SUPABASE_ANON_KEY`.

In another shell with an active python environment, run

```shell
make start-backend
```

This will start the tiler at `http://localhost:8080`.

### Starting a docs server

To start a local docs server, run

```shell
make start-docs-server
```

This will start a local docs server at `http://localhost:8000`. It will automatically rebuild the docs when changes are made.
