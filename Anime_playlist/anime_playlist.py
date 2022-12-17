
# Global Variables
watched_file = 'anime_watched.txt'
to_watch_file = 'anime_to_watch.txt'

# Sort txt file based on first char of line
def sort_txt(file: str):
    # open file in mode
    with open(file, 'r+') as f:
        # store sorted list in lst
        lst = []
        for line in sorted(f):
            if not line.isspace():
                lst.append(line)
        
        # clear txt file
        f.truncate(0)
        f.seek(0)
        
        # write updated sorted list to txt file
        for anime in lst:
            f.write(anime.capitalize())

# Locate and remove 'anime'
# Return true if successful else false.
def search_and_remove(file: str, target: str):
    # open file in read mode
    with open(file, 'r+') as f:
        # capitalize target string
        target = target.capitalize()
        # read and store lines into list
        lines = f.readlines()
        # move file pointer back to beginning
        f.seek(0)
        # truncate file
        f.truncate()
        
        # locate line w/ target
        for line in lines:
            # if not target, write line to file
            if target != line:
                # write line to file
                f.write(line)
    
# Add 'anime' to to_watch_file
def add_to_watch(anime: str):
    # open file in read mode
    with open(to_watch_file, 'a+') as f:
        f.write('\n' + anime.capitalize() + '\n')
    
    sort_txt(to_watch_file)
            
        
def main():
    search_and_remove(watched_file, 'test')

if __name__ == "__main__":
    main()