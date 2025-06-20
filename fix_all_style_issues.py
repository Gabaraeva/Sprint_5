import os
import re


def fix_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Удалить все пустые строки в конце файла
    while lines and lines[-1].strip() == '':
        lines.pop()

    # Добавить ровно одну пустую строку в конце
    lines.append('\n')

    # Исправить E302: добавить 2 пустые строки перед классами/функциями
    new_lines = []
    for i, line in enumerate(lines):
        # Проверить, является ли строка началом класса или функции
        if re.match(r'^(class|def) ', line.lstrip()):
            # Проверить, что перед ней недостаточно пустых строк
            if i > 0 and lines[i - 1].strip() != '':
                new_lines.append('\n')
            if i > 1 and lines[i - 2].strip() != '':
                new_lines.append('\n')

        new_lines.append(line)

    # Объединить обратно в строку
    content = ''.join(new_lines)

    # Исправить E305: добавить 2 пустые строки после функций
    content = re.sub(r'(\n\s*def .+:\n(.+\n)+?)(?=\S)', r'\1\n\n', content, flags=re.DOTALL)
    content = re.sub(r'(\n\s*class .+:\n(.+\n)+?)(?=\S)', r'\1\n\n', content, flags=re.DOTALL)

    # Записать исправленный файл
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    # Обработать все Python-файлы в проекте
    for root, dirs, files in os.walk('.'):
        # Пропустить виртуальное окружение и другие служебные папки
        if '.venv' in root or '__pycache__' in root:
            continue

        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Fixing: {file_path}")
                fix_python_file(file_path)




if __name__ == '__main__':
    main()
