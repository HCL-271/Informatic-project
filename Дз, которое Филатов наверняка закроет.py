import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Third_class {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList array = new ArrayList();
        String s;

        s = sc.next();
        while (!s.equals("#")) {
            array.add(s);
            s = sc.next();
        }
        Iterator I = array.iterator();
        System.out.print("[");
        for (int i = 0; i + 1 < array.size(); i++) {
            System.out.print(array.get(i) + ", ");
        }
        System.out.println(array.get(array.size() - 1) + "]");


        s = sc.next();
        while (!s.equals("#")) {
            array.add(0, s);
            s = sc.next();
        }

        System.out.print("[");
        for (int i = 0; i + 1 < array.size(); i++) {
            System.out.print(array.get(i) + ", ");
        }
        System.out.println(array.get(array.size() - 1) + "]");

        int j = 0;
        s = sc.next();
        while (!s.equals("0")) {
            while ((!s.equals(Integer.toString(j))) && (j < 10)) {
                j++;
            }
            s = sc.next();
            array.add(j, s);
            s = sc.next();
        }

        j = 0;
        while ((!s.equals(Integer.toString(j))) && (j < 10)) {
            j++;
        }
        s = sc.next();
        array.add(j, s);

        System.out.print("[");
        for (int i = 0; i + 1 < array.size(); i++) {
            System.out.print(array.get(i) + ", ");
        }
        System.out.println(array.get(array.size() - 1) + "]");


        s = sc.next();
        while (!s.equals("0")) {
            while ((!s.equals(Integer.toString(j))) && (j < 10)) {
                j++;
            }
            array.remove(j);
            s = sc.next();
            j=0;
        }
        j=0;
        array.remove(j);

        System.out.print("[");
        for (int i = 0; i + 1 < array.size(); i++) {
            System.out.print(array.get(i) + ", ");
        }
        System.out.println(array.get(array.size() - 1) + "]");


    }
}


import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Third_class {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList array = new ArrayList();
        String s;
        String s1;
        Iterator I = array.iterator();
        s = sc.next();
        while (!s.equals("#")) {


            if (s.equals("remove")) {
                s1 = sc.next();
                array.remove(Integer.parseInt(s1));
                System.out.print("[");
                for (int i = 0; i + 1 < array.size(); i++) {
                    System.out.print(array.get(i) + ", ");
                }
                System.out.println(array.get(array.size() - 1) + "]");
            }


            if (s.equals("add")) {
                s1 = sc.next();
                s = sc.next();
                array.add(Integer.parseInt(s1), s);
                System.out.print("[");
                for (int i = 0; i + 1 < array.size(); i++) {
                    System.out.print(array.get(i) + ", ");
                }
                System.out.println(array.get(array.size() - 1) + "]");
            }

            if (s.equals("clear")) {
                array.clear();
                System.out.println("[]");


            }

            if (s.equals("get")) {
                s1 = sc.next();
                System.out.println(array.get(Integer.parseInt(s1)));
                System.out.print("[");
                for (int i = 0; i + 1 < array.size(); i++) {
                    System.out.print(array.get(i) + ", ");
                }
                System.out.println(array.get(array.size() - 1) + "]");

            }
            if (s.equals("set")) {
                s1 = sc.next();
                s = sc.next();
                array.remove(Integer.parseInt(s1));
                array.add(Integer.parseInt(s1), s);
                System.out.print("[");
                for (int i = 0; i + 1 < array.size(); i++) {
                    System.out.print(array.get(i) + ", ");
                }
                System.out.println(array.get(array.size() - 1) + "]");
            }


            s = sc.next();
        }
    }
}
