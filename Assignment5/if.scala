object program {
	def gcd(a:Int, b:Int):Int = {
		var g:Int = 0;

		if (a < b){
			a = a + b;
			b = a - b;
			a = a - b; 
		}

		if(b == 0){
			g = a;
		}
		else{
			g = a % b;

			if(g != 0){
				g = gcd(b,a%b);
			}
		}

		return g;
	}

	def main():Unit = {
		var g:Int = gcd(4,10);
	}
}
