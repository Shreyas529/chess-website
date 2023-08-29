## `server.py` - Running the Flask App

This script initializes and runs the Flask app for your chess website. It sets up the app configuration, database connection, and runs the app in debug mode.

### Usage

- Run this script using the Python interpreter to start your Flask app.
- Access your chess website through a web browser by visiting the provided URL (typically http://localhost:5000).

### Code Explanation

1. Import necessary Flask functionalities, time management, scraping module, and SQLAlchemy.
2. Import the `create_app` function from the `website` package.
3. Create and configure the Flask app instance using `create_app`.
4. Check if the script is run directly using `if __name__ == "__main__":`.
5. Run the Flask app in debug mode using `app.run(debug=True)`.


## `__init__.py` - App Initialization and Configuration

This script initializes and configures the Flask app for the chess website. It integrates extensions for database operations, user authentication, and third-party OAuth (Lichess).

### Code Explanation

- Initializes Flask app instance.
- Sets app's secret key and session lifetime.
- Configures SQLite database URI.
- Initializes SQLAlchemy extension for database operations.
- Initializes OAuth extension for third-party authentication.
- Configures OAuth settings for Lichess.
- Imports blueprints for views and authentication.
- Registers blueprints with URL prefixes.
- Imports User model for database.
- Defines a function to create the database if it doesn't exist.
- Initializes Flask-Login extension for user management.
- Defines a user loader function for Flask-Login.
- Returns the configured app instance from `create_app()`.

---

## `auth.py` - User Authentication and Lichess Login

This script manages user authentication and provides the ability to log in using Lichess credentials. It includes routes for login, sign-up, logout, password recovery, and Lichess authentication.

### Code Explanation

- Import necessary modules and extensions.
- Create a Blueprint named `auth`.
- Define a route to handle user login.
- Authenticate user based on provided email and password.
- If successful, log the user in and redirect to the home page.
- If unsuccessful, display appropriate error messages.
- Define a route for user registration.
- Validate email, name, and password.
- Create a new user and store it in the database.
- Provide success or error messages accordingly.
- Define a route for user logout (requires login).
- Log the user out and redirect to the login page.
- Define a function to send an email for password recovery.
- Compose an email with a new password and send it to the user.
- Define a route for password recovery.
- Generate a random password, update user's password, and send an email.
- Define a route for Lichess login.
- Redirect user to Lichess OAuth authorization.
- Define a route for denied Lichess access.
- Display a message if user denies access during Lichess OAuth.
- Define a route to handle Lichess authorization callback.
- Handle errors if user denies access.
- Obtain access token from Lichess OAuth.
- Use token to fetch user's email and other details from Lichess.
- Get user's Lichess username and rating history.
- Plot and generate an interactive rating history plot using Matplotlib.
- Update user details in the database or create a new user.
- Log the user in and redirect to the home page.

---

## `models.py` - User Database Model

This script defines the database model for user information, including email, name, password, and Lichess account status.

### Code Explanation

- Import necessary modules and extensions.
- Define a class named `User` which inherits from `db.Model` and `UserMixin`.
- Define attributes for the User class:
  - `id`: Primary key for the user table.
  - `email`: Stores the user's email (unique).
  - `name`: Stores the user's name.
  - `password`: Stores the user's password (hashed).
  - `lichess`: Stores a boolean value indicating whether the user's account is linked to Lichess.
- Configure the User class as a database model.
- The User class inherits from `UserMixin` to integrate Flask-Login features.
- Represents a User object in the database, which can store user information.

---
## `views.py` - Route Definitions and Page Rendering

This script defines route handlers for different pages of the chess website. It uses Flask's Blueprint to organize and manage routes.

### Code Explanation

- Import necessary modules and extensions.
- Create a Blueprint named `views`.
- Define route handlers for different pages using the `@views.route()` decorator.

#### `/` and `/home/`:
- Renders the home page (`index.html`).

#### `/news.html/`:
- Requires login.
- Extracts chess news using `extract_news()` from `scrape.py`.
- Renders the news page with the extracted content.

#### `/leaderboard.html/`:
- Requires login.
- Extracts top players' data using `extract_players()` from `scrape.py`.
- Renders the leaderboard page with the extracted content.

#### `/tournments.html/`:
- Requires login.
- Extracts FIDE tournaments data using `extract_tournments()` from `scrape.py`.
- Renders the tournaments page with the extracted content.

#### `/rules.html/`:
- Requires login.
- Renders the rules page.

#### `/openings.html`:
- Requires login.
- Renders the openings page.

#### `/profile.html`:
- Requires login.
- Checks if the user's account is linked to Lichess.
- If linked, reads an interactive plot HTML from a file.
- Renders the profile page with the interactive plot as content.
- If not linked, flashes an error message, logs the user out, and redirects to the login page.

### Notes
- The routes are protected with `@login_required` decorator, ensuring users are logged in to access these pages.

---
## `scrape.py` - Web Scraping Functions

This script contains functions for scraping data from different websites related to chess information.

### Code Explanation

- Import necessary modules and classes.
- Define three functions for extracting different types of data using Selenium and BeautifulSoup.

#### `extract_players()`:
- Scrapes the FIDE website for top-rated players' information.
- Uses Selenium to open a headless Chrome browser and navigate to the FIDE ratings page.
- Waits for the specified element to load on the page.
- Parses the page source with BeautifulSoup.
- Extracts the top rating div containing players' information.
- Modifies image source and players' href to absolute URLs.
- Closes the browser and returns the extracted data as a string.

#### `extract_tournments()`:
- Scrapes the FIDE Calendar page for tournament information.
- Similar to `extract_players()`, navigates to the FIDE Calendar page and waits for a specific element.
- Extracts the section containing tournament profiles.
- Closes the browser and returns the extracted data as a string.

#### `extract_news()`:
- Scrapes Chess.com's news page for chess-related news.
- Similar process as above: uses Selenium to navigate to the news page, waits for element, and parses using BeautifulSoup.
- Extracts the news container div, modifies image source, and returns the extracted data as a string.

### Notes
- These functions use Selenium to interact with web pages, and BeautifulSoup to parse the HTML content.
- The extracted content is returned as a string, which can be safely passed to the templates for rendering.

---

