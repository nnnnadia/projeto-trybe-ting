from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.files = list()
        self.files_filed = set()

    def __len__(self):
        return len(self.files)

    def enqueue(self, value):
        self.files.append(value)

    def dequeue(self):
        if len(self.files) == 0:
            return None
        return self.files.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.files):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.files[index]

    def was_filed(self, file):
        return file in self.files_filed

    def add_file_to_set(self, file):
        file_name = file["nome_do_arquivo"]
        self.files_filed.add(file_name)
