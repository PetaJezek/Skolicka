#include <stdio.h>


#include "temps.h" // this file defines temperatures[] and no_value constants


//Tisknutí hvězd
void tiskMezer(int pocet)
{
	for (int i = 0; i < -1*pocet; i++)
	{
		printf(" ");
	}
};

void tiskHvezd(int pocet) {
	for (int i = 0; i < pocet; i++)
	{
		printf("*");
	}
}

int max(int a, int b) {
	if (a > b) {
		return a;
	}
	else {
		return b;
	}
}
int najdiMin(const int pole[], int delka) {

	int min = 0;

	for (int i = 0; i < delka; i++) {

		if (pole[i] != no_value && pole[i] < min) {
			min = pole[i];
		}
	}
	return min;

}
void tiskTeploty(int cislo, int min) 
{
	tiskMezer(max(min, min-cislo));
	tiskHvezd(-cislo);
	printf("|");
	tiskHvezd(cislo);
	printf("\n");
}
void tiskGrafuTeplot(const int pole[], int delka)
{
	int min = najdiMin(temperatures, delka);
	int last = 0;

	for (int i = 0; i < delka; i++) {
		
		if (pole[i] != no_value) 
		{
			last = pole[i];
		}
		tiskTeploty(last, min);
	}
}

int main(int argc, char** argv)
{
	int delka = sizeof(temperatures) / sizeof(temperatures[0]);
	tiskGrafuTeplot(temperatures, delka);
	return 0;
}