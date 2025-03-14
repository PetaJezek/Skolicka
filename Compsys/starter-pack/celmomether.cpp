#include <stdio.h>

#include "temps.h" // this file defines temperatures[] and no_value constants

//Tisknutí hvězd

void tiskHvezd(int cislo, int min){
	return;
}
void tiskMezer(int cislo, int min){
	return;
}
void tisk(int cislo, int min){ 

	for (int i = -min; i < -cislo; i++)
	{
		/* code */
	}
		
}
int najdiMin(const int pole[], int delka){
	int min = 0;
	for(int i = 0; i < delka; i++){
		if(pole[i]!= no_value && pole[i]< min){
			min = pole[i];
		}
	}
	return min;
}
void logika(const int pole[], int delka, int min)
{
	int last = 0;
	for(int i = 0; i < delka; i++){
		if(pole[i] == no_value){
			tisk(last, min);
		}
		else{
			tisk(pole[i],min);
			last = pole[i];
		}
	}
}


int main(int argc, char **argv)
{
	int delka = sizeof(temperatures) / sizeof(temperatures[0]);
	logika(temperatures, delka, najdiMin(temperatures,delka));

	// Here goes your code, but do not forget to decompose it to functions...
	
	return 0;
}
