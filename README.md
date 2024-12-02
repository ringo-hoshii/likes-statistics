# Description
**likes-statistics** - prints the number of likes under a specified YouTube video given as a single link argument or as a file with links separated by a new line

# Dependencies
pip:
- requests
- matplotlib *(not used, but imported)*

# Usage
To get the likes count from one video:  
`python3 main.py -s [LINK]`

To get the likes count for the list of videos:  
`python3 main.py -l [FILE_WITH_LINKS]`
