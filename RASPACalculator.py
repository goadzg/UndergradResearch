PLow = float(input('Enter the lowest pressure to be calculated (in Pa): '))
PHigh = float(input('Enter the highest pressure to be calculated (in Pa): '))
PInterval = float(input('Enter the pressure interval to be calculated (in Pa): '))
P = PLow
PList = [str(PLow)]
while P < PHigh: #Pressure list is created for later use
    P += PInterval
    PList.append(str(round(P,1)))
P=PLow
PString = str(PLow)
while P < PHigh: #Pressure string is created for copy-pasting into RASPA2 input file
    P += PInterval
    PString += ' '
    PString += str(round(P,1))
print(PList)
print(PString)

Continue = input('Do you want to use the above Pressure List to pull data from the DataPullingFolder? (Y/N): ')
if Continue == 'Y': #Now we'll make list for filenames for each pressure output file
    print('Filenames will look like "output_title_1.1.1_000000_pressure.data"')
    FilenameStart = input('Input the general part of the filename for all data points, up to and including the last underscore: ')
    N = len(PList)
    x = 0
    while x < N:
        if PList[x][-2:] == '.0':
            PList[x] = PList[x][0:(len(PList[x])-2)]
        x += 1
    x = 0
    Filepath = [None]*N
    while x < N: #Creates every file name with the input, the pressure #, and .data at the ending
        Filepath[x] = ['C:\\Users\\goadzg\\Desktop\\DataPullingFolder\\',FilenameStart,str(PList[x]),'.data']
        Filepath[x] = ''.join(Filepath[x])
        x += 1
    x = 0
    Results = [None]*N
    while x < N: #Runs every file through this
        File = open(Filepath[x],'r')
        FileText = File.readlines()
        y = 0
        while y < len(FileText): #Runs through each line of the given file
            if FileText[y][1:51] == 'Average loading absolute [cm^3 (STP)/gr framework]':
                z = 51
                StopZ = 0
                while z < len(FileText[y]) and StopZ == 0: #Runs through each character of the given line
                    if FileText[y][z] == '0' or FileText[y][z] == '1' or FileText[y][z] == '2' or FileText[y][z] == '3' or FileText[y][z] == '4' or FileText[y][z] == '5' or FileText[y][z] == '6' or FileText[y][z] == '7' or FileText[y][z] == '8' or FileText[y][z] == '9':
                        StartPoint = z
                        StopZ = 1
                        Results[x] = FileText[y][StartPoint:(StartPoint+12)]
                        Results[x] = str(Results[x])
                    z += 1
                y = 999999999999999
            y += 1
        File.close()
        x += 1
    FileX = open('C:\\Users\\goadzg\\Desktop\\DataPullingFolder\\X.txt','w')
    FileX.writelines("%s\n" % item  for item in PList)
    FileX.close()
    FileY = open('C:\\Users\\goadzg\\Desktop\\DataPullingFolder\\Y.txt','w')
    FileY.writelines("%s\n" % item  for item in Results)
    FileY.close()
    print('Results have been written into the two results files in the DataPullingFolder.')
else:
    print('"Y" not entered, ending program.')
    quit()
