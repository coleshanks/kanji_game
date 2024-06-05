import requests

def fetch_words_from_jisho(query, num_words=20):
    words = []
    page = 1

    while len(words) < num_words:
        url = f"https://jisho.org/api/v1/search/words?keyword={query}&page={page}"
        response = requests.get(url)
        data = response.json()

        for item in data['data']:
            japanese_word = item['japanese'][0].get('word', item['japanese'][0].get('reading', ''))
            reading = item['japanese'][0].get('reading', '')
            if japanese_word and reading:
                words.append((japanese_word, reading))
            
            if len(words) >= num_words:
                break
        
        page += 1

    return words

# Fetch words for the example query 'N5'
words = fetch_words_from_jisho('N5', num_words=50)

# Save to a txt file in the desired format
file_path = '/Users/coleshanks/Documents/GitHub/kanji_game/jisho/japanese_words.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    for word, reading in words:
        file.write(f"{word},{reading}\n")

print(f"Words have been saved to {file_path}")

