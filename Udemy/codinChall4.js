var Mark = {
    fullName: 'Mark Ruffalo',
    mass: 70,
    height: 180,
    calcBMI: function() {
        this.bmi = (this.mass * this.mass) / this.height;
    }
};

Mark.calcBMI();
console.log(Mark);

var John = {
    fullName: 'John Cena',
    mass: 75,
    height: 170,
    calcBMI2: function() {
        this.bmi = (this.mass * this.mass) / this.height;
    }
};

John.calcBMI2();
console.log(John);

if (Mark.calcBMI() > John.calcBMI2()) {
    console.log("Mark has higher BMI.");
}
else {
    console.log("John has higher BMI.");
}