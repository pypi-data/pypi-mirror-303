import subprocess
from subprocess import PIPE
import tempfile
import argparse


class CssStyle:
    data = "body,li{color:#000}body{line-height:1.4em;max-width:42em;padding:1em;margin:auto}li{margin:.2em 0 0;padding:0}h1,h2,h3,h4,h5,h6{border:0!important}h1,h2{margin-top:.5em;margin-bottom:.5em;border-bottom:2px solid navy!important}h2{margin-top:1em}code,pre{border-radius:3px}pre{overflow:auto;background-color:#f8f8f8;border:1px solid #2f6fab;padding:5px}pre code{background-color:inherit;border:0;padding:0}code{background-color:#ffffe0;border:1px solid orange;padding:0 .2em}a{text-decoration:underline}ol,ul{padding-left:30px}em{color:#b05000}table.text td,table.text th{vertical-align:top;border-top:1px solid #ccc;padding:5px}"
    path = None
    @staticmethod
    def get_file():
        if CssStyle.path is None:
            CssStyle.path = tempfile.mktemp(suffix=".css")
            with open(CssStyle.path, "w") as f:
                f.write(CssStyle.data)
        return CssStyle.path
    
class HTML:

    @staticmethod
    def remove_css_link_from_html(html_file: str):
        with open(html_file, "r") as f:
            content = f.read()
        output = []
        for line in content.split("\n"):
            if not line.startswith('  <link rel="stylesheet"'):
                output.append(line)
        with open(html_file, "w") as f:
            f.write("\n".join(output))



    @staticmethod
    def generate_html_with_pandoc(title: str, input_file: str, output_file: str, enable_latex: bool = True):
        fulltitle = title.replace('!', '\\!').replace('?', '\\?')
        cmd = ["pandoc", input_file, '--css', CssStyle.get_file(), '--metadata', 'pagetitle=' + fulltitle,
            '-s', '-o', output_file]
        if enable_latex:
            cmd.append("--mathjax")
        try:
            p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate()
            if stdout != "" or stderr != "":
                print(stdout)
                print(stderr)
            HTML.remove_css_link_from_html(output_file)

        except Exception as e:
            print("Erro no comando pandoc:", e)
            exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate HTML file from markdown file.')
    parser.add_argument('input', type=str, help='Input markdown file')
    parser.add_argument('output', type=str, help='Output HTML file')
    parser.add_argument('--no-latex', action='store_true', help='Disable LaTeX math rendering')
    parser.add_argument('--title', type=str, default="Problema", help='Title of the HTML file')
    args = parser.parse_args()
    HTML.generate_html_with_pandoc(args.title, args.input, args.output, not args.no_latex)
