
// Taking API GET request from BikeAPI file
// All data from that link will be stored in data argument
fetch("http://127.0.0.1:5001/getmotorcycle").then((data)=>{
    return data.json();
    // Passing object data.json() to below completedata
}).then((completedata)=>{
    // Creating empty variable
    let data="";
    // values has all data, one by one data object
    completedata.map((values)=>{
        // Inside this variable is our div (class = card) from fail korisnik.html
        // Increacing number of data, dependindg on the number of data objects
        data+=` <div class="card">
        <h1 class="title card-title">${values.name}</h1>
        <img class="image" src=${values.img_url} alt="image">
        <p class="font-weight-light">${values.power}</p>
        <p class="font-weight-light">${values.torque}</p>
        <p class="font-weight-light">${values.dry_weight}</p>
    </div>`
    });
    // Accesing to div in korisnik.html by id
    document.getElementById("cards").innerHTML=data;

// Catching errors
}).catch((err)=>{
    console.log(err);
});

