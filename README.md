# Learn Voyage Backend
This is a FastAPI application managed with Poetry, and offers API's to get data of online courses.

## Installation
1. Clone the repository:

```
git clone https://github.com/Hitesh-Saha/learn-voyage-backend.git
```

2. Navigate to the project directory:

```
cd fastapi-app
```

3. Install Poetry (if not already installed):

* On macOS/Linux:

```
curl -sSL https://install.python-poetry.org | python3
```

* On Windows (using PowerShell):

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python
```

4. Install the project dependencies using Poetry:

```
poetry install
```

## Usage
1. Activate the Poetry virtual environment:

```
poetry shell
```

2. Start the FastAPI server:

```
uvicorn main:app --reload
```

3. Open your browser and go to (http://localhost:8000/docs) to access the interactive API documentation (Swagger UI).
4. Explore the API endpoints and test different requests.

## Project Structure
* main.py: Contains the FastAPI application setup and routes.
* app: Directory for additional application modules.
* tests: Directory for unit tests.
* pyproject.toml: Poetry project configuration file.
* poetry.lock: Poetry lock file.
* README.md: Documentation for the project.

## Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature/my-feature).
* Make your changes.
* Commit your changes (git commit -am 'Add new feature').
* Push to the branch (git push origin feature/my-feature).
* Create a new Pull Request.
  
## License
This project is licensed under the MIT License - see the LICENSE file for details.
