import pytest
import inspect
import re
from digital_communications_analyzer import (
    extract_emails,
    extract_phone_numbers,
    extract_dates,
    extract_ip_addresses,
    validate_email,
    validate_phone_number,
    validate_ip_address,
    replace_pattern
)
from test.TestUtils import TestUtils


class TestFunctional:
    """Test cases for regex functionality in the text pattern matcher."""
    
    def test_email_functionality(self):
        """Test email extraction and validation functionality."""
        try:
            # Test email extraction with various scenarios
            assert extract_emails("Contact us at support@example.com") == ["support@example.com"], "Should extract single email"
            
            emails_text = "Email1: admin@test.org, Email2: info@company.net"
            emails = extract_emails(emails_text)
            assert len(emails) == 2, "Should extract multiple emails"
            assert "admin@test.org" in emails, "Should extract first email"
            assert "info@company.net" in emails, "Should extract second email"
            
            # Test complex emails with numbers and special characters
            complex_email = "complex.email+chars123@domain-name.co.uk"
            result = extract_emails(f"Send to: {complex_email}")
            assert complex_email in result, "Should handle complex emails with special chars and numbers"
            
            # Test validation
            assert validate_email("user@example.com") is True, "Should validate standard email"
            assert validate_email("user.name+tag@example.com") is True, "Should validate email with dots and plus"
            assert validate_email("user123@domain-name.co.uk") is True, "Should validate email with numbers and hyphens"
            assert validate_email("invalid-email") is False, "Should reject string without @"
            
            TestUtils.yakshaAssert("test_email_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_email_functionality", False, "functional")
            raise e
    
    def test_phone_functionality(self):
        """Test phone number extraction and validation functionality."""
        try:
            # Test with multiple formats
            phone_text = "Call (123) 456-7890 or 555-987-6543 or 123.456.7890"
            phones = extract_phone_numbers(phone_text)
            assert len(phones) == 3, "Should extract all three phone formats"
            assert "(123) 456-7890" in phones, "Should extract parentheses format"
            assert "555-987-6543" in phones, "Should extract hyphen format"
            assert "123.456.7890" in phones, "Should extract dot format"
            
            # Test different spacing
            assert extract_phone_numbers("1234567890") == ["1234567890"], "Should extract without separators"
            assert extract_phone_numbers("123 456 7890") == ["123 456 7890"], "Should extract with spaces"
            
            # Test validation
            assert validate_phone_number("(123) 456-7890") is True, "Should validate parentheses format"
            assert validate_phone_number("123-456-7890") is True, "Should validate hyphen format"
            assert validate_phone_number("123.456.7890") is True, "Should validate dot format"
            assert validate_phone_number("123 456 7890") is True, "Should validate space format"
            assert validate_phone_number("1234567890") is True, "Should validate no separator format"
            
            TestUtils.yakshaAssert("test_phone_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_phone_functionality", False, "functional")
            raise e
    
    def test_date_functionality(self):
        """Test date extraction functionality with different formats."""
        try:
            # Test single-digit and double-digit formats (MM/DD/YYYY)
            us_dates_text = "Dates: 1/1/2023, 01/01/2023, 1/01/2023, 01/1/2023"
            us_dates = extract_dates(us_dates_text, "MM/DD/YYYY")
            assert len(us_dates) == 4, "Should extract all US date formats"
            assert "1/1/2023" in us_dates, "Should extract single-digit month/day"
            assert "01/01/2023" in us_dates, "Should extract double-digit month/day"
            
            # Test ISO format dates (YYYY-MM-DD)
            iso_dates_text = "ISO dates: 2023-1-1, 2023-01-01, 2023-1-01, 2023-01-1"
            iso_dates = extract_dates(iso_dates_text, "YYYY-MM-DD")
            assert len(iso_dates) == 4, "Should extract all ISO date formats"
            assert "2023-1-1" in iso_dates, "Should extract single-digit month/day in ISO format"
            assert "2023-01-01" in iso_dates, "Should extract double-digit month/day in ISO format"
            
            # Test invalid format
            try:
                extract_dates("Any date", "INVALID-FORMAT")
                assert False, "Should raise ValueError for invalid format"
            except ValueError:
                pass
            
            TestUtils.yakshaAssert("test_date_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_date_functionality", False, "functional")
            raise e
    
    def test_ip_functionality(self):
        """Test IP address extraction and validation functionality."""
        try:
            # Test extraction
            ip_text = "IPs: 192.168.1.1, 10.0.0.1, 127.0.0.1"
            ips = extract_ip_addresses(ip_text)
            assert len(ips) == 3, "Should extract all IPs"
            assert "192.168.1.1" in ips, "Should extract first IP"
            assert "10.0.0.1" in ips, "Should extract second IP"
            assert "127.0.0.1" in ips, "Should extract third IP"
            
            # Test boundary IPs
            boundary_text = "Boundaries: 0.0.0.0, 255.255.255.255"
            boundary_ips = extract_ip_addresses(boundary_text)
            assert len(boundary_ips) == 2, "Should extract boundary IPs"
            assert "0.0.0.0" in boundary_ips, "Should extract minimum IP"
            assert "255.255.255.255" in boundary_ips, "Should extract maximum IP"
            
            # Test validation
            assert validate_ip_address("192.168.1.1") is True, "Should validate typical IP"
            assert validate_ip_address("0.0.0.0") is True, "Should validate minimum IP"
            assert validate_ip_address("255.255.255.255") is True, "Should validate maximum IP"
            
            # Invalid IPs
            assert validate_ip_address("256.0.0.0") is False, "Should reject octet > 255"
            assert validate_ip_address("192.168.1") is False, "Should reject IP with missing octet"
            assert validate_ip_address("a.b.c.d") is False, "Should reject IP with letters"
            
            TestUtils.yakshaAssert("test_ip_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_ip_functionality", False, "functional")
            raise e
    
    def test_pattern_replacement(self):
        """Test pattern replacement functionality."""
        try:
            # Test email replacement
            text = "Contact us at admin@example.com or support@example.com"
            result = replace_pattern(text, r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', "[EMAIL]")
            assert "admin@example.com" not in result, "Should replace first email"
            assert "support@example.com" not in result, "Should replace second email"
            assert result.count("[EMAIL]") == 2, "Should replace ALL occurrences"
            
            # Test phone replacement
            text = "Call (123) 456-7890 or 555-987-6543"
            result = replace_pattern(text, r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', "[PHONE]")
            assert "(123) 456-7890" not in result, "Should replace first phone"
            assert "555-987-6543" not in result, "Should replace second phone"
            assert result.count("[PHONE]") == 2, "Should replace ALL occurrences"
            
            TestUtils.yakshaAssert("test_pattern_replacement", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_pattern_replacement", False, "functional")
            raise e
    
    def test_error_handling(self):
        """Test proper error handling for invalid inputs."""
        try:
            # Test input validation for extraction functions
            for func in [extract_emails, extract_phone_numbers, extract_ip_addresses]:
                try:
                    func(123)  # Non-string input
                    assert False, f"{func.__name__} should raise TypeError for non-string input"
                except TypeError:
                    pass
            
            # Test input validation for validation functions
            for func in [validate_email, validate_phone_number, validate_ip_address]:
                try:
                    func(None)  # None input
                    assert False, f"{func.__name__} should raise TypeError for None input"
                except TypeError:
                    pass
            
            # Test input validation for replace_pattern
            try:
                replace_pattern("text", "pattern", 123)  # Non-string replacement
                assert False, "replace_pattern should raise TypeError for non-string replacement"
            except TypeError:
                pass
            
            TestUtils.yakshaAssert("test_error_handling", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_error_handling", False, "functional")
            raise e
    
    def _get_regex_pattern(self, func):
        """Helper method to extract regex pattern from function source code."""
        source = inspect.getsource(func)
        pattern_match = re.search(r'(r["\'][^"\']+["\'])', source)
        if pattern_match:
            return pattern_match.group(1)
        return ""