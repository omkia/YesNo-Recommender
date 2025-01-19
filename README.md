# YesNo Recommender

**YesNo Recommender** is a Django-based recommender system that helps users make decisions by answering simple yes/no questions. It offers two main features:
1. **Gift Recommender:** Suggests personalized gift ideas based on answers to yes/no questions.
2. **Exercise Recommender:** Recommends exercises tailored to health and muscle needs using yes/no responses.

---

## Features

### 🎁 Gift Recommender
- Answer a series of simple yes/no questions about the recipient (e.g., hobbies, preferences, or lifestyle).
- Receive thoughtful and personalized gift suggestions.

### 💪 Exercise Recommender
- Answer basic yes/no questions about your health and muscle goals.
- Get exercise recommendations tailored to your fitness needs.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/omkia/yesno-recommender.git
   cd yesno-recommender
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Usage
1. Choose the feature you want to use: **Gift Recommender** or **Exercise Recommender**.
2. Answer the yes/no questions presented in the interface.
3. View the results and recommendations instantly.

---

## Tech Stack
- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript (optional enhancements)
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)

---

## Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

