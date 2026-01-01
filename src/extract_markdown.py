#extract_markdown.py
import re

def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result


def extract_markdown_links(text):
    result =  re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    print(result)
    return result

# Previous Version: 
# def extract_markdown_images(text):
#     result = re.findall(r"\!\[(\w+)\]\((.*)\)", text)
#     return result


# def extract_markdown_links(text):
#     result =  re.findall(r"\[(\w+)\]\((.*)\)", text)
#     return result

# Critic for own version:

#     (\w+) for alt text:
#         \w matches "word characters" (letters, numbers, and underscores).
#         + means "one or more" of those.
#         This is good for alt text like my_image_name or image123.
#         The limitation: What if your alt text is "My cool image"? \w+ won't capture the spaces! It would only capture "My" or "cool" or "image" separately, or fail to match altogether if it starts with a space.

#     (.*) for the URL:
#         . matches "any character" (except newline).
#         * means "zero or more" of those.
#         This is generally fine for the URL itself.
#         The limitation: The * quantifier is "greedy." This means it tries to match as much as it possibly can. In a very specific, malformed string (e.g., ![alt](url1) ![alt2](url2) where the ) of url1 was missing), a greedy .* might try to match all the way to the very last ) in the entire string, which wouldn't be what you want for a single image's URL.

# Notes for new version:

#     ([^\[\]]*) for alt text:
#         [ and ] define a "character set."
#         ^ inside a character set (like [^...]) means "match any character that is not in this set."
#         So, [^\[\]] means "any character that is not an opening square bracket [ or a closing square bracket ]."
#         * means "zero or more" of those.
#         The advantage: This allows alt text like "My cool image with spaces!" because it explicitly says "match anything until you hit a ]". This is much more flexible and accurate for real-world markdown.

#     ([^\(\)]*) for the URL:
#         Similarly, [^\(\)] means "any character that is not an opening parenthesis ( or a closing parenthesis )."
#         * means "zero or more" of those.
#         The advantage: This is a "non-greedy" approach. It says, "match any character until you hit a ( or )." This ensures that the URL capture doesn't accidentally run past its intended closing parenthesis ) if there are other parentheses later in the string (for example, if you had a very long string with multiple images or links). It also prevents the .* from being too greedy.
      