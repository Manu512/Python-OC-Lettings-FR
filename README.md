<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png" />
</p>

**Master Branch :** [![CircleCI](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/master.svg?style=shield)](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/master)    |    **Dev Branch :** [![CircleCI](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/dev.svg?style=shield)](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/dev)


## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### MacOs / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---
## Déploiement

Fichier des variables environnements disponible à l'adresse : `oc_lettings_site/settings/.env`

**Particularité :**  
oc_lettings_site/settings contient plusieurs fichiers.
local.py est le fichier de setting avec les variables local et du docker.
heroku.py est le fichier de setting avec les variables utilisé pour l'application heroku.

le fichier .env doit contenir au minimum les lignes suivantes : (Bien entendu ce sont de fausses données)  
`SECRET_KEY='fp$9^59[3]sriajg$_%]=5trot9g!1qa@ew(o-1#@=&4%=hp46(s'`  
`SENTRY_DSN='https://0ae682071519451cb76dc3f7@o977250.ingest.sentry.io/5933731'` # Je vais pas sécuriser l'application et l'afficher ici ;o)  
`ALLOWED_HOSTS=127.0.0.1,[::1],0.0.0.0,.herokuapp.com` # Cette ligne est facultative en mode debug=True


**Pré-requis :**

- Un compte/acces Github
- Un compte/acces CircleCi
- Un Compte/acces DockerHub
- Un Compte/Acces Heroku
- Un Compte/Acces Sentry

### Description du fonctionnement du Pipeline CircleCi

#### Lors d'un commit sur n'importe quelle branche autre que la master :
- workflow 'build-and-test' du Pipeline (le dépôt) Python-OC-Lettings-FR.
  - Il est décomposé en différents 'jobs':
    - build and test : 
      - va lancer les tests (via pytests)
      - contrôler le linting PEP8 via Flake8
- le workflow 'dev-built-and-deploy' attendra notre avail pour se lancer
  - les jobs sont :
    - docker build and push
    - push sur heroku
    - 
#### Lors d'un commit sur la branche master :
   
- le workflow master_commit va se lancer
     - Sa réussite du job ‘build and test’, va déclencher:
        - build docker:
          - Cela va créer une image docker et l'uploader sur le docker hub.
        - push docker:
            Il y aura 2 push identiques mais tagué différemment (1 hash du commit et 1 lastest le dernier)
            Cela a pour but de facilité le déploiement rapide en local sur la dernière version.
        - heroku/deploy-via-git:
            Va lancer le build de l'application sur Heroku via Git.

---

## CircleCi :

Paramétrage nécessaire : 

Création des variables d'environnement au niveau du projet :

- Dans **Projets**:
- Cliquez sur `Project Settings`  (Les 3 petits points)
- Cliquez sur `Environment Variables`  
- Cliquez sur `Add Environment Variables`  

|   Nom des Variables  |   Description   |   Valeurs à renseigner   |
|---    |---   |---    |
|   DOCKER_USER   |   User Docker Hub   |   `manu512`   |
|   DOCKER_TOKEN   |   Token Dockerhub ou Mdp   |   `1321654654654651231654`   |
|   HEROKU_API_KEY |  API Token Heroku  |   `1321654654654651231654`   |
| SENTRY_DSN    | URL Sentry  | `https://0ae682071519451cb7cb551c5d6dc3f7@o977250.ingest.sentry.io/5933731` |
| SECRET_KEY  |  DJANGO SECRET_KEY  |  `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s`  |
---

## Github :

[Github Repository](https://github.com/Manu512/Python-OC-Lettings-FR) permet de faire le versionning de notre projet/application.

---

## Docker Hub :

[Docker-Hub Manu512 Repository](https://hub.docker.com/repository/docker/manu512/oc-lettings) permet de stocker en ligne l'image docker de notre application.  

La commande unique pour récupération de l'application en local et son démarrage immédiat est :

`docker run --pull always -p 8000:8000 --name P13-Application manu512/oc-lettings:lastest`

- P13-Application est le nom de l'application docker  
- manu512 est le compte du Hub Docker  
- lastest peux être remplacé par le hash du commit. Comme son nom l'indique lastest est le dernier commit.

---

## Heroku :
[L'application sur Heroku](https://oc-lettings-512.herokuapp.com/)  

Heroku permet d'heberger notre application.

En cas de necessité ou en cas de suppression, il faut créer l'application 'oc-lettings-512'

heroku auth:login
heroku create oc-lettings-512 --region eu
heroku config:set -a oc-lettings-512 DEBUG=False
heroku config:set -a oc-lettings-512 SENTRY_DSN=https://0ae682071519451cb7cb551c5d6dc3f7@o977250.ingest.sentry.io/5933731
heroku config:set -a oc-lettings-512 SECRET_KEY="fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

---

## Sentry :

Sentry permet de faire le [monitoring de l'application](https://sentry.io/organizations/manu512/projects/manu512/?project=5933731).

Elle permet également de détecter des éventuels bug/issues.