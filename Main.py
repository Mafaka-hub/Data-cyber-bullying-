import random

# Kamus kosakata dasar Tagalog-Inggris (bisa diperluas)
vocabulary = {
    "hello": "kamusta",
    "thank you": "salamat",
    "goodbye": "paalam",
    "water": "tubig",
    "food": "pagkain",
    "house": "bahay",
    "friend": "kaibigan",
    "love": "pag-ibig",
    "school": "paaralan",
    "book": "aklat"
}

# Kamus pribadi untuk Vocabulary Builder
personal_vocab = {}

def flashcards():
    print("\n=== Gamemode: Flashcards ===")
    words = list(vocabulary.keys())
    random.shuffle(words)
    score = 0
    for word in words[:5]:  # Batasi 5 kata per sesi
        answer = input(f"Terjemahkan '{word}' ke Tagalog: ").strip().lower()
        if answer == vocabulary[word]:
            print("Benar!")
            score += 1
        else:
            print(f"Salah. Jawaban: {vocabulary[word]}")
    print(f"Skor Anda: {score}/5")

def quiz():
    print("\n=== Gamemode: Quiz ===")
    score = 0
    for _ in range(5):
        word = random.choice(list(vocabulary.keys()))
        options = [vocabulary[word]] + random.sample(list(vocabulary.values()), 2)
        random.shuffle(options)
        print(f"Apa terjemahan '{word}'?")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        try:
            choice = int(input("Pilih (1-3): ")) - 1
            if options[choice] == vocabulary[word]:
                print("Benar!")
                score += 1
            else:
                print(f"Salah. Jawaban: {vocabulary[word]}")
        except (ValueError, IndexError):
            print("Input tidak valid. Lewati.")
    print(f"Skor Anda: {score}/5")

def translation():
    print("\n=== Gamemode: Translation ===")
    sentences = {
        "I love you": "Mahal kita",
        "How are you?": "Kamusta ka?",
        "What is your name?": "Ano ang pangalan mo?",
        "I am hungry": "Gutom na ako",
        "Where is the bathroom?": "Saan ang banyo?"
    }
    for eng, tag in sentences.items():
        answer = input(f"Terjemahkan: '{eng}' ke Tagalog: ").strip()
        if answer.lower() == tag.lower():
            print("Benar!")
        else:
            print(f"Salah. Jawaban: {tag}")

def vocabulary_builder():
    print("\n=== Gamemode: Vocabulary Builder ===")
    while True:
        action = input("Tambah kata baru (ketik 'add'), lihat kamus (ketik 'view'), atau keluar (ketik 'exit'): ").strip().lower()
        if action == "add":
            eng = input("Kata dalam bahasa Inggris: ").strip().lower()
            tag = input("Terjemahan Tagalog: ").strip().lower()
            personal_vocab[eng] = tag
            print("Kata ditambahkan!")
        elif action == "view":
            if personal_vocab:
                for eng, tag in personal_vocab.items():
                    print(f"{eng} -> {tag}")
            else:
                print("Kamus kosong.")
        elif action == "exit":
            break
        else:
            print("Perintah tidak valid.")

def main():
    print("Selamat datang di Script Belajar Tagalog!")
    while True:
        print("\nPilih gamemode:")
        print("1. Flashcards")
        print("2. Quiz")
        print("3. Translation")
        print("4. Vocabulary Builder")
        print("5. Keluar")
        try:
            choice = int(input("Masukkan pilihan (1-5): "))
            if choice == 1:
                flashcards()
            elif choice == 2:
                quiz()
            elif choice == 3:
                translation()
            elif choice == 4:
                vocabulary_builder()
            elif choice == 5:
                print("Terima kasih telah belajar!")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
