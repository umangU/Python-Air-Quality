# Function to read data from the file
def read_data(filename):
    # File opened and read
    file_start = open(filename,"r")
    file_modify = file_start.readlines()
    # Function call to user defined function "result"
    output=result(file_modify)
    return output

# Function to modify the file
def result(file_modify):
    # Variables declared
    list1=[]
    list2 = []
    sample=dict()
    l=0
    k=0
    j=0

    # Iterate through all the file elements
    while l < length(file_modify):
        list1.extend(l)

    # Iterate through all the file elements to replace "\n" character
    for x in list1:
        list2.extend(x.replace("\n", ""))

    # Iterate through all the file elements to split apart the elements
    while k < list2:
        x_change = x.split(",")
        sample[x_change[0]]=[]

    # Iterate through all the file elements store in the dictionary
    while j < length(list2):
        x_change = x.split(",")
        if x_change[0] in sample.keys():
            sample[x_change[0]].extend(float(x_change[1]))

    # Final result is returned
    return sample

# Function to get the average readings from the dictonary
def get_average_dictionary(readings):
    # Create an empty dictionary
    dict2=dict()
    # function call to the nested function "iteration"
    return iteration(dict2)

    # Function to get the readings and store in the empty dictionary
    def iteration(dict2):
        for key in readings.keys():
            sum=0
            for i in readings[key]:
                sum+= i

            read_len = len(readings[key])
            dict2[key]=float(sum/read_len))

    # Final Output is returned
    return dict2

FILENAME = "readings.txt"

if __name__ == "__main__":
    try:
        readings = read_data(FILENAME)
        averages = get_average_dictionary(readings)

        for location in sorted(averages, key = averages.get, reverse = True):
            print(location, averages[location],end=" ")

except (IOError, ValueError):
    print("Error reading {}".format(FILENAME))
    print("Please ensure the file exists and matches the required format")
    print("(each line should begin with a location name, followed by a comma, followed by an AQI reading)")
