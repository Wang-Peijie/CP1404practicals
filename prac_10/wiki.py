"""CP1404 Prac - Wiki"""
import wikipedia

# Use a boolean variable to control the loop; initially True to keep the loop running
continue_search = True

while continue_search:
    user_input = input("Enter page title: ").strip()
    if not user_input:
        continue_search = False
    else:
        try:
            # Retrieve the Wikipedia page
            page = wikipedia.page(user_input)
            # Print page information
            print(page.title)
            print(page.summary)
            print(page.url)
            print()  # Add a blank line to separate different queries
        except wikipedia.DisambiguationError as e:
            # Handle ambiguous queries (e.g., "python" could refer to multiple things)
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # Only display the first 10 options to avoid excessive output
            print()
        except wikipedia.PageError:
            # Handle cases where the page does not exist
            print(f"Page id \"{user_input}\" does not match any pages. Try another id!")
            print()
        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")
            print()
    print("Thank you.")