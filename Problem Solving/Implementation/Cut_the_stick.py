# https://www.hackerrank.com/challenges/cut-the-sticks/problem

n = int(input())
arr = list(map(int, input().split()))
x = sorted(set(arr))

for i in x:
    print(n)
    c = arr.count(i)
    n = n - c
    
''' ALT JAVA SOLUTION

public class Solution {

	static void solve() throws IOException {
		int n = nextInt();
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = nextInt();
		}
		Arrays.sort(a);
		for (int i = 0; i < n;) {
			int j = i;
			while (j < n && a[j] == a[i]) {
				j++;
			}
			out.println(n - i);
			i = j;
		}
	}
'''
