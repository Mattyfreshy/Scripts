
# Global Variables
watched = 'anime_watched.txt'
to_watch = 'anime_to_watch.txt'

def sort_txt(file: str, mode: str):
    with open(file, mode) as r:
        lst = []
        for line in sorted(r):
            print(line, end='')
            lst.append(line)
        
        for anime in lst:
            r.write(anime)
        
        
def main():
    sort_txt(watched, 'w+')

if __name__ == "__main__":
    main()