import random
import string

class TestHelpers:
    
    @staticmethod
    def generate_random_string(length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
    
    @staticmethod
    def generate_random_number(length=5):
        digits = string.digits
        return ''.join(random.choice(digits) for _ in range(length))
    
    @staticmethod
    def take_screenshot(driver, test_name):
        import os
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        
        # Create directory if not exists
        os.makedirs("screenshots", exist_ok=True)
        
        driver.save_screenshot(filename)
        return filename