# Birthdays

Depuis ce dossier, avec uv installé :

```sh
uv sync
uv run flask --app app run --debug
```

Ouvrez http://127.0.0.1:5000/ dans le navigateur. Pour arrêter le serveur,
utilisez Ctrl + C dans le terminal.

Uv installe si nécessaire Python et les dépendances du projet à partir de
`pyproject.toml` et `uv.lock`. Le fichier `birthdays.db` doit rester dans ce
dossier. Sous WSL, exécutez ces commandes dans le terminal Linux.
