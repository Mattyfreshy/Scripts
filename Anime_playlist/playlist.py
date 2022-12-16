
# Global Variables
watched = 'anime_watched.txt'
to_watch = 'anime_to_watch.txt'

def sort_txt(file: str, mode: str):
    with open(file, mode) as r:
        lines = []
        for line in sorted(r):
            print(line, end='')
        
        r.write(line)
        
        
def main():
    sort_txt(watched, 'w+')

if __name__ == "__main__":
    main()