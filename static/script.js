// var start = document.querySelector(".save_net");
// const addButton = document.getElementById('addRow');
// const resetButton = document.getElementById('resetT');
// let ROWS_COUNTER = 1;

// function addRow() {
//     ROWS_COUNTER++;
//     var str = `
//         <tr class="row">
//             <th>
//                 <input type="number" name="[${ROWS_COUNTER}]order_number" value="${ROWS_COUNTER}" id="">
//             </th>
//             <th>
//                 <input type="number" name="[${ROWS_COUNTER}]step" id="">
//             </th>
//             <th>
//                 <input type="number" name="[${ROWS_COUNTER}]amount" id="">
//             </th>
//         </tr>`
//     ;
//     start.insertAdjacentHTML("beforeBegin", str);
// }

// function resetTable() {
//     document.querySelectorAll(".row").forEach(e => e.parentNode.removeChild(e));
//     ROWS_COUNTER = 1;
// }

// addButton.addEventListener('click', () => addRow());
// resetButton.addEventListener('click', () => resetTable());