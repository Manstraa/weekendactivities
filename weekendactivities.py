def activities() :
  stud=input('Enter-1 If You are Student : ,  Enter-2 If You are Not Student : ')
  if stud==1 :
      aktivite=input('Enter-3 For Go to Soccer Match  :  ,  Enter-4 For Go to Cinema : ')
      if aktivite==3 :
          print('Price to Pay : 89 ')
      elif aktivite==4 :
          print ('Price to Pay : 25 ')
  elif stud==2 :
      aktivite = input('Enter-3 For Go to Soccer Match  :  ,  Enter-4 For Go to Cinema : ')
      if aktivite==3 :
        print('Price to Pay : 177 ')
      elif aktivite==4 :
          print('Price to Pay : 50 ')
print(activities())