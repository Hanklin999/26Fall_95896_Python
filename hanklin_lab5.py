# 2026 Fall 95896
# Student: Hank Lin
# Andrew ID: hanklin


'''
1. Read the file and create a list named movieList using the
with open('filename here', 'r') as f:
<your code here>
Store each movie as a dictionary containing:
{
"id": ...,
"name": ...,
"year": ...,
"country": ...,
"genres": [...]
}
'''

movieList = []

with open('movies.tsv', 'r') as f:
    for line in f:
        parts = line.split("\t")
        
        movieID = int(parts[0].strip())
        name    = parts[1].strip().replace('"', '') #clean quotes
        year    = int(parts[2].strip())
        country = parts[3].strip().replace('"', '') #clean quotes
        genres = [g.strip().replace('"','') for g in parts[4:] if g.strip() != '']
      
        movie = {
            "id": movieID,
            "name": name,
            "year": year,
            "country": country,
            "genres": genres}
        
        movieList.append(movie)

''' a. Display the total number of movies. '''
print(len(movieList))

'''b. Display the first five movies.'''
print(movieList[:5])


'''c. Display the oldest movie in the dataset.'''
oldest = min(movieList, key = lambda movie:movie["year"])
print(oldest)


'''d. Display the newest movie in the dataset.'''   
newest = max(movieList, key = lambda movie:movie["year"])
print(newest)        

    
#%%
'''
2. Write a function named createMovieDictionary(filename). 
The function should create and return a dictionary
where the key is the movie title and the value is the movie dictionary.
Store the returned dictionary in movieDict.
'''

def createMovieDictionary(filename) -> dict:
    movieDict = {}
    
    with open(filename, "r") as f:
        for line in f:
            parts = line.split("\t")
            
            movieID = int(parts[0].strip())
            name    = parts[1].strip().replace('"', '') #clean quotes
            year    = int(parts[2].strip())
            country = parts[3].strip().replace('"', '') #clean quotes
            genres  = [g.strip().replace('"','') for g in parts[4:]  if g.strip() != '']
          
            movie = {
                "id": movieID,
                "name": name,
                "year": year,
                "country": country,
                "genres": genres}
        
            movieDict[movie["name"]] =movie
    return movieDict

movieDict = createMovieDictionary("movies.tsv")

'''
Using a while loop:
a. Prompt the user for a movie title.
b. Display all information about that movie.
c. Print "Not found" if the movie does not exist.
d. Continue until the user enters "Done".
'''

request = input("Enter movie title: ")

while request != "Done":
    if request in movieDict:
        print(movieDict[request])
    else:
        print("Not found")

    request = input("Enter movie title: ")



#%%
'''
3. Create a set named genreSet. Read the file and insert every genre into the set. After processing the file:
'''

genreSet = set()

with open("movies.tsv", "r") as f:
    for line in f:
        parts = line.split("\t")
            
        genres  = [g.strip().replace('"','') for g in parts[4:] if g.strip() != '']
        
        
        for genre in genres:
            genreSet.add(genre)
  
'''a. Display the total number of unique genres.'''
print(len(genreSet))

'''b. Convert the set into a sorted list named genreList.'''
genreList = sorted(genreSet)
print(genreList)

'''c. Display all genres alphabetically.'''
for genre in genreList:
    print(genre)
            
'''d. Display the first and last genre alphabetically.'''       
print(genreList[0])
print(genreList[-1])
# print(genreList)




#%%
'''
4. Create a dictionary named yearDict.
The key should be the movie year.
The value should be a list of all movies released during that year. 
'''

yearDict = {}

for movie in movieList:
    year = movie['year']
    
    if year not in yearDict:
        yearDict[year] = []
    
    yearDict[year].append(movie["name"])

'''a. Display the number of unique years.'''
# print(yearDict)
print(len(yearDict))


'''b. Display the year with the most movies.'''
most = max(yearDict, key = lambda year :len(yearDict[year]))
print(most)

'''c. Display the first ten movies from that year.'''
print(yearDict[most][:10])

'''d. Allow the user to search for a year and display all movies from that year.'''


yearSearch = int(input("Enter a Year: "))

while yearSearch != 0:
    if yearSearch in yearDict:
        print(yearDict[yearSearch])
    else:
        print("Not found")
        
    yearSearch = int(input("Enter a Year: "))