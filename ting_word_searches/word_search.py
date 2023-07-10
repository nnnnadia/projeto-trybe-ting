from ting_file_management.queue import Queue


def add_occurrence(word, lines):
    return [
        {"linha": i + 1, "conteudo": occ}
        for i, occ in enumerate(lines)
        if word.lower() in occ.lower()
    ]


def search_by_word(word, instance: Queue):
    result = list()
    for i in range(len(instance)):
        file = instance.search(i)
        lines = file["linhas_do_arquivo"]
        occurrence = add_occurrence(word, lines)
        if occurrence:
            file_found = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence,
            }
            result.append(file_found)
    return result


def exists_word(word, instance):
    result = search_by_word(word, instance)
    for item in result:
        for occurrence in item["ocorrencias"]:
            occurrence.pop("conteudo")
    return result
