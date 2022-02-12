print("GWeb v1.0")
import os
print("Setting up...")
os.system("pip install gh-md-to-html colorama")
print(Fore.YELLOW + "Note: GWeb only generates files in GFM format." + Style.RESET_ALL)
cd = os.path.dirname(os.path.realpath(__file__))
import glob
files = glob.glob(cd + "/*.md")
import gh_md_to_html
for i in files.nditer(b):
    open(i.replace('.md', '.html')
    print("Generated " + i + ".")
