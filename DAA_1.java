import java.util.*;

public class DAA_1 {
    static void fiboNonRecursive(int n) {
        int a = 0, b = 1;
        System.out.print("Fibonacci Series(Non Recursive):");
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int next = a + b;
            a = b;
            b = next;
        }
        System.out.println();
    }

    static int fiboRecursive(int n) {
        if (n <= 1)
            return n;
        return fiboRecursive(n - 1) + fiboRecursive(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number:");
        int n = sc.nextInt();

        fiboNonRecursive(n);

        System.out.print("Fibonacci Series (Recursive):");
        for (int i = 0; i < n; i++) {
            System.out.print(fiboRecursive(i) + " ");
        }
        sc.close();
    }
}