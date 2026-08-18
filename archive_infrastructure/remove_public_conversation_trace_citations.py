from pathlib import Path

MASTER = Path('/home/ubuntu/projects/ecofarm-89bdc8ac/EcoFarm_Master_Knowledge_Base.md')
text = MASTER.read_text()
old = '[EF-GOV-004](https://github.com/Lonely-Demon/EcoFarm_Archives/blob/main/00_governance_and_archive/EF-GOV-004__ecofarm_1_conversation.jsonl "Historical EcoFarm 1 conversation trace; legacy SRC-0130")'
new = '`[Private preservation trace; no public link]`'
count = text.count(old)
if count == 0:
    raise SystemExit('No raw conversation trace citations found')
MASTER.write_text(text.replace(old, new))
print({'replaced_raw_conversation_citations': count})
