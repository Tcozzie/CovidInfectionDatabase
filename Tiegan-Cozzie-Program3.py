# --------------------------------------
# CSCI 127, Program 3                  |
# October 13, 2021                       |
# Tiegan  Cozzie                            |
# --------------------------------------
file=open("covid.csv","r", encoding="ISO-8859-1")

#produces the average infection rate reported per 100,000 people
def ave_infection_rate(file):
    file=open("covid.csv","r", encoding="ISO-8859-1")
    count=0
    count2=0
    file.readline()
    for line in file:
        line_list=line.split('"')
        # Adds up all the infections
        count+=float(line_list[19])
        count2+=1
        # Divides all the infections with how many lines are within the doc
    count=count/count2
    return count

# Produces a txt file with the countries and their population with deisred name provided by the user
def countries_in_study(file,save_as):
    file=open("covid.csv","r", encoding="ISO-8859-1")
    # File that the information will be writing too
    new_file=open(save_as,"w")
    # List to prevent the same country printing twice in the file
    picked=[]
    # List for the country and popluation to be put into.. *Will be pulling info from this list*
    alphaList=[]
    file.readline()
    for line in file:
        line_list=line.split('"')
        # Makes sure that only countries with a positive population can be within the list
        if int(line_list[15]) >1:
            # Makes sure there is no country printed twice
           if line_list[11] not in picked:
               picked.append(line_list[11])
               # Adds population and country to alphaList
               alphaList.append([int(line_list[15]),line_list[11]])
    # Sorts the population in each country greatest to least
    alphaList.sort(reverse=True)
    count=0
    # Gets the information ready to be written into the new file created by the user
    # Indexing into each list [pop,country] and sorting it
    for x in alphaList:
        count+=1
        country=x[1]
        population=str(x[0])
        new_file.write(str(count).ljust(1)+" "+country.ljust(80)+population+"\n")
    new_file.close()

# Identifies and counts the countries deaths specified by the user
def deaths_in_country(file,country):
    file=open("covid.csv","r",encoding="ISO-8859-1")
    count=0
    file.readline()
    for line in file:
        line_list=line.split('"')
        # Checks if the country is the same as the users desired country
        if line_list[11]==country:
            # Counts the deaths of the country
            count+=int(line_list[9])
    return count


# --------------------------------------

def main(file_name):
    
    print("Global data collected between Jan 1 - Nov 5, 2020".center(50))
    infections = ave_infection_rate(file_name)
    print('*' * 50)
    print("Fortnightly cases reported per 100,000 people,\n(global average): ", end="")
    print(ave_infection_rate(file_name))

    print('*' * 50)
    user_input = input("Save list countries? ('y' for yes) : ")
    if user_input.lower() == 'y':
        save_as = input("Save File As: ")
        save_as += ".txt"
        countries_in_study(file_name, save_as)
        print("File saved as", save_as)

    print('*' * 50)
    country = input("Enter a country in the dataset: ")
    num = deaths_in_country(file_name, country)
    print("The data reports {:d} covid deaths in {}.".format(num, country))

    print('*' * 50)


# --------------------------------------

main(file)
