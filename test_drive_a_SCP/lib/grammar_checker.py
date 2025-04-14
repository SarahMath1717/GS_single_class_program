
class GrammarStats:
    def __init__(self):
        self.passed_sentences = 0
        self.total_sentences = 0

    def check_grammar(self, text):
        result = text[-1] in (".", "!", "?") and text[0].isupper()
        if result == True: 
            self.passed_sentences += 1
            self.total_sentences += 1
        else:
            self.total_sentences += 1
        return result

    def percentage_good(self):
        if self.total_sentences == 0:  # To avoid division by zero
            return 0
        return (self.passed_sentences / self.total_sentences) * 100