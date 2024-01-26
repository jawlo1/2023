<?php
    $servername="localhost";
    $user="root";
    $password="";
    $database="baza";

    $con=mysqli_connect($server,$user,$password,                        $database);
    if( !$con ){
        die("Nie udało się połączyć: ". mysqli_error($con) );
    }
    $data=$_POST['data'];
    $ile=$_POST['osob'];
    $telefon=$_POST['telefon'];
    
    $sql="INSERT INTO rezerwacje( data_rez,         
                                liczba_osob, telefon)
                        VALUES( $data,
                                $ile,
                                $telefon)";

    if( mysqli_query( $con, $sql ) ){
        echo "Dodano rezerwację do bazy";
    }else{
        echo "error: ". mysqli_error($con);
    }
    mysqli_close($con);
?>