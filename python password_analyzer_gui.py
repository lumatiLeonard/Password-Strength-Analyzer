import re
import random
import string
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Load common passwords from rockyou.txt
def load_common_passwords(file_path="rockyou.txt"):
    try:
        with open(file_path, "r", encoding="latin-1") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        messagebox.showerror("Error", "rockyou.txt not found. Please download it and place it in the same directory.")
        return set()

# Save results to a file
def save_results(password, score, feedback, generated_password):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("password_analysis_log.txt", "a") as file:
        file.write(f"Timestamp: {timestamp}\n")
        file.write(f"Password: {'*' * len(password)} (Masked for security)\n")
        file.write(f"Strength Score: {score}/6\n")
        file.write("Feedback:\n")
        for line in feedback:
            file.write(f"- {line}\n")
        if generated_password:
            file.write(f"Generated Password: {generated_password}\n")
        file.write("\n" + "="*40 + "\n")

# Evaluate password strength
def evaluate_password():
    password = entry_password.get()
    common_passwords = load_common_passwords()
    score, feedback = evaluate_password_strength(password, common_passwords)
    
    # Update GUI with results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Strength Score: {score}/6\n")
    if feedback:
        result_text.insert(tk.END, "\nSuggestions to Improve:\n")
        for suggestion in feedback:
            result_text.insert(tk.END, f"- {suggestion}\n")
    else:
        result_text.insert(tk.END, "Your password is strong!\n")
    
    # Generate a strong password if needed
    if score < 4:
        generated_password = generate_strong_password()
        result_text.insert(tk.END, f"\nGenerated Strong Password: {generated_password}")
        # Save results with generated password
        save_results(password, score, feedback, generated_password)
    else:
        # Save results without generated password
        save_results(password, score, feedback, None)

# Generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Core evaluation logic
def evaluate_password_strength(password, common_passwords):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 8 characters.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Check against common passwords
    if password.lower() in common_passwords:
        feedback.append("This password is too common. Avoid using it.")
    else:
        score += 1

    return score, feedback

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("600x500")

# Create GUI Elements
label_password = tk.Label(root, text="Enter Password:", font=("Arial", 12))
entry_password = tk.Entry(root, show="*", width=30, font=("Arial", 12))
button_check = tk.Button(root, text="Check Strength", command=evaluate_password, bg="#4CAF50", fg="white")
result_text = tk.Text(root, height=15, width=60, font=("Arial", 10))
button_generate = tk.Button(root, text="Generate Strong Password", command=lambda: result_text.insert(tk.END, f"\nGenerated Password: {generate_strong_password()}"))

# Layout
label_password.pack(pady=10)
entry_password.pack(pady=5)
button_check.pack(pady=10)
result_text.pack(padx=10, pady=10)
button_generate.pack(pady=10)

# Run the GUI
root.mainloop()