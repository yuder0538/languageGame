#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""替换占位符选项为真实的翻译"""

import json
import re
import random

def load_questions_from_file(file_path):
    """从文本文件加载问题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 JSON 数组
    questions = json.loads(content)
    return questions

def get_all_correct_answers(questions):
    """获取所有正确答案"""
    correct_answers = []
    for q in questions:
        # answer 字段指示正确选项的索引
        answer_idx = q.get('answer', 0)
        correct_answer = q['choices'][answer_idx]
        correct_answers.append(correct_answer)
    return correct_answers

def clean_questions(questions):
    """清理问题，用真实的错误选项替换占位符"""
    placeholder_texts = ["不是這個意思。", "這是另一個句子。", "這個翻譯不對。", 
                         "完全不同的意思。", "這不是這個意思。", "錯誤的翻譯。"]
    
    # 获取所有正确答案作为候选的错误选项
    all_correct_answers = get_all_correct_answers(questions)
    
    cleaned_questions = []
    
    for q in questions:
        text = q['text']
        choices = q['choices'].copy()
        answer = q['answer']
        
        # 检查是否有占位符
        has_placeholder = any(placeholder in choices for placeholder in placeholder_texts)
        
        if has_placeholder:
            # 获取正确答案
            correct_answer = choices[answer]
            
            # 收集需要替换的占位符位置
            new_choices = []
            for choice in choices:
                if choice in placeholder_texts:
                    # 找一个不同的真实选项作为错误答案
                    attempts = 0
                    while attempts < 20:
                        wrong_answer = random.choice(all_correct_answers)
                        # 确保不是正确答案本身
                        if wrong_answer != correct_answer and wrong_answer not in new_choices:
                            new_choices.append(wrong_answer)
                            break
                        attempts += 1
                    else:
                        # 如果找不到合适的，就用占位符
                        new_choices.append(choice)
                else:
                    new_choices.append(choice)
            
            q['choices'] = new_choices
        
        cleaned_questions.append(q)
    
    return cleaned_questions

def save_questions_to_file(questions, file_path):
    """将问题保存到文件"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i, q in enumerate(questions):
            f.write(json.dumps(q, ensure_ascii=False, indent=2))
            if i < len(questions) - 1:
                f.write(',\n')
        f.write('\n]')

def main():
    # 处理德文题目
    print("处理德文题目...")
    german_questions = load_questions_from_file('de_questions.txt')
    print(f"加载 {len(german_questions)} 个德文题目")
    
    german_cleaned = clean_questions(german_questions)
    save_questions_to_file(german_cleaned, 'de_questions.txt')
    print(f"✅ 德文题目已更新")
    
    # 处理日文题目
    print("\n处理日文题目...")
    japanese_questions = load_questions_from_file('ja_questions.txt')
    print(f"加载 {len(japanese_questions)} 个日文题目")
    
    japanese_cleaned = clean_questions(japanese_questions)
    save_questions_to_file(japanese_cleaned, 'ja_questions.txt')
    print(f"✅ 日文题目已更新")
    
    print("\n✅ 所有占位符已替换为真实的翻译！")

if __name__ == "__main__":
    main()
