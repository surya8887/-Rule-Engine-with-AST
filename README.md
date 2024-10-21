Technologies Used
    Python 3.x
    Django 5.x
    Tailwind CSS for styling

Features:
    Create, evaluate, and manage eligibility rules.
    Rules can be combined using logical operators (AND, OR).
    User-friendly interface with form submissions for rule creation and evaluation.
    Abstract Syntax Tree representation for flexible rule management.


Codebase Structure
rule_engin_first/
│
├── manage.py               # Django's command-line utility for administrative tasks
├── rule_engin_first/            # Django project folder
│   ├── __init__.py
│   ├── settings.py         # Settings and configurations for the Django project
│   ├── urls.py             # URL routing for the Django project
│   └── wsgi.py             # WSGI configuration for deployment
│
├── rules/                      # Application folder for the rule engine
│   ├── migrations/             # Database migrations folder
│   ├── __init__.py
│   ├── admin.py                # Django admin configurations
│   ├── apps.py                 # Application configurations
│   ├── models.py               # Models for rules and their metadata
│   ├── views.py                # Views for handling requests and responses
│   ├── urls.py                 # URL routing for the rules app
│   └── test.py                 # test for testing  the rules app
│   ├── forms.py                # Forms for rule creation
│   ├── templates/              # HTML templates for the application
│   │   ├── rule_list.html      # Template for displaying the list of rules
│   │   ├── rule_create.html    # Template for creating new rules
│   │   └── rule_evaluate.html  # Template for evaluating rules
│   └── utils.py                # Utility functions for AST handling and rule evaluation
│
└── static/                     # Static files for CSS and JavaScript
    ├── css/
    │   └── tailwind.css        #Tailwind CSS file
    └── js/
|___ requirements.text          #  List of dependencies for the project

1. Clone the Repository:

    git clone https://github.com/yourusername/rule_engine.git
    cd rule_engin_first

2. Set Up a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Migrate the Database::
    python mange.py makemigrations
    python mange.py migrate
    
4. Run the Development Server:
    python manage.py runserver
    