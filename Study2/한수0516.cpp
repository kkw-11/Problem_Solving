//https://www.acmicpc.net/problem/1065
#include <stdio.h>

int main() {
	//freopen("input.txt", "rt", stdin);
	int x,cnt=0, hundred,ten,one;
	scanf("%d", &x);

	if (x < 100) {
		printf("%d", x);
	}
	else {
		for (int i = 100; i <= x; ++i) {
			hundred = i / 100; //123 /100 = 1
			ten = (i % 100)/10; //123 % 100 = 23 /10 = 2 
			one = (i % 100) % 10;
			if (hundred - ten == ten - one)
				++cnt;
		}
		printf("%d", 99+cnt);
	}
	return 0;
}


// #include <stdio.h>

// int main()
// {
//     int N, count = 0;
//     scanf("%d", &N);
//     if (N < 100)
//         printf("%d\n", N);
//     else
//     {
//         for (int i = 111; i <= N; i++)
//         {
//             int i100, i10, i1;
//             i1 = i % 10;
//             i100 = i / 100;
//             i10 = (i / 10) % 10;

//             if (i10 - i100 == i1 - i10)
//                 count++;
//         }

     
//         printf("%d\n", 99 + count);
//     }
//     return 0;
// }