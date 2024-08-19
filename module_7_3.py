class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        files_deconstruct = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding="utf-8") as file:
                all_words = file.read().lower().split()
                files_deconstruct.update({file_name: all_words})
        return(files_deconstruct)

    def find(self, word):
        result = {}
        for key in wordfinder.get_all_words().keys():
            all_words = wordfinder.get_all_words().get(key)
            if word.lower() in all_words:
                position = all_words.index(word.lower())
                result.update({key: position})
                return (result)
        return (result)

wordfinder = WordsFinder("old_file.txt", "new_file.txt")
print(*wordfinder.find("Ирокез").items())
