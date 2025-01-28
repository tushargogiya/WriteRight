# WriteRight - Your AI-Powered Writing Assistant

**WriteRight** is an intelligent web application built with **Streamlit** for **real-time spell and grammar checking**. It leverages a **fine-tuned T5 model** for grammar correction and a **vocabulary-based spell checker** using **Jaccard similarity**, helping users enhance their writing quality with ease.

## 🚀 Features
### 📝 Spell Checker
- Detects spelling errors in your text and suggests corrections based on a **rich corpus of literary works**.
- Uses **Jaccard Similarity** and **word frequency probabilities** to provide highly accurate corrections.

### 📖 Grammar Checker
- Employs a **fine-tuned T5 model** trained for **grammatical error correction (GEC)**.
- Offers suggestions to **improve sentence structure, word usage, and syntax**.

### 🔍 Interactive UI
- User-friendly **Streamlit interface** for entering text, viewing **side-by-side corrections**, and improving writing quality instantly.

---

## 📦 Requirements
Ensure you have the necessary dependencies installed before running the app:

```sh
pip install -r requirements.txt
```

### Dependencies:
- **streamlit** – Web app framework
- **pandas** – Data manipulation
- **textdistance** – Similarity calculations
- **torch** – Deep learning framework
- **transformers** – Pretrained NLP models
- **sentencepiece** – Tokenization
- **re** – Regular expressions
- **collections** – Data structures

---

## 🎯 How to Use
1. **Enter Text** – Input your text into the application interface.
2. **Check Spelling** – Click **Check Spelling** to detect misspelled words and get suggested corrections.
3. **Check Grammar** – Click **Check Grammar** to receive grammatical suggestions for sentence enhancement.

---

## 🔬 How It Works
### ✨ Spell Checking
- The spell checker **compares each word** in the input against a **vocabulary** compiled from multiple literary texts.
- It suggests corrections based on:
  - **Jaccard Similarity** – Measures how closely a word resembles another.
  - **Word Frequency** – Prioritizes corrections based on real-world usage.

### ✨ Grammar Checking
- Uses a **fine-tuned T5 model** designed specifically for **grammatical error correction (GEC)**.
- Generates multiple **grammatically improved versions** of each sentence.
- Ensures higher **accuracy, fluency, and readability**.

---

## 🔍 Model Details
### 🏆 Grammar Checker Model
- Based on **T5 (Text-to-Text Transfer Transformer)**, fine-tuned for grammatical error correction.
- Trained on a **large-scale dataset**, ensuring high accuracy in grammatical corrections.
- Capable of generating **context-aware and syntactically correct** text outputs.

### 📚 Spell Checker
- Uses a **vocabulary from multiple literary texts and public datasets**.
- Implements **Jaccard Similarity & word frequency probabilities** to determine the most probable correct words.

---

## 📌 Running the App
To launch the **WriteRight** application, use the following command:

```sh
streamlit run app.py
```

This will start the Streamlit app in your **default web browser**, where you can interactively check for **spelling and grammar errors**.

---

## 🚀 Deployment
- **WriteRight** is deployed on **Hugging Face Spaces**.
- You can access the **live version** of the app [here](#).

---

## 🤝 Contributing
We welcome contributions! 🚀 If you’d like to contribute:
- **Fork this repository**
- **Submit issues** for bugs, feature requests, or improvements
- **Create pull requests** with fixes or enhancements

Join the mission to make writing smarter and error-free! 🎉

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and distribute it.

---

## 🌟 Acknowledgments
- **Hugging Face** – For providing robust NLP models.
- **Streamlit** – For simplifying AI app development.
- **Open-source contributors** – For making this project possible.

---

### 🎯 Elevate Your Writing with WriteRight! 🚀

