#!/usr/bin/env python3
"""
Generate tips HTML from YAML data and template.
Usage: python generate_tips.py
"""

import yaml
import html


def load_tips(yaml_file="tips.yaml"):
    """Load tips data from YAML file."""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data['tips']


def generate_tip_html(tip):
    """Generate HTML for a single tip."""
    number = tip['number']
    keyword = html.escape(tip['keyword'])
    content = tip['content']  # Already contains HTML formatting
    
    # Handle optional tags field
    tags_attr = ''
    if 'tags' in tip and tip['tags']:
        tags_str = ' '.join(tip['tags'])
        tags_attr = f' data-tags="{html.escape(tags_str)}"'
    
    return f'''      <li class="tip-row" id="{number}" tabindex="0"{tags_attr}><span class="tip-number">{number}</span>
        <div class="tip"><span class="tip-strong">{keyword}</span> {content}</div>
      </li>'''


def generate_html(template_file="template.html", output_file="index.html"):
    """Generate the complete HTML file."""
    # Load tips data
    tips = load_tips()
    
    # Generate HTML for all tips
    tips_html = "\n".join(generate_tip_html(tip) for tip in tips)
    
    # Read template
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholder with generated tips HTML
    html_content = template.replace('{{TIPS_PLACEHOLDER}}', tips_html)
    
    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {output_file} with {len(tips)} tips")


if __name__ == "__main__":
    generate_html()