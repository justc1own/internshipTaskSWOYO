def text_stat(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            
            # Calculate frequency of all letters in the text
            letters = [char.lower() for char in text if char.isalpha()]
            letter_freq = {char: letters.count(char) / len(letters) for char in set(letters)}
            
            # Calculate number of words in the text
            words = text.split()
            word_amount = len(words)
            
            # Calculate number of paragraphs in the text
            paragraphs = text.split('\n\n')
            paragraph_amount = len(paragraphs)
            
            # Calculate percentage of words containing specific letter
            letter_percentage = {}
            for char in set(letters):
                word_count = sum([1 for word in words if char in word.lower()])
                percentage = (word_count / len(words)) * 100
                letter_percentage[char] = (letter_freq[char], percentage)
                
            # Calculate number of words containing both latin and cyrillic letters
            bilingual_word_amount = sum([1 for word in words if any(char.isalpha() and ord(char) > 128 for char in word)])
            
            return {'letter_freq': letter_freq, 
                    'word_amount': word_amount, 
                    'paragraph_amount': paragraph_amount, 
                    'letter_percentage': letter_percentage, 
                    'bilingual_word_amount': bilingual_word_amount}
    except FileNotFoundError:
        return {'error': 'File not found'}
    except:
        return {'error': 'An error occurred'}
    
'''
Тест 1: 
Текст в файле 'test.txt': The quick brown fox jumps over the lazy dog. 1234 
Результат: 
    {'letter_freq': {'h': 0.04838709677419355, 'l': 0.0967741935483871, 'd': 0.03225806451612903, 'x': 0.03225806451612903, 'w': 0.016129032258064516, 'k': 0.04838709677419355, 'q': 0.016129032258064516, 'f': 0.03225806451612903, 'b': 0.0483870967...115, 'l', 'h': (0.1935483870967742, 0.0), 'x': (0.03225806451612903, 0.0), 'd': (0.06451612903225806, 0.0), 'q': (0.016129032258064516, 0.0), 'w': (0.016129032258064516, 0.0)}, 
    'word_amount': 9, 
    'paragraph_amount': 1,
    'bilingual_word_amount': 0}

Тест 2: 
Текст в файле 'test.txt': The quick brown fox. Jumps! Over... The lazy dog. The end. 
Результат: 
    {'letter_freq': {'h': 0.07142857142857142, 'l': 0.07142857142857142, 'd': 0.03571428571428571, 'x': 0.03571428571428571, 'w': 0.03571428571428571, 'k': 0.03571428571428571, 'e': 0.03571428571428571, 'm': 0.03571428571428571, 'f': 0.03571428571428571,... 0.0), 'b': (0.07142857142857142, 0.07142857142857142), 'v': (0.0, 0.07142857142857142)}, 
    'word_amount': 11,
    'paragraph_amount': 2,
    'bilingual_word_amount': 0}

Тест 3: Текст в файле 'test.txt': В чащах юга жил бы цитрус? Да, но фальшивый экземпляр! Результат: {'letter_freq': {'ь': 0.07, 'з': 0.03, 'д': 0.02, 'л': 0.05, 'с': 0.05, 'р': 0.03, 'э': 0.01, 'ы': 0.01, 'т': 0.02, 'ч': 0.02, 'н': 0.03, 'б': 0.01, 'ь': 0.01, 'ж': 0.03, 'ф': 0.01, 'ш': 0.01, 'й': 0.01, 'а': 0.04, 'и': 0.04, 'г': 0.02, 'ю': 0.01,...6, 'ш': (0.01, 0.0), 'а': (0.03, 0.0), 'ю': (0.01, 0.0), 'й': (0.01, 0.0)}, 'word_amount': 7, 'paragraph_amount': 1, 'bilingual_word_amount': 0}
'''
