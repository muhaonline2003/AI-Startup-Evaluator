<<<<<<< HEAD
AI Startup Evaluator – Startup Ecosystem MVP
===========================================

Overview
--------

This project is a hackathon-friendly **AI Startup Evaluator** and mini **startup ecosystem** built with Streamlit and the OpenAI API.

Founders can submit their startup profiles and pitch decks, get a structured AI evaluation, and appear in a simple startup directory and networking board.

Database / Storage
------------------

- Uses lightweight **JSON files as the database** so it runs easily on any laptop.
- Startups are stored in: `startups.json` (acts as a mini table of startup profiles).
- Founder networking posts are stored in: `networking.json`.
- In a real production system, these JSON files can be replaced with **SQLite** or **PostgreSQL** while keeping the same CRUD patterns.

CRUD Features
-------------

Startup profiles support **full CRUD** from the UI:

- **Create** – founders submit startup details and pitch from the *Founder Submission & AI Evaluation* page.
- **Read** – investors and ecosystem members browse startups in the *Startup Directory (Investor Discovery)* page.
- **Update** – admins/founders can edit startup profiles from the *Manage Startups (CRUD)* page.
- **Delete** – startups can be removed from the JSON database via the *Manage Startups (CRUD)* page.

Each startup is given a simple integer **ID** so it can be selected, edited, and deleted from the interface.

AI Features
-----------

The app connects to the **OpenAI API** and analyzes startup pitches (PDF deck or pasted pitch text):

- Returns a **structured JSON** analysis per startup.
- Provides:
  - Overall **score out of 10**.
  - **Summary** of the startup.
  - **Problem clarity** and **solution strength**.
  - **Market potential** and **business model clarity**.
  - **Investor readiness** and **investor recommendation**.
  - Top **strengths**, **weaknesses**, **risks**, and **suggestions for improvement**.

This analysis powers both the founder-facing feedback and the investor discovery view.

Founder Networking
------------------

The **Founder Networking** page lets founders post what they are looking for:

- Fields: founder name, startup name, **looking for** (investor, cofounder, developer, mentor, early adopters, other), and a short message.
- Posts are saved to `networking.json` and displayed in a simple networking board in the UI.
- This adds a lightweight **founder networking layer** on top of the startup profiles.

How to Run
----------

1. Install dependencies (from the project root):

	```bash
	pip install -e .
	```

2. Set your OpenAI API key, for example in a `.env` file:

	```env
	OPENAI_API_KEY=your_real_key_here
	```

3. Start the Streamlit app:

	```bash
	streamlit run main.py
	```

This will launch the **AI Startup Evaluator** with:

- Founder submission + AI evaluation.
- Startup directory / investor discovery.
- Manage startups (CRUD).
- Founder networking board.

Backend Setup & API
------------------

This project uses a **FastAPI backend** for all CRUD and AI operations. The Streamlit frontend communicates with the backend via HTTP API calls (see `backend_api.py`).

### How to Start the Backend

1. Open a new terminal in the project root.
2. Run the FastAPI server:

   ```bash
   uvicorn backend.main:app --reload
   ```

   - The backend will start at `http://127.0.0.1:8000` by default.
   - You can check the API docs at `http://127.0.0.1:8000/docs`.

### How the Frontend Connects

- The Streamlit app (`main.py`) uses `backend_api.py` to send all data and AI requests to the FastAPI backend.
- Make sure the backend is running **before** starting the Streamlit frontend.

### Health Check

- To verify the backend is running, visit:  
  `http://127.0.0.1:8000/health`
- You should see `{"status": "ok"}`.

### Troubleshooting

- If you see messages like `(Real AI assistant logic not yet implemented)` or mock answers, it means the frontend could not reach the backend or the backend returned an error.
- Make sure both the backend and frontend are running, and that your API key is set.
- Check the backend terminal for errors.

**Windows (with virtual environment):**

- Start the backend (FastAPI):
  ```bash
  .\.venv\Scripts\python -m uvicorn backend.main:app --reload
  ```
- Start the frontend (Streamlit):
  ```bash
  .\.venv\Scripts\python -m streamlit run main.py
  ```

You can also use `python -m ...` if your environment is already activated.

=======
# AI-Startup-Evaluator
>>>>>>> b098cfb4996322a51c7039249668c7b9c7f33975
