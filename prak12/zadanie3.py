import string
stop_words = ["a", "an", "the", "and", "or", "but", "to", "of", "in", "on"]
with open("input.txt", "r") as file:
    text = file.read()
translator = str.maketrans("", "", string.punctuation)
text = text.translate(translator).lower()
words = text.split()
words = [word for word in words if word not in stop_words]
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_word_counts[:10]:
    print(f"{word}: {count}")