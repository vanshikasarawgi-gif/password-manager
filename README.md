# Password Manager 🛡️

A simple **Password Manager** built with Python and Tkinter.  
This app allows users to generate strong random passwords and save them along with website and email information for easy management.

---

## ✨ Features
- **Generate strong passwords** with letters, numbers, and symbols
- **Save passwords** securely to a text file
- **User-friendly interface** with Tkinter
- Prevents saving if **fields are empty**
- Optional: Placeholder text for password entry (can be added for UI polish)

---

## 🛠️ How It Works
1. Enter the **website name** and your **email/username**.
2. Click **Generate Password** to create a random secure password.
3. The password appears in the **password field**.
4. Click **Add** to save the details in `data.txt`.
5. If any field is empty, the app will show an **error message**.
6. Before saving, the app asks for **confirmation** using a popup.

---

## 💻 Requirements
- Python 3.x
- Tkinter (usually included with Python)
- `random` module (built-in)

---

## 🏃 How to Run
1. Clone this repository:
   ```bash
   git clone <your-repo-link>
2. Make sure logo.png is in the same folder as the script.

3. Run the Python script:

python main.py

4. The app window will appear, and you can start generating and saving passwords.

📂 Project Files

main.py → Main Python script for the password manager

logo.png → Logo image displayed in the app

data.txt → File where website, email, and password are saved
