"""
Text Pattern Matcher - Regular Expressions

This program demonstrates basic pattern matching with regular expressions
to extract and validate common data formats like emails, phone numbers, and dates.
"""

import re
from datetime import datetime

def extract_emails(text):
    """
    Extract all email addresses from the given text.
    
    Parameters:
    text (str): The text to search for email addresses
    
    Returns:
    list: List of all email addresses found
    
    Example:
    >>> extract_emails("Contact us at support@example.com or info@company.org")
    ['support@example.com', 'info@company.org']
    
    Notes:
    - Should handle special characters in usernames (._%+-) 
    - Should handle subdomains and different TLDs
    - Should extract complex emails like "user.name+tag123@sub.domain-name.co.uk"
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to match email addresses
    #    Hint: Username part can include [a-zA-Z0-9._%+-]
    #          Domain part can include [a-zA-Z0-9.-]
    #          TLD requires at least 2 letters: [a-zA-Z]{2,}
    # 3. Use re.findall() to return all matches
    pass

def extract_phone_numbers(text):
    """
    Extract all phone numbers from the given text.
    
    Parameters:
    text (str): The text to search for phone numbers
    
    Returns:
    list: List of all phone numbers found
    
    Example:
    >>> extract_phone_numbers("Call (123) 456-7890 or 555-987-6543")
    ['(123) 456-7890', '555-987-6543']
    
    Notes:
    - Should handle various formats: (123) 456-7890, 123-456-7890, 123.456.7890, 123 456 7890
    - Area code may or may not be in parentheses
    - Separators can be dashes, dots, spaces, or none
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to match phone numbers
    #    Hint: Area code: \(?\d{3}\)?
    #          Separators: [-.\s]?
    #          Rest of number: \d{3}[-.\s]?\d{4}
    # 3. Use re.findall() to return all matches
    pass

def extract_dates(text, format="MM/DD/YYYY"):
    """
    Extract all dates in the specified format from the given text.
    
    Parameters:
    text (str): The text to search for dates
    format (str): The expected date format (MM/DD/YYYY or YYYY-MM-DD)
    
    Returns:
    list: List of all dates found
    
    Example:
    >>> extract_dates("Start: 01/15/2023, End: 12/31/2023")
    ['01/15/2023', '12/31/2023']
    >>> extract_dates("Released on 2023-05-25", format="YYYY-MM-DD")
    ['2023-05-25']
    
    Notes:
    - Should handle both single-digit and double-digit month/day values 
    - For MM/DD/YYYY, should match patterns like 1/1/2023, 01/01/2023, etc.
    - For YYYY-MM-DD, should match patterns like 2023-1-1, 2023-01-01, etc.
    - Should raise ValueError for unsupported format parameters
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Choose the pattern based on format parameter
    #    - For MM/DD/YYYY use: \b\d{1,2}/\d{1,2}/\d{4}\b
    #    - For YYYY-MM-DD use: \b\d{4}-\d{1,2}-\d{1,2}\b
    #    - Raise ValueError for any other format
    # 3. Use re.findall() to return all matches
    pass

def extract_ip_addresses(text):
    """
    Extract all IPv4 addresses from the given text.
    
    Parameters:
    text (str): The text to search for IP addresses
    
    Returns:
    list: List of all IPv4 addresses found
    
    Example:
    >>> extract_ip_addresses("Server: 192.168.1.1, Gateway: 10.0.0.1")
    ['192.168.1.1', '10.0.0.1']
    
    Notes:
    - Should match standard IPv4 format (four octets of 1-3 digits separated by dots)
    - Should use word boundaries to avoid matching partial numbers
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to match IPv4 addresses
    #    Hint: Use word boundaries \b to ensure you don't match partial numbers
    #          Pattern: \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
    # 3. Use re.findall() to return all matches
    pass

