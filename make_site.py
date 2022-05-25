import markdown as md
from glob import glob
import os

def get_text_from_file(fname):
    with open(fname,'r', encoding='utf8', errors='ignore') as f:
        text_from_file = f.read()
    return text_from_file

def main():
    # this should build your site
    files_to_convert = glob(r"pages/*.md")
    for mdfile in files_to_convert:
        # text_from_file = get_text_from_file(mdfile)
        try:
            new_name = os.path.basename(mdfile)
            new_name = new_name[:-3] + ".html"
            md.markdownFromFile(input=mdfile, output=new_name, extensions=['tables','attr_list','wikilinks'])
        except Exception as e:
            print(f"Failed on page -{mdfile}- ; Exception was: {e}")

if __name__ == "__main__":
    main()

