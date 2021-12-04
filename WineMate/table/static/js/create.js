function hideall()
{
    $('#numProtocol').hide();
$('#batch').hide();
$('#mal_acids').hide();
$('#lactic_acids').hide();
$('#total_ext').hide();
$('#freesugar').hide();
$('#IF').hide();
$('#sowing').hide();
$('#sorb_acid').hide();
}

hideall();

$('#sel1').on('change', function (){
    if (this.value === 'Стабилизация')
    {
      hideall();
      $('#numProtocol').show();
      $('#mal_acids').show();
      $('#lactic_acids').show();
      $('#total_ext').show();
      $('#freesugar').show();
      $('#IF').show();
      $('#sowing').show();
      $('#sorb_acid').show();

      //   $('#assort').addClass('is-valid')
      //   $('#assort').removeClass('is-invalid')
    }
    else if(this.value === 'Изба')
    {
        hideall();
        $('#mal_acids').show();
        $('#lactic_acids').show();
        $('#sorb_acid').show();
    }
    else if(this.value === 'Високоалкохолни напитки')
    {
        hideall();
        $('#numProtocol').show();
        $('#batch').show();
        $('#IF').show();

        // $('#assort').removeClass('is-valid')
        // $('#assort').addClass('is-invalid')
    }
    else {
        hideall();
    }

})

// const total_ext = document.getElementById('total_ext');
//
// total_ext.addEventListener('total_ext', updateSugarFree)
//
// function updateSugarFree(e)
// {
//     if ($('#sugar').value !== undefined)
//     {
//         $('#freesugarinput').value = parseFloat($('#total_ext').value) - parseFloat($('#sugar').value);
//     }
// }