import os


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
MODELS_DIR = os.path.join(PROJECT_ROOT, "models")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "notebooks")

TRAIN_DATA_PATH = os.path.join(RAW_DATA_DIR, "train.csv")
TEST_DATA_PATH = os.path.join(RAW_DATA_DIR, "test.csv")
DATA_DESCRIPTION_PATH = os.path.join(RAW_DATA_DIR, "data_description.txt")
SAMPLE_SUBMISSION_PATH = os.path.join(RAW_DATA_DIR, "sample_submission.csv")