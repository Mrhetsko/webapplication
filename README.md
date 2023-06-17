# Django Web App with User Posts

This is a simple Django web application that allows users to create, read, update and delete posts.
+ Docker +

### Additionally, very simple page is available online here: https://dmytro66.pythonanywhere.com/
- API interactive docs: [API DOCS](https://dmytro66.pythonanywhere.com/api/schema/docs/)


If you still want to run this app locally:
## Prerequisites

Make sure you have the following installed before running the application:
- Python 3.x: [Download Python](https://www.python.org/downloads/)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mrhetsko/webapp.git
   ```
2. Move to webapp directory:
   ```bash
   cd webapp
   ```

3. Create virtual environment:
   ```bash
   python3 -m venv my_venv_name
   ```
   
4. Activate virtual environment:
    ```bash
    my_venv_name/Scripts/activate.ps1

5. Upgrade pip:
   ```bash
   python3 -m pip install --upgrade pip
   ```
   
6. Install requirements:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

7. Run development server 
   ```bash
   python3 manage.py runserver
   ```
### Now application available on your localhost: default - http://127.0.0.1:8000

P.S. I am aware that normally settings.py, database and some other files shouldn't be here, but for this project I decided to make an exception.
<hr>


## Using Docker:

1. Clone the repository:

   ```bash
   git clone https://github.com/Mrhetsko/webapp.git
   ```
2. Move to webapp directory:
   ```bash
   cd webapp

3. Build:
   ```bash
   docker build . -t docker-django-v0.0
   ```
   
4. Run
   ```bash
   docker run  -p 8000:8000 docker-django-v0.0
   ```

### Now application available on your localhost: default - localhost:8000 or 127.0.0.1:8000