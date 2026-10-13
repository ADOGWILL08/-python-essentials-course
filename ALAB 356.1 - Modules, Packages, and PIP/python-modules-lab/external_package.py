# external_package.py
# Requires colorama; install with: pip install colorama
# Task 3: Demonstrate an external package (colorama) by printing colored text

# Import the pieces of colorama we need:
#   init  - prepares colorama so colors work in the Windows terminal
#   Fore  - sets the text (foreground) color
#   Style - lets us make text bright/bold and reset back to normal
from colorama import init, Fore, Style

# Turn on colorama; autoreset=True returns to normal color after each print
init(autoreset=True)

# Print colored messages with descriptive labels
print(Fore.GREEN + "Success message: colorama is installed and working!")
print(Fore.RED + "Error message: this text is printed in red.")
print(Fore.YELLOW + "Warning message: this text is printed in yellow.")
print(Fore.CYAN + "Info message: this text is printed in cyan.")

# Print bright text, then normal text, to show Style and the reset
print(Style.BRIGHT + "Bright text: this line is bold and bright.")
print("Normal text: colors are reset back to the default.")