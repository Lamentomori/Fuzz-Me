import os
import time
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fuzz_password(length, charset):
    fuzzed_password = charset[0] * length
    index = [0] * length

    while True:
        yield fuzzed_password
        for i in range(length - 1, -1, -1):
            index[i] += 1
            if index[i] == len(charset):
                index[i] = 0
            else:
                fuzzed_password = fuzzed_password[:i] + charset[index[i]] + fuzzed_password[i + 1:]
                break

def check_strength(password, charset):
    fuzz_attempts = 0
    start_time = time.time()
    
    fuzz_generator = fuzz_password(len(password), charset)
    
    while True:
        fuzzed_password = next(fuzz_generator)
        fuzz_attempts += 1
        clear_screen()
        print(f"Attempt {fuzz_attempts}:")
        print(f"({fuzzed_password})", end='\r')
        
        if fuzzed_password == password:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return fuzz_attempts, elapsed_time

def main():
    charset = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}:><.,;0123456789'
    
    while True:
        password = input("Enter a password: ")
        
        fuzz_attempts, elapsed_time = check_strength(password, charset)
        
        if fuzz_attempts == 1:
            print(f"[❌] Password: {password} was cracked in {elapsed_time:.2f} seconds")

        else:
            print(f"[✅] Your password is strong enough to protect against modern threats!")


if __name__ == "__main__":
    main()
