# -*- coding: utf-8 -*-
"""
將 技能參數.md 依職業群拆成獨立 JSON 檔案，便於網頁按需載入。
執行：python scripts/parse_skills.py
"""
import json
import re
import os
from pathlib import Path

MD_PATH = Path(__file__).resolve().parent.parent / "技能參數.md"
DATA_DIR = Path(__file__).resolve().parent.parent / "public" / "data"

def parse_md(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    jobs = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            job_name = m.group(1).strip()
            job = {"name": job_name, "skills": []}
            i += 1
            while i < len(lines):
                line = lines[i]
                if re.match(r"^##\s+", line):
                    break
                skill_m = re.match(r"^###\s+(.+)$", line)
                if skill_m:
                    skill_name = skill_m.group(1).strip()
                    skill = {"name": skill_name, "maxLevel": None, "description": "", "levels": []}
                    i += 1
                    while i < len(lines):
                        line = lines[i]
                        if re.match(r"^###\s+", line) or re.match(r"^##\s+", line):
                            break
                        max_m = re.match(r"^####\s+最高等級[：:]\s*(\d+)", line)
                        if max_m:
                            skill["maxLevel"] = int(max_m.group(1))
                            i += 1
                            continue
                        desc_m = re.match(r"^####\s+技能描述[：:]\s*(.*)$", line)
                        if desc_m:
                            skill["description"] = desc_m.group(1).strip()
                            i += 1
                            continue
                        lv_m = re.match(r"^####\s+等級\s*(\d+)[：:]\s*(.*)$", line)
                        if lv_m:
                            lv = int(lv_m.group(1))
                            effect = lv_m.group(2).strip()
                            skill["levels"].append({"level": lv, "effect": effect})
                            i += 1
                            continue
                        i += 1
                    if skill["name"]:
                        job["skills"].append(skill)
                    continue
                i += 1
            jobs.append(job)
            continue
        i += 1
    return jobs

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    jobs = parse_md(MD_PATH)
    index = []
    for idx, job in enumerate(jobs):
        job_id = f"job-{idx:02d}"
        job["id"] = job_id
        filename = f"{job_id}.json"
        filepath = DATA_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(job, f, ensure_ascii=False, indent=2)
        index.append({"id": job_id, "name": job["name"], "file": filename})
        print(f"已寫入 {filename}: {job['name']} ({len(job['skills'])} 個技能)")
    index_path = DATA_DIR / "index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"\n已寫入 index.json，共 {len(index)} 個職業群。")

if __name__ == "__main__":
    main()
