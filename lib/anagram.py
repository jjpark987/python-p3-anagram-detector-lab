import ipdb

class Anagram:
    def __init__(self, string) -> None:
        self.string = string

    def match(self, strings_list):
        results = []

        self_string = sorted(list(self.string))

        for string in strings_list:
            if self_string == sorted(list(string)):
                ipdb.set_trace()
                results.append(string)
            
        return results
        
anagram = Anagram('enlist').match(['listen','teddy','alfred'])
