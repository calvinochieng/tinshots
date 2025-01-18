var onSale = false, 
  invetoryLevel = 12,
  discount =  3;

if (onSale && invetoryLevel > 10 ){
  console.log('Plenty left');
}
if (onSale && discount > 0){
  console.log('on sale');
}else{
  console.log('Full Price')
}
var a= 0;

console.log(a);
c = `a = ${a}`;
console.log(c);

a = [2,3,4,5,45]

for (var i = 0; i < a.length ; i++) {
  console.log(a[i]);
}