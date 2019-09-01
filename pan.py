import pypandoc

output = pypandoc.convert_file('BST.pptx', 'docx', outputfile="somefile.docx", extra_args=['-V', 'geometry:margin=1.5cm', '--pdf-engine', '/usr/bin/xelatex'])
assert output == ""