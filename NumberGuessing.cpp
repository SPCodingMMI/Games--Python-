#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

int main(){
    srand(time(NULL));
    bool GameOn = true;
    int WinningNumber = rand() % 10 +1; //Going from the range of 1-10
    int PlayerNumber;
    int LifeCounter = 3;

while(GameOn){
    cout << "Guess what number it is: ";
    cin >> PlayerNumber;


    if (PlayerNumber == WinningNumber){
        cout << "CONGRATULATIONS! THE NUMBER YOU GUESSED IS: " << WinningNumber; \
        GameOn = false;
    }
    else if ((PlayerNumber != WinningNumber) && (LifeCounter != 0)){
        LifeCounter -= 1;
        cout << "Try Again\n";
    }
    else if (LifeCounter == 0){
         cout << "YOU LOSE! THE NUMBER IS ACTUALLY: " << WinningNumber;
         GameOn = false;
        }
    }

    return 0;
}
