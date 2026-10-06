import os


def find_all_python_files(start_path="./narnia_map"):
    python_files = []
    for __, _, files in os.walk(start_path):
        for file in files:
            if file.endswith(".txt"):
                python_files.append(file)
    return python_files


files = find_all_python_files()
if len(files) == 0:
    print("Карта ещё не создана!")
else:
    print(*files, sep='\n')
    print(f"Всего файлов txt: {len(files)}")
