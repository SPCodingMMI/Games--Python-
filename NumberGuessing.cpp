#include <iostream>
#include <cstdlib>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main(){
    srand(time(NULL));
    bool GameOn = true;
    int WinningNumber = rand() % 10 +1; //Going from the range of 1-10
    int PlayerNumber;
    int Options;
    int LifeCounter = 3;

while(GameOn){
    cout << "WELCOME TO NUMBER GUESSING\n";
    cout << "1. SURVIVAL MODE\n";
    cout << "2. TRIAL MODE\n";
    cout << "3. EXIT GAME\n";
    cout << "SELECT YOUR MODE\n";
    cin >> Options;

    switch (Options){
        case 1: //Survival Mode

        case 2: //Trial Mode

        case 3: //Exit Game

        default: //Input Errors
            while ((Options <= 0) || (Options > 3)){
                system("cls");
                cout << "WELCOME TO NUMBER GUESSING\n";
                cout << "1. SURVIVAL MODE\n";
                cout << "2. TRIAL MODE\n";
                cout << "3. EXIT GAME\n";
                cout << "SELECT YOUR MODE\n";
                cout << "Please pick between 1-3: ";
                cin >> Options;
            }
    }


    // cout << "Guess what number it is: ";
    // cin >> PlayerNumber;


    // if (PlayerNumber == WinningNumber){
    //     cout << "CONGRATULATIONS! THE NUMBER YOU GUESSED IS: " << WinningNumber;
    //     GameOn = false;
    // }
    // else if ((PlayerNumber != WinningNumber) && (LifeCounter != 0)){
    //     LifeCounter -= 1;
    //     cout << "Try Again\n";
    // }
    // else if (LifeCounter == 0){
    //      cout << "YOU LOSE! THE NUMBER IS ACTUALLY: " << WinningNumber;
    //      GameOn = false;
    //     }
    // }
}
    return 0;
}
