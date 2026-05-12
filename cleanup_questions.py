#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""清理重复问题 - 每个问题只保留一个版本"""

import json
import re

def load_js_file(file_path):
    """从 JS 文件中提取数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 germanQuestions
    german_match = re.search(r'const germanQuestions = (\[.*?\]);', content, re.DOTALL)
    # 提取 japaneseQuestions  
    japanese_match = re.search(r'const japaneseQuestions = (\[.*?\]);', content, re.DOTALL)
    
    german_questions = json.loads(german_match.group(1)) if german_match else []
    japanese_questions = json.loads(japanese_match.group(1)) if japanese_match else []
    
    return german_questions, japanese_questions

def remove_duplicates(questions):
    """移除重复问题，只保留每个问题的第一个版本"""
    seen = {}
    unique_questions = []
    
    for question in questions:
        question_text = question.get('text', '')
        
        if question_text not in seen:
            seen[question_text] = True
            unique_questions.append(question)
    
    return unique_questions

def save_cleaned_files():
    """保存清理后的文件"""
    # 读取原文件
    german_questions, japanese_questions = load_js_file('questions_output.js')
    
    print(f"原始德文题目数: {len(german_questions)}")
    print(f"原始日文题目数: {len(japanese_questions)}")
    
    # 移除重复
    german_cleaned = remove_duplicates(german_questions)
    japanese_cleaned = remove_duplicates(japanese_questions)
    
    print(f"清理后德文题目数: {len(german_cleaned)}")
    print(f"清理后日文题目数: {len(japanese_cleaned)}")
    
    # 保存为文本文件
    with open('de_questions_clean.txt', 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i, q in enumerate(german_cleaned):
            f.write(json.dumps(q, ensure_ascii=False, indent=2))
            if i < len(german_cleaned) - 1:
                f.write(',\n')
        f.write('\n]')
    
    with open('ja_questions_clean.txt', 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i, q in enumerate(japanese_cleaned):
            f.write(json.dumps(q, ensure_ascii=False, indent=2))
            if i < len(japanese_cleaned) - 1:
                f.write(',\n')
        f.write('\n]')
    
    print("\n✅ 清理完成！")
    print("- 德文: de_questions_clean.txt")
    print("- 日文: ja_questions_clean.txt")

if __name__ == "__main__":
    save_cleaned_files()
