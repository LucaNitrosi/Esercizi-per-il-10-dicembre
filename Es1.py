Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> stringa = input("Inserisci una parola per verificare se è palindroma:\n")
stringa2 = stringa[::-1]
if stringa == stringa2:
   print ("La parola è palindroma")
else:
   print ("La parola non è palindroma")
