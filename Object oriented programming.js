

class man{
  constructor(name,height, weight){
      this.name= name
      this.height=height;
      this.weight = weight;
     
  }

  static Sex(){
    console.log('Male');
  }



  description(){
    console.log(this.name + ' is ' + this.height, 'ft and weighs', this.weight, 'pounds');
  }
}



class Nationality extends man{
  constructor(name, height, weight, country){
    super(name, height, weight);
    this.country = country;
  }

  getnationality(){
    console.log(this.name+' is a citizen of '+this.country);
  }
}

let Adam = new Nationality('Adam', '7.2', '120', 'Denmark');






Adam.description();

Adam.getnationality();



//Please i just started my crash on Javascript SE6 last night / this morning ....this is how far i have gone 