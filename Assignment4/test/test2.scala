
object BinarySearch {
  def sorta(a: Array[Int]) {

      val t = a[i];
      def sort1(a: Array[Int]) = {

      def swap(i: Int, j: Int) = {
        val t = a[i]; 
        a[i] = a[j]; 
        a[j] = t;
      }

    def println(ar: Array[Int]) = { }


    } 
  }

  def binarySearch(a: Array[Int]){
    
    if (vs.length == 0) return false;
    var left: Int = 0;
    var right: Int = vs.length - 1;
    var mid: Int = 0;
    while (left != right) {
     
      mid = left + (right - left) / 2;
      if (v <= vs[mid])
        right = mid;
      else
        left = mid + 1;
    }
    return vs[left] == v;
  }
  def binarySearchNewIndex(v: Int, vs: Array[Int]): Boolean = {
    
    if (vs.length == 0) return false;
    var left: Int = 0;
    var right: Int = vs.length;
    var mid: Int = 0;
    while (right - left != 1) {
      
      mid = left + (right - left) / 2;
      if (v < vs[mid])
        ;
      else
        left = mid;
    }
    return vs[left] == v;
  }
}