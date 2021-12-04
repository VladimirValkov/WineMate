function checkMandatory(field) {
    if (field.val() != null && field.val().length > 0 && field.val() != '-----') {
        field.removeClass('is-invalid')
        field.addClass('is-valid')
        return true
    } else {
        field.removeClass('is-valid')
        field.addClass('is-invalid')
        return false
    }
}

function addNavigation(holderid) {
    $('#' + holderid).replaceWith(`<nav class="navbar navbar-expand-sm bg-light navbar-primary">
  <ul class="navbar-nav">
                 <a class="navbar-brand" href="/home/">WineMate</a>
<!--                 <li class="nav-item" id="nav_home"><a class="nav-link" href="/home/" >Home</a></li>-->
                 <li class="nav-item" id="nav1"><a class="nav-link" href="/table/cellar" >Изба</a></li>
                 <li class="nav-item" id="nav2"><a class="nav-link" href="#" >Мостри</a></li>
                 <li class="nav-item" id="nav3"><a class="nav-link" href="#" >Стабилизация</a></li>
                 <li class="nav-item" id="nav4"><a class="nav-link" href="#" >Високоалкохолни напитки</a></li>
  </ul>
</nav>`)
}
