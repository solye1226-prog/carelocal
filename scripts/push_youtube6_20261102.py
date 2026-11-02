import json,subprocess,sys
from pathlib import Path
n=int(sys.argv[1]);files=json.loads(Path(f'docs/youtube6-publication-2026-11-02/changed-{n}.json').read_text(encoding='utf8'))
subprocess.run(['git','add','--',*files],check=True)
subprocess.run(['git','diff','--cached','--check'],check=True)
subprocess.run(['git','commit','-m',f'Publish source-reviewed YouTube Trends follow-up {n}'],check=True)
subprocess.run(['git','push','origin','main'],check=True)
