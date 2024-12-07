import pyfiglet

def generate_ascii_art(text):
 
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    
    user_text = input("Enter text to convert to ASCII art: ").strip()
    
    ascii_art = generate_ascii_art(user_text)
    print("\nHere is your ASCII art:\n")
    print(ascii_art)