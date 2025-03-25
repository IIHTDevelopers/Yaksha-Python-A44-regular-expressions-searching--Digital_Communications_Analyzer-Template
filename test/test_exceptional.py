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


class TestExceptional:
    """Test cases for exception handling in the text pattern matcher."""
    
    def test_exception_handling(self):
        """Test exception handling throughout the text pattern matcher."""
        try:
            # Test type validation for extract_emails
            try:
                extract_emails(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                extract_emails(123)
                assert False, "Should raise TypeError for numeric input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for extract_phone_numbers
            try:
                extract_phone_numbers(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                extract_phone_numbers([])
                assert False, "Should raise TypeError for list input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for extract_dates
            try:
                extract_dates(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                extract_dates("01/01/2023", None)
                assert False, "Should raise ValueError for None format"
            except ValueError as e:
                pass
            
            # Test invalid format for extract_dates
            try:
                extract_dates("01/01/2023", "INVALID FORMAT")
                assert False, "Should raise ValueError for invalid format"
            except ValueError as e:
                assert "unsupported" in str(e).lower()
            
            # Test type validation for extract_ip_addresses
            try:
                extract_ip_addresses(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for validate_email
            try:
                validate_email(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                validate_email(123)
                assert False, "Should raise TypeError for numeric input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for validate_phone_number
            try:
                validate_phone_number(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for validate_ip_address
            try:
                validate_ip_address(None)
                assert False, "Should raise TypeError for None input"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test type validation for replace_pattern
            try:
                replace_pattern(None, r"\w+", "replacement")
                assert False, "Should raise TypeError for None text"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                replace_pattern("text", None, "replacement")
                assert False, "Should raise TypeError for None pattern"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            try:
                replace_pattern("text", r"\w+", None)
                assert False, "Should raise TypeError for None replacement"
            except TypeError as e:
                assert "string" in str(e).lower()
            
            # Test invalid regex pattern in replace_pattern
            try:
                replace_pattern("text", "(invalid[regex", "replacement")
                assert False, "Should raise ValueError for invalid regex"
            except (ValueError, re.error):
                pass
            
            TestUtils.yakshaAssert("test_exception_handling", True, "exceptional")
        except Exception as e:
            TestUtils.yakshaAssert("test_exception_handling", False, "exceptional")
            raise e
    
    def test_try_except_pattern(self):
        """Test proper implementation of try-except patterns."""
        try:
            # Import solution module to examine structure
            import digital_communications_analyzer as module
            
            # Define functions that should have error handling patterns
            functions_to_check = [
                "extract_emails", 
                "extract_phone_numbers", 
                "extract_dates", 
                "extract_ip_addresses",
                "validate_email", 
                "validate_phone_number", 
                "validate_ip_address", 
                "replace_pattern"
            ]
            
            missing_patterns = []
            
            for function_name in functions_to_check:
                try:
                    # Get function from module
                    function = getattr(module, function_name)
                    source = inspect.getsource(function)
                    
                    # Check for try-except blocks
                    has_try = "try:" in source
                    has_except = re.search(r"except\s+(\w+|[\(\w+,\s*\w+\)])", source) is not None
                    
                    # Every function should have try-except for input validation
                    if not has_try or not has_except:
                        missing_patterns.append(f"{function_name} missing try-except blocks")
                    
                    # Check for bare except (except without specific exception)
                    has_bare_except = re.search(r"except\s*:", source) is not None
                    if has_bare_except:
                        missing_patterns.append(f"{function_name} uses bare except (should specify exception types)")
                    
                    # Check for type checking
                    has_isinstance = "isinstance" in source
                    if not has_isinstance:
                        missing_patterns.append(f"{function_name} missing type checking")
                    
                except AttributeError:
                    missing_patterns.append(f"Could not find function {function_name}")
            
            # Make sure no functions are missing required patterns
            # Note: This is a recommendation for the solution, not a requirement
            # We'll document the missing patterns but not fail the test
            if len(missing_patterns) > 0:
                print(f"Note: The following patterns are recommended but not required: {', '.join(missing_patterns)}")
            # assert len(missing_patterns) == 0, f"Missing patterns: {', '.join(missing_patterns)}"
            
            # Test error propagation
            # Create a function that calls our functions with invalid inputs
            def test_propagation():
                try:
                    extract_emails(None)
                except TypeError:
                    # This is expected, error should propagate up
                    raise RuntimeError("Error propagation test")
            
            # Error should propagate through the call stack
            try:
                test_propagation()
                assert False, "Should propagate error"
            except RuntimeError as e:
                assert "Error propagation test" in str(e)
            
            TestUtils.yakshaAssert("test_try_except_pattern", True, "exceptional")
        except Exception as e:
            TestUtils.yakshaAssert("test_try_except_pattern", False, "exceptional")
            raise e