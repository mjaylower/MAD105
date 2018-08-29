package com.company;

public class Main {

    public static void main(String[] args) {
	    int int1 = 56;
	    int int2 = 95;
	    int int3 = 256;

	    int resultsAddition = int1 + int2;
	    int resultSubtraction = int3 - int2;
		int resultsMultiplication = int1 * int3;
		float resultsDivision = (float) int1 / int2;
		double resultsRemaining = (double) int3 % int1;


	    System.out.printf("%d + %d = %d\n", int1, int2, resultsAddition);
		System.out.printf("%d - %d = %d\n", int3, int2, resultSubtraction);
		System.out.printf("%d * %d = %d\n", int1, int3, resultsMultiplication);
		System.out.printf("%d / %d = %f\n", int1, int2, resultsDivision);
		System.out.printf("%d / %d = remainder of %f\n", int3, int1, resultsRemaining);

		}
	}
