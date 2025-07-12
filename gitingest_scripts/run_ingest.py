from gitingest import ingest

repo_url = "https://github.com/trungkien1992/AstraTrade-Project"
summary, tree, content = ingest(
    repo_url,
    include_patterns="*.py,*.md",
    max_file_size=102400  # 100KB
)

with open("digest.txt", "w", encoding="utf-8") as f:
    f.write(f"{summary}\n\n{tree}\n\n{content}")

print("Ingestion complete. Output saved to digest.txt.") 