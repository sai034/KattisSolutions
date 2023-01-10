#	Above Average
#https://open.kattis.com/problems/aboveaverage

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Veda {
    public static void main(String[] args) {
        Scanner scon = new Scanner(System.in);
        int C = scon.nextInt();
        for (int i=0 ; i<C ; i++ ) {
            int n = scon.nextInt();
            List<Integer> list = new ArrayList<>();
            for (int j=0 ; j<n ; j++) {
                list.add(scon.nextInt());
            }
            float average = calculateAverage(list);
         //   System.out.println(average);
        //   System.out.println(list.get(0));
        //   System.out.println(list.get(1));
        //   System.out.println(list.get(2));
            float percentageOfAboveAvgStudents = calculatePercentageOfAboveAvgStudents(list,average);
            System.out.printf("%.3f",percentageOfAboveAvgStudents);
            System.out.print("%\n");
        }
    }

    public static float calculateAverage(List<Integer> list) {
        int sum = 0;
        for (int i=0; i< list.size(); i++) {
            sum += list.get(i);
        }
        return sum / list.size();
    }

    public static float calculatePercentageOfAboveAvgStudents(List<Integer> list, float average) {
        float count = 0;
        for (int i=0; i< list.size(); i++) {
            if (list.get(i) > average) {
                count++;
            }
        }
                  //  System.out.println(count);
               //     System.out.println(list.size());

        return (count / list.size()) * 100;
    }
}
