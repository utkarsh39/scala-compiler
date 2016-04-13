object main {
	def main():Unit = {
		var i:Int = 0;
		var sum:Int = 0;

		for(i <- 0 to 100){
			sum += i;
		}
	}
}