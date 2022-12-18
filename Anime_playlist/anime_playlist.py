import random

# Global Variables
watched_file = 'anime_watched.txt'
to_watch_file = 'anime_to_watch.txt'
watching_file = 'anime_watching.txt'

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
    
# Add 'anime' to file
def add_to_file(file:str, anime: str):
    # open file in read and append mode
    with open(file, 'a+') as f:
        f.write('\n' + anime.capitalize() + '\n')
    
    sort_txt(file)
            
# Remove from watched if in list and add to watched file
def watched(anime:str):
    add_to_file(watched_file, anime)
    search_and_remove(to_watch_file, anime)
        
# randomizer for choosing a random anime to watch from watched list
def to_watch_random():
    with open(to_watch_file, 'r') as f_in:
        with open(watching_file, 'w') as f_out:
            watch_lst = f_in.readlines()
            # get random num within range [0,list length]
            rand_num = random.randint(0, len(watch_lst)-1)
            # print output and write to output file
            print(watch_lst[rand_num])
            f_out.write(watch_lst[rand_num])
        
def main():
    add_to_file(to_watch_file, 'Wotakoi')

if __name__ == "__main__":
    main()