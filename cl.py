import os

# Список файлов и папок, которые мы игнорируем
IGNORE = {
    'node_modules', 'venv', '.venv', '__pycache__', '.git',
    'dist', '.vscode', 'tasks.db', 'package-lock.json','.env'
}

# Список расширений, которые нам нужны
EXTENSIONS = {'.py', '.vue', '.js', '.css', '.json', '.txt'}


def collect_project():
    project_path = os.getcwd()
    output_file = "project_context.txt"

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"PROJECT STRUCTURE AND CODE\n")
        out.write(f"=" * 30 + "\n\n")

        for root, dirs, files in os.walk(project_path):
            # Убираем игнорируемые папки
            dirs[:] = [d for d in dirs if d not in IGNORE]

            for file in files:
                if any(file.endswith(ext) for ext in EXTENSIONS) and file != output_file and file != "collect_code.py":
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, project_path)

                    out.write(f"\nFILE: {relative_path}\n")
                    out.write("-" * (len(relative_path) + 6) + "\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            out.write(f.read())
                    except Exception as e:
                        out.write(f"Error reading file: {e}")
                    out.write("\n" + "=" * 50 + "\n")

    print(f"✅ Готово! Весь код собран в файл: {output_file}")


if __name__ == "__main__":
    collect_project()