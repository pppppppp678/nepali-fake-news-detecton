    # 📰 Nepalese Fake News Detection Engine
> **An Applied Machine Learning & NLP Pipeline for Automated Misinformation Triaging in Low-Resource Languages.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![ML-Library](https://img.shields.io/badge/ML-Scikit--Learn-F7931E.svg)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-0284C7.svg)]()

---

## 🎯 Production & Remote Market Overview
While generic NLP models excel at high-resource languages (like English), **misinformation in low-resource, morphologically rich languages like Nepali presents a severe engineering bottleneck** due to the lack of pre-trained tokenizers, standard corpora, and stop-word metrics. 

This repository demonstrates an end-to-end applied machine learning solution designed to parse, vectorize, and accurately classify textual news items into *Authentic* or *Satirical/Fake* categories, serving real-time inferences through an interactive dashboard.

---

## 🏗️ Architectural Pipeline & System Flow

The core system bypasses traditional low-resource linguistics constraints by utilizing a custom text-processing pipeline integrated with vectorized feature extractors:

```text
[Raw Nepali Text Input]
          │
          ▼
┌───────────────────────────┐
│ Custom Text Preprocessing │ ──► Tokenization, Stop-words Stripping & De-noising
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│ Feature Extraction Layer  │ ──► TF-IDF Vectorizer (N-gram Range: Uni-grams & Bi-grams)
└─────────┬─────────────────┘
          │
          ▼
┌───────────────────────────┐
│  Machine Learning Core    │ ──► Evaluation of MultinomialNB, PassiveAggressive, 
└─────────┬─────────────────┘     and Logistic Regression Classifiers
          │
          ▼
┌───────────────────────────┐
│   Real-Time Inference     │ ──► Streamlit Web Engine Serving Millisecond Response
└───────────────────────────┘
