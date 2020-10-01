cache = {}
no = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
      "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", ""]
words = []  # I used this to help with the length of the longest word for formatting the output


def build(file):
    with open(file) as f:
        data = f.read()
        for word in data.split():
            word = word.lower()
            clean_word = ''
            characters = [char for char in word]
            for char in characters:
                if char.isalnum():  # HERE IT IS
                    clean_word += char
            if len(characters) > 0:
                if clean_word not in no:
                    if clean_word not in cache:
                        cache[clean_word] = 0
                        words.append(clean_word)  # formatting
                    cache[clean_word] += 1


def sort():
    width = sorted(words, key=len, reverse=True)  # formatting
    # print(sorted[0]) # formatting
    output = sorted(cache.items(), key=lambda item: (-item[1], item[0]))
    return output


def print_out(input_list):
    mark = '#'
    for entry in input_list:
        tally = ''.join([char * entry[1] for char in mark])
        print(f'{entry[0]:17}{tally}')


if __name__ == "__main__":
    build('robin.txt')
    # print(sort())
    print_out(sort())

    # 17 formatting
