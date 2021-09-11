# https://www.hackerrank.com/challenges/permutation-equation/problem 

n = int(input())
p = list(map(int, input().split()))
b = [0]*51
for i in range(n):
    b[p[p[i] - 1]] = i + 1
for i in range(1,n+1) : print(b[i]) 
  
''' ALT C++ SOLUTION

for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		--x;
		p[x] = i;
	}

	for (int i = 0; i < n; ++i) {
		cout << p[p[i]] + 1 << "\n";
	} '''
