#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int cube[25];
bool check(int cube[25])
{

	int begin = cube[1];
	for (int i = 2; i <= 4; ++i)
		if (begin != cube[i])
			return false;
	begin = cube[5];
	for (int i = 6; i <= 8; ++i)
		if (begin != cube[i])
			return false;
	begin = cube[9];
	for (int i = 10; i <= 12; ++i)
		if (begin != cube[i])
			return false;
	begin = cube[13];
	for (int i = 14; i <= 16; ++i)
		if (begin != cube[i])
			return false;
	begin = cube[17];
	for (int i = 18; i <= 20; ++i)
		if (begin != cube[i])
			return false;
	begin = cube[21];
	for (int i = 22; i <= 24; ++i)
		if (begin != cube[i])
			return false;


	return true;
}
void one(int c[25])
{
	int temp1 = c[21], temp2 = c[23];
	c[21] = c[4];
	c[23] = c[2];

	c[4] = c[8];
	c[2] = c[6];

	c[6] = c[10];
	c[8] = c[12];

	c[12] = temp1;
	c[10] = temp2;
}
void reone(int c[25])
{
	one(c);
	one(c);
	one(c);
}

void two(int c[25])
{
	int temp1 = c[22], temp2 = c[24];
	c[22] = c[3];
	c[24] = c[1];

	c[3] = c[7];
	c[1] = c[5];

	c[7] = c[11];
	c[5] = c[9];

	c[11] = temp1;
	c[9] = temp2;
}
void retwo(int c[])
{
	two(c);
	two(c);
	two(c);
}
void three(int c[25])
{
	int temp1 = c[11], temp2 = c[12];
	c[11] = c[13];
	c[12] = c[15];

	c[13] = c[2];
	c[15] = c[1];

	c[2] = c[20];
	c[1] = c[18];

	c[20] = temp1;
	c[18] = temp2;
}
void rethree(int c[])
{
	three(c);
	three(c);
	three(c);
}
void four(int c[25])
{
	int temp1 = c[9], temp2 = c[10];
	c[9] = c[14];
	c[10] = c[16];

	c[14] = c[4];
	c[16] = c[3];

	c[4] = c[19];
	c[3] = c[17];

	c[19] = temp1;
	c[17] = temp2;
}
void refour(int c[])
{
	four(c);
	four(c);
	four(c);
}
void five(int c[25])
{
	int temp1 = c[19], temp2 = c[20];
	c[20] = c[24];
	c[19] = c[23];

	c[24] = c[16];
	c[23] = c[15];

	c[16] = c[8];
	c[15] = c[7];

	c[8] = temp2;
	c[7] = temp1;

}
void refive(int c[])
{
	five(c);
	five(c);
	five(c);
}
void six(int c[25])
{
	int temp = c[18], temp2 = c[17];
	c[18] = c[22];
	c[17] = c[21];

	c[22] = c[14];
	c[21] = c[13];

	c[13] = c[5];
	c[14] = c[6];

	c[5] = temp2;
	c[6] = temp;
}
void resix(int c[])
{
	six(c);
	six(c);
	six(c);
}
int main()
{
	for (int i = 1; i < 25; ++i)
		cin >> cube[i];

	int copy[25];
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	one(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}

	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];


	reone(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];


	two(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	retwo(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	three(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	rethree(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	four(copy);

	if (check(copy)) {
		cout << 1;
		return 0;
	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	refour(copy);

	if (check(copy)) {
		cout << 1;
		return 0;

	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	five(copy);

	if (check(copy)) {
		cout << 1;
		return 0;

	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	refive(copy);

	if (check(copy)) {
		cout << 1;
		return 0;

	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	six(copy);

	if (check(copy)) {
		cout << 1;
		return 0;

	}
	for (int i = 1; i < 25; ++i)
		copy[i] = cube[i];

	resix(copy);

	if (check(copy)) {
		cout << 1;
		return 0;

	}
	cout << 0;
	return 0;
}

