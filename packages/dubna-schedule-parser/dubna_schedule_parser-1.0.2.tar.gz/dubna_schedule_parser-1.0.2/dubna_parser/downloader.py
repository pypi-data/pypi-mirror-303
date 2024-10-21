import os
import shutil
import gdown


def clear_or_create_directory(directory: str):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory, exist_ok=True)


def get_download_url(url: str):
    clean_url = url.split('?')[0]
    clean_url = clean_url.replace('/edit', '/export?format=xlsx')
    return clean_url


def download_sheets(file_with_url='links', save_folder='downloads'):
    """перед использованием все таблицы из папки должны быть закрыты
        и не использоваться другими программами"""
    clear_or_create_directory(save_folder)
    with open(file_with_url, 'r') as f:
        urls = f.readlines()

    for i in range(len(urls)):
        url = urls[i].strip()
        if url:
            try:
                clean_url = get_download_url(url)
                file_name = f"file{i + 1}.xlsx"
                save_path = os.path.join(save_folder, file_name)
                gdown.download(clean_url, save_path)

            except gdown.exceptions as e:
                print(f"Ошибка при скачивании {url}: {e}")
