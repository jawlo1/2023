Temat: Funkcje obsługujące tablice<br>

<?php
    $cars=["BMW","Audi","Volvo"];
    $cars[count($cars)]="Fiacik";
    var_dump( $cars );