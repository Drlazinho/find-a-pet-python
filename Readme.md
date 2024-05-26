
# Find Your Pet

Find Your Pet is a web application that allows users to register themselves and their adopted pets. The application is built using the Model-View-Controller (MVC) architecture and employs various tools and libraries to ensure its functionality and maintainability.

* MVC Architecture: The application follows the MVC pattern, separating concerns and promoting code organization.
* Unit Testing: Unit tests are implemented using Pytest, ensuring the correctness of individual components.
* Code Standardization: Pylint is utilized for code linting, enforcing consistent coding style and identifying potential issues.
* Pre-commit Hooks: Pre-commit hooks are employed to automate code checks and protect code quality before committing changes.
* HTTP Request Validation: Pydantic is used to create data validators, ensuring valid input data for API requests.
* Error Handling: A function is implemented to gracefully handle different types of errors, such as BadRequestError, NotFoundError, and UnprocessableEntityError.
* Swagger Documentation: Swagger documentation is generated using Flask-RESTx.


### Routes

* api/people: Creates a new person record along with their pet information.
* api/people/:person_id: Retrieves a specific person's details based on their ID.
* api/pets: Lists all registered pets.
* api/pets/delete: Deletes a pet from the list based on its name.


## Technology Stack:

**Back-end:** Python, flask, pytest, pylint, pydantic

**DB:** sqlite


## Screenshots

![App Screenshot](https://i.pinimg.com/736x/e9/19/45/e91945bec8db7d375c45a1b3eb6d693d.jpg)


## Running Locally:

Clone the project:

```bash
  git clone https://github.com/Drlazinho/find-a-pet-python.git
```

Navigate to the project directory:

```bash
  cd find-a-pet-python
```

* Create a virtual environment using Python 12.2 (recommended):

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server:

```bash
  python run.py
```


### Exemplos

Defining a function that combines the Model, Controller, and View components for route handling:

```python
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView

def person_creator_compose():
    model = PeopleRepository(db_connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view

```


## Documentation

[Documentação Swagger](https://find-a-pet-python.onrender.com/docs)


## License

[MIT](https://choosealicense.com/licenses/mit/)

