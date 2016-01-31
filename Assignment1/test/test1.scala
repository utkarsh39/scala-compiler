object FactorialRecursion {
 
    def main(args: Array[String]) {
        println(factorial(5))
    }
 
    def factorial(n: Int): Int = {
      if (n == 0) 
          return 1
      else
          return n * factorial(n-1)
    }
}