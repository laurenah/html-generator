# imports
import os, argparse

parser = argparse.ArgumentParser(description="Generate a basic HTML template")
parser.add_argument("-n", type=str, nargs='?', help="the name of the html file to be generated, defaults to index", const=1, default='index')
args = parser.parse_args()

with open(args.n + '.html', 'w') as fp:
    pass
    fp.write("<!doctype html>\n<html lang='en'>\n\n<head>\n\t<meta charset='utf-8'>" + 
    "\n\t<title>TITLE HERE</title>\n\t<meta name='description' content=''>" +
    "\n\t<meta name='author' content='author_name'>\n\t<link rel='stylesheet' href='css/styles.css'>" +
    "\n</head>\n\n<body>\n\n</body>\n\n</html>")