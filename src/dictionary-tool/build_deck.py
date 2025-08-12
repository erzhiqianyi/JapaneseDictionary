import json
import os
import genanki

import random


def load_json(file):
    with open(file) as f:
        return json.load(f)


def read_all_csv_files(directory='data/dictionary'):
    word_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            words = load_json(os.path.join(directory, filename))
            for word in words:
                word_list.append(word)
    return word_list


def generate_id():
    return random.randrange(1 << 30, 1 << 31)




def create_deck(deck_id):
    my_deck = genanki.Deck(
        deck_id,
        '私の辞書）'
    )
    return my_deck


def create_model(model_id):
    my_model = genanki.Model(
        model_id,
        'Japanese Vocabulary Model',
        fields=[
            {'name': 'Front'},
            {'name': 'Expression'},
            {'name': 'JLPT'},
            {'name': '品詞'},
            {'name': '活用类型'},
            {'name': '中文释义'},
            {'name': '日文释义'},
            {'name': '詞源'},
            {'name': 'ます形'},
            {'name': 'て形'},
            {'name': 'ない形'},
            {'name': 'た形'},
            {'name': '辞書形'},
            {'name': '可能形'},
            {'name': '意向形'},
            {'name': '意味日文'},
            {'name': '意味中文'},
            {'name': '例文1'},
            {'name': '例文1中文'},
            {'name': '例文2'},
            {'name': '例文2中文'},
            {'name': '假名'},
            {'name': 'Pronunciation'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': """{{#假名}} <h class=POSR>{{Front}}</h> {{/假名}} <p>""",
                'afmt': """{{FrontSide}} <hr> {{#Expression}} <h class=POSR>{{假名}}</h> <p> <h class=POSR>{{Pronunciation}}</h> {{/Expression}} <p> <div style='font-family: calibri; font-size: 20px;'>{{中文释义}}</div> <div style='font-family:微软雅黑; font-size: 20px;'>{{日文释义}}</div> <hr> <div><b>詞源： <p>{{詞源}}</p> </div> {{#品詞}}<div><b>品詞：</b>{{品詞}}</div>{{/品詞}} <hr> <div><b>意味（日文）： <p>{{意味日文}}</p> </div> <div><b>意味（中文）： <p>{{意味中文}}</p> </div> <hr> <div><p>例文：</p></div> <div>{{furigana:例文1}}<br><span class="Ch">{{例文1中文}}</span></div> </p> <div>{{furigana:例文2}}<br><span class="Ch">{{例文2中文}}</span></div> <hr> {{#JLPT}}<div><b>JLPT：</b>{{JLPT}}</div>{{/JLPT}} <hr> {{#活用类型}}<div><b>活用类型：</b>{{活用类型}}</div>{{/活用类型}} {{#ます形}}<div><b>ます形：</b>{{ます形}}</div>{{/ます形}} {{#て形}}<div><b>て形：</b>{{て形}}</div>{{/て形}} {{#ない形}}<div><b>ない形：</b>{{ない形}}</div>{{/ない形}} {{#た形}}<div><b>た形：</b>{{た形}}</div>{{/た形}} {{#辞書形}}<div><b>辞書形：</b>{{辞書形}}</div>{{/辞書形}} {{#可能形}}<div><b>可能形：</b>{{可能形}}</div>{{/可能形}} {{#意向形}}<div><b>意向形：</b>{{意向形}}</div>{{/意向形}}            """,
            }
        ],
        css=""" 
       .card { font-size: 25px; text-align: center; color: black; line-height: 25px; padding-top:35px; } .POSR { background-color: #338eca; line-height: 30px;} .PhoneticSymbol { font-family: MS Gothic; text-align: center; color: #555555; font-size: 18px; } .Ch { font-family: 微软雅黑; color: #555555; font-size: 18px; text-align: justify; line-height: 25px; } .hint { font-family: calibri; font-size: 18px; text-align: center; color: #444444; line-height: 22px; } 
        """
    )
    return my_model


def create_note(word, model):
    my_note = genanki.Note(
        model=model,
        fields=[
            word["漢字"],  # Front
            word["漢字"],
            word["JLPT"],  # JLPT
            word["品詞"],
            word["活用类型"],  # 活用类型
            word["中文释义"],  # 中文释义
            word["日文释义"],  # 日文释义
            word["詞源"],  # 詞源
            word["ます形"],  # ます形
            word["て形"],  # て形
            word["ない形"],  # ない形
            word["た形"],  # た形
            word["辞書形"],  # 辞書形
            word["可能形"],  # 可能形
            word["意向形"],  # 意向形
            word["意味日文"],  # 意味日文
            word["意味中文"],  # 意味中文
            word["例文1"],  # 例文1
            word["例文1中文"],  # 例文1中文
            word["例文2"],  # 例文2
            word["例文2中文"],  # 例文2中文
            word["假名"],  # 假名
            word["ローマ字"]  # Pronunciation
        ]
    )
    return my_note


def start():
    words = read_all_csv_files("../../data/dictionary")
    unique_word = set()
    model_id = generate_id()
    deck_id = generate_id()
    my_model = create_model(model_id)
    my_deck = create_deck(deck_id)
    for word in words:
        if not word["漢字"] in unique_word:
            my_note = create_note(word, my_model)
            my_deck.add_note(my_note)
            unique_word.add(word["漢字"])
    print("total words "+str(len(unique_word)))
    genanki.Package(my_deck).write_to_file('../../data/私の辞書.apkg')
    print("ファイル「私の辞書.apkg」を作成しました。Anki にインポートしてご利用ください。")


if __name__ == "__main__":
    start()
