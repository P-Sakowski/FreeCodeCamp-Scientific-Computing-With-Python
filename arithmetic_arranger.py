def arithmetic_arranger(problems, printResult = False):

  breakSize = 4
  firstLine = ""
  secondLine = ""
  thirdLine = ""
  fourthLine = ""

  for problem in problems:
    if(problems.index(problem) > 4):
      errorMessage = "Error: Too many problems."
      return errorMessage
    
    params = problem.split()

    if(params[1] != '+' and params[1] != '-'):
      errorMessage = "Error: Operator must be '+' or '-'."
      return errorMessage

    if(params[0].isdigit() == False or params[2].isdigit() == False):
      errorMessage = "Error: Numbers must only contain digits."
      return errorMessage

    if(len(str(params[0])) > 4 or len(str(params[2])) > 4):
      errorMessage = "Error: Numbers cannot be more than four digits."
      return errorMessage
    
    paramALength = len(str(params[0]))
    paramBLength = len(str(params[2]))
    lineLength = max([paramALength, paramBLength])+2
    params.append(lineLength)

    #first line
    firstLine += ((lineLength - paramALength) * " ") + str(params[0])
    if(problems.index(problem) < len(problems)-1):
      firstLine += breakSize * " "

    #second line
    secondLine += str(params[1]) + ((lineLength - paramBLength - 1) * " ") + str(params[2])
    if(problems.index(problem) < len(problems)-1):
      secondLine += breakSize * " "

    #third line
    thirdLine += lineLength * "-"
    if(problems.index(problem) < len(problems)-1):
      thirdLine += breakSize * " "

    #fourth line
    if(params[1] == '+'):
      result = int(params[0]) + int(params[2])
    else:
      result = int(params[0]) - int(params[2])
    fourthLine += ((lineLength - len(str(result))) * " ") + str(result)
    if(problems.index(problem) < len(problems)-1):
      fourthLine += breakSize * " "

  arranged_problems = firstLine + "\n" + secondLine + "\n" + thirdLine
  if(printResult ==  True):
    arranged_problems += "\n" + fourthLine

  return arranged_problems