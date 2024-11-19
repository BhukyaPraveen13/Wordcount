# Function to count the number of words in a given text
def word_counter(text):
    """
    Counts the number of words in the provided text.
    Args:
        text (str): The input text.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words), words

def average_word_length(words):
    """Calculate the average word length."""
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def longest_word(words):
    """Return the longest word in the list."""
    return max(words, key=len, default="")

def display_feedback(word_count):
    """Provide feedback based on the word count."""
    if word_count < 5:
        return "That's a short sentence!"
    elif word_count < 20:
        return "Nice, that's a decent length!"
    else:
        return "Wow, that's a lot of words!"

def main():
    """Main function to interact with the user and run the word counter."""
    # Display a user-friendly welcome message with ASCII art
    print(r"""
       __        __               _           _             
       \ \      / /__  _ __ _   _| |__   __ _| |_ ___ _ __ 
        \ \ /\ / / _ \| '__| | | | '_ \ / _` | __/ _ \ '__|
         \ V  V / (_) | |  | |_| | |_) | (_| | ||  __/ |   
          \_/\_/ \___/|_|   \__,_|_.__/ \__,_|\__\___|_|   
    """)
    print("Welcome to the Word Counter!")
    print("You can enter a sentence or paragraph, and I'll count the words for you.")
    print("Type 'exit' to quit the program.\n")
    
    history = []  # List to store history of inputs

    while True:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Enter your text (or type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter. Goodbye!")
            break
        
        # Error handling for empty input
        if not user_input.strip():
            print("Error: You entered an empty input. Please try again.")
            continue
        
        # Count the number of words and get the words list
        word_count, words = word_counter(user_input)
        
        # Calculate average word length and longest word
        avg_length = average_word_length(words)
        longest = longest_word(words)

        # Display the word count and additional information
        print(f"\nThe number of words in your input is: {word_count}")
        print(f"Average word length: {avg_length:.2f} characters")
        print(f"Longest word: '{longest}'")
        print(display_feedback(word_count))
        
        # Store the result in history
        history.append((user_input, word_count))

        # Option to display history
        if len(history) > 1:
            print("\nHistory of your inputs:")
            for idx, (text, count) in enumerate(history, start=1):
                print(f"{idx}: '{text}' - {count} words")
        
        print()  # Add a blank line for better readability

# Run the program
if __name__ == "__main__":
    main()