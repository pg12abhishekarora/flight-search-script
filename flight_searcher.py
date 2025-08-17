# Import the date library to help with formatting
from datetime import datetime

def create_flight_search_link():
    """Asks for flight details and generates a Google Flights search link."""

    print("✈️ Welcome to the Flight Search Link Generator!")

    # --- Get User Input ---
    origin = input("Enter your origin city or airport code (e.g., Delhi or DEL): ")
    destination = input("Enter your destination city or airport code (e.g., SFO): ")
    date_str = input("Enter your departure date (YYYY-MM-DD): ")

    # --- Validate and Format the Date ---
    try:
        # This confirms the user entered a valid date format
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("\n❌ Invalid date format. Please run the script again and use YYYY-MM-DD.")
        return

    # --- Construct the URL ---
    # The base URL for a Google Flights search
    base_url = "https://www.google.com/flights?q="

    # The query string format: flights from [ORIGIN] to [DESTINATION] on [DATE]
    # Spaces are replaced with '+' for the URL
    query = f"flights from {origin} to {destination} on {date_str}".replace(" ", "+")

    final_url = base_url + query

    # --- Display the Result ---
    print("\n✅ Your flight search link is ready!")
    print("Click the link below to see live flight options:")
    print(f"\n{final_url}\n")


# Run the function
create_flight_search_link()
