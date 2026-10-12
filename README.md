# Spark project template

- Example [spark `4.2.0`](https://spark.apache.org/docs/4.2.0/api/python/index.html) setup
- pyspark `4.2.0` [dependencies versions](https://spark.apache.org/docs/4.2.0/api/python/getting_started/install.html#spark-sql)

## Local setup

Execute all `make` commands from `docker/` folder.


Build docker image:

```sh
make build
```

Run spark:

```sh
make run
```

Run example `example_job.py` pyspark job:

```sh
make submit app=example_job.py
```

Create venv and download requirements (for vscode Intellisense engine)

```sh
python -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

`.vscode/settings.json` settings explained

- `python.analysis.extraPaths`: Tells Pylance (the IntelliSense engine) where to look for imported modules.
- `python.envFile`: Tells vscode to load your `.pythonpath` file for running scripts and debugging.
- `python.terminal.useEnvFile`: Ensures integrated terminals automatically load your `PYTHONPATH` when you run scripts.

## UI

- Master UI: [http://localhost:9090/](http://localhost:9090/)
- History server UI: [http://localhost:18080](http://localhost:18080/)
