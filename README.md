# perfect-price-api

Perfect-Price API is a flask-driven backend serving routes for interacting with the endpoints which can scrape price
data from Amazon and Flipkart.

## Technologies used

* Python
* Flask
* Minor dependencies can be found in the requirements.txt file in the root folder.

## Installation / Usage

* Ensure you have python3 globally installed in your system.
* FastApi/Pydantics has different syntax for different python versions.
* We are globally using python **3.10.5**

To check Python version:

```
python -V
```

* Git clone this repo

    ```bash
    git clone git@github.com:0sahil/perfect-price-api.git
    ```

* ### Dependencies

    1. Cd into your the cloned repo:

        ```bash
        cd perfect-price-api
        ```

    2. Create and get into your virtual environment:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

* ### Install your requirements
  
    ```bash
    (venv)$ pip install -r requirements.txt
    ```

* ### Running the Server

    On your terminal, run the server using this one simple command:

    ```bash
    (venv)$ python main.py
    ```

    You can check the endpoints of the API on the browser:
    ```bash
    http://localhost:PORT/docs
    ```
  
* ### Testing using PyTest

    On your terminal, run the tests using this one simple command:

    ```bash
    (venv)$ pytest
    ```
  
* ### Automation using Selenium
    
    On your terminal, run the browser automation to our endpoint using this one simple command:

    ```bash
    (venv)$ python automate.py
    ```
