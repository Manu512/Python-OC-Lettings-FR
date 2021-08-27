<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png" />
</p>


[![CircleCI](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/master.svg?style=svg)](https://circleci.com/gh/Manu512/Python-OC-Lettings-FR/tree/master)






## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
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


## Déploiement

Fichier des variables environnements disponible à l'adresse :
`oc_lettings_site/settings/.env`

Pré-requis :

- Un compte/acces Github
- Un compte/acces CircleCi
- Un Compte/acces DockerHub
- Un Compte/Acces Heroku
- Un Compte/Acces Sentry

### Description du fonctionnement du Pipeline CircleCi

####Lors d'un commit sur n'importe quelle branche:
- Github va déclenché le workflow 'New-Commit' du Pipeline (le depot) Python-OC-Lettings-FR.
  - Il est décomposé en differents 'jobs':
    - build and test : 
      - va lancer les tests (via pytests)
      - controler le linting PEP8 via Flake8
  
  - Si nous sommes dans la branch Master, la reussi du job build and test, va déclencher:
    - build and push docker:
      - Cela va créer une image docker et l'uploader sur le docker hub.
        Il y aura 2 push identiques mais tagué differement (1 hash du commit et 1 lastest le dernier)
        Cela a pour but de facilité le deployment rapide en local sur la derniere version.
    - #TODO : push to heroku : mise en ligne via la plateforme Heroku.

### CircleCi :

Paramétrage nécessaire : 

Création des variable d'environnement au niveau du projet :

- Dans Projets: 
- Cliquez sur `Project Settings`  (Les 3 petits points)
- Cliquez sur `Environment Variables`  
- Cliquez sur `Add Environment Variables`  

|   Nom des Variables  |   Description   |   Valeurs à renseigner   |
|---    |---   |---    |
|   DOCKER_USER   |   User Docker Hub   |   `manu512`   |
|   DOCKER_TOKEN   |   Token Dockerhub ou Mdp   |   `1321654654654651231654`   |
|   HEROKU_API_KEY |  API Token Heroku  |   `1321654654654651231654`   |
### Github :

- git init
- git add .
- git remote add origin ....
- git push origin master ( origin = remote, master = branch ) 


### Docker Hub :

La commande unique pour récupération de l'application en local et son démarrage immédiat est :

`docker run --pull always -p 8000:8000 --name P13-Application manu512/oc-lettings:lastest`

- P13-Application est le nom de l'application docker  
- manu512 est le compte du Hub Docker  
- lastest peux être remplacé par le hash du commit. Comme son nom l'indique lastest est le dernier commit.


### Heroku :

Le principe d'Heroku est d'être un repository supplémentaire a notre code GIT.



Pour créer une application sur Heroku voici la marche a suivre :
En ligne de commande :  
- heroku create (création de l'application)
- git push heroku master (master etant la branche)
- heroku ps:scale web=1 # Permet de s'assurer qu'une instance est lancée.
- heroku open affiche le site.
- heroku logs --tail affiche les log en direct.

### Sentry :
