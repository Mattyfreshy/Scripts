
# Global Variables
watched = 'anime_watched.txt'
to_watch = 'anime_to_watch.txt'

def sort_txt(file: str, mode: str):
    # open file in mode
    with open(file, mode) as f:
        # store sorted list in lst
        lst = []
        for line in sorted(f):
            print(line, end='')
            lst.append(line)
        
        # clear txt file
        f.truncate(0)
        f.seek(0)
        
        # write updated sorted list to txt file
        for anime in lst:
            f.write(anime)
        
        
def main():
    sort_txt(to_watch, 'r+')

if __name__ == "__main__":
    main()