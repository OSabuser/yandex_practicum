# ССЫЛКА НА ОТЧЁТ:
#
# 1. Принцип работы поисковой системы
# Вдохновлялся https://vas3k.blog/blog/352/ и https://habr.com/ru/articles/792452/
#
# 2. Доказательство корректности
#
#
# 3. Временная сложность
#
#
# 4. Пространственная сложность
#
#
class CustomSearchEngine:
    _REQUESTED_DOCUMENTS = 5

    def __init__(self, documents):
        self._cached_index = CustomSearchEngine._generate_inverted_index(documents)

    def search(self, query, number_of_documents=_REQUESTED_DOCUMENTS):
        """
        Поиск релевантных документов, соответствующих запросу.
        ${number_of_documents}: количество документов, которые нужно выдать
        """
        # Получаем список уникальных слов в очередном запросе пользователя
        words = set(query.split())

        # Формируем словарь, где [Ключ] - номер документа, [Значение] - релевантность
        relevance = {}
        for word in words:
            if word in self._cached_index:
                # Если слово встречается в документе, увеличиваем его релевантность
                for doc_id, freq in self._cached_index[word]:
                    if doc_id in relevance:
                        relevance[doc_id] += freq
                    else:
                        relevance[doc_id] = freq

        # Сортировка документов на выдаче производится по убыванию релевантности.
        # Если релевантности документов совпадают —– то по возрастанию их порядковых
        # номеров в базе (то есть во входных данных).
        items = []
        for doc_id, doc_rel in relevance.items():
            # Номера документов с нулевой релевантностью не выводим
            if doc_rel > 0:
                document_number = doc_id + 1
                items.append((document_number, doc_rel))

        # Сортировка по убыванию релевантности и по возрастанию номеров,
        # если релевантность нескольких документов совпадает
        items.sort(key=lambda item: (-item[1], item[0]))

        top_doc_numbers = [doc_id for _, doc_id in items[:number_of_documents]]
        return top_doc_numbers

    @staticmethod
    def _generate_inverted_index(documents):
        """
        Генерация инвертированного индекса для поисковой системы.\n
        [Ключ] -  слово, которое встречается
        в одном или нескольких документах, [Значение] - список пар (номер документа N, количество
        вхождений  ключа-слова в документ N).
        """
        total_documents = len(documents)
        index = {}

        for doc_number in range(total_documents):
            # Список слов, которые встречаются в документе
            words = documents[doc_number].split()

            # Для каждого documents[doc_number] считаем количество вхождений каждого word в нём
            words_occurencies = {}
            for word in words:
                if word in words_occurencies:
                    words_occurencies[word] += 1
                else:
                    words_occurencies[word] = 1

            for word in words_occurencies:
                if word not in index:
                    index[word] = []
                index[word].append((doc_number, words_occurencies[word]))

        return index


def get_search_data():
    total_documents = int(input())
    documents = []
    for _ in range(total_documents):
        documents.append(input())
    total_queries = int(input())
    queries = []
    for _ in range(total_queries):
        queries.append(input())
    return total_documents, documents, total_queries, queries


if __name__ == "__main__":
    total_documents, documents, total_queries, queries = get_search_data()

    engine = CustomSearchEngine(documents)

    for user_query in queries:
        result = engine.search(user_query)
        print(*result)
