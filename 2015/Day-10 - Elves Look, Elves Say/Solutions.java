public class Solutions {
    public static void main(String[] args) {
        String test1 = "211";
        String test2 = "1";
        String test3 = "11";
        String test4 = "21";
        String test5 = "1211";
        String test6 = "111221";
        String test7 = "312211";

        String input = "1321131112";

        System.out.println("211->next: " + generateNextString(test1));
        System.out.println("1->next: " + generateNextString(test2));
        System.out.println("11->next: " + generateNextString(test3));
        System.out.println("21->next: " + generateNextString(test4));
        System.out.println("1211->next: " + generateNextString(test5));
        System.out.println("111221->next: " + generateNextString(test6));
        System.out.println("312211->next: " + generateNextString(test7));

        System.out.println("\"1\" run 5 times: " + calculateFinalNum(test2, 5));

        System.out.println("Length of given input run 40 times: " + calculateFinalNum(input, 40).length());
        System.out.println("Length of given input run 50 times: " + calculateFinalNum(input, 50).length());
    }

    public static String calculateFinalNum(String startingPoint, int iterations) {
        String currentValue = startingPoint;

        for(int i = 0; i < iterations; i++) {
            currentValue = generateNextString(currentValue);
        }

        return currentValue;

    }

    public static String generateNextString(String given) {
        String result = "";
        
        char currentChar = given.charAt(0);
        int curCount = 1;

        for(int i = 1; i < given.length(); i++) {
            if(given.charAt(i) != currentChar) {
                result += Integer.toString(curCount) + currentChar;
                currentChar = given.charAt(i);
                curCount = 1;
            } else {
                curCount++;
            }
        }

        result += Integer.toString(curCount) + currentChar;

        return result;

    }
}
