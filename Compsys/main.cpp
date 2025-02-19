#include <stdio.h>

void Hvezdicky(int pocet) {
  for (int i = 0; i < pocet; i = i + 2) {
    for (int g = 0; g < (pocet - i) / 2; g++) {
      printf(" ");
    }
    for (int j = 0; j < i; j++) {
      printf("*");
    }
    for (int g = 0; g < (pocet - i) / 2; g++) {
      printf(" ");
    }
    printf("\n");
  }
}
void HvezdickyZPole(int pole[], int delka) {
  for (int i = 0; i < delka; i++) {
    for (int j = 0; j < pole[i]; j++) {
      printf("*");
    }
    printf("\n");
  }
}
void Vyhlazeni(int pole[], int delka) {
  for (int i = 0; i < delka - 2; i++) {
    pole[i] = (pole[i] + pole[i + 1] + pole[i + 2]) / 3;
  }
  HvezdickyZPole(pole, delka);
}

void VerticalGraphWithSign(int pole[], int delka) {
  for (int i = 0; i < delka; i++) {
  }
}

int main() {
  printf("Hello World!\n");
  int temps[] = {12, 14, 9, 12, 15, 1, 15, 4, 21, 8, 13, 13, 8};
  int delka = sizeof(temps) / sizeof(int);
  HvezdickyZPole(temps, delka);
  printf("Teď to vyhladím!\n");
  Vyhlazeni(temps, delka);
}
