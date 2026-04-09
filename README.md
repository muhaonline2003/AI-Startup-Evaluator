AI Startup Evaluator
====================

Overview
--------

AI Startup Evaluator is a Streamlit frontend with a FastAPI backend and JSON file storage. Founders can submit a startup pitch, get AI feedback, browse startups, and post networking requests.

Repository Structure
--------------------

- `main.py` - Streamlit UI
- `backend/` - FastAPI app, AI logic, and models
- `backend_api.py` - HTTP client used by Streamlit
- `startups.json` - startup storage
- `networking.json` - networking post storage
- `.env` - local secrets only, not committed
- `.env.example` - template for new users

What the app does
-----------------

- Submit startup details and pitch text
- Run AI pitch analysis through the backend
- Ask the AI assistant startup questions
- View and manage startup records
- Post and browse networking requests

What new users need
-------------------

- Python 3.11+
- A virtual environment in `.venv`
- Their own OpenAI API key

Important about the API key
---------------------------

- Do not commit your real API key to GitHub.
- Keep it in a local `.env` file.
- Other people should add their own key after cloning.
- If someone clones the project without a key, the app can still open, but AI responses will fall back to demo behavior.

Local Setup
-----------

1. Clone the repository:

  ```bash
  git clone https://github.com/muhaonline2003/AI-Startup-Evaluator.git
  cd AI-Startup-Evaluator
  ```

2. Create and activate a virtual environment if needed:

  ```bash
  python -m venv .venv
  .\.venv\Scripts\activate
  ```

3. Install dependencies:

  ```bash
  pip install -e .
  ```

4. Create a `.env` file in the project root with your OpenAI key:

  ```env
  OPENAI_API_KEY=your_real_key_here
  ```

5. Start the backend in one terminal:

  ```bash
  .\.venv\Scripts\python -m uvicorn backend.main:app --reload
  ```

6. Start the frontend in a second terminal:

  ```bash
  .\.venv\Scripts\python -m streamlit run main.py
  ```

7. Open the app in your browser:

  - Streamlit: http://localhost:8501
  - Backend health: http://127.0.0.1:8000/health
  - API docs: http://127.0.0.1:8000/docs

Running Without an API Key
--------------------------

- The app will still launch.
- AI features will use demo or fallback responses.
- For real answers, each user must add their own OpenAI key.

GitHub Upload Steps
-------------------

1. Check changes:

  ```bash
  git status
  ```

2. Add and commit:

  ```bash
  git add .
  git commit -m "Clean project structure and update README"
  ```

3. Push to GitHub:

  ```bash
  git push origin main
  ```

Troubleshooting
---------------

- If the backend does not start, check that `.venv` exists and that you used the correct Windows command.
- If AI responses are demo-only, confirm `OPENAI_API_KEY` is set in `.env` or in the current shell.
- If GitHub rejects a push, run `git pull origin main --allow-unrelated-histories` once and then push again.
