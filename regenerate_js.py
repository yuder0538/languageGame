#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新生成 questions_output.js"""

import json

def load_questions_from_file(file_path):
    """从文本文件加载问题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 JSON 数组
    questions = json.loads(content)
    return questions

def generate_js_output():
    """生成 JavaScript 输出"""
    # 加载清理后的数据
    german_questions = load_questions_from_file('de_questions.txt')
    japanese_questions = load_questions_from_file('ja_questions.txt')
    
    print(f"加载德文题目: {len(german_questions)}")
    print(f"加载日文题目: {len(japanese_questions)}")
    
    # 生成 JS 代码
    german_js = "const germanQuestions = " + json.dumps(german_questions, ensure_ascii=False) + ";\n\n"
    japanese_js = "const japaneseQuestions = " + json.dumps(japanese_questions, ensure_ascii=False) + ";"
    
    # 写入文件
    with open('questions_output.js', 'w', encoding='utf-8') as f:
        f.write(german_js)
        f.write(japanese_js)
    
    print("\n✅ questions_output.js 已更新！")
    print(f"✅ 所有占位符已移除")

if __name__ == "__main__":
    generate_js_output()