def validate_email(email):
    """
    Validate if a string is a properly formatted email address.
    
    Parameters:
    email (str): The email address to validate
    
    Returns:
    bool: True if the email is valid, False otherwise
    
    Example:
    >>> validate_email("user@example.com")
    True
    >>> validate_email("invalid-email")
    False
    
    Notes:
    - Should validate the format matches username@domain.tld
    - Should handle special characters in the username
    - Should handle various domain formats
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to validate email
    #    Hint: Like extract_emails but use ^ and $ to match entire string
    #          ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
    # 3. Use re.match() and return a boolean result
    pass

def validate_phone_number(phone):
    """
    Validate if a string is a properly formatted US phone number.
    
    Parameters:
    phone (str): The phone number to validate
    
    Returns:
    bool: True if the phone number is valid, False otherwise
    
    Example:
    >>> validate_phone_number("(123) 456-7890")
    True
    >>> validate_phone_number("555-1234")
    False
    
    Notes:
    - Should validate various formats: (123) 456-7890, 123-456-7890, etc.
    - Must contain area code and 7 additional digits
    - Separators can be dashes, dots, spaces, or none
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to validate phone numbers
    #    Hint: Like extract_phones but use ^ and $ to match entire string
    #          ^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$
    # 3. Use re.match() and return a boolean result
    pass

def validate_ip_address(ip):
    """
    Validate if a string is a properly formatted IPv4 address.
    
    Parameters:
    ip (str): The IP address to validate
    
    Returns:
    bool: True if the IP address is valid, False otherwise
    
    Example:
    >>> validate_ip_address("192.168.1.1")
    True
    >>> validate_ip_address("256.0.0.1")
    False
    
    Notes:
    - Should validate format follows N.N.N.N where N is 1-3 digits
    - Must verify each octet is in range 0-255
    - Should handle values like 0.0.0.0 and 255.255.255.255
    """
    # TODO: Implement this function
    # 1. Validate input is a string (raise TypeError if not)
    # 2. Create a raw string regex pattern to validate IP format
    #    Hint: Use capture groups to extract each octet: ^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$
    # 3. Use re.match() to check the format
    # 4. If format matches, verify each octet is in range 0-255
    # 5. Return True only if format is valid AND all octets are in valid range
    pass

def replace_pattern(text, pattern, replacement):
    """
    Replace all occurrences of a pattern in text with replacement string.
    
    Parameters:
    text (str): The original text
    pattern (str): The regex pattern to search for
    replacement (str): The replacement string
    
    Returns:
    str: Text with all pattern matches replaced
    
    Example:
    >>> replace_pattern("My SSN is 123-45-6789", r'\d{3}-\d{2}-\d{4}', "XXX-XX-XXXX")
    'My SSN is XXX-XX-XXXX'
    
    Notes:
    - Should replace ALL occurrences, not just the first one
    - All inputs must be strings
    """
    # TODO: Implement this function
    # 1. Validate all inputs are strings (raise TypeError if not)
    # 2. Use re.sub() to replace all occurrences of the pattern
    # 3. Return the modified text
    pass

def main():
    """
    Main function to demonstrate the functionality of the Text Pattern Matcher.
    """
    print("===== TEXT PATTERN MATCHER =====")
    
    # Sample text with various patterns to detect
    sample_text = """
    Contact Information:
    - Email: john.doe@example.com
    - Phone: (555) 123-4567
    - Alt Phone: 555-987-6543
    - IP Address: 192.168.1.1
    
    Important Dates:
    - Start Date: 01/15/2023
    - End Date: 12/31/2023
    - Update Released: 2023-06-15
    """
    
    # TODO: Implement the following sections:
    # 1. Email extraction and validation
    # 2. Phone number extraction and validation
    # 3. Date extraction (both MM/DD/YYYY and YYYY-MM-DD formats)
    # 4. IP address extraction and validation
    # 5. Pattern replacement example
    
    print("\n===== PATTERN MATCHING COMPLETE =====")

if __name__ == "__main__":
    main()