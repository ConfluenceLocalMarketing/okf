import os, yaml, sys

errors = []
for bundle in ['jake-sweeney-used-car-superstore-okf', 'jake-sweeney-mazda-tri-county-okf', 'bmw-of-cincinnati-north-okf']:
    count = 0
    for root, dirs, files in os.walk(bundle):
        for f in files:
            if f == 'viz.html':
                continue
            if not f.endswith('.md'):
                continue
            fp = os.path.join(root, f)
            count += 1
            is_index = f == 'index.md'
            relative = os.path.relpath(fp)
            try:
                with open(fp, encoding='utf-8') as fh:
                    content = fh.read()
                if not content.startswith('---'):
                    if not is_index:
                        errors.append(f'{relative}: missing frontmatter')
                    continue
                parts = content.split('---')
                if len(parts) < 3:
                    if not is_index:
                        errors.append(f'{relative}: malformed frontmatter')
                    continue
                fm = yaml.safe_load(parts[1])
                if not is_index:
                    if not fm or 'type' not in fm or not fm['type']:
                        errors.append(f'{relative}: missing or empty type field')
            except Exception as e:
                errors.append(f'{relative}: error - {e}')
    
    viz_exists = os.path.exists(os.path.join(bundle, 'viz.html'))
    print(f'{bundle}: {count} md files, viz.html={viz_exists}')

if errors:
    print(f'\nERRORS ({len(errors)}):')
    for e in errors:
        print(f'  {e}')
    sys.exit(1)
else:
    print('\nAll bundles conformant.')
