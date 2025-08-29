class Building {
    constructor(this, name, cost, cps){
        this.name = name;
        this.bought = 0;
        this.cost = cost;
        this.cps = cps;
    }
    buy(this){
        this.cost = Math.round(this.cost*115)/100;
        this.bought += 1;
    }
}
class Upgrade{
    constructor(this, name, cost, building, unlock){
        this.name = name
        this.cost = cost
        this.building = building
    }
}
class Multiplier extends Upgrade{
    constructor(this, name, cost, building, unlock, multiplier){
        super(name, cost, building, unlock);
        this.multiplier = multiplier;
    }
}