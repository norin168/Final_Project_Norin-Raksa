import os
from pathlib import Path
from flask import Flask, request, render_template
import pickle
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent
MODELS_DIR = PROJECT_ROOT / "models"

app = Flask(__name__, template_folder=str(PROJECT_ROOT / "templates"))


def _load_pickle(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    with path.open("rb") as f:
        return pickle.load(f)


# Load artifacts using absolute paths so app works from any working directory.
model = _load_pickle(MODELS_DIR / "reg_model.pkl")
columns = _load_pickle(MODELS_DIR / "preprocessor.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.form.to_dict()

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Fix datatype
        df["work_year"] = df["work_year"].astype(int)

        # Apply get_dummies
        df = pd.get_dummies(df)

        # Match training columns
        df = df.reindex(columns=columns, fill_value=0)

        # Predict
        prediction = model.predict(df)[0]

        return render_template("index.html", prediction=round(prediction, 2))

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    app.run(host=host, port=port, debug=debug_mode)
