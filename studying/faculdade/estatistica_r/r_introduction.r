#dataset from titanic survivors

install.packages("titanic") 
library(titanic)
data("titanic_train")
fix(titanic_train)

#visualizing names
names(titanic_train)
titanic_train$Survived

#how many passengers survive? the function table will create a descriptive table with the frequency of each category
#the values for 0 are not survivors and for 1 for survivors
table(titanic_train$Survived)

#now, let's do the same, but using percentage
prop.table(table(titanic_train$Survived))

#as we know, women and children had priority to be saved. Let's analyze this
homens=titanic_train[titanic_train$Sex == "male", ]
mulheres=titanic_train[titanic_train$Sex == "female", ]

prop.table(table(homens$Survived))
prop.table(table(mulheres$Survived))
