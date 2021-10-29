/*Write a function that returns the average value of an arbitrarily long array of numbers. 
Use that function to average up to three numbers entered in the input fields in the PBS playground, and print out the result.
Your solution should also behave sensibly if the user executes 
the code without entering values into any of the inputs.
In case you’re a little rusty, just a reminder that you calculate the average of a set of numbers 
by adding them all together, and then dividing the result of that addition by the amount of numbers being 
averaged.
*/

function avarr(arr){
    var ar = arr ;
 
     if( ar instanceof Array && ar.length){
         
     var total = 0;
     var ans = 0;
     for(var i = 0; i < ar.length; i++) {
         total += parseInt(ar[i]);
     }
     return ans =  total / ar.length
     }
     else {pbs.say('Please enter an array of numbers.' + arr);
         return NaN
         }
 
 }
 
 
 var rawInputs = pbs.inputs();
 avr = avarr(rawInputs);
 
 
 if(isNaN(avr)){
     pbs.say("does not compute!!")
     }
 else {
 pbs.say("The average of the array is : " + avr)
 }
 