# Python Applied to Business — Shanghai, October 2026

Working repository of the module (International MSc in Management, Shanghai term).
Lecturer: Dr. Francisco Astudillo-Pacheco.

You do not install anything on your laptop. The whole module runs in **GitHub Codespaces**: a computer in the
cloud, opened in your browser, with Python, Jupyter, GitHub Copilot and every library of the course already in place
(a new Codespace installs them by itself in about ten minutes; see `requirements.txt`).

## First day, in five steps (detailed in Lab 1.1)

1. Sign in to GitHub with the account you created with your school e-mail address.
2. Open this repository and choose **Use this template → Create a new repository** (owner: you; visibility: private).
3. In *your* copy: **Code → Codespaces → Create codespace on main**. The first start takes a few minutes.
4. Open `notebooks/S01/S01-A_environment_check.ipynb`, select the kernel **Python 3 (course)** and run it from top to bottom.
5. From Session 5: your own Mistral key. Store it as a Codespaces secret named `MISTRAL_API_KEY` (Settings → Codespaces →
   Secrets, with access to your copy of the repository) and restart the Codespace; or paste it once in the notebook with
   *Remember it in this Codespace* ticked.

## House rules

- **Stop your Codespace when you finish** (Codespaces menu → Stop current codespace). A stopped Codespace keeps your files and does not consume hours.
- **Commit and push at the end of every session.** What is pushed is safe; what is only in the Codespace can be lost if the Codespace is deleted.
- **Keys never appear in code.** They live in Codespaces secrets and are read with `os.environ`.
- Use GitHub Copilot as an assistant that you verify: read, test, fix, verify.

## What is where

| Folder | Content |
|---|---|
| `notebooks/S01` … `notebooks/S09` | Practice notebooks, one folder per session |
| `data/` | Every dataset used in class, with its source and licence (`data/README.md`) |
| `utils/` | Small helpers shared by the notebooks (for example, the connection to the language models) |
| `tools/` | Lecturer's tools (data preparation) |
