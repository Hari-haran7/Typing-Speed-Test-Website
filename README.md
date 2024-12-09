# Typing Speed Test Website

A simple and interactive typing speed test website where users can practice typing, measure their speed (WPM) and accuracy, and track their results. This project uses HTML, CSS, JavaScript for the frontend, Python (Flask) for the backend, and SQLite for the database.

---

## Features

- **User Authentication**: Register and log in to track progress.
- **Typing Test**: Type a randomly generated passage within a time limit.
- **Real-Time Feedback**: Displays words per minute (WPM) and accuracy while typing.
- **Results Storage**: Saves test results in a database for future reference.
- **Responsive Design**: Works on desktops and mobile devices.

---

## Project Structure

```
typing_website/
├── app.py                 # Flask backend logic
├── templates/             # HTML files
│   ├── base.html          # Common layout template
│   ├── home.html          # Home page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── test.html          # Typing test page
│   ├── results.html       # Results page
├── static/                # Static files (CSS, JS)
│   ├── css/
│   │   ├── style.css      # Stylesheet
│   ├── js/
│   │   ├── typing.js      # Typing test logic
├── database/              # SQLite database
│   ├── users.db           # User and results data
└── README.md              # Project documentation
```

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask framework)
- **Database**: SQLite

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/typing-speed-test.git
   cd typing-speed-test
   ```

2. Install dependencies:
   ```bash
   pip install Flask
   ```

3. Set up the database:
   - Navigate to the `database/` directory.
   - Create the SQLite database:
     ```bash
     sqlite3 users.db
     ```
   - Run the following SQL to create the `users` table:
     ```sql
     CREATE TABLE users (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT NOT NULL,
         password TEXT NOT NULL
     );
     ```

4. Start the Flask application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. **Register**: Create an account to save your progress.
2. **Log In**: Access your personalized typing tests.
3. **Take a Test**:
   - A random passage will be displayed.
   - Type the text in the input box.
   - Real-time WPM and accuracy will be displayed.
4. **View Results**: After submitting, see your final speed and accuracy.

---

## Future Enhancements

- Add a leaderboard to show top performers.
- Implement a dark mode for better accessibility.
- Include difficulty levels with different passage lengths.
- Store typing history for individual users.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

---

## Contact

For questions or feedback, please reach out to harihara4611@gmail.com
