import pandas as pd

#df=pd.read_csv("data/amazon_books.csv")
#print(df.head())  #Ne arata primele inregistrari in baza de date 
#print(df.shape) #Ne arata numarul de linii si coloane
#print(df.dtypes) #Arata type-ul fiecarei coloane 
#print(df.describe()) #Arata statisticile (mean,std) de pe baza de date
#print(df["Name"].nunique()) #Arata din coloana "x" prin metoda nunique() valorile unice
#print(df["Author"].value_counts()) #Arata frecventa fiecarei inregistrari din coloana "X" prin metoda value_counts
#print(df["Author"].nunique()) #248 autori unici 
#print(df["Author"].value_counts()[:10]) #Primele 10 valori 
#print(df.isnull().sum()) #Verificat daca sunt valori nule pe coloane (nu sunt)
#print(df.sort_values(by="Reviews", ascending=False)[:10]) # Afisam primele 10 carti cu cele mai multe reviews cu dublicate
#print(df.drop_duplicates(subset="Name").sort_values(by="Reviews", ascending=False)[:10]) #top 10 cărți după numărul de reviews fără să repetăm aceeași carte pentru anii diferiți
#