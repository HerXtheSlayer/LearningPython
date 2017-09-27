import os
import sys
import re

walk_dir = os.getcwd()

print('walk_dir = ' + walk_dir)

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)
            file_path_rel = os.path.join(subdir, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path_rel))
            
            SearchString=re.compile(r"^(.+)\nParseRule",re.MULTILINE)
            #rep1.replace(SearchString,
             print(   '''Name: test-unl-import
Path: %r
Version: "1"
Catalog: "unl"
Description:
OperationGuide:
ParseRule''') % file_path_rel


            #with open(file_path, 'rb') as f:
            #    f_content = f.read()
            #    list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
            #    list_file.write(f_content)
            #    list_file.write(b'\n')
