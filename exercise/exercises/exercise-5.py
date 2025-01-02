#bu bölümde kullanıcı bilgisayara numara girişinde bulunmaz ve numarasını aklında tutar
#bilgisayar bu numarayı tahmin etmeye çalışır
#bilgisayar kendi tahminini kullanıcıya sorar ve kullanıcı tahminin doğru olup olmadığı hakkında bilgi verir
#bilgisayar kullanıcının verdiği bilgiye göre tahminini günceller ve tekrar sorar
#bu işlem bilgisayar doğru tahmin yapana kadar devam eder
#bilgisayar kaç tahminde doğru tahmini yapmıştır kullanıcıya gösterilir
#bilgisayar her tahminini çıktı olarak terminale yazdırır

guess = 0
min = 0
max = 100

print("Please think of a number between 0 and 100!")
input("Press Enter to start...")

ans = "h"

while ans != "e":
    guess = (min + max) // 2
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'e' to indicate I guessed correctly.")
    if ans == "h":
        max = guess
    elif ans == "l":
        min = guess
    elif ans == "e":
        print("Game over. Your secret number was: " + str(guess))
    else:
        print("Sorry, I did not understand your input.")