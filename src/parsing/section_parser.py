from pypdf import PdfReader

reader = PdfReader("data/raw_pdf/kimi_k2_5.pdf")

all_text = []

for i, page in enumerate(reader.pages):
    page_text = page.extract_text()
    if page_text:
        all_text.append(page_text)

full_text = "\n".join(all_text)

lines = [line.strip() for line in full_text.split("\n") if line.strip()]

import re

section_pattern = re.compile(r"^\d+\s+[A-Z][A-Za-z\s\-]+$")
subsection_pattern = re.compile(r"^\d+\.\d+\s+[A-Z][A-Za-z\s\-]+$")

section_objects = []
current_section = None
current_subsection = None

def is_section_header(line):
    if section_pattern.match(line):
        return True
    if line.lower() == "references":
        return True
    if line.lower() == "abstract":
        return True
    return False

for line in lines:
    if is_section_header(line):
        current_section = {
            "section_title": line,
            "subsections": [],
            "section_intro_content": []
        }
        section_objects.append(current_section)
        current_subsection = None

    elif current_section and subsection_pattern.match(line):
        current_subsection = {
            "subsection_title": line,
            "content": []
        }
        current_section["subsections"].append(current_subsection)

    else:
      if current_section:
        if current_subsection:
            current_subsection["content"].append(line)
        else:
            # text before first subsection
            current_section["section_intro_content"].append(line)

for sec in section_objects:
    if sec["section_intro_content"]:
        sec["subsections"].insert(0, {
            "subsection_title": sec["section_title"] + " (Overview)",
            "content": sec["section_intro_content"]
        })

    del sec["section_intro_content"]


print("\n--- Section / Subsection Summary ---\n")
for sec in section_objects:
    print(sec["section_title"]) 
    for sub in sec["subsections"]:
        print(f"  - {sub['subsection_title']} ({len(sub['content'])} lines)")