def email_slicer(email):
    """
    Slices an email address into its username and domain.

    Args:
        email (str): The email address to be sliced.

    Returns:
        str: A formatted string containing the username and domain.
             Returns "Invalid email format." if the email is not in the expected format.
    """
    # Validate if the email address contains the '@' symbol
    if '@' not in email:
        return "Invalid email format. Missing '@' symbol."

    try:
        # Split the email address into username and domain using the '@' symbol
        username, domain = email.split('@')
        # Format and return the result
        return f"Username: {username}\nDomain: {domain}"
    except ValueError:
        # Catch ValueError if the email is not in the expected format
        return "Invalid email format."

if __name__ == "__main__":
    # Get user input for the email address
    email_address = input("Enter your email address: ")
    # Call the email_slicer function and store the result
    result = email_slicer(email_address)
    # Print the result
    print(result)
