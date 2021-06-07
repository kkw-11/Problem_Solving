//5. 나이계산
#include<stdio.h>
int main() {
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	char ch[15] ;
	int year;
	int age;
	scanf("%s", ch);
	if (ch[0] != '0')
	{
		year = (ch[0]-48) * 10 + (ch[1]-48) + 1900;
		age = 2019 - year + 1;
		printf("%d ", age);
		if (ch[7] == '1')
			printf("M");
		else
			printf("W");
	}
	else {
		year = (ch[0]-48) * 10 + (ch[1]-48) + 2000;
		age = 2019 - year + 1;
		printf("%d ", age);
		if (ch[7] == '3')
			printf("M");
		else
			printf("W");
	}

	return 0;
}