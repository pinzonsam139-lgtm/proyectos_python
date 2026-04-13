///Me llamo Sam
//Tengo 16 años
///Estoy aprendiendo JavaScript///


let number=Number(prompt("Ingresa 1 para suma,2 para resta,3 para division,4 para multiplicacion:"))
let numero1=Number(prompt("Ingresa el numero 1:"))
let numero2=Number(prompt("Ingresa el numero 2:"))

let multiplicacion=0;
if (number==1){
  suma=numero1+numero2
  console.log(suma)
}
else if(number==2){
  resta=numero1-numero2
  console.log(resta)
}
else if (number==3){
  if (numero2 !== 0){
    division=numero1/numero2
    console.log(division)
  }
  
  else{
    console.log("Error de division numero=0")
  }
}

else if (number==4){
  multiplicacion=numero1*numero2
  console.log(multiplicacion)
}
else{
  console.log("opcion no valida vuelve a intentar")
}