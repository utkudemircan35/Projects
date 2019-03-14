import java.util.Scanner;
import java.math.*;

public class Main {

    public static void toplama(){

        System.out.println("Birinci Sayı: ");
        Scanner s = new Scanner(System.in);
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayı: ");
        double sayi2 = s.nextDouble();
        System.out.println("Sonuç: "+(sayi1+sayi2));

    }

    public static void cikarma() {

        System.out.println("Birinci Sayı: ");
        Scanner s = new Scanner(System.in);
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayı: ");
        double sayi2 = s.nextDouble();
        System.out.println("Sonuç: "+(sayi1-sayi2));

    }

    public static void carpma(){

        System.out.println("Birinci Sayı: ");
        Scanner s = new Scanner(System.in);
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayı: ");
        double sayi2 = s.nextDouble();
        System.out.println("Sonuç: " + (sayi1 * sayi2));

    }

    public static void bolme(){

        System.out.println("Birinci Sayı: ");
        Scanner s = new Scanner(System.in);
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayı: ");
        double sayi2 = s.nextDouble();
        if (sayi2 == 0 ){

            System.out.println("Hata. Bir sayı sıfıra bölünemez");

        }
        else {
            System.out.println("Sonuç: " + (sayi1 / sayi2));
        }

    }

    public static void us_bulma(){

        System.out.println("Birinci Sayı: ");
        Scanner s = new Scanner(System.in);
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayı: ");
        double sayi2 = s.nextDouble();
        System.out.println("Sonuç: "+ Math.pow(sayi1,sayi2));

    }

    public static void kalan_bulma(){

        Scanner s = new Scanner(System.in);
        System.out.println("Sayıyı Giriniz: ");
        double sayi1 = s.nextDouble();
        System.out.println("İkinci Sayıyı Giriniz: ");
        double sayi2 = s.nextDouble();
        if (sayi2 == 0 ){

            System.out.println("Hata. Bir Sayı sıfıra bölünemez ");
        }
        else {

            System.out.println(sayi1 + ", " + sayi2 +" bölümünden kalan: "+(sayi1%sayi2));

        }


    }

    public static void main(String[] args)
    {

        while (true) {


            System.out.println("-----------------------\n\nHesap Makinesi\n\n1.Toplama\n2.Çıkarma\n3.Çarpma\n4.Bölme\n5.Üs Bulma\n6.Kalan Bulma");



            Scanner scan = new Scanner(System.in);
            String islem = scan.nextLine();
            if (islem.equals("1"))
            {
                toplama();
            }
            else if (islem.equals("2"))
            {
                cikarma();
            }
            else if (islem.equals("3"))
            {
                carpma();
            }
            else if (islem.equals("4"))
            {
                bolme();
            }
            else if (islem.equals("5"))
            {
                us_bulma();
            }
            else if (islem.equals("6"))
            {
                kalan_bulma();
            }

        }

    }
}
