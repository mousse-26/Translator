from googletrans import Translator, LANGUAGES

def translate_text_google(text, src_language, dest_language):
    translator = Translator()
    
    try:
        translation = translator.translate(text, src=src_language, dest=dest_language)
        return translation.text
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def display_language_options():
    print("\nSupported languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")
    print("\n")

if __name__ == "__main__":
    source_text = input("Enter the text you want to translate: ")
    display_language_options()

    source_language = input("Enter the source language code (e.g., 'en' for English): ").lower()
    destination_language = input("Enter the destination language code (e.g., 'es' for Spanish): ").lower()

    translated_text = translate_text_google(source_text, source_language, destination_language)

    print(f"\nOriginal Text: {source_text}")
    print(f"Translated Text: {translated_text}")
