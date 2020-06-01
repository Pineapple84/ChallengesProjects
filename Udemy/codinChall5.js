// calculate John's bills and tips=
var billsVal = [124, 48, 268, 180, 42];

if (billsVal[1] < 50 && billsVal[4] < 50) {
    var tips1 = ((20/100) * billsVal[1]);
    var tips2 = ((20/100) * billsVal[4]);
}
if ((billsVal[0] >= 50 && billsVal[0] <= 200) && (billsVal[3] >= 50 && billsVal[3] <= 200)) {
    var tips3 = ((15/100) * billsVal[0]);
    var tips4 = ((15/100) * billsVal[3]);
}
if (billsVal[2] > 200) {
    var tips5 = ((10/100) * billsVal[2]);
}

for (tips1, tips2, tips3, tips4, tips5 < 300; tips1, tips2, tips3, tips4, tips5 = 1;) {
    console.log(tips1);
    console.log(tips2);
    console.log(tips3);
    console.log(tips4);
    console.log(tips5);
        break;
}

var finalPaid1 = tips1 + billsVal[1];
var finalPaid2 = tips2 + billsVal[4];
var finalPaid3 = tips3 + billsVal[0];
var finalPaid4 = tips4 + billsVal[3];
var finalPaid5 = tips5 + billsVal[2];

var finalPaid = [finalPaid1, finalPaid2, finalPaid3, finalPaid4, finalPaid5];

console.log(billsVal);
console.log(finalPaid);

// Find average tips
var John = {
    calcTipsJohn: function() {
        this.tipsAverageJohn = (finalPaid1 + finalPaid2 + finalPaid3 + finalPaid4 + finalPaid5 / 5);
    }
};

John.calcTipsJohn();
console.log(John);


// Calculate Mark's bills and tips
var billsValMark = [77, 375, 110, 45];

if (billsValMark[0] < 100 && billsValMark[3] < 100) {
    var tipsMark1 = ((20/100) * billsValMark[0]);
    var tipsMark2 = ((20/100) * billsValMark[3]);
}
if (billsValMark[2] > 100 && billsValMark[2] < 300) {
    var tipsMark3 = ((10/100) * billsValMark[2]);
}
if (billsValMark[1] > 300) {
    var tipsMark4 = ((25/100) * billsValMark[1]);
}

var tipsSumMark1 = tipsMark1 + billsValMark[0];
var tipsSumMark2 = tipsMark2 + billsValMark[3];
var tipsSumMark3 = tipsMark3 + billsValMark[2];
var tipsSumMark4 = tipsMark4 + billsValMark[1];

// Find average tips
var Mark = {
    calcTipsMark: function() {
        this.tipsAverageMark = ((tipsSumMark1 + tipsSumMark2 + tipsSumMark3 + tipsSumMark4) / 4);
    }
};

Mark.calcTipsMark();
console.log(Mark);

// Compare whom has higher average tips
if (Mark.calcTipsMark() > John.calcTipsJohn()) {
    console.log("Hooray!! Mark has higher average tips.");
}
else {
    console.log("Aha! John has higher average tips.");
}