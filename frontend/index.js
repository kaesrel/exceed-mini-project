document.getElementById("text").innerHTML = "Car Park";

function normalState(text_id, box_id) {
    document.getElementById(text_id).innerHTML = "Available";
    document.getElementById(box_id).style.backgroundColor = "green";
}

function parkingState(text_id, box_id) {
    document.getElementById(text_id).innerHTML = "Not Available";
    document.getElementById(box_id).style.backgroundColor = "red";
}

function lastState(text_id, box_id, time, cost) {
    clock = document.createElement("div");
    clock.classList.add("clock-box");
    clock.id = "w";

    text = document.createElement("div");
    text.classList.add("sub-box-2");
    text.id = "a2";

    text2 = document.createElement("div");
    text2.classList.add("sub-box-2");
    text2.id = "a3";

    box = document.getElementById(box_id);
    box.append(text);
    box.append(text2);
    box.append(clock);
    
    document.getElementById(text_id).innerHTML = "Just Leaving";
    document.getElementById(box_id).style.backgroundColor = "blue";
    // I do not know the format string in js.
    document.getElementById("a2").innerHTML = time;
    document.getElementById("a3").innerHTML = cost;

    var timeLeft = 3;
    var elem = document.getElementById('w');    
    var timerId = setInterval(countdown, 1000);
    function countdown() {
        if (timeLeft == -1) {
        clearTimeout(timerId);
        clock.remove();
        text.remove();
        text2.remove();
        normalState();
        } else {
        elem.innerHTML = timeLeft;
        timeLeft--;
        }
    }
}

function parking(box, state, time, cost) {
    if (state === "0") {
        normalState(box.id, box.id2);
    } else if (state === "1") {
        parkingState(box.id, box.id2);
    } else if (state === "2") {
        // const time = "10";
        // const cost = "50";
        lastState(box.id, box.id2, time, cost);
    }
}
// real function
// function carParking(slot, status) {
//     if (status === "parking") {
//         document.getElementById(slot).innerHTML = "Not Available";
//         document.getElementById(slot).style.backgroundColor = "red";
//     }
// }


    


fetch("")
.then((data) => data.json())
.then((datas) => {
    datas.forEach(data => {
        parking(data.id, data.state, data.time, data.cost);
    });
});
