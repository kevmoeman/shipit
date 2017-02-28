function displayVehicleDetails(v){
  // updates the DOM to display a vehicles details.
  // v is a vehicle json
  console.log(v)
  $('#detail_vehicleid').prop('value',v.vehicle_id);
  $('#detail_Company').val(v.company);
  $('#detail_Location').val(v.location.st_city);

  $('#detail_stationstreet').val(v.location.st_street)
  $('detail_stationzip').val(v.location.station_zip)
  $('detail_stationstate').val(v.location.phonenumber)
}

// Page-Global packages indexed by Id
// var vehicles = {}
// var stations = {}
var vehicles = {}

function on_vehicles_load(data){
  // Delete the current package index
  vehicles = {}
  // index by package id for use in other fuctions on the page.
  //data validation
  console.log(data)
  for (var i = 0; i < data.length; i++){
    v = data[i];
    if(v.vehicle_id in vehicles){
      console.log('Violated unique Id constraint for packages!! p.id='+v.vehicle_id)
      v.vehicle_id = v.vehicle_id+'--'+i
    }

    vehicles[v.vehicle_id] = v;
  }

  var mydata = []
  for(var v_id in vehicles){
    v = vehicles[v_id]

    mydata.push({
      "id":v.vehicle_id,
      "company":v.company,
      "location":v.location.st_city,
    })
  }

  $('#vehicle-table').bootstrapTable({
      data: mydata
  });

  // Register click handler for the package table rows
  $('#vehicle-table > tbody > tr').click(function() {
    // 'this' is the selected html table row
    vehicle_idx = $(this).attr('data-index');
    v_id = mydata[vehicle_idx].id;
    console.log('clicked vehicle:'+ v_id);
    displayVehicleDetails(vehicles[v_id]);
  });
}

$(function () {
    $.getJSON('http://localhost:8080/vehicles', on_vehicles_load);
});
