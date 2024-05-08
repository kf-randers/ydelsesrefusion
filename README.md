# Python app template projekt
Template til nye Python app projekter.
Projekt indeholder en bare bone Flask app
* healthz endpoint
* unit test af healthz endpoint

# Brug af python-app-template
1. Klik på "use this template" og vælg "create a new repository"
2. Udfyld skærmbillede med information om den nye service
3. Åbn dit nye git projekt

# Nyt Python app projekt
Nedenstående relaterer sig til et nyt Python app projekt der er baseret på denne template.

## Udvikling i et Codespace:
1. Gå til det nyoprettede repository i github.
2. Klik på den grønne <>Code knap og vælg "create codespace on \<branch>"
3. Kør ```. ./setup-dev-linux.sh ```, scriptet sætter et virtual environment op og installerer pakkerne i app/requirements.txt og requirements-dev.txt

## Udvikling lokalt:
1. Gå til det nyoprettede repository i github.
2. Klik på den grønne <>Code knap og kopier url'et, clone det med git: ```git clone <url>```
3. Kør ```. ./setup-dev-linux.sh ``` (Linux) eller ```setup-dev-windows.bat``` (Windows), scriptet sætter et virtual environment op og installerer pakkerne i app/requirements.txt og requirements-dev.txt

## Quick start

### Almindelige commands
* Start app'en:  ```python app/app.py```
* Start app'en i docker container: ```docker-compose up```
* Unit tests: ```pytest```
* Unit tests med coverage ```pytest --cov=app```
* Lint: ```flake8 --ignore=E501 app tests --show-source```

### Logning
* Logning gøres med logger og ikke print() functionen
* Logger kan hentes fra [app/utils/logging.py](/app/utils/logging.py)
* Eksempel på prometheus gauge [her](/app/utils/logging.py#L9) og brugt [her](/app/app.py#L15)

### Database
* Eksempel i [app/database.py](/app/database.py)
* Nødvendige pakker [app/Dockerfile](/app/Dockerfile#L13)
* Nødvendigt modul [app/requirements.txt](/app/requirements.txt#L4)
* Opsætning af database lokalt [docker-compose.yml](/docker-compose.yml#L22)

### Skriv til filer
* Hvis der skal skrives til filer skal det være på et eksternt mount
* Eksempel til at test lokalt [docker-compose.yml](/docker-compose.yml#L18)

### Kør kode på bestemt tidspunkt eller med interval
* Eksempel i [app/app.py](/app/app.py#L18)
* Nødvendigt modul [app/requirements.txt](/app/requirements.txt#L5)

# TODO
* deploy
* frontend - new template
