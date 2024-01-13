# Description
**likes-statistics** - it's the script that prints number of likes under specified YouTube video given as argument or from the file in which each line is a link

# Dependencies
pip:
- requests
- matplotlib *(omitted, but required)*

# Usage
To get likes count from one video:  
`python3 main.py -s [LINK]`

To get likes count for the list of videos:  
`python3 main.py -l [LINKS_FILE]`
