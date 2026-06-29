#!/usr/bin/env python3
import os
import glob

workspace = r'c:\Users\comp-itf\Desktop\website tabakvest'
proposals = ['proposal_1_minimalist', 'proposal_4_boutique', 'proposal_5_cinematic']

updated_count = 0
for proposal in proposals:
    pattern = f'https://tabakvest85.be/{proposal}/'
    replacement = './'
    
    for html_file in glob.glob(os.path.join(workspace, proposal, '*.html')):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern in content:
            updated = content.replace(pattern, replacement)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f'✓ {os.path.basename(html_file)}')
            updated_count += 1

print(f'\nUpdated {updated_count} files!')
