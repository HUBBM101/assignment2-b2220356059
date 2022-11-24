# RIZA ÇAKIR 2220356059

patient_data_list = []       # main list
text = []       # for reading function
outputs = " "       # for writing function
patients = []       # list only contains names
prob = 0        # for probability function
probPatient = []         # for probability function
outputFile = open("doctors_aid_outputs.txt", "w")       # opens file for writing


def reading():      # reading function
    inputFile = open("doctors_aid_inputs.txt", "r")     # opens file for reading
    global text
    text = inputFile.read().splitlines()        # reads file and splits every line


reading()       # runs reading function


def writing():
    outputFile.write(outputs)       # writes out outputs to the outputFile


def create():
    patient_data_list.append(patient)       # appends patient's list to the main list
    patients.append(patient[0])      # appends patient's name to name list
    global outputs
    outputs = "Patient {0} is recorded.\n".format(patient[0])       # output fot writing 
    writing()       # runs writing function


def remove():
    global outputs
    outputs = "Patient {0} is removed.\n".format(patient)       # output fot writing
    patient_data_list.pop(ind)
    patients.pop(ind)
    writing()       # runs writing function


def probability():
    ind = patients.index(lines[1])      # finds patients place in lists
    global probPatient
    probPatient = patient_data_list[ind]        # finds patient in the patient data list
    accuracy = float(probPatient[1])        # turns accuracy to float
    rate = probPatient[3].split("/")        # splits 4. element on the list
    sick = float(rate[0])       # turns 
    healthy = float(rate[1])
    global prob
    prob = 100*((sick*accuracy)/((sick*accuracy)+healthy*(1-accuracy)))         # Bayes' theorem
    prob = round(prob , 2)      # rounds risk to two decimal places
    global outputs
    outputs = "Patient {0} has a probability of %{1} having {2}.\n".format(probPatient[0] , str(prob) , probPatient[2])       # output fot writing


def recommendation():
    probability()       # runs probability function
    risk = (float(probPatient[5]))*100      # makes risk a float number
    global outputs
    if prob > risk:     # checks for prob/risk ratio
        outputs = "System suggest {} to have the treatment.\n".format(probPatient[0])       # output fot writing
    else:
        outputs = "System suggest NOT {} to have the treatment.\n".format(probPatient[0])       # output fot writing


def listing():
    global outputs
    outputs = f"{'Patient':<16} {'Diagnosis':<16} {'Disease':<16} {'Diseases':<16} {'Treatment':<16} {'Treatment':<16}\n"       # for table
    writing()       # runs writing function
    outputs = f"{'Name':<16} {'Accuracy':<16} {'Name':<16} {'Incidence':<16} {'Name':<16} {'Risk':<16}\n"       # for table
    writing()       # runs writing function
    outputs = "-"*95+"\n"       # for table
    writing()       # runs writing function
    for patient in patient_data_list        # gets every patients pwn list from main list
        outputs = f"{patient[0]:<16} {str(100*float(patient[1]))+'%':<16} {patient[2]:<16} {patient[3]:<16} {patient[4]:<16} {str(int(100*(float(patient[5]))))+'%':<16}\n"         # output for patient's information
        writing()       # runs writing function


for line in text:       # main loop

    lines = line.split(" ", 1)      # separets commands from others

    if "create" in lines:       # searchs for create

        if lines[1] in patients:         # searchs for duplication
            outputs = "Patient Hayriye cannot be recorded due to duplication.\n"      # output for duplication
            writing()       # runs writing function

        else:
            lines.remove("create")  # removes create from line
            patient = lines[0].split(", ")  # makes another list for patients
            create()  # runs create function

    elif "recommendation" in lines:         # searchs for recommendation

        if lines[1] in patients:        # checks for patient
            recommendation()        # runs recommendation function
            writing()       # runs writing function

        else:
            outputs = "Recommendation cannot be calculated due to absence.\n"      # output for absence
            writing()       # runs writing function

    elif "probability" in lines:        # searchs for probability

        if lines[1] in patients:        # checks for patient
            probability()       # runs probability function
            writing()       # runs writing function

        else:
            outputs = "Probability cannot be calculated due to absence.\n"      # output for absence
            writing()       # runs writing function

    elif "remove" in lines:         # searchs for remove

        if lines[1] in patients:
            patient = lines[1]  # gets patient's name
            ind = patients.index(patient)  # finds the patient's index
            remove()  # runs remove function

        else:
            outputs = "Patient {0} cannot be removed due to absence.\n".format(lines[1])
            writing()

    elif "list" in lines:       # searchs for list
        listing()       #  runs list function

