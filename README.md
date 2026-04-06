# Salary Prediction Web App

A Flask-based machine learning web app that predicts a data-job salary in USD from a small set of user inputs.

## Features

- Web form for entering job-related inputs
- Salary prediction using a pre-trained regression model
- Simple Flask backend with HTML template rendering
- Production-ready serving option with `waitress`

## Project Structure

```text
final_project/
├── Data/
│   └── ds_salaries.csv
├── models/
│   ├── preprocessor.pkl
│   └── reg_model.pkl
├── notebooks/
│   ├── Raksa-Norin-Final.ipynb
│   └── models/
│       ├── preprocessor.pkl
│       └── reg_model.pkl
├── src/
│   ├── __init__.py
│   └── app.py
├── templates/
│   └── index.html
├── REPORT.pdf
├── requirements.txt
└── README.md
```

## Dataset

The project includes `Data/ds_salaries.csv`, which contains salary-related records with columns such as:

- `work_year`
- `experience_level`
- `employment_type`
- `job_title`
- `salary`
- `salary_currency`
- `salary_in_usd`
- `employee_residence`
- `remote_ratio`
- `company_location`
- `company_size`

The app predicts a salary value in USD using the saved model artifacts in `models/`.

## Inputs Used by the Web App

The current web form in `templates/index.html` collects these fields:

- `work_year`
- `experience_level`
- `employment_type`
- `job_title`
- `company_size`

On submission, the app:

1. Converts the form data to a pandas DataFrame
2. Casts `work_year` to integer
3. Applies `pd.get_dummies(...)`
4. Reindexes the result to match the saved training columns from `models/preprocessor.pkl`
5. Uses `models/reg_model.pkl` to generate a prediction

## Requirements

Install the pinned dependencies from `requirements.txt`:

- `flask==3.1.0`
- `pandas==2.2.3`
- `numpy==2.1.3`
- `scikit-learn==1.6.1`
- `waitress==3.0.2`

## Setup

### 1. Create and activate a virtual environment

```zsh
cd /Users/digi/Downloads/final_project
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```zsh
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Running the App

### Development mode

Run the Flask app directly:

```zsh
cd /Users/digi/Downloads/final_project
python3 src/app.py
```

By default, it starts on:

- `http://127.0.0.1:5000`

Optional environment variables:

```zsh
export FLASK_DEBUG=1
export FLASK_HOST=127.0.0.1
export PORT=5000
python3 src/app.py
```

### Production-style mode

To avoid Flask’s development server warning, run the app with `waitress`:

```zsh
cd /Users/digi/Downloads/final_project
waitress-serve --listen=127.0.0.1:5000 src.app:app
```

## How to Use

1. Open the app in your browser
2. Enter:
   - work year
   - experience level
   - employment type
   - job title
   - company size
3. Click **Predict Salary**
4. View the predicted salary in USD on the page

## Notes

- The app loads model files using absolute paths derived from `src/app.py`, so it can be started from different working directories.
- `templates/` is configured explicitly from the project root.
- If a required model file is missing, the app raises a clear `FileNotFoundError` at startup.
- Because the model is loaded from a pickle file, you should use the pinned scikit-learn version from `requirements.txt` for best compatibility.

## Troubleshooting

### "This is a development server" warning

That warning is expected when running:

```zsh
python3 src/app.py
```

For a production-style server, use:

```zsh
waitress-serve --listen=127.0.0.1:5000 src.app:app
```

### Model file not found

Make sure these files exist:

- `models/reg_model.pkl`
- `models/preprocessor.pkl`

### Dependency or pickle compatibility issues

Reinstall the exact package versions:

```zsh
python3 -m pip install -r requirements.txt
```

## Related Files

- `src/app.py` — Flask backend and prediction logic
- `templates/index.html` — web form UI
- `models/reg_model.pkl` — trained regression model
- `models/preprocessor.pkl` — saved training columns used for reindexing
- `Data/ds_salaries.csv` — dataset used in the project
- `notebooks/Raksa-Norin-Final.ipynb` — notebook for experimentation/training
- `REPORT.pdf` — project report

## License

No license file is currently included in the project.

