#!/usr/bin/env bash
set -euo pipefail

COURSE_KERNEL="python-business"
EMBEDDING_MODEL="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# Do not keep large pip download caches inside the Codespace.
export PIP_NO_CACHE_DIR=1
export TOKENIZERS_PARALLELISM=false

echo "[SETUP] Updating pip..."
python -m pip install --user --no-cache-dir --upgrade pip

echo "[SETUP] Installing CPU-only PyTorch..."
python -m pip install --user --no-cache-dir \
  torch \
  --index-url https://download.pytorch.org/whl/cpu

echo "[SETUP] Installing course dependencies..."
if [[ -f requirements.lock.txt ]]; then
  python -m pip install --user --no-cache-dir -r requirements.lock.txt
else
  python -m pip install --user --no-cache-dir -r requirements.txt
fi

echo "[SETUP] Registering Jupyter kernel..."
python -m ipykernel install --user \
  --name "${COURSE_KERNEL}" \
  --display-name "Python 3.11 - Python Applied to Business"

echo "[SETUP] Preloading multilingual embeddings model..."
python - <<PY
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("${EMBEDDING_MODEL}")

print("[OK] Embeddings model cached:", "${EMBEDDING_MODEL}")
print("[OK] Embedding dimension:",
      model.get_sentence_embedding_dimension())
PY

echo "[SETUP] Running offline environment verification..."
python scripts/verify_environment.py

echo "[READY] Course environment installed successfully."
