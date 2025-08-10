🇬🇧 Japanese Learning Helper 

📌 Project Overview

This is a tool for collecting and learning Japanese vocabulary. Users can add unfamiliar Japanese words to the repository, and the system will automatically generate definitions, example sentences, and pronunciations, exporting them as Anki flashcards to aid efficient memorization and review.

⚙️ Features

Automated Learning Workflow: From collecting words to generating Anki flashcards, the entire process is automated.

Multilingual Support: Supports definitions, example sentences, and pronunciations in both Japanese and Chinese.

Efficient Memorization: Utilizes Anki flashcards for spaced repetition learning, enhancing memory retention.

Open Source: All code and data are open source, contributions and improvements are welcome.


📦 Installation and Usage

1. Clone the Repository:

```bash
git clone https://github.com/erzhiqianyi/JapaneseDictionary

cd JapaneseDicionary
```

2. Install Dependencies:

```bash
pip install -r requirements.txt
Add Words:
```

3. Add Words:

Add unfamiliar Japanese words to the words.csv file, one word per line.

5. Generate Anki Flashcards:

Run the following command:

```bash
python generate_anki.py
```

This command will generate an .apkg file, which you can import into Anki for study.


📦 Supplement — How to Generate Flashcards

Two Ways to Generate Anki Flashcards

1. Automatic Generation from Raw Words (Requires API Access)
If you have access to the ChatGPT API, you can use the scripts in this repository to automatically call the API, generate detailed definitions and example sentences for your vocabulary, and output Anki flashcard packages (.apkg files).

Advantage: fully automated, suitable for batch processing.

Example command:

```bash
python generate_anki.py  
```

2. Importing Files Generated via ChatGPT Web or Client

If you do not have API access, you can manually use the ChatGPT web or desktop client to input words and generate the definitions and examples. Then save the results in a specified file format (TSV).

Place the generated file into the repository folder and run the import script to create your Anki deck.

Advantage: no API needed, good for small manual operations.

🛠️ Contributing

We welcome contributions to this project:

Fork the Repository: Click the "Fork" button at the top right of the page.

Create a Branch: Create a new branch in your forked repository.

Make Changes: Make changes in the new branch and commit them.

Submit a Pull Request: Submit your changes to the main branch of the original repository.


📄 Prompt For Japanese Vocabulary Analysis

```
あなたは日本語学習の専門アシスタントです。
以下の日本語単語について、次の内容を詳しく解析してください。
まとめて出力と言ったとき、私が私た単語を集めて、TSVファイルとして出力してください。
fields=[
        {'name': '漢字'},
        {'name': '假名'},    
        {'name': '品詞'},
        {'name': 'ローマ字'},
        {'name': '詞源'},
        {'name': '活用类型'},
        {'name': '中文释义'},
        {'name': '日文释义'},
        {'name': '意味日文'},
        {'name': '意味中文'},
        {'name': '例文1'},
        {'name': '例文1中文'},
        {'name': '例文2'},
        {'name': '例文2中文'},
        {'name': 'JLPT'},
        {'name': 'ます形'},
        {'name': 'て形'},
        {'name': 'ない形'},
        {'name': 'た形'},
        {'name': '辞書形'},
        {'name': '可能形'},
        {'name': '意向形'},
    ]
```


📄 License

This project is licensed under the MIT License. See the LICENSE file for details.