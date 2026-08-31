from words import add_words, get_word_meaning


def wa():
    """Topic particle explanation."""
    print("Topic particle.")


def ga():
    """Subject particle explanation."""
    print("Subject particle. It indicates existence.")
    print("Often used with ARIMASU (あります - existence of non-living) and IMASU (います - existence of living).")


def o():
    """Object marker explanation."""
    print("Object marker.")
    print("Comes before following words:")
    print("1. たべます - To eat")
    print("2. のみます - To drink")
    print("3. みます - To see")
    print("4. ききます - To listen")
    print("5. よみます - To read")
    print("6. かきます - To write")
    print("7. かいます - To buy")
    print("8. べんきょうします - To study")
    print("9. すいます - To smoke")
    print("10. といます - To take (photo)")
    print("11. あいます - To meet (friend)")


def e():
    """Direction particle explanation."""
    print("Direction particle. Used before:")
    print("1. いきます - To go")
    print("2. きます - To come")
    print("3. かえります - To return")


def ni():
    """Location and time particle explanation."""
    print("Referred as location and time particle.")
    print("Location particle: It indicates existence.")
    print("Often used with ARIMASU (あります - To have) and IMASU (います - To exist).")


def de():
    """Location or means particle explanation."""
    print("Location or Means particles")
    print("A. Location particle: わたしは としょかんで べんきょう します。(I study at library.)")
    print("B. Means particle (by, with): としょかんで ほんを かります。(I borrow a book at the library.)")
    print("Used with:")
    print("1. きります - To cut, slice")
    print("2. おくります - To send")
    print("3. あげます - To give")
    print("4. もらいます - To receive")
    print("5. かします - To lend")
    print("6. かります - To borrow")
    print("7. おしえます - To teach")
    print("8. ならいます - To learn")
    print("9. かけます - To make (phone call)")


if __name__ == "__main__":
    while True:
        try:
            print("\n===== WELCOME TO JAPANESE GUIDE =====")
            print("Select what to learn:")
            print("1. Particles")
            print("2. Word meaning")
            print("3. Add new word")
            print("4. Exit")

            choice = int(input("\nEnter your choice: "))

            match choice:
                case 1:
                    print("\n--- Particle Guide ---")
                    part = input("Enter particle (wa, ga, o, e, ni, de): ").strip().lower()
                    if part == 'wa':
                        wa()
                    elif part == 'ga':
                        ga()
                    elif part == 'o':
                        o()
                    elif part == 'e':
                        e()
                    elif part == 'ni':
                        ni()
                    elif part == 'de':
                        de()
                    else:
                        print("Invalid particle. Please try again.")

                case 2:
                    word = input("\nEnter word to find meaning: ").strip()
                    print(get_word_meaning(word))

                case 3:
                    print("\n--- Add New Word ---")
                    word = input("Enter Japanese word: ").strip()
                    meaning = input("Enter meaning: ").strip()
                    add_words(word, meaning)

                case 4:
                    print("Thank you for learning! Goodbye!")
                    break

                case _:
                    print("Invalid choice. Please select 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3, or 4).")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
