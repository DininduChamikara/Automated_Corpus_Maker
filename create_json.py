import json


def get_word_indices(sentence):
    # Split the sentence into words using whitespace and punctuation as delimiters
    words = sentence.split()

    # Initialize a list to store word indices
    word_indices = []

    start = 0
    for word in words:
        end = start + len(word)
        word_indices.append([word, start, end, ""])
        start = end + 1  # Add 1 for the space between words

    return word_indices


output_file = "pre_annotation.json"

with open("./roar_media_documents.json", "r", encoding="utf-8") as f:
    input_sentences = json.load(f)

# Sample sentences (replace with your input sentences)
# input_sentences = [
#     "රාජ්කොට් සෞරාෂ්ට්‍ර ක්‍රිකට් සංගම් ක්‍රීඩාංගණයේදී තරගය පැවැත්විණි.",
#     "ආසියානු ක්‍රිකට් ශුර ශ්‍රී ලංකා කණ්ඩායම සහ සත්කාරක ඉන්දීය කණ්ඩායම අතර 20/20 ක්‍රිකට් තරගාවලියේ 3 වැනි සහ අවසන් 20/20 ක්‍රිකට් තරගය ලකුණු 91කින් ජයගනිමින් ඉන්දියාව තරගාවලියේ ජය හිමි කර ගනු ලැබීය.",
# ]

resultArray = []

for input_sentence in input_sentences:
    word_indices = get_word_indices(input_sentence)
    output_list = [input_sentence, {"entities": word_indices}]

    resultArray.append(output_list)

# Write the result to the JSON file
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(resultArray, json_file, ensure_ascii=False, indent=4)
