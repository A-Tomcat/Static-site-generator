from markdown_to_html_node import markdown_to_html_node
import re, os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError(f"No h1 Header in Markdown Text!")

def generate_page(from_path = "content/index.md", template_path = "template.html", dest_path = "public/index.html"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    from_content = ""
    template_content = ""
    with open(from_path, "r") as file:
        from_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()
    title_to_be = extract_title(from_content)
    from_html = markdown_to_html_node(from_content).to_html()
    
    template_content = template_content.replace(r"{{ Title }}", title_to_be)
    template_content = template_content.replace(r"{{ Content }}", from_html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as page:
        page.write(template_content)