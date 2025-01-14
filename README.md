# BewerbungAI-
A tool for creating personalized AI-based job application letters

---
## 📦 Installation:
Follow these steps to set up the application on your Mac 

--- 

### 1. Clone the Repository 
```bash
https://github.com/zerodrive16/BewerbungAI-.git
```
Copy the repository to a desired folder or your IDE workspace.

### 2. Create a Virtual Environment
Run the following command to create a virtual environment in the project directory:
```bash
python -m venv <name>
```

### 3. Activate the Virtual Environment
Activate the Virtual Environment: 
```bash
source <name>/bin/activate
```
Note: It is important to stay within the virtual environment to ensure other commands work 

### 4. Install Homebrew (if not done) (MacOS)
Install Homebrew using the command below: 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 5. Install Node.js
#### With Homebrew (MacOS):
```bash
brew install node
```
#### With Windows: 
Download and Install Node.js from the official [Node.js Website] (https://nodejs.org/en)
During installation ensure that the Path is also Included in the Environment Variable in the system

Check Versions (MacOS & Windows)
```bash
node -v
npm -v
```

### 6. Installing packages
Navigate to the project folder to access the requirements.txt file
```bash
cd /path/to/your/BewerbungAI/BewerbungAI
```
After this the folder requirements.txt is accessible which can be downloaded 
```bash
pip install -r requirements.txt
```

### 7. Starting the program 
Almost done now. It is important to run the react build and later run the django server if problems occurr
with "react-scripts" the dependency needs to be added in the *package.json*. 
```bash
cd frontend
npm run build
cd ..
python manage.py runserver

(If error with react-scripts) 
"dependencies": {
  "react-scripts": "^5.0.1",
  ...
}
```

## 🎉 You are All Set! 
Your application is ready to use. If any issues encounter, feel free to raise an issue in the Github Repository (https://github.com/zerodrive16/BewerbungAI-) 

## 🚀 Features 
- Generate personalized AI-based job application letters
- Ensures extra safety with personalized data
- Simplicity and Easy to Use Tool 


