# django-assignment

Set up a Django project and create a URL that takes POST requests. Take the following inputs in the body:

1. name
2. phone
3. email
4. address
   which can have up to 10 inputs.

Create a PDF with a template header of any logo you like.
Put the logo at the top as static for all pdfs and create a dynamic table to be populated below the logo as per the inputs in the POST request.
The inputs can be variable numbers; the function should accommodate them.
Create a random URL to access/download this PDF, which will expire, and delete the file from the server in 1 hour.

# Running the server

```bash
    poetry install

    poetry shell

    ./manage.py runserver
```

# API endpoints
Check out api endpoints at /swagger