object main {
	def main():Unit = {
		var a:Array[Int] = Array[Int](1,2,3);
		var i:Int = 0;
		var j:Int = 0;

		if(i <= 3){
			a[i] = a[i] + 1;
		}
		
		if(i >= 2){
			a[i] = a[i] - 1;
		}
		else{
			a[i] = 1;
		}
	}
}
