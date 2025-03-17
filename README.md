# Password Strength Analyzer

## Features
- **Graphical User Interface (GUI):** Built with Tkinter for ease of use.
- **Result Logging:** All analyses are saved to `password_analysis_log.txt`.

## How to Use the GUI
1. Run the script:
   ```bash
   python password_analyzer_gui.py
2. Enter a password in the input field. 
3. Click Check Strength to view results. 
4. If the password is weak, click Generate Strong Password for a secure alternative. 
## Log File Format
All results are saved to `password_analysis_log.txt` with:
- Timestamp of analysis.
- Masked password input (for security).
- Strength score and feedback.
- Generated password(if applicable).
## Example Log Entry
`Timestamp: 2023-10-25 14:30:00
Password: ********** (Masked for security)
Strength Score: 3/6
Feedback:
- Add at least one uppercase letter.
- Add at least one special character.

Generated Password: aB3$kL9@qR2!`
