from pathlib import Path
root=Path(__file__).resolve().parents[1]
ext={'.py','.js','.css','.html','.sql'}
files=[]; lines=0
for p in root.rglob('*'):
    if p.is_file() and p.suffix in ext and 'node_modules' not in p.parts:
        n=sum(1 for _ in p.open(errors='ignore'))
        files.append((str(p.relative_to(root)),n)); lines+=n
print(f'Production-style source LOC: {lines}')
for f,n in sorted(files,key=lambda x:-x[1]): print(f'{n:6} {f}')
