# 🖼️ Simple Image Scraper using DuckDuckGo (Unofficial API)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![Stars](https://img.shields.io/github/stars/mejiwmi/ImageScraper?style=social)


This is a **lightweight and easy-to-use image scraper** designed for quick plug-and-play usage. No complex setup or configuration needed—just install the dependencies and start scraping.

## 🚀 Features

- ✅ Plug and play — minimal setup required  
- 🔍 Uses the **unofficial DuckDuckGo image search API**  
- 📦 Supports up to **100 images per query** (API limitation)  
- 🛠️ Great for quick dataset creation or small-scale image scraping tasks

## ⚠️ Limitations

- The scraper uses **DuckDuckGo’s unofficial API**, which imposes a **hard limit of 100 images per query**.
- If you need a larger number of images for a particular category, try breaking your main query into **multiple subqueries** with slight variations.
- Image counts can vary based on **niche** — some topics yield fewer results.
- DuckDuckGo image scraping is **less reliable than paid APIs** like Google's, so expect inconsistency in results.

## 📦 Installation

1. Clone the repository  
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script and pass your desired search terms.

## 💡 Tips

- Break broad search terms into more specific ones  
  _Example:_ Instead of `dogs`, try `golden retriever face`, `puppy playing`, etc.
- Scrape in **batches** if you hit the 100-image cap.

## 🤝 Contributions

Feel free to fork and improve! Suggestions, bug fixes, and enhancements are welcome.


