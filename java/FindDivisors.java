// Count the number of divisors of a positive integer n.
// Random tests go up to n = 500000, but fixed tests go higher.

public class FindDivisors {

  public long numberOfDivisors(int n) {
    // TODO please write your code below this comment
    int dividend = 1;
    int divisors = 0;
    while (dividend <= n) {

      if (n % dividend == 0) {
        divisors += 1;
      }
      dividend++;
    }
    return divisors;
  }

  public static void main(String[] args) {
    FindDivisors object1 = new FindDivisors();
    System.out.println(object1.numberOfDivisors(30));
  }
}