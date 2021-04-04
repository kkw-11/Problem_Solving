#include <iostream>

int main()
{
	int a, b;
	int sum = 0;

	scanf_s("%d%d",&a,&b);


	for (int i = 1; i <= a; ++i) {
		if(i%b==0)
			sum += i;
	}

	printf("%d\n",sum);

}