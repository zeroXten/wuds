# Wake Up; Do Something

A collection of practical psychological insights to help you think straight and act real when the world gets weird.

## What is this?

This site presents 100+ evidence-based tips about human psychology, cognitive biases, and mental health. Each tip is designed to be immediately actionable and grounded in research.

## How to update the site

The site is generated from two main files:

- `tips.yaml` - Contains all the tips and their metadata
- `template.html` - The HTML template with styling and JavaScript

To regenerate the site:

```bash
python3 generate_tips.py
```

This reads the tips from `tips.yaml` and injects them into `template.html` to create `index.html`.

## Files

- `index.html` - Generated site (don't edit directly)
- `template.html` - HTML template 
- `tips.yaml` - Tips content and tags
- `generate_tips.py` - Build script
- `favicon.svg` - Site icon