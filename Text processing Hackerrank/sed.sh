Day 5:
'Sed' command #1 sed -e 's/\bthe\b/this/'
'Sed' command #2 sed -e 's/[tT][Hh][Yy]/your/g'
'Sed' command #3 sed -e 's/[tT][Hh][Yy]/{&}/g'
'Sed' command #4 sed -e 's/[0-9]\{4\}\s/**** /1' | sed -e 's/[0-9]\{4\}\s/**** /1' | sed -e 's/[0-9]\{4\}\s/**** /1'
Command #5 sed -r -e 's/(.... )(.... )(.... )(....)/\4 \3\2\1/g'