def run_task1():
    while True:
        # Запит користувача на введення речення
        text = input("Enter a sentence (at least 7 words): ")
        
        # Розбиваємо текст на слова за допомогою пробілів
        words = text.split()
        
        # Перевірка: чи є у списку хоча б 7 слів
        if len(words) >= 7:
            break
        print("Error! The sentence must contain at least 7 words. Try again.\n")
    
    # Шукаємо слово, яке повторюється рівно два рази
    duplicate_word = ""
    for word in words:
        # Рахуємо, скільки разів слово зустрічається в списку
        if words.count(word) == 2:
            duplicate_word = word
            break
            
    # Виводимо результати на екран
    print(f"\nEntered sentence: {text}")
    if duplicate_word != "":
        print(f"Found identical words that appear twice: {duplicate_word}")
    else:
        print("No pair of identical words repeating exactly twice was found in this sentence.")
