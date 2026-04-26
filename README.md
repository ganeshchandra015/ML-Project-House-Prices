# House Prices Regression Project

This project is your next structured machine learning project after Titanic.

It is designed to teach:

1. regression instead of classification
2. target skew and log transformation
3. stronger missing-value strategy
4. regularized linear models
5. ensemble regressors
6. reusable inference workflow

## Kaggle Competition Link

Competition page:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

Direct data page:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data

You need to sign in to Kaggle and accept the competition rules before the download becomes available.

## Expected Raw Files

After download, place these files in `data/raw/`:

1. `train.csv`
2. `test.csv`
3. `data_description.txt`
4. `sample_submission.csv`

## Project Structure

```text
ML-Project-House-Prices/
  README.md
  requirements.txt
  .gitignore
  setup.py
  data/
    raw/
    processed/
  notebooks/
  models/
  results/
  src/
    __init__.py
    config.py
    data_processing.py
    model.py
    pipeline.py
    utils.py
```

## Recommended Learning Order

1. Explore target distribution and missingness in the notebook.
2. Build a linear regression baseline.
3. Compare Ridge, Lasso, and Elastic Net.
4. Add Random Forest and Gradient Boosting later.
5. Refactor only after notebook logic is stable.

## Environment Setup

From the project root:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Git Setup

Initialize the repository locally:

```powershell
git init
git add .
git commit -m "Initial House Prices project scaffold"
```

Create a new empty GitHub repository, for example `ML-Project-House-Prices`, then connect it:

```powershell
git remote add origin https://github.com/<your-username>/ML-Project-House-Prices.git
git branch -M main
git push -u origin main
```

If you prefer SSH:

```powershell
git remote add origin git@github.com:<your-username>/ML-Project-House-Prices.git
git branch -M main
git push -u origin main
```

## Optional Kaggle API Download

If you want command-line download support later, install the Kaggle API and place your Kaggle token in:

`C:\Users\ChandrG\.kaggle\kaggle.json`

Then run:

```powershell
kaggle competitions download -c house-prices-advanced-regression-techniques -p data/raw
```

After download, unzip the archive contents into `data/raw/`.

## First Milestone

Do not jump to ensembles immediately.

Your first milestone should be:

1. inspect `SalePrice`
2. split train and validation data
3. build a baseline preprocessing workflow
4. train linear regression
5. examine residuals
6. then compare regularized models

## Starter Source Files

The `src/` package is intentionally minimal right now.

You will fill it in only after the notebook logic is validated, exactly as you did with Titanic.