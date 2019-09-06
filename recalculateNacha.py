import time

oldNachaFile = open("testOldNacha.txt")
newNachaFile = open("testNEWNacha.txt","w")
"""Only deal with Credits and Debits
Batch Debits = 225
Bach Credits = 220

Credit (deposit) to checking account = 22
Prenote for credit to checking account = 23
Debit (withdrawal) to checking account = 27
Prenote for debit to checking account = 28
Credit to savings account = 32
Prenote for credit to savings account = 33
Debit to savings account = 37
Prenote for debit to savings account = 38

col 39,40 are amount for line items
"""
batchCredits = 0
batchDebits = 0
lineAmount = 0
batchAmount = 0
batchCreditTotalArr = []
batchDebitTotalArr = []
totalBatchCount = 1
inBatchCount = 0
batchCount = 0
blockCount = 0 #This is every record counted up
newLine9s = 0
batchRoutingTotal = 0
batchRoutingTotalsArr = []
bartSimpson = 0
fileEntryAddendaCount = 0
fileBatchRoutingTotalsArr = []

def truncate(f, n):
    print("truncating")
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    print('.'.join([i, (d+'0'*n)[:n]])) 


for line in oldNachaFile:
    # print("==========")
    line = str(line)
    # print(line)
    lineAmount = 0
    blockCount +=1
    #
    #Reset batch info at start of new batch
    #
    if line.startswith("52"):
        batchCredits = 0
        batchDebits = 0
        inBatchCount = 0
        batchRoutingTotal = 0
        batchCount += 1
        batchRoutingTotalsArr = []


    #
    #Setup Amounts for Debits or Credits
    #
    if line.startswith("627") or line.startswith("637"):
        lineAmount = line[37:39]
        batchDebits += int(lineAmount)
        inBatchCount +=1
        fileEntryAddendaCount +=1

        batchRoutingTotal = line[3:11:1]
        # print(batchRoutingTotal)
        batchRoutingTotal = int(batchRoutingTotal)
        batchRoutingTotalsArr.append(batchRoutingTotal)
        # print(batchRoutingTotalsArr)


    elif line.startswith("622") or line.startswith("632"):
        lineAmount = line[37:39]
        batchCredits += int(lineAmount)
        inBatchCount +=1
        fileEntryAddendaCount +=1

        batchRoutingTotal = line[3:11:1]
        batchRoutingTotal = int(batchRoutingTotal)
        batchRoutingTotalsArr.append(batchRoutingTotal)



    #
    # Setup batch Trailer
    #
    if line.startswith("82"):
        #Debits are from col 21-32
        batchDebitResultsOld = line[20:32:1]
        # print(batchDebitResultsOld)
        batchDebitResultsNew = 000000000000
        batchDebitResultsNew += batchDebits
        batchDebitResultsNew = str(batchDebitResultsNew).zfill(12)
        # print(batchDebitResultsNew)

        #credits are from 33-44
        batchCreditResultsOld = line[32:44:1]
        # print(batchCreditResultsOld)
        batchCreditResultsNew = 000000000000
        batchCreditResultsNew += batchCredits
        batchCreditResultsNew = str(batchCreditResultsNew).zfill(12)
        # print(batchCreditResultsNew)

        #update line counts
        lineCount = line[5:10:1]
        lineCount = 00000
        lineCount += inBatchCount
        lineCount = str(lineCount).zfill(5)
        # print(line)
        # print("lineCount")
        # print(lineCount)

        #don't forget to adjust the amount
        lineBegin = line[0:5:1]
        lineAfterCount=line[10:20:1]
        lineEnd = line[44:]
        # print(lineBegin)
        # print(lineAfterCount)
        # print(line)
        #Extradite these cols from the line and marry it with the new results
        
        
        batchRoutingTotal = 0
        rnum = 0
        print('===')
        while rnum < len(batchRoutingTotalsArr):
            batchRoutingTotal += batchRoutingTotalsArr[rnum]
            # print(batchRoutingTotal)
            rnum +=1
        print('batchRoutingTotal')
        print(batchRoutingTotal)
        fileBatchRoutingTotalsArr.append(batchRoutingTotal)
        batchRoutingTotal = str(batchRoutingTotal).zfill(10)
        batchRoutingTotal = str(batchRoutingTotal)
        # lenCheck = len(str(batchRoutingTotal))
        # lenCheck = int(lenCheck)
        # print(lenCheck)
        # if str(lenCheck) < '6':
        # import math
        # bartSimpson = (batchRoutingTotal * 1000) / 1000
        # print(bartSimpson)

        #Dont forget the total DONE
        batchCreditTotalArr.append(batchCredits)
        batchDebitTotalArr.append(batchDebits)
        # print("Credit")
        # print(batchCreditTotal)
        # print("Debit")
        # print(batchDebitTotal)
        # print(totalBatchCount)
        
        line=lineBegin + lineCount + batchRoutingTotal + batchDebitResultsNew + batchCreditResultsNew + lineEnd
        totalBatchCount +=1

    #
    # Setup File Trailer
    #
    if line.startswith("90"):
        # print(line)
        # print(batchCreditTotalArr)
        # print(batchDebitTotalArr)


        #File Debts
        fileBatchDebitResultsOld = line[31:43:1]
        #loop through batchDebitTotal array and add those numbers together
        d = 0
        batchDebitTotal = 0
        while d < len(batchDebitTotalArr):
            # print(batchDebitTotalArr[d])
            batchDebitTotal += batchDebitTotalArr[d]
            d += 1
        # print("New File debit Total:")
        # print(batchDebitTotal)
        fileBatchDebitResultsNew = 000000000000
        fileBatchDebitResultsNew += batchDebitTotal
        fileBatchDebitResultsNew = str(fileBatchDebitResultsNew).zfill(12)
        # print(fileBatchDebitResultsNew)


        #File Credits
        c = 0
        batchCreditTotal = 0
        while c < len(batchCreditTotalArr):
            # print(batchCreditTotalArr[c])
            batchCreditTotal += batchCreditTotalArr[c]
            c += 1
        # print("New File credit Total:")
        # print(batchCreditTotal)
        fileBatchCreditResultsOld = line[43:55:1]
        # print(fileBatchCreditResultsOld)
        fileBatchCreditResultsNew = 000000000000
        fileBatchCreditResultsNew += batchCreditTotal
        fileBatchCreditResultsNew = str(fileBatchCreditResultsNew).zfill(12)
        # print(fileBatchCreditResultsNew)


        #update line counts
        FilebatchCount = line[2:7:1]
        # print(FilebatchCount)
        FilebatchCount = 00000
        FilebatchCount += batchCount
        FilebatchCount = str(FilebatchCount).zfill(6)
        # print(line)
        # print("lineCount")
        # print(FilebatchCount)


        #Update block Count 
        """Block count:
        Total number of records (lines) in file divided by 10.
        if not evenly divisible, additional lines of 9s are added to fill out the block
        """
        isDivisible = blockCount % 10
        if isDivisible != 0:
            newLine9s = 10 - isDivisible
        blockCount += newLine9s
        # print(isDivisible)
        fileBlockCount = line[8:13:1]
        # print(fileBlockCount)
        fileBlockCount = 00000
        fileBlockCount += blockCount
        fileBlockCount = str(fileBlockCount).zfill(6)
        # print(line)
        # print("lineCount")
        print(fileBlockCount)


        #put it all together
        #fileEntryAddendaCount = line[13:21:1]
        fileEntryAddendaCount = str(fileEntryAddendaCount)
        fileEntryAddendaCount = str(fileEntryAddendaCount).zfill(8)

        # print(fileEntryAddendaCount)
        rnum = 0
        #fileEntryHash = line[21:31:1]
        fileEntryHash = 0
        # print('===')
        print('=-=-=-=')
        print(fileBatchRoutingTotalsArr)
        while rnum < len(fileBatchRoutingTotalsArr):
            fileEntryHash += fileBatchRoutingTotalsArr[rnum]
            # print(batchRoutingTotal)
            rnum +=1
        print('fileEntryHash')
        print(fileEntryHash)
        fileEntryHash = str(fileEntryHash).zfill(10)
        if (len(fileEntryHash) > 10):
            print('yes')
            fileEntryHash = fileEntryHash[1:]
        print(fileEntryHash)
        # fileReserved = line
        # fileLineBegin = line[0:5:1]
        # fileLineAfterCount=line[10:20:1]
        # fileLineEnd = line[44:]
        # print(fileLineBegin)
        # print(fileLineAfterCount)
        # line=lineBegin + lineCount + lineAfterCount + batchDebitResultsNew + batchCreditResultsNew + fileLineEnd + "\n"
        # print(line)
        # print(line)
        line = '9' + FilebatchCount + fileBlockCount +fileEntryAddendaCount+ fileEntryHash + fileBatchDebitResultsNew + fileBatchCreditResultsNew + '\n'
        # print(line)



    newNachaFile.write(line)
    time.sleep(.01)

if newLine9s != 0:
    newLines = 0
    while newLines < newLine9s:
        newNachaFile.write("9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n")
        newLines +=1



oldNachaFile.close()
newNachaFile.close()

