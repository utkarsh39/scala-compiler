object program{
	def ncr(n:Int, r:Int):Int = {
		if(r > n || r < 0){
			return 0;
		}

		if(r == 0){
			return 1;
		}

		return ncr(n - 1, r) + ncr(n - 1, r - 1);
	}

	def main():Unit = {
		var m:Int = ncr(5,2);
	}
}