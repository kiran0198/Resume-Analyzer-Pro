import os
import sys
import nltk

AUTHOR = "Kiran K. Sahu"
VERSION = "1.0.0"

print("=" * 65)
print("        Resume Analyzer Pro Installer")
print("=" * 65)
print(f"Version : {VERSION}")
print(f"Author  : {AUTHOR}")
print("=" * 65)

# ---------------------------------------------------
# STEP 1 - Download NLTK Resources
# ---------------------------------------------------

print("\n[1/4] Installing NLTK Resources...")

packages = [
    "punkt",
    "punkt_tab",
    "wordnet",
    "omw-1.4"
]

for package in packages:
    nltk.download(package, quiet=True)
    print(f"   ✓ {package}")

# ---------------------------------------------------
# STEP 2 - Check Folder Structure
# ---------------------------------------------------

print("\n[2/4] Checking Project Structure...")

folders = [
    "models",
    "assets",
    "screenshots",
    "data"
]

for folder in folders:

    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"   ✓ Created : {folder}")

    else:
        print(f"   ✓ Exists  : {folder}")

# ---------------------------------------------------
# STEP 3 - Verify Models
# ---------------------------------------------------

print("\n[3/4] Verifying ML Models...")

required_models = [
    "models/tfidf_vectorizer.pkl",
    "models/chi2_selector.pkl",
    "models/svm_resume_classifier.pkl"
]

missing = []

for model in required_models:

    if os.path.exists(model):
        print(f"   ✓ {os.path.basename(model)}")

    else:
        print(f"   ✗ Missing -> {os.path.basename(model)}")
        missing.append(model)

# ---------------------------------------------------
# STEP 4 - Final Status
# ---------------------------------------------------

print("\n[4/4] Installation Summary")

if len(missing) == 0:

    print("\n✅ Installation Successful!")
    print("\nEverything is ready.")
    print("\nRun the application using:")
    print("\npython -m streamlit run app.py")

else:

    print("\n⚠ Installation Incomplete")
    print("\nMissing files:")

    for item in missing:
        print(" -", item)

print("\n" + "=" * 65)
print("Thank you for using Resume Analyzer Pro")
print(f"Developed by {AUTHOR}")
print("=" * 65)