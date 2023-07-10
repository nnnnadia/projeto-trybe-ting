from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    if instance.was_filed(path_file):
        return

    file = txt_importer(path_file)
    if file:
        formatted_file_obj = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(formatted_file_obj)
        instance.add_file_to_set(formatted_file_obj)
        print(formatted_file_obj)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
