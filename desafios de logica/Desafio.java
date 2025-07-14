// (salario bruto - percentual de imposto mediante ao salário) + adicional de benficios

import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {
        try (Scanner leitorDeEntradas = new Scanner(System.in)) {
            float valorSalario = leitorDeEntradas.nextFloat();
            float valorBeneficio = leitorDeEntradas.nextFloat();
            float valorImposto;

            if (valorSalario >= 0 && valorSalario <= 1100) 
            {
                valorImposto = 0.05F * valorSalario;
            }
            else if (valorSalario > 1100 && valorSalario <= 2500) 
            {
                valorImposto = 0.10F * valorSalario;
            } 
            else {
                valorImposto = 0.15F * valorSalario;
            }

            float saida = valorSalario - valorImposto + valorBeneficio;
            System.out.println(String.format("%.2f", saida));
        }
    }
}