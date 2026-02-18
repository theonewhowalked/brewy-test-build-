import sys
import time
from notebooklm_mcp.auth import load_cached_tokens
from notebooklm_mcp.api_client import NotebookLMClient

COMPANY_NAME = "Brewy"
NOTEBOOK_TITLE = f"Brand Brain: {COMPANY_NAME}"
FILE_PATH = "marketing/paid_media_strategy.md"
FILE_TITLE = "Paid Media Strategy"

def main():
    tokens = load_cached_tokens()
    if not tokens: sys.exit(1)
    client = NotebookLMClient(cookies=tokens.cookies, csrf_token=tokens.csrf_token)
    
    # Find Notebook
    notebook_ids = [nb.id for nb in client.list_notebooks() if nb.title == NOTEBOOK_TITLE]
    if not notebook_ids:
        print("Notebook not found")
        sys.exit(1)
    notebook_id = notebook_ids[0]

    # Upload
    print(f"Uploading {FILE_TITLE}...")
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        client.add_text_source(notebook_id, content, FILE_TITLE)
        print("  ✅ Done")
    except Exception as e:
        print(f"  ❌ Failed: {e}")

if __name__ == "__main__":
    main()
