
no = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
      "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", ""]


def word_count(s):
    # Your code here
    cache = {}
    for word in s.split():
        word = word.lower()
        new_word = ''
        characters = [char for char in word]
        for char in characters:
            if char not in no:
                new_word += char
        if len(characters) > 0:
            if new_word not in no:
                if new_word not in cache:
                    cache[new_word] = 0
                cache[new_word] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
