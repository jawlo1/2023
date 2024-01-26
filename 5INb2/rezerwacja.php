<?php
    $servername="localhost";
    $user="root";
    $password="";
    $database="baza";

    $con=mysqli_connect( $servername,
                         $user,
                         $password,
                         $database );
    if( !$con ){
        die( "nie udało się połączyć" . mysqli_error($con) );
    }

    $data=$_POST["data"];
    $osob=$_POST["osob"];
    $telefon=$_POST["telefon"];

    $sql="insert into 
            rezerwacje( data_rez, 
                        liczba_osob, 
                        telefon) 
                values($data, $osob,$telefon)";
    if( mysqli_query( $con, $sql ) ){
        echo "Dodano rezerwacje do bazy";
    }else{
        echo "error: " .mysqli_error($con);
    };
    mysqli_close( $con );



