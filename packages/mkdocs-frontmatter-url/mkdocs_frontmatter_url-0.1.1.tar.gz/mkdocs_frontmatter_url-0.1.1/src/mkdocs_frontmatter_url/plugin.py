import re
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

log = logging.getLogger(__name__)

class FrontmatterUrlPlugin(BasePlugin):
    config_scheme = (
        ('button-text', config_options.Type(str, default='Visit link')),
        ('frontmatter-url-name', config_options.Type(str, default='url')),
    )

    def on_page_markdown(self, markdown, page, config, files):
        log.info(f"on_page_markdown triggered for page: {page.file.src_path}")
        log.info(f'Meta information:{page.meta}')
        url_selector = self.config['frontmatter-url-name']
        url = page.meta.get(f'{url_selector}')
        
        if not url:
            log.warning(f"No URL found in frontmatter for page: {page.file.src_path}")
            return markdown

        button_text = self.config['button-text']
        
        # CSS styles for the tag-like button
        css_styles = """
        <style>
        .frontmatter-url-tag {
            display: inline-block;
            padding: 5px 10px;
            background-color: #f0f0f0;
            color: #333;
            border-radius: 20px;
            text-decoration: none;
            font-size: 14px;
            margin-bottom: 20px;
            transition: background-color 0.3s;
        }
        .frontmatter-url-tag:hover {
            background-color: #e0e0e0;
        }
        .frontmatter-url-tag i {
            margin-right: 5px;
        }
        </style>
        """

        # Font Awesome link
        font_awesome_link = '<script src="https://kit.fontawesome.com/e147252cfa.js" crossorigin="anonymous"></script>'
        # font_awesome_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">'

        # Button HTML with icon
        button_html = f'<a href="{url}" class="frontmatter-url-tag" target="_blank"><i class="fas fa-comment-alt"></i>{button_text}</a>'

        # Combine all elements
        additional_html = f"<head>{css_styles}\n{font_awesome_link}\n</head>{button_html}\n\n"

        # Insert the additional HTML after the first heading
        pattern = r'^(#.*?\n)'
        if re.search(pattern, markdown, re.MULTILINE):
            markdown = re.sub(pattern, f'\\1\n{additional_html}', markdown, count=1, flags=re.MULTILINE)
        else:
            # If no heading is found, append to the end of the document
            markdown = f'\n{additional_html} + {markdown}'

        log.info(f"Markdown processed for page: {page.file.src_path}")
        return markdown
