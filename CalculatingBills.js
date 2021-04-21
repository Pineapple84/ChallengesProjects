function calculator(bills1, bills2, bills3) {
    if (bills1 < 50) {
        var tip1 = (20 / 100) * 48;
        console.log(tip1);
    }
    if (50 < bills2 < 200) {
        var tip2 = (15 / 100) * 124;
        console.log(tip2);
    }
    if (50 < bills3) {
        var tip3 = (10 / 100) * 268;
        console.log(tip3);
    }

    var bills = [48, 124, 268];
    console.log(bills);

    var billsTip1 = 48 + 9.6;
    var billsTip2 = 124 + 18.6;
    var billsTip3 = 268 + 26.8;

    var billsTipsAcc = [billsTip1, billsTip2, billsTip3];
    console.log(billsTipsAcc);
}

calculator(48, 124, 268)
