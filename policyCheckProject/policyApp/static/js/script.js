// let submit = document.querySelector('.submit')
// let btn = document.querySelector('.click-btn')
// let stable = document.querySelector('.stable')
// let unstable = document.querySelector('.unstable')
// let body = document.querySelector('body')
// let calc_value = document.querySelector('.calc_value')
// let check = document.getElementsByClassName("check")

// let resultNote = document.querySelector('.result-note')
// let divStable = document.createElement('div')
// let pStable = document.createElement('p')
// let actionStable = document.createElement('h5')
// let noteStable = document.createElement('p')




// // formula for psc to be calculated
// let total_yes_length = document.querySelectorAll('input[value="Yes"]').length;
// let total_no_length = document.querySelectorAll('input[value="No"]').length

// btn.addEventListener('click',()=>{
//   submit.style.display = 'block'
//   let yes_count = 0;
//   let no_count = 0;
//   for(let i = 0; i < check.length; i++){
//     if(check[i].value ==='Yes' && check[i].checked){
//       yes_count++
//     }else if(check[i].value ==='No' && check[i].checked){
//       no_count++
//     }
//   }

// let numerator_value = 7 + (yes_count - no_count)
// let denominator_value = 1 + (total_yes_length + total_no_length)

// let final_value = Math.ceil((numerator_value / denominator_value) * 100)
// console.log(final_value)
// calc_value.textContent = `Score: ${(final_value)}%`



// if(final_value >=70){
//   // stable.style.display = 'block';
//   pStable.innerText = "Stable policy choice"
//   actionStable.innerText = "Action"
//   noteStable.innerText = "May proceed with implementation"
  
//   divStable.appendChild(pStable);
//   divStable.appendChild(actionStable);
//   divStable.appendChild(noteStable);
//   divStable.style.backgroundColor ="#5cc019"
//   divStable.style.border ="1px solid none"
//   divStable.style.color ="whitesmoke"
//   divStable.style.fontWeight ="400"
//   divStable.style.borderRadius ="5px"
//   divStable.style.padding ="7px"
//   resultNote.appendChild(divStable)
// }else{
//   pStable.innerText = "Unstable policy choice"
//   actionStable.innerText = "Action"
//   noteStable.innerText = "Refine decision or try other options"
  
//   divStable.appendChild(pStable);
//   divStable.appendChild(actionStable);
//   divStable.appendChild(noteStable);
//   divStable.style.backgroundColor ="#ff4500"
//   divStable.style.border ="1px solid none"
//   divStable.style.color ="whitesmoke"
//   divStable.style.fontWeight ="400"
//   divStable.style.borderRadius ="5px"
//   divStable.style.padding ="7px"
//   resultNote.appendChild(divStable)
// }
//  console.log(`yes: ${yes_count}, no:${no_count}`)
//  getChart(yes_count,no_count)
// })

// //  Drawing charts
// function getChart(yes_count,no_count){
//   google.charts.load('current', { 'packages': ['corechart'] });
//   google.charts.setOnLoadCallback(drawChart);
//   function drawChart(){
//     let data = google.visualization.arrayToDataTable([
//       ['Reply', 'Count',{ role: 'style' }],
//       ['Yes', yes_count,'#00f'],
//       ['No', no_count,'#f00']
//     ]);

//     const options = {
//       title: 'Policy Choice Stability Check',
//       width: 500,
//       height: 300,
//       legend: 'none',
//       bars: 'vertical',
//       hAxis: {
//         title: 'Replies'
//       },
//       vAxis: {
//         title: 'Count'
//       },
//     };
//   let chart = new google.visualization.ColumnChart(document.getElementById('chartContainer'));
//   chart.draw(data, options);
//   }
// }



// convert checkboxes to radio
//    const checkboxYes = document.getElementById("justified_yes");
//       const checkboxNo = document.getElementById("justified_no");
//       const checkboxYes1 = document.getElementById("red_yes");
//       const checkboxNo1 = document.getElementById("red_no");
//       const checkboxYes2 = document.getElementById("pra_yes");
//       const checkboxNo2 = document.getElementById("pra_no");
//       const checkboxYes3 = document.getElementById("int_yes");
//       const checkboxNo3 = document.getElementById("int_no");
//       const checkboxYes4 = document.getElementById("cost_yes");
//       const checkboxNo4 = document.getElementById("cost_no");
//       const checkboxYes5 = document.getElementById("fin_yes");
//       const checkboxNo5 = document.getElementById("fin_no");
      
//       // Add event listeners to the checkboxes
//       checkboxYes.addEventListener("change", function() {
//           if (checkboxYes.checked) {
//               checkboxNo.checked = false;
//           }
//       });
//       checkboxNo.addEventListener("change", function() {
//           if (checkboxNo.checked) {
//               checkboxYes.checked = false;
//           }
//       });


//       checkboxYes1.addEventListener("change", function() {
//         if (checkboxYes1.checked) {
//             checkboxNo1.checked = false;
//         }
//     });
//     checkboxNo1.addEventListener("change", function() {
//         if (checkboxNo1.checked) {
//             checkboxYes1.checked = false;
//         }
//     });

    
//     checkboxYes2.addEventListener("change", function() {
//       if (checkboxYes2.checked) {
//           checkboxNo2.checked = false;
//       }
//   });
//   checkboxNo2.addEventListener("change", function() {
//       if (checkboxNo2.checked) {
//           checkboxYes2.checked = false;
//       }
//   });

     
//   checkboxYes3.addEventListener("change", function() {
//     if (checkboxYes3.checked) {
//         checkboxNo3.checked = false;
//     }
// });
// checkboxNo3.addEventListener("change", function() {
//     if (checkboxNo3.checked) {
//         checkboxYes3.checked = false;
//     }
// });

// checkboxYes4.addEventListener("change", function() {
//   if (checkboxYes4.checked) {
//       checkboxNo4.checked = false;
//   }
// });
// checkboxNo4.addEventListener("change", function() {
//   if (checkboxNo4.checked) {
//       checkboxYes4.checked = false;
//   }
// });

// checkboxYes5.addEventListener("change", function() {
//   if (checkboxYes5.checked) {
//       checkboxNo5.checked = false;
//   }
// });
// checkboxNo5.addEventListener("change", function() {
//   if (checkboxNo5.checked) {
//       checkboxYes5.checked = false;
//   }
// });
    