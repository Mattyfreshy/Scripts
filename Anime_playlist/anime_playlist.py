
# Global Variables
watched_file = 'anime_watched.txt'
to_watch_file = 'anime_to_watch.txt'

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

def search_txt(file: str, target: str) -> bool:
    # open file in read mode
    with open(file, 'r') as f:
        for line in f:
            if target.lower() == line.lower():
                return True
        return False
    
def add_to_watch(anime: str):
    # open file in read mode
    with open(to_watch_file, 'a+') as f:
        f.write('\n' + anime.capitalize() + '\n')
    
    sort_txt(to_watch_file)
            
        
def main():
    #sort_txt(to_watch_file)
    add_to_watch("test")

if __name__ == "__main__":
    main()