var mockdata =
[
    {
        "id": '1x23',
        "size": "small",
        "src": {
          "addr_id": 1,
          "addr_person": "Rob Base",
          "addr_street": "123 Code St",
          "addr_city":"Minneapolis",
          "addr_state":"MN",
          "addr_zip": "55414"
        },
        "dst": {
          "addr_id": 2,
          "addr_person": "Van Stacker",
          "addr_street": "42 Engi Ln",
          "addr_city":"Seattle",
          "addr_state":"WA",
          "addr_zip": "98109"
        }
    },
    {
        "id": 'avd14',
        "size": "small",
        "src": {
          "addr_id": 1,
          "addr_person": "Rob Base",
          "addr_street": "123 Code St",
          "addr_city":"Minneapolis",
          "addr_state":"MN",
          "addr_zip": "55414"
        },
        "dst": {
          "addr_id": 3,
          "addr_person": "Connor B. Zee",
          "addr_street": "42 Engi Ln",
          "addr_city":"Seattle",
          "addr_state":"WA",
          "addr_zip": "98109"
        }
    },
    {
        "id": 'xx214',
        "size": "small",
        "src": {
          "addr_id": 3,
          "addr_person": "Connor B. Zee",
          "addr_street": "42 Engi Ln",
          "addr_city":"Seattle",
          "addr_state":"WA",
          "addr_zip": "98109"
        },
        "dst": {
          "addr_id": 1,
          "addr_person": "Rob Base",
          "addr_street": "123 Code St",
          "addr_city":"Minneapolis",
          "addr_state":"MN",
          "addr_zip": "55414"
        }
    },
];

function displayPackageDetails(p){
  // updates the DOM to display a packages details.
  // p is a package json
  $('#detail_src_id').prop('value',p.src.addr_id);
  $('#detail_src_name').val(p.src.addr_person);
  $('#detail_src_street').val(p.src.addr_street);
  $('#detail_src_state').val(p.src.addr_state);
  $('#detail_src_zip').val(p.src.addr_zip);

  $('#detail_dst_id').val(p.dst.addr_id);
  $('#detail_dst_name').val(p.dst.addr_person);
  $('#detail_dst_street').val(p.dst.addr_street);
  $('#detail_dst_state').val(p.dst.addr_state);
  $('#detail_dst_zip').val(p.dst.addr_zip);

}

// Page-Global packages indexed by Id
var packages = {}
var selected = ''
$(function () {
    // todo Query service and get package information.
    // data = http get on packages resource

    // Delete the current package index
    packages = {}

    // index by package id for use in other fuctions on the page.
    for (var i = 0; i < mockdata.length; i++){
      p = mockdata[i];
      if(p.id in packages){
        console.log('Violated unique Id constraint for packages!! p.id='+p.id)
        p.id = p.id+'--'+i
      }

      packages[p.id] = p;
    }

    var mydata = []
    for(var p_id in packages){
      p = packages[p_id]

      mydata.push({
        "id":p.id,
        "size":p.size,
        "src":p.src.addr_person,
        "dst":p.dst.addr_person
      })
    }

    $('#package-table').bootstrapTable({
        data: mydata
    });

    // Register click handler for the package table rows
    $('#package-table > tbody > tr').click(function() {
      // 'this' is the selected html table row
      pkg_idx = $(this).attr('data-index');
      p_id = mydata[pkg_idx].id;
      console.log('clicked package:'+ p_id);
      displayPackageDetails(packages[p_id]);
    });
});
