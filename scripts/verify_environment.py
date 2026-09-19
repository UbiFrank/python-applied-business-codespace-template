"""Offline smoke test for the course Codespace.

This test intentionally does not call any external LLM API. It validates that
all course libraries import correctly and that the local embedding model is
available.
"""
from __future__ import annotations

import importlib
import sys

PACKAGES = {
    "jupyterlab": "jupyterlab",
    "IPython kernel": "ipykernel",
    "NumPy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "openpyxl": "openpyxl",
    "requests": "requests",
    "LangChain": "langchain",
    "LangChain OpenAI": "langchain_openai",
    "LangChain Groq": "langchain_groq",
    "LangChain Google": "langchain_google_genai",
    "LangChain Community": "langchain_community",
    "LangChain Chroma": "langchain_chroma",
    "ChromaDB": "chromadb",
    "sentence-transformers": "sentence_transformers",
    "LangChain HuggingFace": "langchain_huggingface",
    "CrewAI": "crewai",
    "CrewAI Tools": "crewai_tools",
    "LiteLLM": "litellm",
    "PyPDF": "pypdf",
    "Unstructured": "unstructured",
    "Wikipedia": "wikipedia",
}

failed: list[str] = []
print(f"Python: {sys.version.split()[0]}")
for label, module_name in PACKAGES.items():
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "installed")
        print(f"[OK] {label}: {version}")
    except Exception as exc:
        failed.append(f"{label}: {exc}")
        print(f"[FAIL] {label}: {exc}")

try:
    from sentence_transformers import SentenceTransformer
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    model = SentenceTransformer(model_name)
    dim = model.get_sentence_embedding_dimension()
    print(f"[OK] Embeddings model: {model_name} ({dim} dimensions)")
except Exception as exc:
    failed.append(f"Embeddings model: {exc}")
    print(f"[FAIL] Embeddings model: {exc}")

if failed:
    print("\nEnvironment verification failed:")
    for item in failed:
        print(" -", item)
    raise SystemExit(1)

print("\n[READY] Offline environment verification passed.")
