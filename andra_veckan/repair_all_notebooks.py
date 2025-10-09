import nbformat

# Lista med dina notebooks
notebooks = ["dicts.ipynb", "lists.ipynb"]

for nb_file in notebooks:
    repaired_file = nb_file.replace(".ipynb", "_repaired.ipynb")
    try:
        # Läs notebooken
        with open(nb_file, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        # Skriv tillbaka som en reparerad notebook
        nbformat.write(nb, repaired_file)
        print(f"{nb_file} reparerad och sparad som {repaired_file} ✅")
    except Exception as e:
        print(f"Något gick fel med {nb_file}: {e} ❌")
