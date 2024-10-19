# thea-aa

## Installation process
Prerequisites:
- Python, 3.9 or newer
- Pip, the Python package installer
- Git, the version control system
- A code editor, such as Visual Studio Code
- Bun (or npm), but bun is recommended

1. Clone the repository
```bash
git clone git@github.com:rice-apps/thea-aa.git
```

2. Create a virtual environment in the backend directory
```bash
cd backend-thea-aa
python -m venv venv
```

3. Activate the virtual environment
```bash
source venv/bin/activate
```

4. Install the required packages
```bash
pip install -r requirements.txt
```

5. Run the backend server
```bash
python manage.py runserver
```

6. Install dependencies in the frontend
```bash
cd ../frontend-thea-aa
bun install
```

7. Run the frontend server
```bash
bun run dev
```