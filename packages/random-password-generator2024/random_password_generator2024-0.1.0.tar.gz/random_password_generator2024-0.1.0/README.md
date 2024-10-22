# Random Password Generator

A Python package to generate random, secure passwords.

## Example usage

    if __name__ == "__main__":
        password_generator = PasswordGenerator()

    
        Generate 5 unique passwords
        for _ in range(5):
            password = password_generator.generate_password(
                length=16, 
                use_upper=True, 
                use_lower=True, 
                use_numbers=True,
                use_special=True)
            print("Generated password:", password)`
