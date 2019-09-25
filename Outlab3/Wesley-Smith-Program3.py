# ---------------------------------------
# Wesley Smith
# CSCI 127, Joy and Beauty of Data
# Program 3: Music CSV Library
# ---------------------------------------
# This program takes a comma separated list
# and depending on what the user's choice is
# it will give the user the information they
# choose to look up.
# ---------------------------------------

def menu():
    print()
    print("1. Identify longest song.")
    print("2. Identify number of songs in a given year.")
    print("3. Identify all songs by a given artist.")
    print("4. Compare two artists and see who produced more songs.")
    print("5. Quit.")

def longest_song(file):
    fileref = open(file,'r')

    # Set up our new lists to grab the duration values and song titles that match the greatest duration value
    all_song_lengths = []
    max_titles = []

    # Skips the first title line of the data
    next(fileref)
    
    for line in fileref:
        values = line.split(',')
        # Grabs all the song durations and creates a list to sort by max and find the highest duration value
        all_song_lengths.append(float(values[9]))
        max_length = round(max(all_song_lengths))

        # If the rounded duration value for each line is equal to the max length of our songs, we grab the song title of that line on [-2]
        if max_length == round(float(values[9])):
            max_titles.append(values[-2])
        
    print("\n" + "Title:", max_titles[-1])
    print("Length to the nearest second:",max_length)

def songs_by_year(year, file):
    count = 0
    fileref = open(file, 'r')
    num_year = str(year)
    for line in fileref:
        values = []
        values = line.split(',')
        # Easier to grab the values by reversing the list than dealing with the comma split on [15]
        values.reverse()
        # Year becomes the first value [0] in our newly reversed list and what we are searching for
        search_year = values[0]
        search_year = search_year.strip('\n')

        if num_year == search_year:
            count = count + 1
    print('')
    print("The number of songs from", str(year), "is" , str(count))
    fileref.close()

def all_songs_by_artist(art, file):
    fileref = open(file, 'r')
    print('')
    print('Songs In Alphabetical Order')
    print('---------------------------')
    # Create a blank list to add songs by the artist to
    all_songs = []
    for line in fileref:
        values = line.split(',')
        # If the searched artist input is the same as the index value at [2], it gets appended to our blank list all_songs
        if values[2].lower() == art:
            all_songs.append(values[-2])
    # Sorts all the songs into alphabetical order before printing them
    all_songs.sort()

    for i, value in enumerate(all_songs, 1):
        print("{}. {}".format(i, value))
        
    print('---------------------------')    
    print('')

# This function takes the user input of two different artists,
# compares the number of songs created and tells us who produced more songs
def who_has_more_songs(one, two, file):
    fileref = open(file, 'r')
    print('')
    count_one = 0
    count_two = 0
    for line in fileref:
        values = line.split(',')
        # Checks for the artists name and counts the number of songs by each of them
        if values[2].lower() == one:
            count_one = count_one + 1
        if values[2].lower() == two:
            count_two = count_two + 1
    # Compares each artists number of songs        
    if count_one > count_two:
        print(one.title() , "produced more songs than", two.title())
        print("They produced", str(count_one), "songs total while", two.title(), "produced", str(count_two))
    elif count_two > count_one:
        print(two.title() , "produced more songs than", one.title())
        print("They produced", str(count_two), "songs total while", one.title(), "produced", str(count_one))
    else:
        print("Both", one.title(),"and", two.title(), "produced", count_one, "songs")
# --------------------------------------

def main():
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            longest_song("music.csv")
        elif (choice == 2):
            year = int(input("Enter desired year: "))
            songs_by_year(year, "music.csv")
        elif (choice == 3):
            artist = input("Enter name of artist: ").lower()
            all_songs_by_artist(artist, "music.csv")
        elif (choice == 4):
            artist_one = input("Enter the first artist's name: ").lower()
            artist_two = input("Enter the second artist's name: ").lower()
            who_has_more_songs(artist_one, artist_two, "music.csv")
        elif (choice != 5):
            return

# --------------------------------------

main()
