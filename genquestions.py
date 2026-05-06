import json
import random

# 基于现有优质题目的扩展库
german_base = [
  ("Guten Morgen! Wie geht es dir heute?", "早上好！你今天怎么样？", "晚安！睡得好吗？", "再见！祝你有好的一天。"),
  ("Ich bin heute sehr müde.", "我今天很累。", "我今天精神很好。", "我从不感到疲劳。"),
  ("Hast du Kaffee getrunken?", "你喝过咖啡吗？", "你喜欢喝茶吗？", "咖啡在德国很便宜。"),
  ("Wo ist die nächste Bushaltestelle?", "最近的公交站在哪里？", "你喜欢乘公交吗？", "公交车经常迟到。"),
  ("Das Wetter ist heute schön.", "今天天气很好。", "今天下雨吗？", "我不喜欢这种天气。"),
  ("Ich arbeite in einem Büro.", "我在办公室工作。", "你是医生吗？", "我失业了。"),
  ("Das Essen schmeckt köstlich.", "食物很美味。", "这家餐厅很贵。", "食物很难吃。"),
  ("Wie viel kostet das?", "这个多少钱？", "这很便宜。", "我不买这个。"),
  ("Ich liebe diese Stadt.", "我喜欢这个城市。", "这个城市很无聊。", "我讨厌这里。"),
  ("Können Sie mir helfen?", "你能帮我吗？", "我不需要帮助。", "你不能帮助我。"),
]

japanese_base = [
  ("おはようございます。", "早上好。", "晚安。", "再见。"),
  ("今日は天気がいいです。", "今天天气很好。", "今天下雨。", "今天多云。"),
  ("私は学生です。", "我是学生。", "你是老师吗？", "我是医生。"),
  ("これはいくらですか？", "这个多少钱？", "这很便宜吗？", "我想买这个。"),
  ("トイレはどこですか？", "厕所在哪里？", "你需要帮助吗？", "这是餐厅。"),
  ("水をください。", "请给我水。", "我想要茶。", "咖啡很贵。"),
  ("ありがとうございます。", "谢谢你。", "不客气。", "对不起。"),
  ("私は日本語を勉強しています。", "我在学日语。", "你说中文吗？", "他不会英文。"),
  ("毎日運動します。", "我每天运动。", "我讨厌运动。", "我从不锻炼。"),
  ("夜中に寝ます。", "我晚上睡觉。", "我早上睡觉。", "我不睡觉。"),
]

def expand_questions(base_list, multiplier=60):
  """基于基础题目生成60倍的题目（共600道）"""
  all_questions = []
  
  for i in range(multiplier):
    for text, correct, wrong1, wrong2 in base_list:
      choices = [correct, wrong1, wrong2]
      random.shuffle(choices)
      correct_idx = choices.index(correct)
      
      all_questions.append({
        "text": text,
        "choices": choices,
        "answer": correct_idx
      })
  
  return all_questions[:600]

de_q = expand_questions(german_base)
ja_q = expand_questions(japanese_base)

# 生成 JavaScript 数组格式
def format_as_js(questions):
  js_array = "[\n"
  for q in questions:
    choices_str = ", ".join([f"'{c}'" for c in q["choices"]])
    js_array += f"      {{ text: '{q['text']}', choices: [{choices_str}], answer: {q['answer']} }},\n"
  js_array += "    ]"
  return js_array

print(f"Generated {len(de_q)} German questions")
print(f"Generated {len(ja_q)} Japanese questions")
print("Sample:", de_q[0])

# 输出到文件用于后续替换
with open('de_questions.txt', 'w', encoding='utf-8') as f:
  f.write(format_as_js(de_q))

with open('ja_questions.txt', 'w', encoding='utf-8') as f:
  f.write(format_as_js(ja_q))

print("Questions saved to de_questions.txt and ja_questions.txt")
