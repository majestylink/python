# Lendigo Assessment

## Local setup

The application was built on a Linux machine with [Python] 3.9.12 [redis] and [rabbbitmq] installed. Virtual environment was managed by [pip] though you can opt for other virtual environment tools (`requirements.txt` is included). Ensure your machine has all these tools to locally run this web application.

A typical setup to the app up and running locally is stated below:

- Get the program source files: You can clone it from Github via:
    ```bash
    git clone https://github.com/majestylink/hacker-news-api.git
    ```
- Change directory into the source code folder:
    ```bash
    cd lendigo
    ```
- Activate virtual environment (You can use virtualenv, venv, poetry, or conda):
    ```bash
    source venv/bin/activate
    ```
- Install the web application's dependencies ([pip] is used here but you are at liberty to use any other tool. `requirements.txt` is included):
    ```bash
    pip install -r requirements.txt
    ```
- Create migrations (migrations folder already populated. If you prefer to start afresh, delete all the files in the `migrations` folder of each major app &mdash; `news` &mdash; except the `__init__.py` files. Then, in your terminal, execute `python manage.py makemigrations`):

    ```bash
    python manage.py migrate
    ```

- Create super user by executing and login:

    ```bash
    python manage.py createsuperuser
    ```

    Provide the details requested by the prompts that follow.

- Run the application. You will need a second terminal to start the [Celery] tasks. In one terminal, start the application:

    ```bash
    python manage.py runserver
    ```

    You can **optionally** provide a port as the default port is `8000`. To provide a port, the command above becomes:

    ```bash
    python manage.py runserver port_number
    ```

    You can now visit your browser and navigate to `http://localhost:8000/` or `http://localhost:port_number/` as the case may be.


- In another terminal, start the rabbitmq (In my case I use the command below. Also ensure your virtual environment is activated):

    ```bash
    sudo rabbitmq
    ```
  
- In another terminal, start the redis server (In my case I use the command below. Also ensure your virtual environment is activated):

    ```bash
    redis-server
    ```
  
- In another terminal, start the celery beat by (ensure your virtual environment is activated):

    ```bash
    celery -A lendigo beat -l info
    ```
  
- Finally, open another terminal, start the celery worker by (ensure your virtual environment is activated):

    ```bash
    celery -A lendigo worker -l info
    ```