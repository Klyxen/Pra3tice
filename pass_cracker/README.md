# Password & PIN Cracker

This script cracks passwords and PINs by brute-forcing them. It checks each character in a password one by one, and tries every possible combination for a given PIN. Simple, but effective.

## What it does:
1. **Password Cracker**: Scans each character of the password and tries to match it with printable characters.
2. **PIN Cracker**: Tries every combination of digits for a given PIN length.

## Requirements:
None. It uses basic Python libraries, just `string`.

## Code Breakdown:
- **Password Cracker**:
  - It loops through every printable character and compares it with each character in the password.
  - Once it finds a match, it moves on to the next character.
  - In the end, it gives you the password you put in.

- **PIN Cracker**:
  - It checks a given PIN by brute-forcing every possible combination for the length of the PIN.
  - It keeps guessing till it finds the right one.

### Main Class - `Scan`:
The `Scan` class does the job for the password part:
- **`scan()`**: Loops through printable characters and matches each one to the target password, adding the matched character to the result.

### PIN Cracking:
- The script calculates the length of the PIN and tries every possible guess, from `000` up to the max length. Once it finds the PIN, it stops.

___

# How to Use:

### 1. **Download the script from GitHub**:
   - You can either **clone** the repository or **download** the ZIP file.
   
   **To clone** the repository:
   - Make sure you have [Git](https://git-scm.com/) installed.
   - Open your terminal and run:
     ```bash
     git clone https://github.com/your-username/password-pin-cracker.git
     ```
   - Navigate to the folder where the script was cloned:
     ```bash
     cd password-pin-cracker
     ```

   **To download as a ZIP**:
   - Go to the [GitHub repository page](https://github.com/your-username/password-pin-cracker).
   - Click the green **"Code"** button and then select **"Download ZIP"**.
   - Extract the ZIP file to your preferred location.

### 2. **Open your terminal**:
   - Navigate to the directory where the script is located using the `cd` command:
     ```bash
     cd /path/to/script
     ```

### 3. **Run the script**:
   - Make sure you have Python 3 installed. If not, you can download it from [here](https://www.python.org/downloads/).
   - Run the script with the following command:
     ```bash
     python password_pin_cracker.py
     ```

### 4. **Input the password or PIN**:
   - When prompted, enter the password you want to crack or the PIN you want to guess.
   - The script will start running and print the results in the terminal.

## License:
MIT License. Do whatever, just don't blame me if it breaks stuff.
